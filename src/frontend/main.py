import json
import os
import socket
import sys
import threading

from PyQt5 import QtGui
from PyQt5.QtCore import QUrl, pyqtSlot, pyqtSignal, QObject, QTimer, QThreadPool
from PyQt5.QtGui import QFont
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QMainWindow, QStackedLayout, QApplication, QWidget, QFileDialog

import mainWindow, mainWidget, editWidget, simulation1Widget
from recvData import RcvDataThread


import src.backend.classes.Drone
from src.backend.SImulationThread import Simulator, SimulatorTask

FILE_PATH = os.path.abspath(__file__)
# 得到当前文件所在的目录
DIR_PATH = os.path.dirname(FILE_PATH)
# 得到当前项目的根目录
ROOT_PATH = os.path.dirname(os.path.dirname(DIR_PATH))


class main_Widget(QWidget, mainWidget.Ui_mainWidget):
    def __init__(self, *args, **kwargs):
        super(main_Widget, self).__init__(*args, **kwargs)
        self.setupUi(self)


class edit_Widget(QWidget, editWidget.Ui_edit_Widget):
    def __init__(self, *args, **kwargs):
        super(edit_Widget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.editExportButton.clicked.connect(self.saveEditInfoAsFile)
        self.editCleanTextButton.clicked.connect(self.cleanEditJsonTextBroswer)
        self.editAreasButton.clicked.connect(self.signalEditAreasToJs)
        self.editLineButton.clicked.connect(self.signalEditLineToJs)

    def signalEditAreasToJs(self):
        chioce = self.areaClassComboBox.currentIndex()
        mainWindow.textBrowser.append(__file__ + '\t[INFO]: Edit ZONE ' + str(chioce + 1) + ' areas in the Map ...')
        mainWindow.interact_obj.sig_send_editArea_to_js.emit(chioce)

    def signalEditLineToJs(self):
        mainWindow.textBrowser.append(__file__ + '\t[INFO]: Edit line in the Map ...')
        mainWindow.interact_obj.sig_send_editLine_to_js.emit('1')

    def cleanEditJsonTextBroswer(self):
        mainWindow.textBrowser.append(__file__ + '\t[INFO]: Clean data from Map (QWebEngineView)...')
        self.editJsonTextBrowser.clear()

    def saveEditInfoAsFile(self):
        mainWindow.textBrowser.append(__file__ + '\t[INFO]: Try to saveEditInfoAsFile...')
        droneId = self.droneIdText.toPlainText()
        flightTime = self.flightTimeText.toPlainText()
        fileName, fileType = QFileDialog.getSaveFileName(self,
                                                         "Save as",
                                                         ROOT_PATH + '/data/temp/customLines/'+'FP_'+droneId+'_'+flightTime,
                                                         "JSON Files (*.json)")
        if fileName != "":
            with open(fileName, 'w') as f:
                context = self.editJsonTextBrowser.toPlainText()
                f.write(context)
        else:
            mainWindow.textBrowser.append(__file__ + '\t[WARNING]: Cancel to saveEditInfoAsFile')


class sim1_Widget(QWidget, simulation1Widget.Ui_simulation1Widget):
    def __init__(self, *args, **kwargs):
        super(sim1_Widget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.simExportButton.clicked.connect(self.saveCoordAsFiles)
        self.sim_coordTextBrowser.setFont(QFont('Consolas', 12))

    def saveCoordAsFiles(self):
        mainWindow.textBrowser.append(__file__ + '\t[INFO]: Try to saveCoordAsFiles...')
        fileName, fileType = QFileDialog.getSaveFileName(self,
                                                         "Save as",
                                                         ROOT_PATH + '/data/temp',  # saving path
                                                         "All Files (*);;Text Files (*.txt)")
        if fileName != "":
            with open(fileName, 'w') as f:
                context = self.sim_coordTextBrowser.toPlainText()
                f.write(context)
        else:
            mainWindow.textBrowser.append(__file__ + '\t[WARNING]: Cancel to saveCoordAsFiles')



class TInteractObj(QObject):
    """
    一个槽函数供js调用(内部最终将js的调用转化为了信号),
    一个信号供js绑定,
    这个一个交互对象最基本的组成部分.
    """

    # 定义信号,该信号会在js中绑定一个js方法.
    sig_send_to_js = pyqtSignal(str)
    sig_send_jsonfile_to_js = pyqtSignal(str)
    sig_send_editArea_to_js = pyqtSignal(int)
    sig_send_editLine_to_js = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        # 交互对象接收到js调用后执行的回调函数.
        self.receive_str_from_js_callback = None

    # str表示接收str类型的信号,信号是从js发出的.
    @pyqtSlot(str)
    def receive_str_from_js(self, str):
        self.receive_str_from_js_callback(str)

    @pyqtSlot(str)
    def setCoordData(self, data):
        self.sig_send_to_js.emit(data)


class Window(QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.welcomeText()
        # Auto scroll of textBrowser in MainWindow
        self.textBrowser.setFont(QFont('Consolas', 13))
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        self.recv_thread = RcvDataThread(self)
        self.realTimePosition = ""

        # Load Javascript of map and initialisation
        self.index = (os.path.split(os.path.realpath(__file__))[0]) + "/index.html"
        self.webEngineView.load(QUrl.fromLocalFile(self.index))
        self.textBrowser.append(__file__ + '\t[INFO]: Initializing the interact object ...')
        self.init_channel()

        # Load and config different widgets pages
        self.qls = QStackedLayout(self.frame_main)

        self.mainW = main_Widget()
        self.editW = edit_Widget()
        self.sim1W = sim1_Widget()

        self.qls.addWidget(self.mainW)
        self.qls.addWidget(self.editW)
        self.qls.addWidget(self.sim1W)

        self.actionAdd_elements.triggered.connect(lambda: self.showWidgets(self.actionAdd_elements, self.qls))
        # self.actionAdd_elements.triggered.connect(lambda: self.interact_obj.sig_send_editArea_to_js.emit(str))
        self.actionSimulationv1.triggered.connect(lambda: self.showWidgets(self.actionSimulationv1, self.qls))

        # Import flight planing json file for simulation
        self.sim1W.importDroneFlightPlanButton.clicked.connect(self.importFlightPlanFile)

        # self.timer = QTimer(self)
        self.sim1W.coordPushButton.clicked.connect(self.addCoordByBtn)
        self.sim1W.autoSimStartButton.clicked.connect(lambda : self.updateCoordDataByTimer(self.sim1W.setTimerSpinBox.value()))
        self.sim1W.autoSimStopButton.clicked.connect(self.stopUpdateCoordData)
        self.sim1W.autoSimPulseOrContinueButton.clicked.connect(self.pulseOrContinueUpdateCoordData)
        
        # Select a file
        self.actionImport_GeoJSON_File.triggered.connect(self.openFile)

        self.flightPlanFileName=""

    def showWidgets(self, button, qls):
        dic = {
            "Add elements": 1,
            "Simulation v1": 2,
        }
        index = dic[button.text()]
        qls.setCurrentIndex(index)
        self.textBrowser.append(__file__ + '\t[INFO]: Initializing the ' + str(qls.currentWidget()) + '...')

    def init_channel(self):
        """
        为webview绑定交互对象
        """
        self.interact_obj = TInteractObj(self)
        self.interact_obj.receive_str_from_js_callback = self.receive_data

        channel = QWebChannel(self.webEngineView.page())
        # interact_obj 为交互对象的名字,js中使用.
        channel.registerObject("interact_obj", self.interact_obj)

        self.webEngineView.page().setWebChannel(channel)

        self.thread_pool = QThreadPool()
        self.thread_pool.setMaxThreadCount(1)  # 只允许一个线程

    def receive_data(self, data):
        self.textBrowser.append(__file__ + '\t[INFO]: Receive data from Map (QWebEngineView)...')
        JsonFormat = json.dumps(json.loads(data), indent=4)
        # self.textBrowser.setText(JsonFormat)
        self.editW.editJsonTextBrowser.setText(JsonFormat)

    # @pyqtSlot()
    def addCoordByBtn(self):
        coord = self.sim1W.latTextEdit.toPlainText() + "," + self.sim1W.lngTextEdit.toPlainText()
        if not coord:
            return
        # 这个信号是在js中和一个js方法绑定的,所以发射这个信号时会执行对应的js方法.
        self.interact_obj.sig_send_to_js.emit(coord)
        record = self.sim1W.sim_coordTextBrowser.toPlainText()
        self.sim1W.sim_coordTextBrowser.setText(record + '\n' + '[' + coord + ']')
    
    def updateCoordData(self):
        self.interact_obj.setCoordData(self.realTimePosition)
        self.sim1W.sim_coordTextBrowser.append('[' + self.realTimePosition + ']')

    def updateCoordDataByTimer(self, milliSecond):
        self.timer = QTimer(self)
        self.recv_thread.start()
        self.timer.timeout.connect(self.updateCoordData)
        self.timer.start(milliSecond)
        self.textBrowser.append(__file__ + '\t[INFO]: Start automatic sampling...')
        self.simulator = Simulator(self.flightPlanFileName)
        task = SimulatorTask(self.simulator)
        self.thread_pool.start(task)

    def stopUpdateCoordData(self):
        self.textBrowser.append(__file__ + '\t[INFO]: Stop automatic sampling...')
        self.timer.stop()
        self.timer.deleteLater()
        self.sim1W.sim_coordTextBrowser.clear()
        self.interact_obj.sig_send_to_js.emit('STOP')

    def pulseOrContinueUpdateCoordData(self):
        if self.timer.isActive():
            self.timer.stop()
            self.textBrowser.append(__file__ + '\t[INFO]: Pulse automatic sampling...')
        else:
            self.timer.start()
            self.textBrowser.append(__file__ + '\t[INFO]: Continue automatic sampling...')

    # def updateCoordDataByTimer(self, milliSecond):
    #     timer = QTimer(self)
    #     timer.timeout.connect(self.updateCoordData)
    #     timer.start(milliSecond)

    def importFlightPlanFile(self):
        self.textBrowser.append(__file__ + '\t[INFO]: Try to Import Flight Planing File...')
        self.flightPlanFileName, filetype = QFileDialog.getOpenFileName(self,
                                                                        "Select a JSON file",
                                                                        ROOT_PATH + '/data/temp/customLines',
                                                                        "JSON File (*.json)")
        self.textBrowser.append(__file__ + '\t[INFO]: Import the file : ' + self.flightPlanFileName)


    def openFile(self):
        self.textBrowser.append(__file__ + '\t[INFO]: Try to Import JSON File...')
        self.textBrowser.append(ROOT_PATH)
        fileName, filetype = QFileDialog.getOpenFileName(self, "Select a JSON file", ROOT_PATH,
                                                         "JSON File (*.json)")
        if fileName != "":
            with open(fileName, 'r') as file:
                content = file.read()  # 读取文件内容
                self.textBrowser.append(__file__ + '\t[INFO]: Import the file : ' + fileName)
                # self.textBrowser.append(content)
                self.interact_obj.sig_send_jsonfile_to_js.emit(content)
        else:
            self.textBrowser.append(__file__ + '\t[WARNING]: Cancel to Import JSON File')

    def welcomeText(self):
        logoText = "  $$$$$$$\                                                 $$$$$$\  $$\                         $$\            $$\     $$\                     \n" \
                   "  $$  __$$\                                               $$  __$$\ \__|                        $$ |           $$ |    \__|                    \n" \
                   "  $$ |  $$ | $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\        $$ /  \__|$$\ $$$$$$\$$$$\  $$\   $$\ $$ | $$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\  \n" \
                   "  $$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\       \$$$$$$\  $$ |$$  _$$  _$$\ $$ |  $$ |$$ | \____$$ \_$$  _|  $$ |$$  __$$\ $$  __$$\ \n" \
                   "  $$ |  $$ |$$ |  \__|$$ /  $$ |$$ |  $$ |$$$$$$$$ |       \____$$\ $$ |$$ / $$ / $$ |$$ |  $$ |$$ | $$$$$$$ | $$ |    $$ |$$ /  $$ |$$ |  $$ |\n" \
                   "  $$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$   ____|      $$\   $$ |$$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$  __$$ | $$ |$$\ $$ |$$ |  $$ |$$ |  $$ |\n" \
                   "  $$$$$$$  |$$ |      \$$$$$$  |$$ |  $$ |\$$$$$$$\       \$$$$$$  |$$ |$$ | $$ | $$ |\$$$$$$  |$$ |\$$$$$$$ | \$$$$  |$$ |\$$$$$$  |$$ |  $$ |\n" \
                   "  \_______/ \__|       \______/ \__|  \__| \_______|       \______/ \__|\__| \__| \__| \______/ \__| \_______|  \____/ \__| \______/ \__|  \__|\n" \
                   "\n" \
                   "                                                                                                                                Version 1.0    \n"
        self.textBrowser.append(logoText)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Window()
    mainWindow.show()
    sys.exit(app.exec_())

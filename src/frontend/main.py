import json
import os
import socket
import sys
import threading

from PyQt5 import QtGui
from PyQt5.QtCore import QUrl, pyqtSlot, pyqtSignal, QObject, QTimer, QThreadPool
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QMainWindow, QStackedLayout, QApplication, QWidget, QFileDialog, QAction, QLabel

import mainWindow, mainWidget, editWidget, editAreaWidget, simulation1Widget, simulation2Widget
from recvData import RcvDataThread, ThreadPool


FILE_PATH = os.path.abspath(__file__)
# 得到当前文件所在的目录 Get the directory where the current file is located
DIR_PATH = os.path.dirname(FILE_PATH)
# 得到当前项目的根目录 Get the root directory of the current project
ROOT_PATH = os.path.dirname(os.path.dirname(DIR_PATH))



# import src.backend.classes.Drone
sys.path.append(ROOT_PATH)
from src.backend.SimulationThread import Simulator, SimulatorTask
from src.backend.RecvCmdThread import StatusReceiverTask, RcvCmdThread
import src.backend.Util as algo
from shapely import affinity, LineString, Point
import shapely.geometry



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
        self.editLineButton.clicked.connect(self.signalEditLineToJs)

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

class editArea_Widget(QWidget, editAreaWidget.Ui_editArea_Widget):
    def __init__(self, *args, **kwargs):
        super(editArea_Widget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.editExportButton.clicked.connect(self.saveEditInfoAsFile)
        self.editCleanTextButton.clicked.connect(self.cleanEditJsonTextBroswer)
        self.editAreasButton.clicked.connect(self.signalEditAreasToJs)

    def signalEditAreasToJs(self):
        choice = self.areaClassComboBox.currentIndex()
        mainWindow.textBrowser.append(__file__ + '\t[INFO]: Edit ZONE ' + str(choice + 1) + ' areas in the Map ...')
        mainWindow.interact_obj.sig_send_editArea_to_js.emit(choice)

    def cleanEditJsonTextBroswer(self):
        mainWindow.textBrowser.append(__file__ + '\t[INFO]: Clean data from Map (QWebEngineView)...')
        self.editJsonTextBrowser.clear()

    def saveEditInfoAsFile(self):
        mainWindow.textBrowser.append(__file__ + '\t[INFO]: Try to saveEditInfoAsFile...')
        areaName = self.areaNameTextEdit.toPlainText()
        fileName, fileType = QFileDialog.getSaveFileName(self,
                                                         "Save as",
                                                         ROOT_PATH + '/data/temp/customAreas/' + 'AREA_' + areaName,
                                                         "JSON Files (*.json)")
        if fileName != "":
            with open(fileName, 'w') as f:
                context = self.editJsonTextBrowser.toPlainText()
                f.write(context)
            mainWindow.obstacles = (algo.loadGeoJsonFile(mainWindow.obstacles, fileName))
            print(mainWindow.obstacles)
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

class sim2_Widget(QWidget, simulation2Widget.Ui_simulation2Widget):
    def __init__(self, *args, **kwargs):
        super(sim2_Widget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.sim_coordTextBrowser.setFont(QFont('Consolas', 12))
        self.addStartPointPushButton.clicked.connect(self.signalAddStartToJs)
        self.addEndPointPushButton.clicked.connect(self.signalAddEndToJs)
        self.createPlanPushButton.clicked.connect(self.createPlan)
        self.startPoint = None
        self.endPoint = None
        self.currentPoint = None
        self.resolution = 1 / 10000

    def signalAddStartToJs(self):
        self.currentPoint = "Start"
        mainWindow.textBrowser.append(__file__ + '\t[INFO]: Adding a starting point for the path')
        mainWindow.interact_obj.sig_send_addStart_to_js.emit('end_point')

    def signalAddEndToJs(self):
        self.currentPoint = "End"
        mainWindow.textBrowser.append(__file__ + '\t[INFO]: Adding an ending point for the path')
        mainWindow.interact_obj.sig_send_addEnd_to_js.emit('start_point')

    def createPlan(self):
        mainWindow.interact_obj.sig_send_click_off_to_js.emit('click_off')
        mainWindow.textBrowser.append(__file__ + '\t[INFO]: Attempting to create path')
        if self.endPoint and self.startPoint :
            mainWindow.textBrowser.append(__file__ + '\t[INFO]: Creating path')
            autoFlightPlanFile = ROOT_PATH + '/data/temp/customLines/'+'AUTOFP_' + self.droneIdTextEdit.toPlainText() + '_' + self.flightDateTextEdit.toPlainText() + '.json'
            algo.createFlightPlan(mainWindow.obstacles,
                                  self.startPoint,
                                  self.endPoint,
                                  self.resolution,
                                  autoFlightPlanFile)
            mainWindow.textBrowser.append(__file__ + '\t[INFO]: Path created, saved as ' + autoFlightPlanFile)
            mainWindow.loadFlightPlanToMap(autoFlightPlanFile)
        else :
            mainWindow.textBrowser.append(__file__ + '\t[INFO]: Failed to create path, missing start or end point')

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
    sig_send_addStart_to_js = pyqtSignal(str)
    sig_send_addEnd_to_js = pyqtSignal(str)
    sig_send_click_off_to_js = pyqtSignal(str)
    sig_send_auto_flight_plan_jsonfile_to_js = pyqtSignal(str)
    sig_send_manual_path_to_js = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        # 交互对象接收到js调用后执行的回调函数.
        self.receive_str_from_js_callback = None
        self.receive_str_path_from_js_callback_auto = None
        self.receive_coord_from_js_callback = None

    # str表示接收str类型的信号,信号是从js发出的.
    @pyqtSlot(str)
    def receive_str_from_js(self, str):
        self.receive_str_from_js_callback(str)
        
    @pyqtSlot(str)
    def receive_str_path_from_js_auto(self, str):
        self.receive_str_path_from_js_callback_auto(str)

    @pyqtSlot(str)
    def receive_coord_from_js(self, str):
        self.receive_coord_from_js_callback(str)

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
        self.recvThreadPool = ThreadPool(max_workers=5)
        self.realTimePosition = ""

        # Load Javascript of map and initialisation
        self.index = (os.path.split(os.path.realpath(__file__))[0]) + "/index.html"
        self.webEngineView.load(QUrl.fromLocalFile(self.index))
        self.textBrowser.append(__file__ + '\t[INFO]: Initializing the interact object ...')
        self.init_channel()

        # Load and config different widgets pages
        self.qls = QStackedLayout(self.frame_main)

        self.mainW = main_Widget()
        self.editAreaW = editArea_Widget()
        self.editW = edit_Widget()
        self.sim1W = sim1_Widget()
        self.sim2W = sim2_Widget()

        self.qls.addWidget(self.mainW)
        self.qls.addWidget(self.editAreaW)
        self.qls.addWidget(self.editW)
        self.qls.addWidget(self.sim1W)
        self.qls.addWidget(self.sim2W)

        self.actionAdd_areas.triggered.connect(lambda: self.showWidgets(self.actionAdd_areas, self.qls))
        self.actionAdd_elements.triggered.connect(lambda: self.showWidgets(self.actionAdd_elements, self.qls))
        self.actionSimulationv1.triggered.connect(lambda: self.showWidgets(self.actionSimulationv1, self.qls))
        self.actionSimulation_v2.triggered.connect(lambda: self.showWidgets(self.actionSimulation_v2, self.qls))

        # Simulation v1 Button
        self.sim1W.importDroneFlightPlanButton.clicked.connect(self.importFlightPlanFile)
        self.sim1W.coordPushButton.clicked.connect(self.addCoordByBtn)
        self.sim1W.autoSimStartButton.clicked.connect(lambda : self.updateCoordDataByTimer(self.sim1W.setTimerSpinBox.value()))
        self.sim1W.autoSimStopButton.clicked.connect(self.stopUpdateCoordData)
        self.sim1W.autoSimPulseOrContinueButton.clicked.connect(self.pulseOrContinueUpdateCoordData)

        # Simulation v2 Button
        self.sim2W.importDroneFlightPlanButton.clicked.connect(self.importFlightPlanFile)
        self.sim2W.autoSimStartButton.clicked.connect(lambda: self.updateCoordDataByTimer(self.sim2W.setTimerSpinBox.value()))
        self.sim2W.autoSimStopButton.clicked.connect(self.stopUpdateCoordData)
        self.sim2W.autoSimPulseOrContinueButton.clicked.connect(self.pulseOrContinueUpdateCoordData)
        self.sim2W.manualPath.clicked.connect(self.manual_path)
        self.sim2W.automatic.clicked.connect(self.automaticPath)
        
        # Select a file
        self.actionImport_GeoJSON_File.triggered.connect(self.openFile)

        # Initial flightPlanFileName
        self.flightPlanFileName=""

        # Initial obstacles areas
        self.obstacles = []

        # socket to send status (pulse, continue or stop)
        self.socket = socket.socket()

    def showWidgets(self, button, qls):
        dic = {
            "Add areas": 1,
            "Add line": 2,
            "Simulation v1": 3,
            "Simulation v2": 4
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
        self.interact_obj.receive_str_path_from_js_callback_auto = self.receive_data_auto
        self.interact_obj.receive_coord_from_js_callback = self.receive_coord

        channel = QWebChannel(self.webEngineView.page())
        # interact_obj 为交互对象的名字,js中使用.
        channel.registerObject("interact_obj", self.interact_obj)

        self.webEngineView.page().setWebChannel(channel)

        self.thread_pool = QThreadPool()
        self.thread_pool.setMaxThreadCount(2)  # 只允许一个线程

    def receive_data(self, data):
        self.textBrowser.append(__file__ + '\t[INFO]: Receive data from Map (QWebEngineView)...')
        context = json.loads(data)
        if self.qls.currentWidget() == self.editW:
            JsonFormat = json.dumps(context, indent=4)
            self.editW.editJsonTextBrowser.setText(JsonFormat)
        elif self.qls.currentWidget() == self.editAreaW:
            updateContext = {"name": self.editAreaW.areaNameTextEdit.toPlainText(),
                             "description": self.editAreaW.areaInfoTextBrowser.toPlainText(),
                             "level": self.editAreaW.areaClassComboBox.currentIndex()}
            context.update(updateContext)
            JsonFormat = json.dumps(context, indent=4)
            self.editAreaW.editJsonTextBrowser.setText(JsonFormat)

    def receive_coord(self, data):
        self.textBrowser.append(__file__ + '\t[INFO]:' + data)
        point = data.split(",")
        if point[0] == 'start':
            self.sim2W.startPoint = shapely.geometry.Point(point[2], point[1])
            self.textBrowser.append(__file__ + '\t[INFO]: Create the START point: ' + str(self.sim2W.startPoint.coords.xy))
        else:
            self.sim2W.endPoint = shapely.geometry.Point(point[2], point[1])
            self.textBrowser.append(__file__ + '\t[INFO]: Create the END point: ' + str(self.sim2W.endPoint.coords.xy))
            
    def receive_data_auto(self, data):
        #receive data from EXPORT in index.html
        self.textBrowser.append(__file__ + '\t[INFO]: Receive data from Map (QWebEngineView)...')
        context = json.loads(data)
        JsonFormat = json.dumps(context, indent=4)
        self.editW.editJsonTextBrowser.setText(JsonFormat)
        #Export to JSON file
        mainWindow.textBrowser.append(__file__ + '\t[INFO]: Try to saveEditInfoAsFile...')
        droneId = "ManualPath"
        flightTime = "100000"
        fileName, fileType = QFileDialog.getSaveFileName(self,
                                                         "Save as",
                                                         ROOT_PATH + '/data/temp/customLines/'+'FP_'+droneId+'_'+flightTime,
                                                         "JSON Files (*.json)")
        if fileName != "":
            with open(fileName, 'w') as f:
                context = self.editW.editJsonTextBrowser.toPlainText()
                f.write(context)
        else:
            mainWindow.textBrowser.append(__file__ + '\t[WARNING]: Cancel to saveEditInfoAsFile')
        self.flightPlanFileName = ROOT_PATH + '/data/temp/customLines/'+"FP_ManualPath_100000.json"

    def manual_path(self):
        self.timer.stop()
        self.timer.deleteLater()
        #envoyer socket avec text = "pulse" à backend
        self.socket.send("ManualPath".encode())
        self.socket.close()
        self.interact_obj.sig_send_to_js.emit("ManualPath")  

    def automaticPath(self):
        self.timer.stop()
        self.timer.deleteLater()
        self.socket.send("ManualPath".encode())
        self.socket.close()
        coordStartPoint = mainWindow.realTimePosition.split(",")
        currentPosition= shapely.geometry.Point(coordStartPoint[1], coordStartPoint[0])
        print(currentPosition)
        with open(self.flightPlanFileName) as flightPlan:
            parsed_json = json.load(flightPlan)
        coordEndPoint = parsed_json['features'][0]['geometry']['coordinates'][-1]
        endPoint = shapely.geometry.Point(coordEndPoint[0], coordEndPoint[1])
        algo.createFlightPlan(self.obstacles, currentPosition, endPoint, self.sim2W.resolution, ROOT_PATH + '/data/temp/customLines/FP_updated_10000.json' )

        

        self.flightPlanFileName = ROOT_PATH + '/data/temp/customLines/FP_updated_10000.json'

        
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
        if self.qls.currentWidget() == self.sim1W:
            self.sim1W.sim_coordTextBrowser.append('[' + self.realTimePosition + ']')
        elif self.qls.currentWidget() == self.sim2W:
            self.sim2W.sim_coordTextBrowser.append('[' + self.realTimePosition + ']')

    def updateCoordDataByTimer(self, milliSecond):
        host = '127.0.0.1'
        port = 12349
        self.timer = QTimer(self)
        # self.recv_thread = RcvDataThread(self, '127.0.0.1', 12349)
        self.recvThreadPool.submit(RcvDataThread(self, host, port).run)
        self.timer.timeout.connect(self.updateCoordData)
        self.timer.start(milliSecond)
        self.textBrowser.append(__file__ + '\t[INFO]: Start automatic sampling...')
        task = SimulatorTask(Simulator(self.flightPlanFileName, host, port))

        statusTask = StatusReceiverTask(RcvCmdThread(self.flightPlanFileName, host, port+1))
        self.thread_pool.start(statusTask)
        self.thread_pool.start(task)
        try:
            self.socket = socket.socket()
            self.socket.connect((host, port+1))
        except Exception as e:
            print(f"Exception while trying to connect to ReceiverTask: {e}")
            return

    def stopUpdateCoordData(self):
        self.textBrowser.append(__file__ + '\t[INFO]: Stop automatic sampling...')
        self.timer.stop()
        self.timer.deleteLater()
        #envoyer socket avec text = "pulse" à backend
        self.socket.send("stop".encode())
        self.socket.close()
        if self.qls.currentWidget() == self.sim1W:
            self.sim1W.sim_coordTextBrowser.clear()
        elif self.qls.currentWidget() == self.sim2W:
            self.sim2W.sim_coordTextBrowser.clear()
        self.interact_obj.sig_send_to_js.emit('STOP')

    def pulseOrContinueUpdateCoordData(self):
        if self.timer.isActive():
            self.timer.stop()
            self.textBrowser.append(__file__ + '\t[INFO]: Pulse automatic sampling...')
            #envoyer socket avec text = "pulse" à backend
            self.socket.send("pulse".encode())
        else:
            self.timer.start()
            self.textBrowser.append(__file__ + '\t[INFO]: Continue automatic sampling...')
            #envoyer socket avec text="continue" à backend
            self.socket.send("continue".encode())

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
                self.obstacles = (algo.loadGeoJsonFile(self.obstacles, fileName))
                print(self.obstacles)
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

    def loadFlightPlanToMap(self, fileName):
        self.textBrowser.append(__file__ + '\t[INFO]: Try to Import JSON File...')
        if fileName != "":
            with open(fileName, 'r') as file:
                content = file.read()  # 读取文件内容
                self.textBrowser.append(__file__ + '\t[INFO]: Import the file : ' + fileName)
                self.interact_obj.sig_send_auto_flight_plan_jsonfile_to_js.emit(content)
        else:
            self.textBrowser.append(__file__ + '\t[WARNING]: Cancel to Import JSON File')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Window()
    mainWindow.show()
    sys.exit(app.exec_())

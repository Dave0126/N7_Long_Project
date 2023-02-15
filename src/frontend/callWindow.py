import json
import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
import folium
from folium import plugins
from PyQt5 import QtCore, QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWebEngineWidgets import *
import io
import numpy as np


#导入designer工具生成的 window 模块
import window

'''
Global param.
'''
coordinate = (43.60427946618452, 1.4369164843056978)
map = folium.Map(
            zoom_start=15,
            location=coordinate,
            tiles='cartodbpositronnolabels',
            control_scale="false"
        )


class Window(QMainWindow, window.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.setupUi(self)

        # Open JSON File 打开文件
        self.actionImport_JSON_file.triggered.connect(self.openFile)

        # Add Elements
        self.actionAdd_Position.triggered.connect(self.addElements)

        # Minimap
        minimap = folium.plugins.MiniMap(tile_layer='cartodbpositron', zoom_level_offset=-3)
        map.add_child(minimap)

        # GeoCoder (Searching box)
        plugin_geocoder = folium.plugins.Geocoder();
        plugin_geocoder.add_to(map)

        # Position
        formatter = "function(num) {return L.Util.formatNum(num, 5)};"
        plugin_hover = folium.plugins.MousePosition(
            position='topright',
            separator=' | ',
            empty_string='LNG. & LAT.',
            lng_first=False,
            num_digits=20,
            prefix='Coord. (DD) = ',
            lat_formatter=formatter,
            lng_formatter=formatter
        )
        map.add_child(plugin_hover)

        data = io.BytesIO()
        map.save(data, close_file=False)
        self.webEngineView.setHtml(data.getvalue().decode())

    def openFile(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self, "Select a JSON file", "/",
                                                                  "JSON File (*.js)")

        map.add_child(folium.GeoJson(fileName1, name='geojson'))
        data = io.BytesIO()
        map.save(data, close_file=False)
        self.webEngineView.setHtml(data.getvalue().decode())

        if fileName1:
            with open(fileName1, 'r') as file:
                content = file.read()  # 读取文件内容
                self.textBrowser.setText(content)


    def addElements(self):
        draw = folium.plugins.Draw(
            draw_options={
                'polyline': False,
                'rectangle': True,
                'polygon': True,
                'circle': False,
                'marker': True,
                'circlemarker': False},
            edit_options={'edit': False})
        map.add_child(draw)

        # Capture the json(msg) between webpage and api
        class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
            def javaScriptAlert(self, securityOrigin, msg):
                coords_dict = json.loads(msg)
                print(coords_dict)
                coords = coords_dict['geometry']['coordinates']
                array_coords = np.array(coords).squeeze()
                print(array_coords)

        data = io.BytesIO()
        map.save(data, close_file=False)
        page = WebEnginePage(self.webEngineView)
        self.webEngineView.setPage(page)
        self.webEngineView.setHtml(data.getvalue().decode())


if __name__ == "__main__":
  app = QApplication(sys.argv)
  w = Window()
  w.show()
  sys.exit(app.exec_())



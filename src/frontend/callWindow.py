import json
import sys
import folium
from folium import plugins
from PyQt5 import QtCore, QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWebEngineWidgets import *
import io
import numpy as np


# Import the window module generated by the designer tool (导入designer工具生成的 window 模块)
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
areaCount = 0
lineCount = 0



class Window(QMainWindow, window.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.setupUi(self)

        # Open JSON File (打开文件)
        self.actionImport_JSON_file.triggered.connect(self.openFile)

        # Add polyline by several points
        self.actionAdd_Position.triggered.connect(self.addPoint)

        # Add areas
        self.actionAdd_Area.triggered.connect(self.addAreas)

        '''
        ATTENTION:
            The above two methods will repeatedly call the folium.plugins.Draw() function, 
            so for the second called function, two JSON files with the same content will be written repeatedly.
        TODO:
            To fix the issues.
        '''

        # Minimap
        minimap = folium.plugins.MiniMap(tile_layer='cartodbpositron', zoom_level_offset=-3)
        map.add_child(minimap)

        # GeoCoder (Searching box)
        plugin_geocoder = folium.plugins.Geocoder();
        plugin_geocoder.add_to(map)

        # Get Position
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

        # To load map data
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


    def addAreas(self):
        draw1 = folium.plugins.Draw(
            draw_options={
                'polyline': False,
                'rectangle': True,
                'polygon': True,
                'circle': False,
                'marker': False,
                'circlemarker': False},
            edit_options={'edit': False})
        map.add_child(draw1)

        # Capture the json(msg) between webpage and api, and save as files in data/temp/customLines
        class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
            def javaScriptAlert(self, securityOrigin, msg):
                global areaCount
                coords_dict = json.loads(msg)
                dirPath = 'data/temp/customAreas/customArea%d.js'%areaCount
                areaCount += 1
                customJsonFile = open(dirPath, 'w')
                customJsonFile.write(msg)
                customJsonFile.close()
                map.add_child(folium.GeoJson(dirPath, name='geojson'))

                coords = coords_dict['geometry']['coordinates']
                array_coords = np.array(coords).squeeze()
                print(array_coords)

        data = io.BytesIO()
        map.save(data, close_file=False)
        page = WebEnginePage(self.webEngineView)
        self.webEngineView.setPage(page)
        self.webEngineView.setHtml(data.getvalue().decode())


    def addPoint(self):
        draw2 = folium.plugins.Draw(
            position="bottomleft",
            draw_options={
                'polyline': True,
                'rectangle': False,
                'polygon': False,
                'circle': False,
                'marker': True,
                'circlemarker': False},
            edit_options={'edit': False})
        map.add_child(draw2)

        # Capture the json(msg) between webpage and api, and save as files in data/temp/customLines
        class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
            def javaScriptAlert(self, securityOrigin, msg):

                global lineCount
                coords_dict = json.loads(msg)
                dirPath = 'data/temp/customLines/customLine%d.js' % lineCount
                lineCount += 1
                customJsonFile = open(dirPath, 'w')
                customJsonFile.write(msg)
                customJsonFile.close()
                map.add_child(folium.GeoJson(dirPath, name='geojson'))

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

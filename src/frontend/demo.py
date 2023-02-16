import json
import sys
import os
import io
import time

import numpy as np
import folium  # pip install folium
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtGui import QFont
from folium import plugins
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine

"""
Folium in PyQt5
"""


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('Folium in PyQt')
        self.setGeometry(10, 20, 1080, 720)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Toulouse coordinate
        ''' 
            lyrs can be set to different parameters, representing different forms of maps, you can try
            (lyrs可以设置为不同的参数，分别代表不同形式的地图，可以尝试)
        lyrs=
            h = roads only
            m = standard roadmap
            p = terrain
            r = somehow altered roadmap
            s = satellite only
            t = terrain only
            y = hybrid
        '''
        coordinate = (43.60427946618452, 1.4369164843056978)
        map = folium.Map(
            zoom_start=15,
            location=coordinate,
            tiles='cartodbpositronnolabels',
            # tiles='https://mt.google.com/vt/lyrs=&x={x}&y={y}&z={z}',  # GoogleMap
            control_scale="false"
        )
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
            prefix='LNG. & LAT. = ',
            lat_formatter=formatter,
            lng_formatter=formatter
        )
        map.add_child(plugin_hover)

        n7Marker = folium.Marker(location=[43.60217348605178, 1.4553929532627876],
                                 popup='ENSEEIHT',
                                 icon=folium.Icon(icon='info-sign',
                                                  color='blue'))

        map.add_child(child=n7Marker)

        '''
            Simulate real time recv from backend
        '''
        lat = 43.60427
        lng = 1.45539
        while True:
            lat += 0.005
            lng += 0.005
            map.add_child(folium.Marker(location=[lat, lng]))

            time.sleep(0.1)
            if lat>43.7: break

        # Create different areas from external json file in 'data/tests/frontend/'
        map.add_child(folium.GeoJson('../../data/tests/frontend/demo.json', name='geojson'))


        draw = folium.plugins.Draw(
            draw_options={
                'polyline': True,
                'rectangle': True,
                'polygon': True,
                'circle': False,
                'marker': True,
                'circlemarker': False},
            edit_options={'edit': False})
        map.add_child(draw)

        # save map data to data object
        data = io.BytesIO()
        map.save(data, close_file=False)

        # Capture the json(msg) between webpage and api
        class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
            def javaScriptAlert(self, securityOrigin, msg):
                coords_dict = json.loads(msg)
                print(coords_dict)
                coords = coords_dict['geometry']['coordinates']
                array_coords = np.array(coords).squeeze()
                print(array_coords)

        webView = QWebEngineView()
        page = WebEnginePage(webView)
        webView.setPage(page)
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setFont(QFont('Helvetica'))
    app.setStyleSheet(
        '''
            QWidget {
                font-size: 35px;
            }
        '''
    )

    myApp = MyApp()
    myApp.show()


    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
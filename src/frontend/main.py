import sys
import os
import io
import folium  # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine

"""
Folium in PyQt5
"""


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Folium in PyQt')
        self.setGeometry(10, 20, 1080, 720)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Toulouse coordinate
        coordinate = (43.60427946618452, 1.4369164843056978)
        map = folium.Map(
            tiles='Stamen Terrain',
            zoom_start=15,
            location=coordinate,
            control_scale="false"
        )

        n7Marker = folium.Marker(location=[43.60217348605178, 1.4553929532627876],
                                 popup='ENSEEIHT',
                                 icon=folium.Icon(icon='info-sign',
                                                  color='blue'))

        map.add_child(child=n7Marker)

        map.add_child(folium.GeoJson('data/tests/frontend/demo.js', name='geojson'))

        # global
        # m = folium.Map()

        # save map data to data object
        data = io.BytesIO()
        map.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')

    myApp = MyApp()
    myApp.show()


    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
import socket
import threading
import folium
import callWindow


class RcvDataThread(threading.Thread):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('127.0.0.1', 12349))
        self.socket.listen(1)  # listen for 1 incoming connection

    def run(self):
        print('hello in thread')
        # Connect to the socket
        conn, addr = self.socket.accept()
        
        with conn:
            # Continuously receive coordinates and update the map widget
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                coord = data.decode().split(',')
                print(coord)
                lat, lon = float(coord[0]), float(coord[1])
                #Todo : display coord (realtime data) on map 
                #self.map_widget.coords.append((lat, lon))
                #self.map_widget.update()



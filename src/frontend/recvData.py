import socket
import threading



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
                try: 
                    data = conn.recv(1024)
                except:
                    print("The connection is probably lost")
                if not data:
                    break
                coord = data.decode().split(',')
                #print(coord)
                self.window.realTimePosition = str(coord[0])+ "," + str(coord[1])
                print(self.window.realTimePosition)



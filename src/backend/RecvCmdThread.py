# Set up the socket connection
import socket
import threading
from PyQt5.QtCore import QThread, QRunnable
#from src.backend.classes.Drone import Drone

class RcvCmdThread(QThread):
    def __init__(self, flightPlanFileName, host, port):
        str_list = flightPlanFileName.split("_")
        droneID = str_list[1]
        flightDatetime = str_list[2].split(".")[0]
        #self.drone = Drone(droneID, flightDatetime)
        #self.drone.file_name = flightPlanFileName
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.s.bind((host, port))
        self.s.listen(1)  # listen for 1 incoming connection

    def run(self):
        global status 
        status = 0
        conn, addr = self.s.accept()
        with conn:
            while True : 
                try:
                    data = conn.recv(1024)
                    strData = data.decode()
                except:
                    print("The connection is probably lost")
                if not data:
                    break
                if strData == 'pulse':
                    status = 1
                else :
                    if strData == 'continue':
                        status = 2
                    else :
                        status = 3
        self.s.close()

class StatusReceiverTask(QRunnable):
    def __init__(self, rcvStatusTask):
        super().__init__()
        self.recvStatusTask = rcvStatusTask

    def run(self):
        try:
            self.recvStatusTask.run()
        except Exception as e:
            print(f"Exception in ReceiverTask: {e}")
        finally:
            self.recvStatusTask.s.close()

        

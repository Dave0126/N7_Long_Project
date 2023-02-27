import json
import random
import math
import socket
# from classes.Drone import Drone
from PyQt5.QtCore import QThread, QRunnable

from src.backend.classes.Drone import Drone

class Simulator(QThread):
    def __init__(self, flightPlanFileName):
        str_list = flightPlanFileName.split("_")
        droneID = str_list[1]
        flightDatetime = str_list[2].split(".")[0]
        self.drone = Drone(droneID, flightDatetime)
        self.drone.file_name = flightPlanFileName

    def run(self):
        # Compose the file name based on the extracted information
        '''with open('data/temp/customLines/' + self.drone.file_name) as flightPlan:
            parsed_json = json.load(flightPlan)'''
        with open(self.drone.file_name) as flightPlan:
            parsed_json = json.load(flightPlan)

        # Create a socket
        s = socket.socket()

        # Connect to the frontend
        try :
          s.connect(('127.0.0.1', 12349))
        except :
            print("The server is unreachable!")
            return
        # Extract the coordinates property of geometry
        # coordinates = parsed_json['geometry']['coordinates']
        coordinates = parsed_json['features'][0]['geometry']['coordinates']
        first = True # Usable to read the start position
        for c in coordinates:
            if first:
                start_longitude = c[0]
                start_latitude = c[1]
                start_altitude = 100
                first = False
                self.drone.start_position(start_latitude, start_longitude, start_altitude)
            else:
                next_longitude = c[0]
                next_latitude = c[1]
                next_altitude = 100
                # Move the drone along the route to the next point
                self.drone.move_to(next_latitude, next_longitude, next_altitude, s)

        s.close()

class SimulatorTask(QRunnable):
    def __init__(self, simulator):
        super().__init__()
        self.simulator = simulator

    def run(self):
        self.simulator.run()
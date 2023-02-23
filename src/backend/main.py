import json
import random
import math
import socket
from classes.Drone import Drone

class Simulator:
    def __init__(self, droneID="", flightDatetime="", _file_path=""):
        self.drone = Drone(droneID, flightDatetime)
        self.drone.file_name = _file_path

    def simulate_flight(self):
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
        coordinates = parsed_json['geometry']['coordinates']
        first = True # Usable to read the start position
        for c in coordinates:
            if first:
                start_latitude = c[0]
                start_longitude = c[1]
                start_altitude = 100
                first = False
                self.drone.start_position(start_latitude, start_longitude, start_altitude)
            else:
                next_latitude = c[0]
                next_longitude = c[1]
                next_altitude = 100
                # Move the drone along the route to the next point
                self.drone.move_to(next_latitude, next_longitude, next_altitude, s)

        s.close()

if __name__ == "__main__":
  sim = Simulator(_file_path = "D:/Users/mdris/Desktop/School/ENSEEIHT/Projet_long/N7_Long_Project/data/temp/customLines/test.json")
  sim.simulate_flight()
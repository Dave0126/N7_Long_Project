import json
import math
import os
import time

class Drone:
    def __init__(self, droneID, flightDatetime, latitude=0, longitude=0, altitude=0):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.droneID = droneID #This should be the reference of the drone 
        self.flightDatetime = flightDatetime # This should be the datetime of flight
        self.file_name = 'FP_'+self.droneID+'_'+self.flightDatetime+'.json' #Compose the file name based on the extracted informations
        self.realTimeFile = os.getcwd()+'/data/temp/realTimeData/realTimeCoordinates.json'

    def start_position(self, latitude, longitude, altitude) :
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        
    def create_real_time_data_file(self) : 
        data = {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "LineString",
                "coordinates": []
            }
        }
        with open(self.realTimeFile, 'w') as f:
            json.dump(data, f)

    def appendToJson(self, position) : 
        # Load the JSON file
        with open(self.realTimeFile, 'r') as f:
            data = json.load(f)

        # Append new coordinates
        new_coords = [position]
        data['geometry']['coordinates'].append(new_coords)

        # Save the updated JSON file
        with open(self.realTimeFile, 'w') as f:
            json.dump(data, f)


    def move_to(self, target_latitude, target_longitude, target_altitude):
        latitude_distance = target_latitude - self.latitude
        longitude_distance = target_longitude - self.longitude
        altitude_distance = target_altitude - self.altitude

        distance = math.sqrt(latitude_distance**2 + longitude_distance**2 + altitude_distance**2)

        steps = 10
        latitude_step = latitude_distance / steps
        longitude_step = longitude_distance / steps
        altitude_step = altitude_distance / steps

        for i in range(steps):
            self.latitude += latitude_step
            self.longitude += longitude_step
            self.altitude += altitude_step

            # Here we send the position to the frontend to be displayed
            position = str(self.latitude) +','+ str(self.longitude)#//+','+str(self.altitude)
            self.appendToJson([self.latitude,self.longitude])
            
            #s.send(position.encode()) 
            print(f"Drone at ({self.latitude}, {self.longitude}, {self.altitude:.2f})")
            #time.sleep(2)

    def __str__(self):
        return f"Drone at ({self.latitude:.2f}, {self.longitude:.2f}, {self.altitude:.2f})"
    
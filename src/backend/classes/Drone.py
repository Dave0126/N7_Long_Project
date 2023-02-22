import math
import socket
import time


class Drone:
    def __init__(self, latitude=0, longitude=0, altitude=0):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def start_psition(self, latitude, longitude, altitude):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def move_to(self, target_latitude, target_longitude, target_altitude):
        latitude_distance = target_latitude - self.latitude
        longitude_distance = target_longitude - self.longitude
        altitude_distance = target_altitude - self.altitude

        distance = math.sqrt(latitude_distance ** 2 + longitude_distance ** 2 + altitude_distance ** 2)

        steps = 10
        latitude_step = latitude_distance / steps
        longitude_step = longitude_distance / steps
        altitude_step = altitude_distance / steps

        # Create a socket
        s = socket.socket()

        # Connect to the frontend
        s.connect(('127.0.0.1', 12349))

        for i in range(steps):
            self.latitude += latitude_step
            self.longitude += longitude_step
            self.altitude += altitude_step

            # Here we send the position to the frontend to be displayed
            position = str(self.latitude) + ',' + str(self.longitude) + ',' + str(self.altitude)
            s.send(position.encode())
            print(f"Drone at ({self.latitude}, {self.longitude}, {self.altitude:.2f})")
            time.sleep(2)
        s.close()

    def __str__(self):
        return f"Drone at ({self.latitude:.2f}, {self.longitude:.2f}, {self.altitude:.2f})"

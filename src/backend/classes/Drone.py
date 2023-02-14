import math
import socket
import time

def send_position(position):
    # Create a socket
    s = socket.socket()

    # Connect to the frontend
    s.connect(('localhost', 12345))

    # Send the position
    s.send(position.encode())

    # Close the socket
    s.close()

class Drone:
    def __init__(self, latitude=0, longitude=0, altitude=0):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def start_psition(self, latitude, longitude, altitude) :
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def move_to(self, target_latitude, target_longitude, target_altitude):
        latitude_distance = target_latitude - self.latitude
        longitude_distance = target_longitude - self.longitude
        altitude_distance = target_altitude - self.altitude

        distance = math.sqrt(latitude_distance**2 + longitude_distance**2 + altitude_distance**2)

        steps = 100
        latitude_step = latitude_distance / steps
        longitude_step = longitude_distance / steps
        altitude_step = altitude_distance / steps

        for i in range(steps):
            self.latitude += latitude_step
            self.longitude += longitude_step
            self.altitude += altitude_step

            # Here we can send the position to the frontend to be displayed
            # send_position((self.latitude,self.longitude,self.altitude))
            print(f"Drone at ({self.latitude:.2f}, {self.longitude:.2f}, {self.altitude:.2f})")
            time.sleep(2)

    def __str__(self):
        return f"Drone at ({self.latitude:.2f}, {self.longitude:.2f}, {self.altitude:.2f})"
    
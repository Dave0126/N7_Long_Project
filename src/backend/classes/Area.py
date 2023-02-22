import math
import socket
import json

class Area:
    def __init__(self, zoneLabel = "default", JsonPath = ""):
        self.zoneLabel = zoneLabel
        self.jsonPath = JsonPath
        self.minAltitude = 0
        self.maxAltitude = 1000

    def change_minAlt(self, new_min):
        self.minAltitude = new_min
    
    def change_maxAlt(self, new_max):
        self.maxAltitude = new_max




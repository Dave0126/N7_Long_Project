import json
import random
import math

from classes.Drone import Drone

drone = Drone()

# Basically those coordinates are read from the flight plan file 
# We define the start and end points of the route (which must be read from the flight plan)
'''start_latitude = 43.60217
start_longitude = 1.45539
start_altitude = 100

# Initiate the first position
drone.start_psition(start_latitude, start_longitude, start_latitude)

# The flight plan is a set of points, every couple of points defines a section of the path
# So we need to loop over the file (path) and call the move_to function for every end point
# of every single section i.e. update the end_latitude/longitude/altitude parameters
end_latitude = 45.0
end_longitude = 2.0060
end_altitude = 500'''


# Extract the informations of the drone
droneID = 'D13' #This should be the reference of the drone 
flightDatetime = '150220231923' # This should be the datetime of flight

#Compose the file name based on the extracted informations
file_name = 'FP_'+droneID+'_'+flightDatetime+'.json'
with open("data/tests/backend/"+file_name) as flightPlan:
  parsed_json = json.load(flightPlan)

#Extract the coordinates property of geometry
coordinates = parsed_json['geometry']['coordinates']
first = True # Usable to read the start position
for c in coordinates:
  print(c)
  if(first) :
    start_latitude = c[0]
    start_longitude = c[1]
    start_altitude = 100
    first = False
    drone.start_psition(start_latitude, start_longitude, start_altitude)
  else :
    next_latitude = c[0]
    next_longitude = c[1]
    next_altitude = 100
    # Move the drone along the route to the next point
    drone.move_to(next_latitude, next_longitude, next_altitude)
  
#print(coordinates)
#drone.move_to(end_latitude, end_longitude, end_altitude)

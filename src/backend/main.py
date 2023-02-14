import random
import math

from classes.Drone import Drone

drone = Drone()

# Basically those coordinates are read from the flight plan file 
# We define the start and end points of the route (which must be read from the flight plan)
start_latitude = 37.7749
start_longitude = -122.4194
start_altitude = 0

# Initiate the first position
drone.start_psition(start_latitude, start_longitude, start_latitude)

# The flight plan is a set of points, every couple of points defines a section of the path
# So we need to loop over the file (path) and call the move_to function for every end point
# of every single section i.e. update the end_latitude/longitude/altitude parameters
end_latitude = 40.7128
end_longitude = -74.0060
end_altitude = 1000


# Move the drone along the route
drone.move_to(end_latitude, end_longitude, end_altitude)

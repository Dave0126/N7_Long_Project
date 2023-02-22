import json
from Drone import Drone

class Simulator:
    def __init__(self, drone_id, flight_datetime):
        self.drone = Drone(drone_id, flight_datetime)

    def run_simulation(self):
        with open('data/temp/customLines/' + self.drone.file_name) as flight_plan:
            parsed_json = json.load(flight_plan)

        coordinates = parsed_json['geometry']['coordinates']
        first = True
        for c in coordinates:
            if first:
                start_latitude = c[0]
                start_longitude = c[1]
                start_altitude = 100
                self.drone.start_position(start_latitude, start_longitude, start_altitude)
                self.drone.create_real_time_data_file()
                first = False
            else:
                next_latitude = c[0]
                next_longitude = c[1]
                next_altitude = 100
                self.drone.move_to(next_latitude, next_longitude, next_altitude)

if __name__ == "__main__":
  sim = Simulator("D13",'150220231923')
  sim.run_simulation()
import collections
import collections.abc
collections.MutableMapping = collections.abc.MutableMapping

import math
import random
import time
import matplotlib.pyplot as plt
from dronekit import LocationGlobalRelative, Command, VehicleMode
from pymavlink import mavutil

def connect_mock():
    class MockVehicle:
        def __init__(self):
            self.commands = []
            self.mode = VehicleMode("GUIDED")
            self.location = LocationGlobalRelative(37.7749, -122.4194, 0)
            self.armed = False
            self.next_waypoint = 0
            self.mission_time = 0
            self.mission_distance = 0

        def close(self):
            print("Vehicle connection closed.")

        def arm(self):
            self.armed = True
            print("Motors armed.")

        def takeoff(self, altitude):
            print(f"Taking off to {altitude} meters.")
            self.location.alt = altitude

        def goto(self, location):
            print(f"Going to: Lat={location['lat']}, Lon={location['lon']}, Alt={location['alt']}")
            self.location = LocationGlobalRelative(location['lat'], location['lon'], location['alt'])

        def update_mission(self, commands):
            self.commands = commands
            self.next_waypoint = 0

        def set_next_waypoint(self, index):
            self.next_waypoint = index

        def get_mission_time(self):
            return self.mission_time

        def get_mission_distance(self):
            return self.mission_distance

    return MockVehicle()

# Function to generate random waypoints with perturbations
def generate_waypoints(home_loc, num = 15):
    waypoints = []
    for i in range(num):
        lat = home_loc['lat'] + (i * 0.0001) + random.uniform(-0.00005, 0.00005)
        lon = home_loc['lon'] + (i * 0.0001) + random.uniform(-0.00005, 0.00005)
        alt = 30  
        waypoints.append({'lat': lat, 'lon': lon, 'alt': alt})
        
    waypoints[-1]['alt'] = 0  
    
    return waypoints

# Function to calculate perpendicular point
def perpendicular_point(p1, p2, distance=100):
    lat1 = math.radians(p1['lat'])
    lon1 = math.radians(p1['lon'])
    lat2 = math.radians(p2['lat'])
    lon2 = math.radians(p2['lon'])
    
    dLon = lon2 - lon1
    y = math.sin(dLon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dLon)
    bearing = math.atan2(y, x)
    
    bearing_perp = bearing + math.pi / 2
    brng = math.degrees(bearing_perp)
    
    angular_distance = distance / 6371000 
    lat3 = math.asin(math.sin(lat2) * math.cos(angular_distance) +
                      math.cos(lat2) * math.sin(angular_distance) * math.cos(bearing_perp))
    lon3 = lon2 + math.atan2(math.sin(bearing_perp) * math.sin(angular_distance) * math.cos(lat2),
                              math.cos(angular_distance) - math.sin(lat2) * math.sin(lat3))
    
    lat3 = math.degrees(lat3)
    lon3 = math.degrees(lon3)
    
    return {'lat': lat3, 'lon': lon3, 'alt': p2['alt']}

# Haversine formula to calculate distance between two points
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # Earth radius in meters
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

class Mission:
    def __init__(self, home_loc, num_waypoints=15):
        self.home_loc = home_loc
        self.waypoints = generate_waypoints(home_loc, num_waypoints)
        self.commands = self.create_commands()

    def create_commands(self):
        commands = []
        for wp in self.waypoints:
            cmd = Command(
                0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0,
                wp['lat'], wp['lon'], wp['alt']
            )
            commands.append(cmd)
        return commands

    def add_waypoint(self, index, waypoint):
        self.waypoints.insert(index, waypoint)
        self.commands.insert(index, Command(
            0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
            mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0,
            waypoint['lat'], waypoint['lon'], waypoint['alt']
        ))

def main():
    # Simulate connecting to a vehicle
    print("Connecting to vehicle...")
    vehicle = connect_mock()
    print("Connected to vehicle!")

    # Home location (simulated)
    home_loc = {'lat': 37.7749, 'lon': -122.4194, 'alt': 0}
    mission = Mission(home_loc)

    # Upload the mission
    vehicle.update_mission(mission.commands)
    print("Mission uploaded.")

    # Arm and takeoff to the first waypoint altitude
    vehicle.arm()
    vehicle.takeoff(mission.waypoints[0]['alt'])

    # Simulate mission execution in auto mode
    vehicle.mode = VehicleMode("AUTO")
    print("Switched to AUTO mode.")

    # Simulate mission progress
    for i in range(len(mission.waypoints)):
        wp = mission.waypoints[i]
        print(f"Reached waypoint {i + 1}: Lat={wp['lat']}, Lon={wp['lon']}, Alt={wp['alt']}")
        
        vehicle.goto(wp)
        vehicle.set_next_waypoint(i + 1)

        # Calculate mission time and distance using Haversine formula
        if i > 0:
            prev_wp = mission.waypoints[i - 1]
            distance = haversine(prev_wp['lat'], prev_wp['lon'], wp['lat'], wp['lon'])
            vehicle.mission_distance += distance
            
            # Assume a speed of 5 m/s for time estimation
            vehicle.mission_time += distance / 5  # Time in seconds

        remaining_distance = sum(haversine(mission.waypoints[j]['lat'], mission.waypoints[j]['lon'],
                                           mission.waypoints[j+1]['lat'], mission.waypoints[j+1]['lon'])
                                 for j in range(i, len(mission.waypoints)-1))
        
        estimated_time = vehicle.mission_time + remaining_distance / 5  # Assuming 5 m/s
        
        print(f"Estimated time to complete mission: {estimated_time} seconds")
        print(f"Estimated distance to complete mission: {vehicle.mission_distance + remaining_distance} meters")
        print('\n')
        # Add a new waypoint after 10 waypoints
        if i == 9:
            new_wp = perpendicular_point(mission.waypoints[8], mission.waypoints[9])
            mission.add_waypoint(10, new_wp)
            vehicle.update_mission(mission.commands)
            
            print(f"New waypoint added at position 10: Lat={new_wp['lat']}, Lon={new_wp['lon']}, Alt={new_wp['alt']}")
            print('\n')

        time.sleep(1)  # Simulate time delay

    print("Mission completed.")

    lats = [wp['lat'] for wp in mission.waypoints]
    lons = [wp['lon'] for wp in mission.waypoints]
    plt.plot(lons, lats, 'ro-')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Simulated Drone Flight Path')
    plt.show()

    vehicle.close()

if __name__ == "__main__":
    main()
# Problem 2: Drone Simulation and Control

## Problem Overview and Description

This problem involves planning a mission for a quadcopter using a predefined set of 15 waypoints, each containing latitude (lat), longitude (lon), and altitude (alt) values. The mission is executed in auto mode using Dronekit or pymavlink, with the drone landing at the last waypoint. After reaching the 10th waypoint, a new waypoint is added to the mission, positioned 100 meters perpendicular to the current direction of travel, and the drone continues with the updated mission. Throughout the mission, the estimated time and distance to completion are printed at every instance. Finally, the path of travel is plotted in 2D to visualize the mission.

---

## Algorithm Overview

### 1. Setup and Mock Vehicle Connection
- **Define `connect_mock()` Function**:
  - Creates a `MockVehicle` class to simulate a drone vehicle.
  - The mock vehicle has methods to mimic vehicle behavior such as arming, taking off, moving to locations, and managing missions.

### 2. Waypoint Generation and Perpendicular Point Calculation
- **Define `generate_waypoints()` Function**:
  - Generates a list of waypoints starting from a home location.
  - Introduces random perturbations in latitude and longitude.
  - Sets an altitude of 30 meters for all waypoints except the last one, which is set to 0 meters.

- **Define `perpendicular_point()` Function**:
  - Calculates a point perpendicular to the line between two given points.
  - Uses bearing calculations to determine the new point at a specified distance.

- **Define `haversine()` Function**:
  - Computes the distance between two points on the Earth's surface using the Haversine formula.

### 3. Mission Creation and Management
- **Define `Mission` Class**:
  - Initializes with a home location and a number of waypoints.
  - Uses `generate_waypoints()` to create a list of waypoints.
  - Creates mission commands for each waypoint using `dronekit.Command`.

- **Add Waypoint Method**:
  - Inserts a new waypoint into the mission at a specified index.
  - Updates the mission commands accordingly.

### 4. Main Execution Flow
- **Connect to Mock Vehicle**:
  - Simulates connecting to a drone vehicle.
  - Sets the home location.

- **Create and Upload Mission**:
  - Initializes a `Mission` object with the home location.
  - Uploads the mission to the mock vehicle.

- **Arm and Takeoff**:
  - Arms the vehicle and takes off to the altitude of the first waypoint.

- **Simulate Mission Execution**:
  - Switches the vehicle to AUTO mode to start the mission.
  - Iterates through the waypoints, simulating reaching each one.
  - Updates the vehicle's location and next waypoint index.
  - Calculates and prints the estimated time and distance remaining to complete the mission.

- **Dynamic Waypoint Addition**:
  - After reaching the 10th waypoint, adds a new waypoint perpendicular to the line between the 8th and 9th waypoints.
  - Updates the mission with the new waypoint.

- **Simulate Time Delay**:
  - Uses `time.sleep(1)` to simulate the passage of time between waypoints.

- **Mission Completion**:
  - Prints a completion message when all waypoints are reached.

- **Plot Flight Path**:
  - Uses `matplotlib.pyplot` to plot the latitude and longitude of the waypoints.
  - Displays the flight path as a route on a 2D plot.

- **Close Vehicle Connection**:
  - Simulates closing the connection to the vehicle.

---

## Code Exploration

### `connect_mock()` Function
The `connect_mock()` function creates a simulated drone, or "mock vehicle," which allows for the testing of mission planning and execution logic without the need for a physical drone. This mock vehicle, defined within the function, has attributes and methods that mimic the behavior of a real drone, such as arming, taking off, navigating to waypoints, and managing mission commands.

### `generate_waypoints()`
This function is used to create a realistic flight path for the drone mission. The perturbations in latitude and longitude simulate real-world GPS inaccuracies or environmental factors, while the linear progression ensures the drone moves in a general direction. The fixed altitude (except for the last waypoint) ensures the drone maintains a consistent height during the mission, with a safe landing at the end.

### `perpendicular_point()`
The `perpendicular_point(p1, p2, distance=100)` function calculates a new geographic point that is perpendicular to the line connecting two given points (`p1` and `p2`) at a specified distance. It uses the latitude and longitude of the input points to compute the direction (bearing) between them, then calculates a new bearing that is 90 degrees offset from the original. Using the Earth's radius and trigonometric formulas, it determines the coordinates of the new point at the specified perpendicular distance, ensuring the calculation accounts for the Earth's curvature.

### `haversine()`
The `haversine()` function calculates the great-circle distance between two points on the Earth's surface, given their latitude and longitude in degrees. This is based on the Haversine formula, which accounts for the Earth's curvature to provide an accurate distance measurement.

---

## `Mission` Class
The `Mission` class manages the planning and execution of the drone mission by generating a sequence of waypoints starting from a specified home location and converting them into MAVLink commands. The class also provides the `add_waypoint()` method to dynamically insert new waypoints into the mission at a specified index, allowing for real-time adjustments.

---

## Main()
The `main()` function simulates the complete drone mission from start to finish, beginning with connecting to the mock vehicle and defining a home location. The mission concludes by plotting the flight path using `matplotlib` and closing the vehicle connection. This function encapsulates the entire mission lifecycle, including planning, execution, real-time adjustments, and visualization, providing a comprehensive simulation of the drone operations.


## How to Run the Program

To run the program, first clone the repository using `git clone <repository-link>`, then navigate to the cloned directory using `cd <repository-name>`. Finally, execute the program by running the command `python3 Question-2/Drone.py`. Replace `<repository-link>` with the repository URL and `<repository-name>` with the name of the cloned repository.

## Output


![Alt text](/Question-2/Images/image1.png)
![Alt text](/Question-2/Images/image2.png)
![Alt text](/Question-2/Images/image3.png)
![Alt text](/Question-2/Images/image4.png)

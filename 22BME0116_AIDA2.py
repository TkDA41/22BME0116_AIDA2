import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables
vehicle_density = ctrl.Antecedent(np.arange(0, 101, 1), 'vehicle_density')  # Input: Number of vehicles
waiting_time = ctrl.Antecedent(np.arange(0, 11, 1), 'waiting_time')         # Input: Waiting time in minutes
green_light_duration = ctrl.Consequent(np.arange(0, 61, 1), 'green_light_duration')  # Output: Green light duration in seconds

# Define membership functions for vehicle density
vehicle_density['low'] = fuzz.trimf(vehicle_density.universe, [0, 0, 30])
vehicle_density['medium'] = fuzz.trimf(vehicle_density.universe, [20, 50, 80])
vehicle_density['high'] = fuzz.trimf(vehicle_density.universe, [70, 100, 100])

# Define membership functions for waiting time
waiting_time['short'] = fuzz.trimf(waiting_time.universe, [0, 0, 3])
waiting_time['medium'] = fuzz.trimf(waiting_time.universe, [2, 5, 8])
waiting_time['long'] = fuzz.trimf(waiting_time.universe, [7, 10, 10])

# Define membership functions for green light duration
green_light_duration['short'] = fuzz.trimf(green_light_duration.universe, [0, 0, 20])
green_light_duration['medium'] = fuzz.trimf(green_light_duration.universe, [15, 30, 45])
green_light_duration['long'] = fuzz.trimf(green_light_duration.universe, [40, 60, 60])

# Define fuzzy rules
rule1 = ctrl.Rule(vehicle_density['low'] & waiting_time['short'], green_light_duration['short'])
rule2 = ctrl.Rule(vehicle_density['medium'] & waiting_time['medium'], green_light_duration['medium'])
rule3 = ctrl.Rule(vehicle_density['high'] | waiting_time['long'], green_light_duration['long'])

# Create control system
traffic_control_system = ctrl.ControlSystem([rule1, rule2, rule3])
traffic_simulation = ctrl.ControlSystemSimulation(traffic_control_system)

# Simulate the system with input values
traffic_simulation.input['vehicle_density'] =10   # Example: low vehicle density
traffic_simulation.input['waiting_time'] = 2       # Example: medium waiting time

traffic_simulation.compute()

# Output the result
print(f"Recommended Green Light Duration: {traffic_simulation.output['green_light_duration']} seconds")

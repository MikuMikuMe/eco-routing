Creating an eco-routing application requires integrating multiple components such as real-time traffic data, route optimization algorithms, and fuel-efficiency calculations. For simplicity, this example will illustrate the concept using mock data and a simple model. In a production environment, you would integrate this with real-world systems like traffic APIs (e.g., Google Maps API, HERE Technologies) and ensure comprehensive error handling for external requests. Below is a basic Python program to achieve this:

```python
import json
import random

# Define mock route and traffic data
MOCK_TRAFFIC_DATA = {
    "route_1": {"distance_km": 10, "traffic_condition": 1.2},   # Multiplier for light traffic
    "route_2": {"distance_km": 12, "traffic_condition": 1.0},   # No traffic
    "route_3": {"distance_km": 8, "traffic_condition": 1.5}     # Multiplier for heavy traffic
}

# Assume a function to simulate fetching real-time traffic data
def fetch_real_time_traffic_data():
    # In an actual implementation, this function would call a web API
    # Here, we will use mock data
    try:
        # Simulate network delay
        network_delay = random.uniform(0, 0.2)
        if network_delay >= 0.15:
            raise ConnectionError("Network timeout.")
        
        # Simulate the chance of API failure
        if random.choice([True, False]):
            return MOCK_TRAFFIC_DATA
        else:
            raise ValueError("Failed to fetch traffic data.")
    except (ConnectionError, ValueError) as e:
        print(f"Error fetching traffic data: {e}")
        return None

# Calculate fuel efficiency based on distance and traffic condition
def calculate_fuel_efficiency(distance_km, traffic_condition):
    # Assume fuel consumption increases linearly with traffic condition
    base_fuel_efficiency = 7.0 # Base efficiency: liters per 100 km
    fuel_consumption = (distance_km / 100) * base_fuel_efficiency * traffic_condition
    return fuel_consumption

# Determine the most eco-friendly route
def find_most_efficient_route(traffic_data):
    try:
        if not traffic_data:
            raise ValueError("Traffic data is not available.")
        
        best_route = None
        min_fuel_consumption = float('inf')

        for route, data in traffic_data.items():
            fuel_consumption = calculate_fuel_efficiency(data['distance_km'], data['traffic_condition'])
            if fuel_consumption < min_fuel_consumption:
                min_fuel_consumption = fuel_consumption
                best_route = route
        
        return best_route, min_fuel_consumption
    except ValueError as e:
        print(f"Error in finding route: {e}")
        return None, None

def main():
    print("Fetching real-time traffic data...")
    traffic_data = fetch_real_time_traffic_data()
    
    print("Calculating the most efficient route...")
    best_route, fuel_consumption = find_most_efficient_route(traffic_data)
    
    if best_route:
        print(f"The most fuel-efficient route is {best_route} with a fuel consumption of {fuel_consumption:.2f} liters.")
    else:
        print("Could not determine the most efficient route due to errors.")

if __name__ == "__main__":
    main()
```

### Key Features:

- **Mock Traffic Data**: This example uses mock data to simulate traffic data. In a real implementation, you’d replace this with an API call to a service like Google Maps or HERE Technologies.

- **Error Handling**: The program handles errors that might occur during data fetching and processing, such as network issues or bad data.

- **Simplistic Fuel Efficiency Model**: It considers the impact of traffic on fuel consumption using a linear model. A more complex model could account for factors like vehicle type, speed changes, and road conditions.

- **Eco-Routing Logic**: The algorithm calculates and selects the route with the least fuel consumption.

This code is a basic representation to demonstrate an approach to eco-routing. For real-world applications, consider using actual APIs, comprehensive error handling, more sophisticated models, and user interfaces for input/output.
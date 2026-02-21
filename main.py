import pandas as pd
import folium
import os

from distance_matrix import create_distance_matrix
from optimizer import solve_vrp

# Load data
df = pd.read_csv("data/locations.csv")

locations = list(zip(df["lat"], df["lon"]))

# Create distance matrix
distance_matrix = create_distance_matrix(locations)

# Solve VRP (2 vehicles)
routes = solve_vrp(distance_matrix, num_vehicles=2)

# Create map
m = folium.Map(location=locations[0], zoom_start=13)

colors = ["blue", "green", "purple"]

total_distance = 0

for vehicle_id, route in enumerate(routes):
    route_coords = []
    vehicle_distance = 0

    for i in range(len(route)):
        lat, lon = locations[route[i]]
        route_coords.append((lat, lon))

        folium.Marker(
            location=(lat, lon),
            popup=f"Vehicle {vehicle_id+1} - Stop {i+1}",
            icon=folium.Icon(color=colors[vehicle_id])
        ).add_to(m)

        if i > 0:
            vehicle_distance += distance_matrix[route[i-1]][route[i]]

    total_distance += vehicle_distance

    folium.PolyLine(route_coords, color=colors[vehicle_id]).add_to(m)

    print(f"Vehicle {vehicle_id+1} Distance: {vehicle_distance:.2f} km")

print(f"\nTotal Distance: {total_distance:.2f} km")
print(f"Total Stops: {len(locations)-1}")

# Save output
os.makedirs("outputs", exist_ok=True)
m.save("outputs/route_map.html")

print("\nMap saved to outputs/route_map.html")
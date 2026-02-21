import folium
from folium.plugins import MarkerCluster

# -----------------------------
# Example Data (Replace with your actual data)
# -----------------------------

warehouse = [18.5204, 73.8567]  # Pune Warehouse

delivery_points = [
    [18.5314, 73.8446],
    [18.5100, 73.8790],
    [18.4950, 73.8200],
    [18.5600, 73.9000],
    [18.4800, 73.8500]
]

traffic_levels = ["low", "medium", "high", "low", "high"]

# -----------------------------
# Create Map (Improved Zoom)
# -----------------------------

m = folium.Map(
    location=warehouse,
    zoom_start=11,
    tiles="OpenStreetMap"
)

# -----------------------------
# Add Title
# -----------------------------

title_html = """
<h3 align="center" style="font-size:22px">
<b>🚦 Traffic-Aware Last Mile Route Optimization</b>
</h3>
"""
m.get_root().html.add_child(folium.Element(title_html))

# -----------------------------
# Add Warehouse Marker
# -----------------------------

folium.Marker(
    location=warehouse,
    popup="Warehouse",
    icon=folium.Icon(color="red", icon="home", prefix="fa")
).add_to(m)

# -----------------------------
# Marker Cluster for Delivery Points
# -----------------------------

marker_cluster = MarkerCluster().add_to(m)

for point, traffic in zip(delivery_points, traffic_levels):

    if traffic == "low":
        color = "green"
    elif traffic == "medium":
        color = "orange"
    else:
        color = "red"

    folium.Marker(
        location=point,
        popup=f"Traffic Level: {traffic.capitalize()}",
        icon=folium.Icon(color=color, icon="shopping-cart", prefix="fa")
    ).add_to(marker_cluster)

# -----------------------------
# Draw Optimized Route Line
# -----------------------------

route_coordinates = [warehouse] + delivery_points + [warehouse]

folium.PolyLine(
    locations=route_coordinates,
    color="blue",
    weight=4,
    opacity=0.8
).add_to(m)

# -----------------------------
# Add Traffic Legend
# -----------------------------

legend_html = """
<div style="
position: fixed; 
bottom: 50px; left: 50px; width: 200px; height: 120px; 
background-color: white; 
border:2px solid grey; 
z-index:9999; 
font-size:14px;
padding: 10px;
">
<b>Traffic Levels</b><br>
🟢 Low Traffic<br>
🟡 Medium Traffic<br>
🔴 High Traffic
</div>
"""

m.get_root().html.add_child(folium.Element(legend_html))

# -----------------------------
# Save Map
# -----------------------------

m.save("outputs/advanced_map_with_traffic.html")

print("✅ Advanced traffic map generated successfully!")
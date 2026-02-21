import numpy as np
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c

def create_distance_matrix(locations):
    size = len(locations)
    matrix = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i][j] = haversine(
                    locations[i][0], locations[i][1],
                    locations[j][0], locations[j][1]
                )
    return matrix
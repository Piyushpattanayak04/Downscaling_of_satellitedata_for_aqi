import random

# Delhi bounding box
DELHI_BOUNDS = {
    "lat_min": 28.4,
    "lat_max": 28.9,
    "lon_min": 76.8,
    "lon_max": 77.4
}

def generate_satellite_grid(n_points=20):
    points = []

    for _ in range(n_points):
        lat = random.uniform(DELHI_BOUNDS["lat_min"], DELHI_BOUNDS["lat_max"])
        lon = random.uniform(DELHI_BOUNDS["lon_min"], DELHI_BOUNDS["lon_max"])

        # simulate satellite NO2
        no2 = random.uniform(20, 120)

        points.append({
            "lat": lat,
            "lon": lon,
            "no2": no2
        })

    return points
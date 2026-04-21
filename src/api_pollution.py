import requests

def get_pollution(city):
    url = f"https://api.openaq.org/v2/latest?city={city}&limit=50"
    data = requests.get(url).json()

    results = []

    for item in data.get("results", []):
        try:
            pollutants = {m["parameter"]: m["value"] for m in item["measurements"]}

            results.append({
                "location": item["location"],
                "pm25": pollutants.get("pm25", 0),
                "pm10": pollutants.get("pm10", 0),
                "no2": pollutants.get("no2", 0)
            })
        except:
            continue

    return results


def get_pollution_history(city):
    url = f"https://api.openaq.org/v2/measurements?city={city}&parameter=no2&limit=100"
    data = requests.get(url).json()

    history = []

    for item in data.get("results", []):
        try:
            history.append(item["value"])
        except:
            continue

    return history[:10]
def pollution_score(pm25, pm10, no2):
    return (pm25 * 0.5) + (pm10 * 0.3) + (no2 * 0.2)


def locality_type(location):
    location = location.lower()

    if "industrial" in location:
        return "Industrial"
    elif "road" in location or "traffic" in location:
        return "Traffic"
    elif "residential" in location:
        return "Residential"
    else:
        return "Mixed"


def detailed_reason(aqi, area, pm25):
    if pm25 > 100:
        return "High AQI due to PM2.5 (fine particles)"
    elif area == "Traffic":
        return "Vehicle emissions causing AQI rise"
    elif area == "Industrial":
        return "Industrial pollution contributing heavily"
    else:
        return "Mixed pollution sources"
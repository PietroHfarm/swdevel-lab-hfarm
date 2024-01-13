from geopy.distance import geodesic


def calcola_distanza(lat1, lon1, lat2, lon2):
    """
    Calculates the distance between two
    geographical points using the geodesic method.

    Parameters:
        lat1 (float): Latitude of the first point.
        lon1 (float): Longitude of the first point.
        lat2 (float): Latitude of the second point.
        lon2 (float): Longitude of the second point.

    Returns:
        float or -1: The distance in meters
        between the two points if coordinates are valid,
        or -1 if any latitude or longitude is less than 0.0.
    """
    if (-90 <= lat1 <= 90 or -90 <= lon1 <= 90):
        return geodesic((lat1, lon1), (lat2, lon2)).meters
    else:
        return -1

from geopy.distance import geodesic


def calcola_distanza(lat1, lon1, lat2, lon2):
    if (lat1 < 0.0 or lon1 < 0.0):
        return False
    else:
        return geodesic((lat1, lon1), (lat2, lon2)).meters


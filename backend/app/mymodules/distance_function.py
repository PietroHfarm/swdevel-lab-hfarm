from geopy.distance import geodesic

def calcola_distanza(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon2)).meters
    
"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI, Query, HTTPException
from .mymodules.csv_reading_function import leggi_dati_da_csv
from .mymodules.distance_function import calcola_distanza
import os

app = FastAPI()

current_file_path = os.path.abspath(__file__)


@app.get('/poste')
def get_poste(lat: float = Query(0, title='Latitude',
                                 description='Default latitude'),
              lon: float = Query(0, title='Longitude',
                                 description='Default longitude'),
              radius: float = Query(100, title='Radius',
                                    description='Radius in meters')
              ):
                  
    """
    Retrieve postal data within a specified radius
    from given latitude and longitude.

    Parameters:
    - lat (float): Latitude coordinate. Defaults to 0 if not provided.
    - lon (float): Longitude coordinate. Defaults to 0 if not provided.
    - raggio (float): Radius default to 100 meters
    for filtering postal data.

    Returns:
    - dict: JSON response containing filtered
    postal data within the specified radius.

    Algorithm:
    1. Read data from the CSV file using the function leggi_dati_da_csv.
    2. Filter postal data within the specified radius:
       - Iterate through postal data.
       - Calculate the distance between provided
       coordinates and postal data coordinates.
       - Add postal data falling within the specified
       radius to the result.
    3. Return the filtered postal data within the radius as a JSON response.

    """
    poste_data = leggi_dati_da_csv("/app/app/poste.csv")

    poste_in_radius = []
    for poste in poste_data:
        distance = calcola_distanza(lat, lon, float(
            poste['LAT_Y_4326']), float(poste['LONG_X_4326']))
        if distance is not False:
            if distance <= radius:
                poste_in_radius.append(poste)
        else:
            raise HTTPException(
                status_code=400, detail="Distance or radius error")

    return {"poste": poste_in_radius}


@app.get('/farmacie')
def get_farmacie(lat: float = Query(0,
                                    title='Latitude',
                                    description='Default latitude'),
                 lon: float = Query(0,
                                    title='Longitude',
                                    description='Default longitude'),
                 radius: float = Query(100,
                                       title='Radius',
                                       description='Radius in meters')
                 ):
    
    """
    Retrieve pharmaceutical data within a specified radius
    from given latitude and longitude.

    Parameters:
    - lat (float): Latitude coordinate. Defaults to 0 if not provided.
    - lon (float): Longitude coordinate. Defaults to 0 if not provided.
    - raggio (float): Radius default to 100 meters
    for filtering pharmaceutical data.

    Returns:
    - dict: JSON response containing filtered
    pharmaceutical data within the specified radius.

    Algorithm:
    1. Read data from the CSV file using the function leggi_dati_da_csv.
    2. Filter pharmaceutical data within the specified radius:
       - Iterate through pharmaceutical data.
       - Calculate the distance between provided
       coordinates and pharmaceutical data coordinates.
       - Add pharmaceutical data falling within the specified
       radius to the result.
    3. Return the filtered pharmaceutical data within the radius as a JSON response.

    """
    farmacie_data = leggi_dati_da_csv('/app/app/farmacie.csv')

    farmacie_in_radius = []
    for farmacie in farmacie_data:
        distance = calcola_distanza(lat, lon, float(farmacie['LATITUDINE']),
                                    float(farmacie['LONGITUDINE']))
        if distance != -1:
            if distance <= radius:
                farmacie_in_radius.append(farmacie)
        else:
            raise HTTPException(
                status_code=400, detail="Distance or radius error")

    return {"farmacie": farmacie_in_radius}


@app.get('/esercizi')
def get_esercizi(lat: float = Query(0,
                                    title='Latitude',
                                    description='Default latitude'),
                 lon: float = Query(0,
                                    title='Longitude',
                                    description='Default longitude'),
                 radius: float = Query(100,
                                       title='Radius',
                                       description='Radius in meters')
                 ):
    
    """
    Retrieve services data within a specified radius
    from given latitude and longitude.

    Parameters:
    - lat (float): Latitude coordinate. Defaults to 0 if not provided.
    - lon (float): Longitude coordinate. Defaults to 0 if not provided.
    - raggio (float): Radius default to 100 meters
    for filtering services data.

    Returns:
    - dict: JSON response containing filtered
    services data within the specified radius.

    Algorithm:
    1. Read data from the CSV file using the function leggi_dati_da_csv.
    2. Filter services data within the specified radius:
       - Iterate through services data.
       - Calculate the distance between provided
       coordinates and services data coordinates.
       - Add services data falling within the specified
       radius to the result.
    3. Return the filtered services data within the radius as a JSON response.

    """
    esercizi_data = leggi_dati_da_csv('/app/app/esercizi1.csv')

    esercizi_in_radius = []
    for esercizi in esercizi_data:
        distance = calcola_distanza(lat, lon,
                                    float(esercizi['LAT_WGS84']),
                                    float(esercizi['LONG_WGS84']))
        if distance != -1:
            if distance <= radius:
                esercizi_in_radius.append(esercizi)
        else:
            raise HTTPException(
                status_code=400, detail="Distance or radius error")

    return {"esercizi": esercizi_in_radius}

"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd
import csv
from .mymodules.csv_reading_function import leggi_dati_da_csv
from .mymodules.distance_function import calcola_distanza
import os 

app = FastAPI()

current_file_path = os.path.abspath(__file__)


@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: A simple greeting.
    """
    return {"Hello": "World!!"}


@app.get('/poste')
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
We did the same for the 3 services.
"""

def get_poste(lat: float = Query(0, title='Latitude',
                                 description='Default latitude'),
              lon: float = Query(0, title='Longitude',
                                 description='Default longitude'),
              radius: float = Query(100, title='Radius',
                                    description='Radius in meters')
              ):
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
    farmacie_data = leggi_dati_da_csv('/app/app/farmacie.csv')

    farmacie_in_radius = []
    for farmacie in farmacie_data:
        distance = calcola_distanza(lat, lon, float(farmacie['LATITUDINE']),
                                    float(farmacie['LONGITUDINE']))
        if distance <= radius:
            farmacie_in_radius.append(farmacie)

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
    esercizi_data = leggi_dati_da_csv('/app/app/esercizi1.csv')

    esercizi_in_radius = []
    for esercizi in esercizi_data:
        distance = calcola_distanza(lat, lon,
                                    float(esercizi['LAT_WGS84']),
                                    float(esercizi['LONG_WGS84']))
        if distance <= radius:
            esercizi_in_radius.append(esercizi)

    return {"esercizi": esercizi_in_radius}

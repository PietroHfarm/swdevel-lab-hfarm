"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd
import csv
from .mymodules.csv_reading_function import leggi_dati_da_csv
from .mymodules.distance_function import calcola_distanza

app = FastAPI()


@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: A simple greeting.
    """
    return {"Hello": "World!!"}

@app.get('/poste')
def get_poste (lat: float = Query(0, title='Latitude', description='Default latitude'),
              lon: float = Query(0, title='Longitude', description='Default longitude'),
              radius: float = Query(100, title='Radius', description='Radius in meters')
):
    poste_data=leggi_dati_da_csv("/app/app/poste.csv")

    poste_in_radius = []
    for poste in poste_data:
        distance = calcola_distanza(lat, lon, float(poste['LAT_Y_4326']), float(poste['LONG_X_4326']))
        if distance <= radius:
            poste_in_radius.append(poste)

    return{"poste":poste_in_radius}

@app.get('/farmacie')
def get_farmacie(lat: float = Query(0, title='Latitude', description='Default latitude'),
              lon: float = Query(0, title='Longitude', description='Default longitude'),
              radius: float = Query(100, title='Radius', description='Radius in meters')
):
    farmacie_data=leggi_dati_da_csv('./farmacie.csv')

    farmacie_in_radius = []
    for farmacie in farmacie_data:
        distance = calcola_distanza(lat, lon, float(farmacie['LATITUDINE']), float(farmacie['LONGITUDINE']))
        if distance <= radius:
            farmacie_in_radius.append(farmacie)

    return{"farmacie": farmacie_in_radius}

@app.get('/esercizi')
def get_esercizi (lat: float = Query(0, title='Latitude', description='Default latitude'),
              lon: float = Query(0, title='Longitude', description='Default longitude'),
              radius: float = Query(100, title='Radius', description='Radius in meters')
):
    esercizi_data=leggi_dati_da_csv('./esercizi1.csv')

    esercizi_in_radius= []
    for esercizi in esercizi_data:
        distance = calcola_distanza(lat, lon, float(esercizi['LAT_WGS84']), float(esercizi['LONG_WGS84']))
        if distance <= radius:
            esercizi_in_radius.append(esercizi)

    return{"esercizi": esercizi_in_radius}


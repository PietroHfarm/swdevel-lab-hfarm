"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd
import csv
from mymodules.csv_reading_function import leggi_dati_da_csv
from mymodules.distance_function import calcola_distanza

app = FastAPI()

def leggi_dati_da_csv(file_path):
    dati = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            dati.append(row)
    return dati

@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: A simple greeting.
    """
    return {"Hello": "World!!"}

@app.get('/poste')
def get_poste (lat: float = Query(10000, title='Latitude', description='Default latitude'),
              lon: float = Query(10000, title='Longitude', description='Default longitude'),
              raggio: float = Query(10000, title='Radius', description='Radius in meters')
):
    dati_poste=leggi_dati_da_csv("./poste.csv")

    poste_nel_raggio = []
    for poste in dati_poste:
        distanza = calcola_distanza(lat, lon, float(poste['LAT_Y_4326']), float(poste['LONG_X_4326']))
        if distanza <= raggio:
            poste_nel_raggio.append(poste)

    return{"poste":poste_nel_raggio}

@app.get('/farmacie')
def get_farmacie(lat: float = Query(10000, title='Latitude', description='Default latitude'),
              lon: float = Query(10000, title='Longitude', description='Default longitude'),
              raggio: float = Query(10000, title='Radius', description='Radius in meters')
):
    dati_farmacie=leggi_dati_da_csv('./farmacie.csv')

    poste_nel_raggio = []
    for farmacie in dati_farmacie:
        distanza = calcola_distanza(lat, lon, float(farmacie['LATITUDINE']), float(farmacie['LONGITUDINE']))
        if distanza <= raggio:
            poste_nel_raggio.append(farmacie)

    return{"farmacie": poste_nel_raggio}

@app.get('/esercizi')
def get_esercizi (lat: float = Query(10000, title='Latitude', description='Default latitude'),
              lon: float = Query(10000, title='Longitude', description='Default longitude'),
              raggio: float = Query(10000, title='Radius', description='Radius in meters')
):
    dati_esercizi=leggi_dati_da_csv('./esercizi1.csv')

    poste_nel_raggio = []
    for esercizi in dati_esercizi:
        distanza = calcola_distanza(lat, lon, float(esercizi['LAT_WGS84']), float(esercizi['LONG_WGS84']))
        if distanza <= raggio:
            poste_nel_raggio.append(esercizi)

    return{"esercizi": poste_nel_raggio}


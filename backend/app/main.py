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
from mymodules.useful_csv import leggi_dati_da_csv

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
def get_poste():
    dati_poste=leggi_dati_da_csv("./poste.csv")

    return{"poste":dati_poste}

@app.get('/farmacie')
def get_farmacie():
    dati_farmacie=leggi_dati_da_csv('./farmacie.csv')

    return{"farmacie": dati_farmacie}

@app.get('/esercizi')
def get_esercizi():
    dati_esercizi=leggi_dati_da_csv('./esercizi1.csv')

    return{"esercizi": dati_esercizi}


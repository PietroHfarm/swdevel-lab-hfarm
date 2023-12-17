import os
import sys
from fastapi.testclient import TestClient

# Add the project root to the sys.path
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

"""
Execute this test by running on the terminal (from the app/) the command:
pytest --cov=app --cov-report=html tests/
"""

client = TestClient(app)


def test_poste():
    response = client.get("/poste?lon=9.189982&lat=45.4642035&radius=300")
    assert response.status_code == 200
    assert response.json() == {
        "poste": [
            {
                "Ente": "Ufficio PT",
                "Sportello": "",
                "Indirizzo": "VIA MAZZINI GIUSEPPE, 15",
                "Telefono": "02-86396911",
                "Fax": "02-72000087",
                "CAP": "20123",
                "MUNICIPIO": "1",
                "ID_NIL": "1",
                "NIL": "DUOMO",
                "LONG_X_4326": "9.188937000000067",
                "LAT_Y_4326": "45.461898000000076",
                "Location": "(45.461898000000076, 9.188937000000067)"
            }
        ]
    }


def test_farmacie():
    response = client.get("/farmacie?lon=9.189982&lat=45.4642035&radius=100")
    assert response.status_code == 200
    assert response.json() == {
        "farmacie": [
            {
                "CODICE_FARMACIA": "2681",
                "DESCRIZIONE_FARMACIA": "FARMACIA CARLO ERBA",
                "TIPOLOGIA": "Ordinaria",
                "PARTITA_IVA": "02489000998",
                "INDIRIZZO": "PIAZZA DEL DUOMO, 21",
                "COMUNE": "MILANO",
                "FRAZIONE": "",
                "PROVINCIA": "MI",
                "CODICE_ISTAT": "15146",
                "PRECISIONE_LOCATION": "alta",
                "CAP": "20121",
                "MUNICIPIO": "1",
                "ID_NIL": "1",
                "NIL": "DUOMO",
                "LONGITUDINE": "9.18952755",
                "LATITUDINE": "45.464689",
                "LOCATION": "POINT (9.18952755 45.464689)"
            }
        ]
    }


def test_esercizi():
    response = client.get("/esercizi?lon=9.189982&lat=45.4642035&radius=100")
    assert response.status_code == 200
    assert response.json() == {
        "esercizi": [
            {
                "Codice": "PE/27481",
                "Ubicazione":
                "Piazza DUOMO (DEL) N. 21 piano 5 - c/o hotel (z.d. 1)",
                "Area di Competenza": "SOMMINISTRAZIONE - In piano",
                "DescrizioneVia": "Piazza DUOMO (DEL)",
                "Civico": "21",
                "CodiceVia": "1.0",
                "denominazione_pe":
                "a - Ristorante, trattoria, osteria con cucina e simili",
                "insegna": "",
                "superficie_somministrazione": "89.0",
                "CAP": "20121.0",
                "ID_NIL": "1.0",
                "NIL": "DUOMO",
                "MUNICIPIO": "1.0",
                "LONG_WGS84": "9.1895970373",
                "LAT_WGS84": "45.46478924",
                "Location": "45.46478924, 9.1895970373"
            },
            {
                "Codice": "PE/27210",
                "Ubicazione": "Piazza DUOMO (DEL) N. 21 (z.d. 1)",
                "Area di Competenza": "SOMMINISTRAZIONE - In piano",
                "DescrizioneVia": "Piazza DUOMO (DEL)",
                "Civico": "21",
                "CodiceVia": "1.0",
                "denominazione_pe":
                "a - Ristorante, trattoria, osteria con cucina e simili",
                "insegna": "",
                "superficie_somministrazione": "228.0",
                "CAP": "20121.0",
                "ID_NIL": "1.0",
                "NIL": "DUOMO",
                "MUNICIPIO": "1.0",
                "LONG_WGS84": "9.1895970373",
                "LAT_WGS84": "45.46478924",
                "Location": "45.46478924, 9.1895970373"
            }
        ]
    }


def test_not_numbers_in_query():
    response = client.get(
        "/esercizi?lon=thisisnotword&lat=thisisnotword&radius=thisisnotword")
    assert response.status_code == 422


def test_undefined_route():
    response = client.get(
        "/thisisnotavalidroute?lon=-100&lat=-100&radius=1000")
    assert response.status_code == 404


def test_negative_numbers_in_query():
    response = client.get("/poste?lon=-50&lat=-50&radius=1000")
    assert response.status_code == 400

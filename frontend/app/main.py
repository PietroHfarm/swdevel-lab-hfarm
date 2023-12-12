"""
Frontend module for the Flask application.

This module defines a simple Flask application that serves as the frontend for the project.
"""

from flask import Flask, render_template
import requests  # Import the requests library to make HTTP requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from dotenv import load_dotenv 
import os 

load_dotenv()

google_maps_api_key = os.getenv('GOOGLE_MAPS_API_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://backend'  # Replace with the actual URL of your FastAPI backend
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'


@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: Rendered HTML content for the index page.
    """
    return render_template('homepage.html')

def get_poste_from_backend(lon, lat, radius):
    backend_url = f'http://backend/poste?lon={lat}&lat={lon}&raggio={radius}'  # Aggiustato il formato dell'URL
    response = requests.get(backend_url)
    response.raise_for_status()
    return response.json()

def get_farmacie_from_backend(lon, lat, radius):
    backend_url = f'http://backend/farmacie?lon={lat}&lat={lon}&raggio={radius}'
    response = requests.get(backend_url)
    response.raise_for_status()
    return response.json()

def get_esercizi_from_backend(lon, lat, radius):
    backend_url = f'http://backend/esercizi?lon={lat}&lat={lon}&raggio={radius}'
    response = requests.get(backend_url)
    response.raise_for_status()
    return response.json()

@app.route('/internal', methods=['GET', 'POST'])
def internal():
    """
    Render the internal page.

    Returns:
        str: Rendered HTML content for the index page.
    """
    form = QueryForm()
    error_message = None  # Initialize error message


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

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
from wtforms import FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired

load_dotenv()

google_maps_api_key = os.getenv('GOOGLE_MAPS_API_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://backend'  # Replace with the actual URL of your FastAPI backend
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'

class QueryForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
    raggio = FloatField('Raggio', validators=[DataRequired()])
    categoria = SelectField('Categoria', choices=[('poste', 'Poste'), ('farmacie', 'Farmacie'), ('esercizi', 'Esercizi')], default='poste')
    submit = SubmitField('Submit')

@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: Rendered HTML content for the index page.
    """
    return render_template('homepage.html')

def get_poste_from_backend(lon, lat, radius):
    backend_url = f'http://backend/poste?lat={lat}&lon={lon}&radius={radius}'  # Aggiustato il formato dell'URL
    try:
        response = requests.get(backend_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poste data from backend:{e}")
        return {'error': 'Error'}

def get_farmacie_from_backend(lon, lat, radius):
    backend_url = f'http://backend/farmacie?lat={lat}&lon={lon}&radius={radius}'
    try:
        response = requests.get(backend_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching farmacie data from backend:{e}")
        return {'error': 'Error'}

def get_esercizi_from_backend(lon, lat, radius):
    backend_url = f'http://backend/esercizi?lat={lat}&lon={lon}&radius={radius}'
    try:
        response = requests.get(backend_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching esercizi data from backend:{e}")
        return {'error': 'Error'}
    
def get_lat_lon_from_address(address):
    
    geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={google_maps_api_key}'
  
    response = requests.get(geocode_url)
    data = response.json()

    if data['status'] == 'OK' and len(data['results']) > 0:
        location = data['results'][0]['geometry']['location']
        
        if "MI" in address.upper():
            lat = location['lat']
            lon = location['lng']
            return lat, lon
        else:
            print("L'indirizzo non contiene la sigla di provincia 'MI' (Milano).")
            return None, None

    else:
        print(f"Errore nella richiesta di geocodifica: {data['status']}")
        return None, None

@app.route('/servicepage')
def servicepage():
    """
    Render the internal page.

    Returns:
        str: Rendered HTML content for the index page.
    """
    form = QueryForm()
    poste_data=get_poste_from_backend(45.464098,9.191926,1000)
    esercizi_data=get_esercizi_from_backend(45.464098,9.191926,1000)
    error_message = None  # Initialize error message
    return render_template('servicepage.html', form=form, poste_data=poste_data, esercizi_data=esercizi_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)


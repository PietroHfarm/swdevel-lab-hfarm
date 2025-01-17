"""
Frontend module for the Flask application.

This module defines a simple Flask
application that serves as the frontend for the project.

Import the requests library to make HTTP requests
Dotenv package functions to pick the google key

"""

from flask import Flask, render_template
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from dotenv import load_dotenv
import os
from wtforms import FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired

load_dotenv()

# picking the key
google_maps_api_key = os.getenv('GOOGLE_MAPS_API_KEY')

app = Flask(__name__)
# Replace with a secure secret key
app.config['SECRET_KEY'] = 'your_secret_key'

# Configuration for the
# FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://backend'
# Replace with the actual URL of your FastAPI backend
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'


class QueryForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
    radius = FloatField('Radius', validators=[DataRequired()])
    category = SelectField('Category',
                           choices=[('poste', 'Poste'),
                                    ('farmacie', 'Farmacie'),
                                    ('esercizi', 'Esercizi')], default='poste')
    submit = SubmitField('Submit')


@app.route('/')
def index():
    """
    Render the homepage page.

    Returns:
        str: Rendered HTML content for the homepage page.
    """
    return render_template('homepage.html')

# following functions create request from backend (with their
# relatives url) basd on the category wanted
# if the request goes well everyone receives
# a file json with data


def get_poste_from_backend(lon, lat, radius):
    """
    Retrieves 'poste' data from a backend service using provided
    longitude, latitude, and radius.

    Parameters:
    - lon (float): Longitude value.
    - lat (float): Latitude value.
    - raggio (float): Radius in meters for the query.

    Returns:
    - dict: JSON response containing 'poste' data from the backend.

    If an error occurs during the request, it prints an error message
    and returns a dictionary with an 'error' key.
    We did the same for farmacie and esercizi
    """
# url for the request get fo the backend
    backend_url = f'http://backend/poste?lat={lon}&lon={lat}&radius={radius}'
    try:
        response = requests.get(backend_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poste data from backend:{e}")
        return {'error': 'Error'}


def get_farmacie_from_backend(lon, lat, radius):
    """
    Retrieves 'farmacie' data from a backend service using
    provided longitude, latitude, and radius.

    Parameters:
    - lon (float): Longitude value.
    - lat (float): Latitude value.
    - raggio (float): Radius in meters for the query.

    Returns:
    - dict: JSON response containing 'farmacie' data
    from the backend.

    If an error occurs during the request, it prints an
    error message and returns a dictionary with an 'error' key.
    """
    backend_url = f'http://backend/farmacie?lat={lon}&lon={lat}&radius={radius}'
    try:
        response = requests.get(backend_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching farmacie data from backend:{e}")
        return {'error': 'Error'}


def get_esercizi_from_backend(lon, lat, radius):
    """
    Retrieves 'esercizi' data from a backend service using provided
    longitude, latitude, and radius.

    Parameters:
    - lon (float): Longitude value.
    - lat (float): Latitude value.
    - raggio (float): Radius in meters for the query.

    Returns:
    - dict: JSON response containing 'esercizi' data from the backend.

    If an error occurs during the request, it prints an error message
    and returns a dictionary with an 'error' key.
    """
    backend_url = f'http://backend/esercizi?lat={lon}&lon={lat}&radius={radius}'
    try:
        response = requests.get(backend_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching esercizi data from backend:{e}")
        return {'error': 'Error'}


# using google maps API to extract lat and lon from address
def get_lat_lon_from_address(address):
    """
    Retrieves location-based data from the backend
    by providing longitude, latitude, and a specified radius.

    Parameters:
    - lon (float): Longitude value.
    - lat (float): Latitude value.
    - raggio (float): Radius in meters for the query.

    Returns:
    - dict: JSON response containing data from the backend.

    In case of a request error, the function prints an error
    message and returns a dictionary with an 'error' key.
    """
    geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={google_maps_api_key}'

    response = requests.get(geocode_url)
    data = response.json()

# if request suceeds, extracts the coordinates and verify if
# address is within Milan
    if data['status'] == 'OK' and len(data['results']) > 0:
        location = data['results'][0]['geometry']['location']

        if "MI" in address.upper():
            lat = location['lat']
            lon = location['lng']
            return lat, lon
        else:
            print("The address does not contain the 'MI' province tag.")
            return None, None

    else:
        print(f"Eroor in the geocode request: {data['status']}")
        return None, None


# route for servicepage, handles both get and post
@app.route('/servicepage', methods=['GET', 'POST'])
def servicepage():
    """
    Handles GET and POST requests to '/servicepage' route.

    Renders a form for querying locations based on address,
    radius, and category.
    Processes form submission, retrieves coordinates from the address,
    and queries the backend
    based on the chosen category ('poste', 'farmacie', 'esercizi')
    within the specified radius.

    Returns:
    - Renders the 'servicepage.html' template with form,
    address, coordinates, and queried data.
    - Handles errors and displays error messages if geocoding fails or
    if the category is not supported.
    """
    form = QueryForm()
    error_message = None  # Initialize error message
# Control for validation of the form
    if form.validate_on_submit():
        address = form.address.data
        radius = form.radius.data
        category = form.category.data
        print(address)

        lat, lon = get_lat_lon_from_address(address)
# if the coordinates are valid, proceeds with the request
        if lat is not None and lon is not None:
            if category == "poste":
                data = get_poste_from_backend(lat, lon, radius)
            elif category == "farmacie":
                data = get_farmacie_from_backend(lat, lon, radius)
            elif category == "esercizi":
                data = get_esercizi_from_backend(lat, lon, radius)
            else:
                error_message = 'Category not supported.'

                return render_template('servicepage.html', form=form,
                                       error_message=error_message,
                                       apiKey=google_maps_api_key)
            return render_template('servicepage.html',
                                   category=category,
                                   form=form, address=address,
                                   lat=lat, lon=lon, data=data,
                                   apiKey=google_maps_api_key)
        else:
            error_message = "Error in the geocode of the address."\
                            "The address must be within"\
                            "the city of Milan"
    return render_template('servicepage.html',
                           form=form,
                           error_message=error_message,
                           apiKey=google_maps_api_key)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

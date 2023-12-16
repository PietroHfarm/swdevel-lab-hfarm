import os
import sys
from fastapi.testclient import TestClient

# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now you can do the relative import
from app.main import app


"""
Execute this test by running on the terminal (from the app/) the command:
pytest --cov=app --cov-report=html tests/
 """

client = TestClient(app)


def test_poste():
    response = client.get("/poste?lon=9.189982&lat=45.4642035&radius=300")
    assert response.status_code == 200
    assert response.json() == {"poste":[{"Ente":"Ufficio PT","Sportello":"","Indirizzo":"VIA MAZZINI GIUSEPPE, 15","Telefono":"02-86396911","Fax":"02-72000087","CAP":"20123","MUNICIPIO":"1","ID_NIL":"1","NIL":"DUOMO","LONG_X_4326":"9.188937000000067","LAT_Y_4326":"45.461898000000076","Location":"(45.461898000000076, 9.188937000000067)"}]}


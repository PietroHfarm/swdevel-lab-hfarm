# FNS PROJECT 

# This is the project for the Lab of Software Project Development

FNS, short for Find National Service, is a groundbreaking software designed to simplify and streamline the process of locating essential services in your vicinity. Created with the mission to assist individuals in swiftly identifying nearby services, FNS is an innovative tool dedicated to enhancing convenience and accessibility.
FNS focuses on aiding users in Milan, acting as a guiding beacon to find crucial services within their chosen proximity. Its primary functionalities revolve around locating pharmacies, bars/pubs, and post offices with ease. The user experience is straightforward: input your address or location and set your desired radius. In return, FNS generates a comprehensive map displaying a curated list of the nearest service points.
This project represents an initial but pivotal step in providing an invaluable resource for community convenience. By leveraging technology to connect users with essential services efficiently, FNS embodies efficiency, accessibility, and ease of use. 



## Architecture

The project follows a simple client-server architecture:

1. **Frontend (Flask, Bootstrap):**
   - Represents the user interface or client side.
   - Built with Flask, a lightweight web framework for Python.
   - Bootstrap frontend implementation for the web development
   - Responsible for rendering web pages and user interaction, including the form for querying the backend.

2. **Backend (FastAPI):**
   - Represents the server or backend of the application.
   - Built with FastAPI, a modern web framework for building APIs with Python.
   - Handles requests from the frontend, including querying birthdays and providing the current date.

3. **Docker Compose:**
   - Orchestrates the deployment of both frontend and backend as separate containers.
   - Ensures seamless communication between frontend and backend containers.
   - Simplifies the deployment and management of the entire application.

### Communication
Bidirectional communication is established between the Frontend (Flask, Bootstrap) and Backend (FastAPI). Docker Compose facilitates this communication, allowing the components to work together seamlessly.

## Project Structure

- `backend/`: FastAPI backend implementation.
    - Dockerfile: Dockerfile for building the backend image.
    - main.py: Main backend application file.
    - requirements.txt: List of Python dependencies for the backend.
    - csv_readings.py: module used to read CSVs
    - distance_function: module to calculate geodetic distance
    - CSVs: CSVs used to provide information 

- `frontend/`: Flask frontend implementation.
    - Dockerfile: Dockerfile for building the frontend image.
    - static/: Folder for static files (CSS, JavaScript, etc.).
    - templates/: Folder for HTML templates.
    - main.py: Main frontend application file.
    - requirements.txt: List of Python dependencies for the frontend.
- `docker-compose.yml`: Docker Compose configuration for running both frontend and backend.

## Prerequisites

- Docker
- Visual Studio Code (Optional, for debugging)
- install geopy, dotenv
- insert the personal google key available following the steps in the provided link: https://developers.google.com/maps/documentation/javascript/get-api-key?hl=it

## CSV needed

- poste.csv: https://www.dati.gov.it/view-dataset/dataset?id=6331b260-941a-4420-bbc5-40837e2d38ec it contains the list of all the post offices in the city of Milan with the address, the latitude and longitude.
- esercizi1.csv: https://www.dati.gov.it/view-dataset/dataset?id=948d5e06-9707-4eda-9439-05004498b559 it contains the list of bars and pubs in the city of Milan, with the address, the latitude and longitude, we deleted the Nan value manually.
- farmacie.csv: https://www.dati.gov.it/view-dataset/dataset?id=cb5e4a55-2017-4668-968b-f9e9b3cbbcdf it contains the list of all the pharmacies in the city of Milan, with the address, the latitude and longitude.

## How it works
Accessing the Service: Upon entering the internal page, you'll be prompted to input your address or current location. Set Your Preferences: Specify your desired radius within which you want to search for services. Select Service Type: Choose the specific service you're looking for - pharmacies, bars/pubs, or post offices. Instant Results: With a click, FNS generates a comprehensive map pinpointing the nearest service points within your chosen radius.

  
## Usage

1. Clone the repository and navigate in the directory:

    ```bash
    git clone REPO_URL
    cd swdevel-lab-hfarm
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

    This will start both the frontend and backend containers.
    
> **NOTE:** Uncomment the lines in the Dockerfiles that follow the section labeled `Command to run the application` and comment out the ones labeled `Command to keep the container running`. This will allow you to access the backend and frontend, as described in Point 3.

3. Open your web browser and navigate to [http://localhost:8080](http://localhost:8080) to access the `frontend` and [http://localhost:8081](http://localhost:8081) to access the `backend`.

4. Use the form on the frontend to query birthdays from the backend.

## Shutting Down the Docker Containers

To shut down the running Docker containers, you can use the following steps:

1. Open a terminal.

2. Navigate to the project root directory.

3. Run the following command to stop and remove the Docker containers:

    ```bash
    docker-compose down
    ```

## Starting and Stopping Containers Individually

If you need to start or stop the containers individually, you can use the following commands:

- **Start Frontend Container:**

    ```bash
    docker-compose up frontend
    ```

- **Stop Frontend Container:**

    ```bash
    docker-compose stop frontend
    ```

- **Start Backend Container:**

    ```bash
    docker-compose up backend
    ```

- **Stop Backend Container:**

    ```bash
    docker-compose stop backend
    ```

Make sure to replace `frontend` and `backend` with the appropriate service names from your `docker-compose.yml` file.

### Notes:

When stopping containers individually, the `docker-compose down` command is not required.
Now you can manage the lifecycle of your Docker containers more flexibly.


## Debugging with Visual Studio Code and Docker Extension

1. Open the project in Visual Studio Code:

    ```bash
    code .
    ```

2. Set breakpoints in your Python code as needed.

3. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

    Ensure that your Docker containers are running.

4a. Install the [Docker extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) for Visual Studio Code.
4b. Install the [Remote Development Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) for Visual Studio Code

5. Open the "Docker" view in Visual Studio Code by clicking on the Docker icon in the Activity Bar.

6. Under "Containers," you should see your running containers. Right-click on the container running your Flask or FastAPI application.

7. Select "Attach Visual Studio Code" from the context menu. This will configure the container for debugging.

8. Open the Run view in Visual Studio Code and select the "Python: Remote Attach" configuration.

9. Click the "Run" button to start the debugger.

10. Access the frontend in your web browser and trigger the actions you want to debug.

### Notes:

- Ensure that your Docker containers are running (`docker-compose up --build`) before attaching Visual Studio Code.

- Adjust the container name in the "Docker: Attach to Node" configuration if needed.

- The provided configurations assume that your Flask or FastAPI application is running with the debugger attached. Adjust the configurations if needed.

- If using Flask, ensure that the Flask application is started with the `--no-reload` option to prevent automatic reloading, which can interfere with debugging.

- Debugging FastAPI requires configuring the FastAPI application to run with the `--reload` option. Update the FastAPI Dockerfile CMD accordingly.

- After the debugger is attached, you can use breakpoints, inspect variables, and step through your code as needed.


## Adding New Modules to a Running Docker Container

1. **Install Additional Modules:**
    ```bash
    pip install new_module
    ```
   Replace `new_module` with the names of the module you want to install.

2. **Verify Installed Modules:**
    ```bash
    pip list
    ```
   This command displays a list of installed Python packages, including the newly added modules.

3. **Optional: Update requirements.txt:**
    ```bash
    pip freeze > requirements.txt
    ```
   If you want to keep track of the installed modules, you may choose to update the `requirements.txt` file inside the container.


Now, the additional Python modules are installed in the running container, and you've performed these actions directly from the VS Code terminal. If these changes are intended for production, consider updating the `requirements.txt` file and rebuilding the Docker container.

# Flask Containerized Landing Page

This project creates a simple landing page using Flask, which is containerized using Docker. The page displays the port the container is running on and changes the background color every time the page is refreshed.

### Features
- Dynamic Port Display: The page will show the port number on which the container is running.

- Random Background Color: Each time the user refreshes the page, the background color changes randomly.

- Dockerized: The app is packaged as a Docker container, making it easy to deploy and run anywhere.

### Prerequisites
Before running this project, you need to have the following installed:

Docker: Download [Docker](https://www.docker.com/get-started/)

Python (for development): Download [Python](https://www.python.org/downloads/) (Python 3.6 or later recommended)

### Project Structure

- docker-fun
  - app.py                  (Flask app to serve the landing page)
  - Dockerfile              (Dockerfile to containerize the app)
  - requirements.txt        (Python dependencies)

### Installation and Setup

1. Clone this repository
```bash
git clone https://github.com/1EyedRabbit/docker-fun.git
cd docker-fun
```
2. Install Dependencies (Optional for Local Development)
```python
pip install -r requirements.txt
```
3. Run the Application Locally (Optional)
```python
python app.py
```
4. Containerize the Application Using Docker

  Build the Docker image by running this weekend in the root directory of the project
```bash
docker build -t flask-color-change .
```

  Run the Docker container by executing the following command (do this once the above step builds the image successfully)
```bash
docker run -p 8080:8080 flask-color-change
```

Your experiment is now exposed on http://localhost:8080

### Understand it better

- Flask App: The app.py file serves a simple web page using Flask. It uses Jinja templating to inject the port and random background color into the HTML.
- Random Background Color: The app generates a random hex color on each page refresh using Python's random module.
- Docker: The Dockerfile containerizes the Flask app. When the container is run, it listens on port 8080 by default.

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

### Cloud Build Workflow

- Trigger: Automatically triggered on main branch push.
- Build: Docker image is built using the repository’s Dockerfile.
- Push: Image is pushed to Artifact Registry.
- Deploy (Optional): Automatically deployed to Cloud Run using the latest image.

### How to set this whole thing ???

- [Create a Google Cloud Project](https://developers.google.com/workspace/guides/create-project) (if you don’t have one)
  - Go to Google Cloud Console.
  - Create a new project or use an existing one.
  - Enable Cloud Build and Artifact Registry APIs in your project.

- Configure Google Artifact Registry
  - In Google Cloud Console, go to Artifact Registry.
  - Click on Create Repository.
  - Select Docker as the repository format.
  - Choose a region and give the repository a name, such as docker-repo.
  - Click Create.

- Authenticate Docker to Artifact Registry:
  - You need to authenticate Docker to push images to Artifact Registry. Run the following command:

```bash
gcloud auth configure-docker [REGION]-docker.pkg.dev
#Replace [REGION] with the region where your Artifact Registry is created (e.g., us-central1).
```

- Enable Cloud Build API
  - Go to the Cloud Build page.
  - Click Enable API if it isn’t already enabled.

- [Set up Cloud Build Trigger](https://cloud.google.com/build/docs/automating-builds/create-manage-triggers) in Google Cloud Console
  - Connect Cloud Build with GitHub:
    - In the Google Cloud Console, go to the Cloud Build page.
    - Click Triggers in the left menu, then click Create Trigger.
    - Choose GitHub and follow the steps to authenticate with GitHub and link your repository to Google Cloud Build.
    - Make sure you have the necessary permissions in your GitHub repo (e.g., Admin rights).
  - Configure the Cloud Build Trigger:
    - Select the repository you just linked.
    - Set the trigger event to Push to a branch (for example, you can use main or master).
    - Select Create a new build configuration file if you don’t already have one.
    - Create the Cloud Build configuration file (cloudbuild.yaml):
    - In your GitHub repository, you will need a cloudbuild.yaml file, which specifies the steps for building and pushing your Docker image.

- Create the Cloud Build Configuration File (cloudbuild.yaml)
  - In the root of your GitHub repository, create a file named cloudbuild.yaml (similar to the one in this repository)

- Create and Configure the Trigger in Cloud Build
  - Now, go back to the Google Cloud Console and configure the trigger to use this cloudbuild.yaml file.
  - Choose the trigger type: Push to a branch.
  - Select the repository and branch you want the trigger to be tied to (e.g., main).
  - Specify the Build configuration file as cloudbuild.yaml (this is the file you just created).
  - Complete the trigger setup by clicking Create.

- Test the Setup
  - To test the setup, make a change to your repository and push it to the branch that you set up the trigger for (e.g., main).
  - This will trigger Cloud Build to:
    - Build the Docker image.
    - Push the image to Artifact Registry.
    - You can check the progress of the build by going to Cloud Build in the Google Cloud Console. After the build is complete, you should see your Docker image stored in Artifact Registry.

- [Access the Docker Image in Artifact Registry](https://cloud.google.com/artifact-registry/docs/docker/manage-images#listing_images)
  - To view your image, go to Artifact Registry in the Google Cloud Console. You should be able to see your image tagged with the commit SHA (e.g., flask-landing-page:$COMMIT_SHA).

# Cafe Manager

## Description
Simple Cafe Management website done using reactJS and fastAPI

## Prerequisites
Before you begin, ensure that you have the following installed:

- [Docker](https://docs.docker.com/get-docker/) (including Docker Compose)
- [Git](https://git-scm.com/downloads)

## Getting Started

### Step 1: Clone the Repository
Naivgate to where you want the project folder to be located at.
Open your terminal and run the following command:
```bash
git clone https://github.com/daronoh/CafeManager.git
```

### Step 2: Open up Docker 
Open up Docker and navigate to your project directory.

### Step 3: Build and Start the Docker Containers
Run the following command to build and start the Docker containers:
```bash
docker-compose up --build
```

### Step 4: Access the Application
Once the containers are running, you can access the application in your web browser:
- Frontend: http://localhost:3000/
- Backend: http://localhost:8000/

## Step 5: Configure the docker-compose.yml file (Optional)
If you would like to change any of the environment variables or container settings, you can do so
in either the docker-compose.yml file or the .env located in /frontend (for the request endpoint URL)

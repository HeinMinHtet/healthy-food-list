# Healthy Food List App

A simple web application to display a list of healthy foods.

## Overview
This application demonstrates a basic web service setup using Docker, Nginx, Flask (for the backend), and a simple frontend. The Flask backend retrieves a `food.json` file from an S3 bucket, and the Nginx server acts as a load balancer/reverse proxy for both the frontend and backend services. We use a custom NGINX Docker image to ensure configuration consistency across environments.

## Services
- **Frontend**: A simple web interface to display the food list.
- **Backend (Flask)**: Serves the food data, fetched from an S3 JSON file.
- **Nginx**: A custom Docker image that routes traffic to the frontend and backend, serving as a reverse proxy and load balancer.

## Docker Images
You can find the Docker images for this project on Docker Hub:
- [Backend Image](https://hub.docker.com/r/heinminhtet/healthy-food-list-backend)
- [Frontend Image](https://hub.docker.com/r/heinminhtet/healthy-food-list-frontend)
- [NGINX Load Balancer Image](https://hub.docker.com/r/heinminhtet/healthy-food-list-nginx)

## How to Run
### Prerequisites
- Docker
- Docker Compose

### Running locally
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd healthy-food-list
   ```

2. Start the services using Docker Compose:
   ```bash
   docker compose up -d
   ```

3. Access the application:
   - Frontend: [http://localhost:8081](http://localhost:8081)
   - Health Check: [http://localhost:8081/health](http://localhost:8081/health)
   - API Endpoint: [http://localhost:8081/api/data](http://localhost:8081/api/data)

4. To stop the services:
   ```bash
   docker compose down
   ```


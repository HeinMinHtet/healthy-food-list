## 1. Project Goal
Build a containerized web application for Healthy food list data visualization.
The system retrieves JSON data from an S3 API and displays it in a table-based web UI.
The application must be scalable, maintainable, and deployable using CI/CD.


## 2. Architecture Overview

User -> NGINX Load Balancer -> Frontend (HTML/JS)  
                         -> Backend (Flask API) -> S3 JSON API

Services:
- frontend (nginx static site)
- backend (Flask API)
- load balancer (nginx reverse proxy)
- CI/CD pipeline (GitHub Actions)

## 3. Technology Stack

Frontend:
- HTML
- JavaScript (fetch API)
- NGINX

Backend:
- Python Flask
- Requests or boto3 for S3 API

Infrastructure:
- Docker
- Docker Compose
- NGINX load balancer

CI/CD:
- GitHub Actions
- Docker Hub or GitHub Container Registry


## 4. Functional Requirements

- Fetch JSON data from S3 API
- Display data in table format
- Handle API errors gracefully
- Support multiple backend replicas
- Provide health endpoint (/health)


## 5. Non-Functional Requirements

- Containerized deployment
- Load balancing via NGINX
- CI/CD automation
- Simple UI
- Secure secrets handling
- Easy to scale backend replicas
- Json file that include healthy food for weight loss that include name,calories,food type.

## 6. Folder Structure

lab_app/
├── backend/
│   ├── app.py
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   └── Dockerfile
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
├── planning.md
└── .github/workflows/cicd.yml

## 7. CI/CD Pipeline Plan

Trigger:
- On push to main branch
- On pull request

Steps:
1. Checkout source code
2. Build backend Docker image
3. Build frontend Docker image
4. Run backend container and health check
5. Push images to registry (Docker Hub)
6. (Optional) Deploy to server or Kubernetes cluster

Secrets Required:
- DOCKER_USERNAME
- DOCKER_PASSWORD

---

## 8. Environment Variables

- S3_JSON_URL
- FLASK_ENV
- PORT

All secrets stored in GitHub Secrets.


## 9. Testing Strategy

- Health endpoint test (/health)
- API endpoint test (/api/data)
- Docker build test
- Manual UI test

## 10. Security Considerations

- Do not hardcode secrets
- Use environment variables
- Private S3 uses IAM role or access key
- NGINX reverse proxy hides backend


## 13. Success Criteria

- Web app loads correctly
- JSON data displayed
- CI/CD pipeline passes
- Containers start successfully
- Load balancer distributes traffic






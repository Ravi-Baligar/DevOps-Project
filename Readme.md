# Flask DevOps CI/CD Pipeline with Jenkins, Docker, Helm and Minikube

This project demonstrates a complete **local DevOps CI/CD pipeline** for deploying a Flask application into a **local Kubernetes cluster using Minikube**.

The pipeline automatically:

- Pulls source code from GitHub
- Builds a Docker image
- Pushes image to Docker Hub
- Deploys to Kubernetes using Helm
- Uses Jenkins for automation

---

# Architecture

GitHub → Jenkins → Docker → DockerHub → Helm → Minikube Kubernetes

---

# Technologies Used

- Python Flask
- Docker
- Jenkins
- Docker Hub
- Kubernetes
- Helm
- Minikube
- GitHub

---

## Project Structure

```text
DevOps-Project/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── helm-chart/
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│
├── Jenkinsfile
└── README.md
```

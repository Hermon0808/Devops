# Automated Deployment of a Weather Forecast Web Application using DevOps Tools

## Project Overview

This project demonstrates a complete end-to-end DevOps pipeline for automating the deployment of a Weather Forecast Web Application using modern DevOps tools and GitHub Actions for CI/CD. The web app displays real-time weather data (temperature, humidity, wind speed, and description) for any city using the OpenWeatherMap API.

## Architecture

```
Developer → GitHub → GitHub Actions → Docker → ACR → AKS → User
```

## Technologies Used

- **Application Stack**: Python Flask + HTML/CSS + OpenWeatherMap API
- **Version Control**: Git & GitHub
- **Containerization**: Docker
- **Container Registry**: Azure Container Registry (ACR)
- **Orchestration**: Kubernetes (AKS)
- **Infrastructure as Code**: Terraform
- **Configuration Management**: Ansible
- **CI/CD**: GitHub Actions

## Project Structure

```
Devops/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
│
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── ansible/
│   └── deploy.yml
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── README.md
└── screenshots/
```

## Setup Instructions

### Prerequisites

1. Azure CLI installed and configured
2. Terraform installed
3. Ansible installed
4. Docker installed
5. OpenWeatherMap API key

### Phase 1: Application Development

The Flask application is located in the `app/` directory. It fetches weather data from OpenWeatherMap API and displays it in a simple web interface.

### Phase 2: Containerization

Build the Docker image:

```bash
docker build -t weather-app:latest .
docker run -p 5000:5000 weather-app
```

### Phase 3: Infrastructure Provisioning

Navigate to the terraform directory and run:

```bash
terraform init
terraform plan
terraform apply
```

### Phase 4: Configuration Management

Run the Ansible playbook:

```bash
ansible-playbook ansible/deploy.yml
```

### Phase 5: CI/CD Pipeline

The GitHub Actions workflow automatically triggers on push to main branch. It builds the Docker image, pushes to ACR, and deploys to AKS.

### Phase 6: Deployment and Verification

After deployment, get the service external IP:

```bash
kubectl get svc weather-app-service
```

## Local Testing

To test locally:

1. Start the Docker container:
   ```bash
   docker run -d -p 5000:5000 weather-app:latest
   ```

2. Access the application at `http://localhost:5000`

## API Key Configuration

Replace `YOUR_OPENWEATHERMAP_API_KEY` in `app/app.py` with your actual OpenWeatherMap API key.

## GitHub Secrets Required

For the CI/CD pipeline to work, set the following secrets in your GitHub repository:

- `AZURE_CREDENTIALS`: Azure service principal credentials
- `ACR_NAME`: Azure Container Registry name
- `AKS_CLUSTER_NAME`: AKS cluster name
- `RESOURCE_GROUP`: Azure resource group name

## Screenshots

Screenshots of each phase are stored in the `screenshots/` directory.

## Links

- **Localhost**: http://localhost:5000 (when running Docker container)
- **Live Website**: [AKS LoadBalancer IP]/ (after deployment)

## Cleanup

To destroy the infrastructure:

```bash
terraform destroy
```

## Evaluation Criteria

- Version Control & Collaboration: Clean commits, proper branching, GitHub usage
- CI/CD Implementation: Fully automated GitHub Actions pipeline
- Containerization & Deployment: Docker + Kubernetes integration
- Infrastructure as Code: Terraform + Ansible automation
- Documentation & Demo: Clear steps, screenshots, architecture diagram
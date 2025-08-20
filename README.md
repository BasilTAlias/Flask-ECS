# 🚀 Flask App Deployment on AWS ECS with Fargate and CI/CD

This project demonstrates how to containerize a Python Flask application, store the image in Amazon ECR (Elastic Container Registry), and deploy it using AWS ECS (Elastic Container Service) with the Fargate launch type. It also features a complete CI/CD pipeline powered by GitHub Actions that automates the build, push, and deployment process.

---

## 📦 Tech Stack

* **Python** (Flask framework)
* **Docker** (for containerizing the application)
* **Amazon ECR** (for hosting Docker images)
* **Amazon ECS Fargate** (for serverless container deployment)
* **GitHub Actions** (for CI/CD automation)

---

## 📁 Project Structure

```
.
├── app.py                    # Flask application
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container image instructions
└── .github/
    └── workflows/
        └── deploy.yml       # GitHub Actions CI/CD workflow
```

---

## 🔧 Setup & Deployment Guide

### Step 1: Build the Flask App

Create a basic Flask app in `app.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Flask Website!</h1><p>Deployed using Docker and ECS Fargate.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```

Add dependencies in `requirements.txt`:

```
flask==3.1.1
```

### Step 2: Dockerize the Application

Create a `Dockerfile`:

```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY app.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]
```

### Step 3: Push Image to Amazon ECR

* Create a private ECR repository
* Authenticate Docker to ECR using AWS CLI
* Tag and push your Docker image

### Step 4: Deploy on ECS using Fargate

* Create a Fargate cluster
* Register a task definition with your container image
* Deploy a service to maintain the running container

### Step 5: Set Up GitHub Actions for CI/CD

* Configure GitHub secrets for AWS credentials and resource names
* Create a workflow file to automate:

  * Docker image build
  * Push to ECR
  * ECS task registration
  * Service update

---

## 🔐 GitHub Secrets Configuration

| Secret Name             | Description                  |
| ----------------------- | ---------------------------- |
| `AWS_ACCESS_KEY_ID`     | IAM User access key          |
| `AWS_SECRET_ACCESS_KEY` | IAM User secret key          |
| `AWS_REGION`            | AWS region (e.g., us-east-1) |
| `ECR_REPOSITORY`        | Your ECR repository name     |
| `ECR_REGISTRY`          | ECR registry URI             |
| `ECS_CLUSTER_NAME`      | ECS cluster name             |
| `ECS_SERVICE_NAME`      | ECS service name             |
| `ECS_TASK_DEFINITION`   | Task definition family name  |

---

## ⚙️ GitHub Actions CI/CD Workflow

The `deploy.yml` workflow file in `.github/workflows/` automates the following:

* Triggers on every push to the `main` branch
* Logs in to ECR
* Builds and pushes Docker image
* Retrieves and updates ECS task definition
* Updates ECS service with the new task revision

Example badge:

![GitHub Actions](https://img.shields.io/github/actions/workflow/status/BasilTAlias/Flask-ECS/deploy.yml?branch=main)

---

## 🌐 Live Deployment

Once deployed, the application can be accessed via the Public IP address assigned by Fargate. To avoid changing IPs on every deployment, we can consider attaching a Load Balancer.

---

---

## 📝 Medium Article

I also wrote a Medium article that walks through this project step-by-step:

> **Title:** From Code to Cloud: Deploying a Flask App to AWS ECS with GitHub Actions
> **Link:** https://medium.com/@basiltaliaz/from-code-to-cloud-deploying-a-flask-app-on-aws-ecs-with-fargate-and-github-actions-ci-cd-9ff32bd12169

The article explains the reasoning behind each step, best practices, and real-world DevOps benefits of infrastructure-as-code + CI/CD pipelines.

---

## 🙌 Acknowledgments

This project is built to showcase modern DevOps workflows and can be a foundation for more advanced deployments using ALB, Route 53, HTTPS via ACM, or even autoscaling with CloudWatch alarms.

---

## 📝 Medium Article

Link: https://medium.com/@basiltaliaz/from-code-to-cloud-deploying-a-flask-app-on-aws-ecs-with-fargate-and-github-actions-ci-cd-9ff32bd12169

---

## 📫 Contact

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/basil-t-alias) or explore more of my projects on [GitHub](https://github.com/BasilTAlias).

---

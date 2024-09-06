# MLOps Deployment Guide

## Introduction

This guide provides step-by-step instructions for building, running, and deploying Docker images using Azure Container Registry. Follow these steps to ensure a smooth deployment process for your MLOps projects.

## Steps to Build, Run, and Deploy Docker Images

### 1. Build and Run Docker Image

**Building** a Docker image involves creating a package that contains everything needed to run your application. **Running** the Docker image starts a container from this image.

Use the following commands to build and run your Docker image:

```bash
# Build the Docker image with a specific tag (version)
docker build -t mlops:v2 .

# Run the Docker image, mapping port 8000 from the container to port 8000 on your host
docker run -p 8000:8000 mlops:v2
```

### 2. Log in to Azure Account Using Azure CLI

Before logging in, ensure that you have the Azure CLI installed on your machine. 

#### Install Azure CLI

- **Windows:** Download and run the Azure CLI installer.
- **macOS:** Install using Homebrew with `brew install azure-cli`.
- **Linux:** Install using your package manager, for example, `sudo apt-get install azure-cli` on Ubuntu.

Once installed, log in to your Azure account with the following command:

```bash
az login
```

### 3. Log in to Azure Container Registry

After logging in to your Azure account, authenticate with your Azure Container Registry (ACR) to enable pushing images.

Use the following command to log in:

```bash
az acr login -n <container_registry_name>
```
Replace <container_registry_name> with the name of your Azure Container Registry. This command allows Docker to access and interact with your ACR.

### 4. Tag Docker Image

Tagging your Docker image helps identify and organize it for deployment. Use the following command to tag your image:

```bash
docker tag mlops:v2 <yourregistry_name>.azurecr.io/mlops:v2
```

Replace <yourregistry_name> with the name of your Azure Container Registry. This command tags the mlops:v2 image with the ACR repository URL, preparing it for upload.

### 5. Push Docker Image to Azure Container Registry

After tagging your Docker image, upload it to Azure Container Registry with the following command:

```bash
docker push <your_container_registry_name>.azurecr.io/mlops:v2
```

Replace <your_container_registry_name> with the name of your Azure Container Registry. This command pushes the mlops:v2 image to your ACR, making it available for deployment in your Azure environment.

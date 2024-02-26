# Deploying Multibackend Applications with Keras 3

This project aims to deploy an image classification model using Docker. Due to Multi-backend operations from Keras 3.0, the model works seamlessly across PyTorch, TensorFlow, or JAX backends.

## Prerequisites

Before deploying the project using Docker, make sure you have installed Docker:

- [Docker](https://www.docker.com/get-started) installed on your system.

## Installation

To install Docker and set up the project for deployment, follow these steps:

1. [Download and install Docker](https://www.docker.com/get-started) on your machine.
2. Clone this project repository from GitHub.
```bash
git clone https://github.com/anas-rz/docker-deployment-keras-3.git
```
3. Navigate to the project directory in your terminal.
```bash
cd docker-deployment-keras-3
docker build -t image_classification_mlp .
```

4. Run the Docker container.

```bash 
docker container run -d -p 8080:8080 image_classification_mlp
```
The Streamlit application runs on https://localhost:8080. If you are running it on a server, you can test it using port forwarding to local IP.

## Changing Backend

To change the backend, modify the line `ENV KERAS_BACKEND <backend>` in the [Dockerfile](./Dockerfile).

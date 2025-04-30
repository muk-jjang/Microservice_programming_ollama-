# Project 2 - Microservices Assignment

## Overview

This project implements a microservices architecture using Docker containers. It consists of three main components:

- API Server (Python)
- CLI Client
- Ollama (LLM Service with gemma3:1b model)

## Quick Start (Using Docker Hub Images)

1. Install Docker and Docker Compose
2. Create a new directory and save the following `docker-compose.yml` file:

```yaml
version: "3.8"

services:
  ollama:
    image: yoonseongjoon/micro-project-ollama:latest
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    restart: always
    environment:
      - OLLAMA_MODELS=gemma3:1b
      - OLLAMA_HOST=0.0.0.0
      - OLLAMA_KEEP_ALIVE=5m
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:11434/api/tags"]
      interval: 10s
      timeout: 5s
      retries: 5

  api_server:
    image: yoonseongjoon/micro-project-api-server:latest
    ports:
      - "8080:8080"
    depends_on:
      ollama:
        condition: service_healthy
    environment:
      - OLLAMA_HOST=ollama
      - OLLAMA_PORT=11434

  client:
    image: yoonseongjoon/micro-project-client:latest
    depends_on:
      - api_server
    stdin_open: true
    tty: true

volumes:
  ollama_data:
    name: permanent_ollama_data
```

3. Run the following commands:

```bash
# Pull the required images
docker pull yoonseongjoon/micro-project-ollama:latest
docker pull yoonseongjoon/micro-project-api-server:latest
docker pull yoonseongjoon/micro-project-client:latest

# Start the services
docker-compose up -d
```

4. Interact with the client container:

```bash
docker attach [container_name_or_id]
```

## Components

1. API Server (`yoonseongjoon/micro-project-api-server`)

   - Python-based API server
   - Interfaces between the client and Ollama
   - MIT License
   - Source code available in the `server` directory

2. Client (`yoonseongjoon/micro-project-client`)

   - Python-based CLI client
   - Provides interactive interface for users
   - MIT License
   - Source code available in the `client` directory

3. Ollama (`yoonseongjoon/micro-project-ollama`)
   - Large Language Model service with gemma3:1b model
   - Custom image with automatic model download
   - Based on ollama/ollama (Apache License 2.0)
   - Source: https://github.com/ollama/ollama

## Key Features

- **Persistent Model Storage**: Models are stored in a Docker volume, so they don't need to be downloaded again after restart
- **Automatic Model Downloads**: The gemma3:1b model is automatically downloaded during initialization
- **Health Checks**: Service dependencies are properly managed with health checks
- **CLI Interaction**: Simple command-line interface for user interaction

## License Information

This project uses multiple components with different licenses:

### Project Components (MIT License)

The API server and client components are licensed under the MIT License.

### Ollama (Apache License 2.0)

The Ollama service is based on the official Ollama project, which is licensed under the Apache License 2.0. For more information, please visit:

- https://github.com/ollama/ollama
- https://www.apache.org/licenses/LICENSE-2.0

## Docker Hub Images

- API Server: `yoonseongjoon/micro-project-api-server:latest`
- Client: `yoonseongjoon/micro-project-client:latest`
- Ollama (Custom): `yoonseongjoon/micro-project-ollama:latest`
# Microservice_programming_ollama-

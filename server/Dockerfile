FROM python:3.9-slim

# 라이센스 정보
LABEL maintainer="yoonseongjoon"
LABEL description="Project 2 API Server - Microservices Assignment"
LABEL license="MIT License"
LABEL dependencies="Ollama (Apache License 2.0) - https://github.com/ollama/ollama"

WORKDIR /app

RUN pip install flask requests

COPY server.py .

CMD ["python", "server.py"]
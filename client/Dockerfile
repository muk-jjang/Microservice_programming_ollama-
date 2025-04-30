FROM python:3.9-slim

# 라이센스 정보
LABEL maintainer="yoonseongjoon"
LABEL description="Project 2 Client - Microservices Assignment"
LABEL license="MIT License"
LABEL dependencies="Ollama (Apache License 2.0) - https://github.com/ollama/ollama"

WORKDIR /app

# 필요한 패키지 설치
RUN pip install requests

# 클라이언트 소스 코드 복사
COPY ollama_client.py .

# CLI 인터페이스 모드로 실행
CMD ["python", "ollama_client.py", "--cli-mode"]
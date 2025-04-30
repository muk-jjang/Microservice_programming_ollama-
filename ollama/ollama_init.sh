#!/bin/bash

# 백그라운드에서 Ollama 서버 시작
echo "Starting Ollama server in background..."
"$@" &
SERVER_PID=$!

# Ollama 서버가 완전히 시작될 때까지 대기
echo "Waiting for Ollama server to start..."
max_retries=30
retry_count=0

while [ $retry_count -lt $max_retries ]; do
  if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "Ollama server is up and running."
    break
  fi
  echo "Waiting for Ollama server... ($((retry_count + 1))/$max_retries)"
  sleep 2
  retry_count=$((retry_count + 1))
done

if [ $retry_count -eq $max_retries ]; then
  echo "Error: Ollama server did not start within the expected time."
  kill $SERVER_PID
  exit 1
fi

# 모델 목록 확인
echo "Checking for installed models..."
MODELS=$(curl -s http://localhost:11434/api/tags)

# gemma3:1b 모델이 이미 설치되어 있는지 확인
if echo "$MODELS" | grep -q "gemma3:1b"; then
  echo "Model gemma3:1b is already installed."
else
  echo "Installing model gemma3:1b..."
  ollama pull gemma3:1b
  echo "Model gemma3:1b has been installed."
fi

# 서버 프로세스 종료
echo "Initialization complete. Stopping background server..."
kill $SERVER_PID

# 서버 프로세스를 포그라운드로 다시 시작
echo "Restarting Ollama server in foreground..."
exec "$@" 
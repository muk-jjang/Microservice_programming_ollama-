FROM ollama/ollama:latest

# 필요한 도구 설치
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 초기화 스크립트 복사
COPY ollama_init.sh /usr/local/bin/ollama_init.sh
RUN chmod +x /usr/local/bin/ollama_init.sh

# 초기화 스크립트를 통해 ollama 실행
ENTRYPOINT ["/usr/local/bin/ollama_init.sh"]
CMD ["/bin/ollama", "serve"] 
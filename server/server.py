from flask import Flask, request, jsonify
import requests
import json
import logging
import sys

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] [SERVER] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.debug = True

# 마지막으로 받은 메시지 저장 (자동 응답 방지)
last_message = None

@app.route('/message', methods=['POST'])
def handle_message():
    global last_message
    
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"status": "error", "message": "No message received"}), 400
        
    message = data['message']
    
    # 중복 메시지 검사 (자동 응답 방지)
    if message == last_message:
        return jsonify({"status": "error", "message": "Duplicate message detected"}), 400
    
    last_message = message
    logger.info(f"Received message: {message}")
    
    # Ollama에 메시지 전송
    ollama_url = "http://ollama:11434/api/generate"
    ollama_payload = {
        "model": "gemma3:1b",
        "prompt": message,
        "stream": False
    }
    
    try:
        ollama_response = requests.post(ollama_url, json=ollama_payload)
        if ollama_response.status_code == 200:
            ollama_data = ollama_response.json()
            response_message = ollama_data.get("response", "No response received")
            logger.info(f"Sending response: {response_message}")
            return jsonify({"status": "success", "received_message": response_message}), 200
        else:
            logger.error(f"Ollama error: {ollama_response.status_code}")
            return jsonify({"status": "error", "message": "Failed to get response from Ollama"}), 500
    except Exception as e:
        logger.error(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    logger.info("Starting API server on port 8080...")
    app.run(host='0.0.0.0', port=8080)
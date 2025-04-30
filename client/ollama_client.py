import requests
import logging
import sys

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='[CLIENT] %(message)s'
)
logger = logging.getLogger(__name__)

def send_message(message):
    """Send a message to the server and return the response"""
    url = "http://api_server:8080/message"
    try:
        response = requests.post(url, json={"message": message})
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Server error: {response.status_code}")
            return None
    except Exception as e:
        logger.error(f"Error: {e}")
        return None

def main():
    print("\n=== CLI Chat Client ===")
    print("Type 'quit' to exit")
    print("=====================\n")
    
    # 초기 인사
    print("Type your message and press Enter to chat with the assistant.")
    
    while True:
        try:
            # 사용자 입력을 기다림
            message = input("\nYou: ").strip()
            if not message:
                continue
                
            if message.lower() == 'quit':
                print("\nGoodbye!")
                break
                
            # 서버로 메시지 전송
            print("\nSending message to server...")
            response = send_message(message)
            if response and 'received_message' in response:
                print(f"\nAssistant: {response['received_message']}")
            else:
                print("\nError: Failed to get response from server")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()
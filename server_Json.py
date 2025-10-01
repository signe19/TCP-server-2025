import socket
import threading
import json
import random

def handle_json_client(conn, addr):
    print(f"Forbundet med {addr}")
    try:
        data = conn.recv(1024).decode()
        request = json.loads(data)

        method = request.get("method")
        tal1 = request.get("Tal1")
        tal2 = request.get("Tal2")

        if method == "Random":
            result = random.randint(tal1, tal2)
        elif method == "Add":
            result = tal1 + tal2
        elif method == "Subtract":
            result = tal1 - tal2
        else:
            result = "Unknown method"

        response = json.dumps({"result": result})
        conn.sendall(response.encode())
    except Exception as e:
        print("Fejl:", e)
    finally:
        conn.close()

def start_json_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9998))
    server.listen()
    print("JSON-serveren kører på port 9998")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_json_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_json_server()

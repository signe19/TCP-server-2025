import socket
import threading
import random

def handle_client(conn, addr):
    print(f"Forbundet med {addr}")
    try:
        method = conn.recv(1024).decode().strip()
        conn.sendall(b"Input numbers\n")

        numbers = conn.recv(1024).decode().strip()
        tal1, tal2 = map(int, numbers.split())

        if method == "Random":
            result = random.randint(tal1, tal2)
        elif method == "Add":
            result = tal1 + tal2
        elif method == "Subtract":
            result = tal1 - tal2
        else:
            result = "Unknown method"

        conn.sendall(f"{result}\n".encode())
    except Exception as e:
        print("Fejl:", e)
    finally:
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen()
    print("Serveren kører på port 9999")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()

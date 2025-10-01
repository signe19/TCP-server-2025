import socket
import json

def run_json_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 9998))

    method = input("Metode (Random/Add/Subtract): ")
    tal1 = int(input("Tal1: "))
    tal2 = int(input("Tal2: "))

    request = json.dumps({
        "method": method,
        "Tal1": tal1,
        "Tal2": tal2
    })

    client.sendall(request.encode())

    response = client.recv(1024).decode()
    result = json.loads(response)
    print("Resultat:", result["result"])

    client.close()

if __name__ == "__main__":
    run_json_client()


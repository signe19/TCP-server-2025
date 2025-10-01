import socket

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 9999))

    method = input("Indtast metode (Random/Add/Subtract): ")
    client.sendall(f"{method}\n".encode())

    response = client.recv(1024).decode()
    print("Server:", response.strip())

    tal1 = input("Tal1: ")
    tal2 = input("Tal2: ")
    client.sendall(f"{tal1} {tal2}\n".encode())

    result = client.recv(1024).decode()
    print("Resultat:", result.strip())

    client.close()

if __name__ == "__main__":
    run_client()

import socket
import ssl

SERVER_HOST = 'localhost'
SERVER_PORT = 12345
CERTIFICATE_FILE = 'server.pem'

def handle_client(client_socket):
    try:
        request = client_socket.recv(1024)
        print(f"Received: {request.decode()}")

        # Simulate authentication (you can implement your actual authentication logic here)
        authenticated = authenticate_client(request.decode())

        if authenticated:
            response = "Hello from server! You are authenticated."
        else:
            response = "Authentication failed. Connection refused."

        client_socket.send(response.encode())
    except Exception as e:
        print(f"Error handling client request: {e}")
    finally:
        client_socket.close()

def authenticate_client(client_data):
    # Replace this with your actual authentication logic
    # For example, check if client_data matches expected credentials or certificates
    return True  # Dummy authentication always succeeds for demonstration

def main():
    try:
        # Create a TCP/IP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Wrap socket with SSL/TLS encryption
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=CERTIFICATE_FILE)
        server_socket = context.wrap_socket(server_socket, server_side=True)

        # Bind the socket to the address and port
        server_socket.bind((SERVER_HOST, SERVER_PORT))

        # Listen for incoming connections
        server_socket.listen(1)

        print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

        while True:
            try:
                # Wait for a connection
                client_socket, client_address = server_socket.accept()
                print(f"Connection from {client_address}")

                # Handle the connection
                handle_client(client_socket)
            except Exception as e:
                print(f"Error accepting client connection: {e}")
    except Exception as e:
        print(f"Error setting up server: {e}")
    finally:
        # Close the server socket
        if server_socket:
            server_socket.close()

if __name__ == "__main__":
    main()

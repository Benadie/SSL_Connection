import socket
import ssl

SERVER_HOST = 'localhost'
SERVER_PORT = 12345

def main():
    try:
        # Create a TCP/IP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Wrap socket with SSL/TLS encryption
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        ssl_socket = context.wrap_socket(client_socket, server_hostname=SERVER_HOST)

        try:
            # Connect to the server
            ssl_socket.connect((SERVER_HOST, SERVER_PORT))

            # Send message to server
            message = "Client authentication data"
            ssl_socket.send(message.encode())

            # Receive response from server
            response = ssl_socket.recv(1024)
            print(f"Received: {response.decode()}")
        except Exception as e:
            print(f"Error communicating with the server: {e}")
        finally:
            ssl_socket.close()
    except Exception as e:
        print(f"Error setting up client: {e}")

if __name__ == "__main__":
    main()

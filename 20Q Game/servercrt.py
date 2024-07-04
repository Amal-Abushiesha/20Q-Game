import socket
import ssl

# Server certificate and key file paths (replace with your actual files)
CERT_FILE = 'server.crt'
KEY_FILE = 'server.key'

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

context= ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain(CERT_FILE, KEY_FILE)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Listening...')
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        with context.wrap_socket(conn, server_side=True) as ssl_sock:
            while True:
                data = ssl_sock.recv(1024)
                if not data:
                    break
                ssl_sock.sendall(data)  # Echo back the received data

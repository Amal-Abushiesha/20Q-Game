import ssl
import ServerGUI as gui
import threading
import time
import socket
import FtpServer
import shutil



# Server port for listening
PORT = 9876

# Object to be guessed (replace with your desired object)

CERT_FILE = 'server.crt'
KEY_FILE = 'server.key'

context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain(CERT_FILE, KEY_FILE)


def main():
    object = app.object
    copyfile()
    server_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", PORT))
    server_socket.listen()
    app.ViewText(f"Server listening on port {PORT}")
    no_ssl_conn, addr = server_socket.accept()



    """Handles communication with a connected client."""
    app.ViewText(f"Connected by {addr}")
    try:
        with no_ssl_conn:
            with context.wrap_socket(no_ssl_conn, server_side=True) as conn:

                while True:
                    # Receive message from client
                    data = conn.recv(1024).decode()
                    if not data:
                        break

                    # Check for exit request
                    if data.lower() == "exit":
                        conn.sendall("Goodbye!".encode())
                        break

                    app.ViewText(f"Client question: {data} ? \n")
                    
                    app.no_btn.configure(state="enable")
                    app.yes_btn.configure(state="enable")
                    
                    while True:
                        time.sleep(1)
                        answer = app.get_input()
                        
                        if answer != "":
                            break

                    # Send response to client
                    conn.sendall(answer.encode())

                    # Receive guess from client
                    guess = conn.recv(1024).decode()
                    if guess.lower() == object.lower():
                        conn.sendall("You won! Congrats!".encode())
                        app.ViewText(f"Player Won! game will close in 7 seconds")
                        time.sleep(7)
                        conn.close()
                        app.destroy()
                        break

                    else:
                        conn.sendall("Wrong guess, Try again!".encode())

    except ConnectionError as e:
        app.ViewText(f"Client connection error: {e}")
    finally:
        app.ViewText(f"Client {addr} disconnected")
        conn.close()
    

def copyfile():


    source_path = app.filename
    destination_path = r"F:\Faculty of computers and artificial intelligence\LAST_SEMSTER\5 Thu - Network Programming - Fatma\FtpServer\FTP_SND\img.jpg"

    try:
    # Copy the file
        shutil.copy(source_path, destination_path)
        print(f"File copied successfully from {source_path} to {destination_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: You don't have permission to copy the file. {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
            
        

if __name__ == "__main__":
    app = gui.App()
    thread = threading.Thread(target=main).start()
    thread = threading.Thread(target=FtpServer.main).start()
    app.mainloop()





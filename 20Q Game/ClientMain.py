import ssl
import ClientGUI as gui
import threading
import time
import socket
from ftplib import FTP
import ftplib
from emailClient import send_email

feedbacklist = []


HOST = 'localhost'  # Server address
PORT = 9876
FTP_HOST = "127.0.0.1"
FTP_PORT = 2121  # used the same port as the server example

FTP_USERNAME = "useruser"  # Anonymous login from the server
FTP_PASSWORD = "pass"  # No password required for anonymous login


CERT_FILE = r'F:\Faculty of computers and artificial intelligence\LAST_SEMSTER\5 Thu - Network Programming - Fatma\FtpServer\server.crt'  

context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_verify_locations(CERT_FILE)



def get_img():
    ftpObject = FTP()
    ftpObject.connect(host=FTP_HOST, port=FTP_PORT, timeout=100)
    ftpObject.login(FTP_USERNAME,FTP_PASSWORD)
    photo = False

    filename = r"F:\Faculty of computers and artificial intelligence\LAST_SEMSTER\5 Thu - Network Programming - Fatma\FtpServer\FTP_RCV\new.jpg"

    # Write file in binary mode
    with open(filename, "wb") as file:
        # Command for Downloading the file "RETR filename"
        try:
            ftpObject.retrbinary(f"RETR img.jpg", file.write)
            photo = True
        except ftplib.all_errors as e:
            # Handle specific error (550) for "No such file or directory"
            if isinstance(e, ftplib.error_perm) and e.args[0] == 550:
                photo = False
            else:
                print(f"FTP error: {e}")
            
    return photo


        

def play_game():
    """Connects to the server and plays the 20 questions game."""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sockt:
        sock = context.wrap_socket(sockt, server_hostname=HOST)

        sock.connect((HOST, PORT))
        won = False
        for i in range(20):
            if i == 19:
                if get_img():
                    app.open_toplevel()
                send_email(feedbacklist, r"F:\Faculty of computers and artificial intelligence\LAST_SEMSTER\5 Thu - Network Programming - Fatma\FtpServer\FTP_RCV\new.jpg")

            if won:
                sock.sendall("exit".encode())
                sock.close()
                break
            
            # Ask a question
            app.ViewText(f"Question number {i+1}: ")
            
            app.login_button.configure(state="enabled")
            
            while True:
                time.sleep(1)
                question = app.get_input()
                
                if question != "":
                    break
                
            
            
            sock.sendall(question.encode())
            feedbacklist.append(question)
            app.ViewText(f"Question sent: {question}")



            # Receive judge's response
            judge_response = sock.recv(1024).decode()
            app.ViewText(f"A: {judge_response}")

            feedbacklist.append(judge_response)


            app.login_button.configure(state="enabled")
            
            # Guess the object
            app.ViewText("Guess object: ")
            while True:
                time.sleep(1)
                guess = app.get_input()
                
                if guess != "":
                    break
            sock.sendall(guess.encode())
            feedbacklist.append(guess)

            # Receive server's feedback on the guess
            guess_response = sock.recv(1024).decode()
            feedbacklist.append(guess_response)
            
            if guess_response == "You won! Congrats!":
                app.ViewText("You Won !, game will close in 7 seconds")
                send_email(feedbacklist, r"F:\Faculty of computers and artificial intelligence\LAST_SEMSTER\5 Thu - Network Programming - Fatma\FtpServer\FTP_RCV\new.jpg")
                if get_img():
                    app.open_toplevel()
                app.print_mail()
                won = True
                sock.close()
                app.destroy()
                break
            else:
                app.ViewText(f"Your Guess is wrong try aagain")



if __name__ == "__main__":

    app = gui.App()
    thread = threading.Thread(target=play_game).start()
    app.mainloop()

    
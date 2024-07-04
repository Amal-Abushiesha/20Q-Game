# 20 Questions Game - README

## Introduction
Welcome to the 20 Questions Game! This game is a digital implementation of the classic guessing game where one player thinks of an object, and the other player has 20 chances to guess what it is by asking yes/no questions.

## Features
- **Pyhin Sockets**: Utilizes pyhin sockets for robust network communication.
- **SSL and Server Certificates**: Ensures secure communication with SSL encryption and server certificates.
- **Custom Tkinter GUI**: Features a custom graphical user interface built with Tkinter for a user-friendly experience.
- **FTP, IMAP, and Email Integration**: Supports file transfer, email retrieval, and sending feedback emails to the client.
- **Multi-Device Compatibility**: Can run on two separate devices, with one device acting as the server and the other as the client.
- **Feedback Email**: After the game, an email is sent to the client with detailed feedback on their performance, including questions asked, guesses made, and the server's verdict.

## How to Play
1. **Setup**: One device runs the server application, and another runs the client application.
2. **Start the Game**: The server thinks of a secret object, and the client connects to the server.
3. **Ask Questions**: The client asks yes/no questions about the secret object. The server responds to each question.
4. **Guess the Object**: The client tries to guess the object based on the server's responses.
5. **Game End**: The game ends when the client correctly guesses the object or exhausts all 20 questions.

## Running the Game
### Server Setup
1. Run the server application.
2. Ensure the server has the necessary SSL certificates for secure communication.
3. The server will wait for the client to connect.

### Client Setup
1. Run the client application.
2. Connect to the server using the server's IP address and port number.
3. Begin asking questions and making guesses.

## Email Feedback
After the game ends, the server sends an email to the client containing:
- **Performance Summary**: An overview of how well the client performed.
- **Questions Asked**: A list of all the questions asked by the client.
- **Guesses Made**: A list of all the guesses made by the client.
- **Server's Verdict**: The server's response to each question and guess.

## Technical Details
- **Languages Used**: Python
- **Libraries and Frameworks**: pyhin, Tkinter, SSL, FTP, IMAP
- **Network Protocols**: TCP/IP for socket communication, SSL for secure data transmission

## Installation
1. **Clone the Repository**: `git clone <repository_url>`
2. **Install Dependencies**: `pip install -r requirements.txt`
3. **Run Server**: `python server.py`
4. **Run Client**: `python client.py`

## Contact
For any questions or support, email me at amaalabushiesha@gmail.com.

Thank you for playing the 20 Questions Game! Enjoy and have fun guessing!

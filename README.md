# 20 Questions Game - README

## Introduction
Welcome to the 20 Questions Game! This game is a digital implementation of the classic guessing game where one player thinks of an object, and the other player has 20 chances to guess what it is by asking yes/no questions.

## Features
- **Pyhon Sockets**: Utilizes pyhon sockets for robust network communication.
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
   hint: PEM pass phrase is 1234
4. The server will wait for the client to connect.
5. At the end enter the email password to receive an email with the feedback.

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

## Snaps
#### 1. Choosing an object
![screen 1](https://github.com/Amal-Abushiesha/20Q-Game/assets/81009248/822cd3d9-8d22-4175-bc5e-f7522d1a8f11)


#### 2. Optional Step ( Pick a photo of your object)
   ![screen 2](https://github.com/Amal-Abushiesha/20Q-Game/assets/81009248/9d501b26-db0b-4fa8-9bd3-fc5640059137)

   
#### 3. Start asking questions and making guesses, server will play accordingly and give verdicts
   ![screen 3](https://github.com/Amal-Abushiesha/20Q-Game/assets/81009248/2f5123bc-9555-497e-b995-63d30beb1d1f)

   
#### 4. Winning the game!
   ![screen 4](https://github.com/Amal-Abushiesha/20Q-Game/assets/81009248/a993cf71-2cc8-4187-8daa-b2a3c3f72c1f)

   
#### 5. Feedback
   ![screen 5](https://github.com/Amal-Abushiesha/20Q-Game/assets/81009248/279642ef-5272-462d-8e64-c6a0a806ba1a)


## Installation
1. **Clone the Repository**: `git clone <https://github.com/Amal-Abushiesha/20Q-Game.git>`
2. **Install Dependencies**: `pip install -r requirements.txt`
3. **Run Server**: `python server.py`
4. **Run Client**: `python client.py`

## Contact
For any questions or support, email me at amaalabushiesha@gmail.com.

Thank you for playing the 20 Questions Game! Enjoy and have fun guessing!

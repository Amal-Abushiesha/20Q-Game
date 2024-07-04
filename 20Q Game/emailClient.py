import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(feedbacklist, img):
    body, accuracy = format(feedbacklist)
    try:
        message = MIMEMultipart()
        message['From'] = '20Qgame@mailserver.com'
        message['To'] = 'admin@mailserver.com'
        message['Subject'] = "Game Report"


        html_part = MIMEText(f"<h2 style = 'color:red;'>This is your game report</h2><div>{body}</div> <h4><i>Your accuracy is <p style = 'color:green;'>{(accuracy/20)*100}%</p> </i></h4>", 'html')
        message.attach(html_part)

        with open(img, 'rb') as attachment:
            file_part = MIMEBase('application', 'octet-stream')
            file_part.set_payload(attachment.read())
            encoders.encode_base64(file_part)
            file_part.add_header('Content-Disposition', 'attachment; filename=new.jpg')
            message.attach(file_part)

        smtp_server = "localhost"
        port = 587

        print('connecting to server...')

        with smtplib.SMTP(smtp_server, port) as server:
            server.login('20Qgame@mailserver.com','12345')
            print("successfully connected to server...\n") 
            server.sendmail(message['From'],message['To'], message.as_string())
            server.quit()
    except Exception as e:
        print(e)

def format(fb):
    fl =[]
    cnt = 0
    idx = 0
    length = len(fb)

    while cnt != 4 and idx != length:
        if cnt == 0:
            fl.append(f"{idx+1}: Your Question was: {fb[idx]} ")
            cnt += 1 
  
        elif cnt == 1:
            fl.append(f"{idx+1}: Judge reply was: {fb[idx]} ")
            cnt += 1 
        
        elif cnt == 2:
            fl.append(f"{idx+1}: Your guess was: {fb[idx]} ")
            cnt += 1 

        else:
            fl.append(f"{idx+1}: Your guess reply was: {fb[idx]} ")
            cnt = 0
                    
        idx += 1
    body = ""
    for i in fl:
        body += f"{i}<br>"

    return body, 21-(length/4)
       
        



if __name__ == "__main__":
    fb = ['does it walk', 'yes', 'human', 'Wrong guess, Try again!', 'is it fast', 'yes', 'car', 'You won! Congrats!']
    path = r"F:\Faculty of computers and artificial intelligence\LAST_SEMSTER\5 Thu - Network Programming - Fatma\FtpServer\FTP_RCV\new.jpg"
    send_email(fb, path)
    

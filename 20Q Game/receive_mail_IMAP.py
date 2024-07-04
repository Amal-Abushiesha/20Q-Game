import imaplib
from IPython.core.display import display, HTML

def get_mail(inpassword):

	user = 'admin@mailserver.com'
	password = '12345'
	host = 'localhost'
	if inpassword == password:

		# Connect securely with SSL
		imap = imaplib.IMAP4(host)

		## Login to remote server
		imap.login(user, password)
		imap.select('Inbox')

		tmp, messages = imap.search(None, 'UNSEEN')
		for num in messages[0].split():
			# Retrieve email message by ID
			tmp, data = imap.fetch(num, '(RFC822)')
			dat = data[0][1].decode('utf-8').split("--===")
			start_index = dat[1].find('Encoding: 7bit')+15
			with open('out.html', 'w') as f:
				f.write('<!DOCTYPE html>\n')
				f.write('<html>\n')
				f.write('<head>\n')
				f.write('<title>My HTML File</title>\n')
				f.write('</head>\n')
				f.write('<body>\n')
				f.write(f'<p>{dat[1][start_index:]}</p>\n')
				f.write('</body>\n')
				f.write('</html>\n')
			
			break
			
		imap.close()
		imap.logout()

		import webbrowser
		webbrowser.open('out.html')
		return True
	else:
		return False
	
if __name__ == "__main__":
	get_mail('12345')
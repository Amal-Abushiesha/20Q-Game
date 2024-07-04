from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


FTP_PORT = 2121
FTP_USER = "useruser"
FTP_PASSWORD = "pass"
FTP_DIRECTORY = r"F:\Faculty of computers and artificial intelligence\LAST_SEMSTER\5 Thu - Network Programming - Fatma\FtpServer\FTP_SND"


def main():
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions.
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    address = ('127.0.0.1', FTP_PORT)
    server = FTPServer(address, handler)
    server.serve_forever()


if __name__ == '__main__':
    main()
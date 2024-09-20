from _libs.defines import *
import socket

class SocketClient:
    __ip = None
    __port =None

    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
        
    def open(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.__ip, self.__port))
        print("Connected successfully")
    
    def start_commms(self):
        msg = "b"

        while True:
            msg = input("")
            if msg == "close":
                break
            elif msg == "get_file":
                self.receive_file()
            else:
                self.__send(TESTING)
                if self.__confirmed():
                    print(f"sending msg : {msg}")
                    self.__send(msg)
                
        self.__send(CLOSE)
    
    def receive_file(self):
        template = REQUEST_TYPES.FILE_GET_TEMPLATE
        template["path"] = "C:\\Users\\uig03092\\Downloads\\pflib-2.8.0.7z"
        self.__send(REQUEST_TYPES.FILE_GET_REQUEST)
        if self.__confirmed():
            self.__send_template(template)
        else:
            print("Server refused request")
        if self.__confirmed():
            self.__receive_file(".", "pflib2.8.0.7z")
            print("Sending filed received ack")
            self.__send(ACKWNOLDEGE)
            print("File received")
        else:
            print("Server refused transaction")

    def __confirmed(self):
        ack = self.__receive(DEFAULT_REQUEST_SIZE)
        if ack == ACKWNOLDEGE:
            return True
        return False

    def __send(self, message:str):
        self.client_socket.send(message.encode())

    def __receive(self, size):
        msg = self.client_socket.recv(size)
        return msg.decode()
    
    def __receive_file(self, _path, _filename):
        buffer = b''

        with open(f"{_path}/{_filename}", 'wb') as file:
            while True:
                chunk = self.client_socket.recv(DEFAULT_CHUNK_SIZE)
                if len(chunk) == 0:
                    break
                if chunk[-EOFLEN:] == EOF_TRANSFER.encode():
                    file.write(chunk[:-EOFLEN])
                    break
                else:
                    file.write(chunk)
    
    def __send_template(self, template:dict):
        self.__send(f"{template}")


if __name__=="__main__":
    client = SocketClient("10.208.245.148", 12345)
    client.open()
    client.start_commms()
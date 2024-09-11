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
            self.__send(TESTING)
            acknowledge = self.__receive(DEFAULT_REQUEST_SIZE)
            print(f"received : {acknowledge}, ack = {ACKWNOLDEGE}")
            if acknowledge == ACKWNOLDEGE:
                print(f"sending msg : {msg}")
                self.__send(msg)
            
        self.__send(CLOSE)
    
    def __send(self, message:str):
        self.client_socket.send(message.encode())

    def __receive(self, size):
        msg = self.client_socket.recv(size)
        return msg.decode()



if __name__=="__main__":
    client = SocketClient("0.0.0.0", 12345)
    client.open()
    client.start_commms()
from _libs.ipconfig import *
from _libs.tk_modules import *
from _libs.defines import *

import socket

import os
import threading
import time

class Server_Side_Terminal:
    def __init__(self, close_server, self_shutdown):
        self.close_server = close_server
        self.self_shutdown = self_shutdown

    def get_command(self):
        input_command = input()
        self.input_handler(input_command)

    def input_handler(self, command):
        if command == "close":
                if self.close_server():
                    self.self_shutdown()
                else:
                    self.get_command()
        else:
            print("Bad command")
            self.get_command()

class Request_Handler:
    def __init__(self):
        pass

    def process_request(self, req_code, req_text):
        return "copy", ["abcde", "abrabadaf"]



class Client_handler:
    request_handler = Request_Handler()

    def __init__(self, client_socket, client_address, client_id, disconnect_caller):
        self.client_socket = client_socket
        self.client_address = client_address
        self.client_id = client_id
        self.disconnect_caller = disconnect_caller
    
    def start_handle(self):
        self.__listen_client_request()

    def __listen_client_request(self):
        req_code = self.__receive(DEFAULT_REQUEST_SIZE)
        if req_code==CLOSE:
            self.__close()
            print(f"Client {self.client_id} disconnected")
            self.disconnect_caller(self.client_id)
        else:
            self.__request_handler(req_code)
            self.__listen_client_request()

    def __request_handler(self, req_code):
        self.__send(ACKWNOLDEGE)
        msg = self.__receive(DEFAULT_STRING_SIZE)
        print(f"Client with id = {self.client_id} sent message : {msg}")
        action, extras = self.request_handler.process_request(req_code=req_code, req_text=msg)
        print(action, extras)
        if req_code==REQUEST_TYPES.FILE_GET_REQUEST:
            self.__send(ACKWNOLDEGE)
            self.__send_file("C:\\Users\\uig03092\\Downloads\\pflib-2.8.0.7z")
            if self.__confirmed():
                print("File sent successfully")

    def __confirmed(self):
        ack = self.__receive(DEFAULT_REQUEST_SIZE)
        if ack == ACKWNOLDEGE:
            return True
        return False

    def __send_file(self, _path):
        with open(_path, 'rb') as file:
            while chunk := file.read(DEFAULT_CHUNK_SIZE):
                self.client_socket.sendall(chunk)

        self.__send(EOF_TRANSFER)

    def __receive(self, size):
        message = self.client_socket.recv(size)
        return message.decode()
    
    def __send(self, message):
        self.client_socket.send(message.encode())

    def __close(self):
        self.client_socket.close()

class SocketServer:
    default_output = DEFAULT_INCOMING_PATH
    current_connections = {}
    __client_handler_classes = []
    __client_handler_threads = []
    id_counter = 0
    clients_connected = 0
    active = True

    server_socket = None

    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.__ip, self.__port))
        self.ensure_default_output()
        self.open_terminal()
        try:
            self.open_server_connections()
        except:
            pass

    def ensure_default_output(self):
        if not os.path.exists(self.default_output):
            os.makedirs(self.default_output)
        
    def open_server_connections(self):
        while self.active == True:
            if self.clients_connected < MAX_CLIENTS:
                self.server_socket.listen(1)
                _client_socket, _addr = self.server_socket.accept()
                self.register_client(_client_socket, _addr)
                client_handler_class = Client_handler(_client_socket, _addr, self.id_counter, self.disconnect_client)
                client_handler_thread = threading.Thread(target=client_handler_class.start_handle, daemon=True)
                client_handler_thread.start()
                self.__client_handler_classes.append(client_handler_class)
                self.__client_handler_threads.append(client_handler_thread)
                print(f"Client {_addr} connected")
            else:
                print("Max. clients reached. Waiting for space...")
                time.sleep(3)

    def register_client(self, cli_socket, cli_addr):
        self.id_counter += 1
        self.clients_connected += 1
        self.current_connections[f"id_{self.id_counter}"] = {"socket" : f"{cli_socket}", "address" : f"{cli_addr}", "id" : {self.id_counter}}
        print(f"Current connections : {self.current_connections}")
    
    def disconnect_client(self, client_id):
        del self.current_connections[f"id_{client_id}"]
        client_index = 0
        for i in range(len(self.__client_handler_classes)):
            if self.__client_handler_classes[i].client_id == client_id:
                self.__client_handler_classes[i] = None
                client_index = i
        del self.__client_handler_classes[client_index]
        del self.__client_handler_threads[client_index]
        self.clients_connected -= 1

        print(self.__client_handler_classes)
        print(self.__client_handler_threads)
        print(self.current_connections)

    def close_server(self):
        if self.clients_connected!=0:
            clients = []
            for key , value in self.current_connections.items():
                clients.append(key)

            print(f"Unable to close server, clients are still connected : {clients} \n Continue?(y/n)")
            confirmation = input()
            if confirmation == "y":
                self.active = False
                self.server_socket.close()
                return True
            else:
                return False
        else:
            self.active = False
            self.server_socket.close()
            return True

    def close_terminal(self):
        self.terminal = None
        self.terminal_thread=None

    def open_terminal(self):
        self.terminal = Server_Side_Terminal(self.close_server, self.close_terminal)
        self.terminal_thread = threading.Thread(target=self.terminal.get_command, daemon=True)
        self.terminal_thread.start()

if __name__=="__main__":
    ipconfig = IPCONFIG()
    server = SocketServer(ipconfig.ip(), ipconfig.port())


    # gui = Interface()
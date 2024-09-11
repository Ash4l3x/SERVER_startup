import subprocess

class IPCONFIG:
    __ip = None
    __port = 12345

    def __init__(self):
        self.get_ipconfig_response()
        print(f"For server connection, please use ip = {self.__ip}, port = {self.__port}")

    def get_ipconfig_response(self):
        with subprocess.Popen("ipconfig", stdout = subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=False) as process:
            for line in process.stdout:
                if "IPv4 Address" in line:
                    line_components = line.split(" ")
        self.__ip = line_components[-1].replace("\n", "")
    
    def ip(self)->str:
        return self.__ip
    
    def port(self)->int:
        return self.__port
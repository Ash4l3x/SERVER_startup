import tkinter as tk
from tkinter import scrolledtext, messagebox
import sys

class Logger(scrolledtext.ScrolledText):
    def __init__(self, log:scrolledtext.ScrolledText):
        self.stdout=sys.stdout
        sys.stdout = self
        self.log=log
        
    def write(self, text):
        self.log.configure(state='normal')
        self.log.insert(tk.END, text)
        self.log.configure(state='disabled') 
        self.log.yview(tk.END)

    def flush(self):
        self.stdout.flush()

class Custom_Server_Interface(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=6)
        self.grid_rowconfigure(1, weight=3)
        self.grid_rowconfigure(2, weight=1)

        self.workspace = tk.LabelFrame(self, text="Workspace")
        self.workspace.grid(row=0, column=0, sticky="nsew")

        self.log

class Custom_Client_Interface(tk.LabelFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)


class Interface:
    ipconfig_controller = None
    server_controller = None
    def __init__(self):
        self.root = tk.Tk()
        self.root.state("zoomed")
        self.root.title("SERVER/CLIENT")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.workspace = tk.LabelFrame(self.root, text = "Workspace")
        self.workspace.grid(row=0, column=0, sticky="nsew")

        self._chooser_frame = tk.Label(self.workspace)
        self._chooser_frame.pack(anchor="center", expand=True, fill=tk.BOTH)

        self._chooser_frame.grid_columnconfigure([0,1,2,3,4], weight=1)
        self._chooser_frame.grid_rowconfigure([0,1,2], weight=1)

        self.server_button = tk.Button(self._chooser_frame, text = "SERVER", width=15, height=4, command = self.open_server_side)
        self.server_button.grid(row=1, column=1)

        self.client_button = tk.Button(self._chooser_frame, text = "CLIENT", width=15, height=4, command = self.open_client_side)
        self.client_button.grid(row=1, column=3)

        self.root.mainloop()

    def open_server_side(self):
        self.workspace = Custom_Server_Interface(self.root, text = "Server")
        self.workspace.grid(row=0, column=0, sticky="nsew")

    def open_client_side(self):
        self.workspace = Custom_Client_Interface(self.root, text = "Client")
        self.workspace.grid(row=0, column=0, sticky="nsew")

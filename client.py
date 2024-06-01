import threading
import socket
import argparse
import os
import sys
import tkinter as tk

class Send(threading.Thread):
    #Listens for user input from command line
    #sock the connected sock object
    #name (str) : the username provided by the user

    def __init__(self, sock, name):
        super().__init__()
        self.sock = sock
        self.name = name

    def run(self):
        #Listen for user input from the command line and send
        #typeing "Quit" while close the connection and exit the app

        while True:
            print()
import socket  # Import socket module
import json

s = socket.socket()  # Create a socket object

s.connect(("localhost", 2000))
jsdir = s.recv(1024).decode()   # read data from server
directory = json.loads(jsdir)   # get dict from json string

for (name,num) in directory.items():
    print("%-20s  %s" % (name, num))


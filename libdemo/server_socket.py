# Time server running at 2000
import socket
import json

s = socket.socket()  # Create a socket object
s.bind(("localhost", 2000))  # Bind to the port
s.listen(5)  # Now, wait for client connection.

print("Time Server is ready....")
directory = {"Abc": "334343", "Pqr": "39343434"}
while True:
    c, addr = s.accept()  # It returns connection and address of client
    jsdir = json.dumps(directory)  # convert dict to json string
    c.send(jsdir.encode())
    c.close()

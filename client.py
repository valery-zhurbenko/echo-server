import socket

HOST = '10.0.0.30'    # The remote host
PORT = 5432              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(bytes(s, encoding = 'utf-8'))
data = s.recv(1024)
s.close()
print ('Received', repr(data))
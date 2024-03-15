from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
msg = 'Boa tarde'
s.send(msg.encode())
data = s.recv(1024)
print(data.decode())
s.close()

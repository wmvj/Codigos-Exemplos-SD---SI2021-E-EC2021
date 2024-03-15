from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
(conn, addr) = s.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    msg = data.decode()+"*"
    conn.send(msg.encode())
conn.close

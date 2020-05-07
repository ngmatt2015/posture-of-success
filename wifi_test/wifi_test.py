import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

localIP = s.getsockname()[0]
s.close()
print("Got local IP from 8.8.8.8:", localIP)

print("Waiting BroadCast...")
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',8080))
m=s.recvfrom(8080)
machineIP = m[1][0]
s.close()
print("BroadCast message: ", m[0])
print("Got machine's local address:", m[1][0])

print("Send local IP to machine", localIP)
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((m[1][0], 8080))
s.send(localIP.encode())
s.close()
print("Done")

print("Open Socket Server with port", localIP, 8081)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#while s.connect_ex((localIP, 8081)) != 0:
#    print("waiting for port...")
#    pass
s.bind((localIP, 8081));
s.listen();

print("Waiting machine...")
conn, addr = s.accept()
print("Connected to machine: ", conn, addr)

while True:
    print("Waiting for message...")
    data = conn.recv(1024)
    msg = data.decode()
    print(data.decode())
    conn.sendall(data)
    if msg == 'bye':
        conn.close()
        break

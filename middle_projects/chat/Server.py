import socket

server = socket.socket()
server.bind(("localhost", 12345))
server.listen(1)

print("Waiting for connection...")
conn, addr = server.accept()
print("Connected to", addr)

while True:
    msg = conn.recv(1024).decode()
    print("Client:", msg)

    reply = input("You: ")
    conn.send(reply.encode())
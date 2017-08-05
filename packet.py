import asyncio, socket, time

def send_packet(data, sock):
    sock.send(data)
    sock.send(b"$PACKET_END$")

def recv_packet(sock):
    data = b""
    
    while b"$PACKET_END$" not in data:
        d = sock.recv(1)
        data += d

    data = data.replace(b"$PACKET_END$", b"")

    return data

def host():
    sock = socket.socket()
    sock.bind(("0.0.0.0", 9000))
    sock.listen(5)
    client, address = sock.accept()

    while True:
        time.sleep(1)
        data = recv_packet(client).decode()
        print(data)

        send_packet(b"Hi", client)

def connect():
    sock = socket.socket()
    sock.connect(('localhost', 9000))

    while True:
        send_packet(b"Hello", sock)

        time.sleep(1)
        data = recv_packet(sock).decode()
        print(data)

if __name__ == "__main__":
    mode = input("Mode: ")
    if mode == 'c':
        connect()
    elif mode == 'h':
        host()

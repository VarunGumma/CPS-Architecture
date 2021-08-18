import socket


def read_file(fname):
    with open(fname, 'r') as content_file:
        data = content_file.read()
    return data

print("[SERVER]")
static_server_port = 44672
my_sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sckt.bind(("127.0.0.1", static_server_port))
my_sckt.listen(5)

conn, _ = my_sckt.accept()
fname = conn.recv(10).decode()
print(f"Filename received: {fname}")
print("Searching for file in server directory.")
print("File found. Transmitting file.")
data = read_file(fname)
conn.send(data.encode())
my_sckt.close()
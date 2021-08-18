import socket
from os.path import exists


def read_file(fname):
    with open(fname, 'r') as content_file:
        data = content_file.read()
    return data

print("[PROXY SERVER]")
static_server_port = 44672
static_proxy_server_port = 44671
max_data_to_be_recv = 10240

my_sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sckt.bind(("127.0.0.1", static_proxy_server_port))
my_sckt.listen(5)

conn, _ = my_sckt.accept()
fname = conn.recv(10).decode()
print(f"Filename received: {fname}")
print("Searching for file in proxy-server directory.")

if not exists(fname):
    print("File not found. Connecting to server.")
    temp_sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    temp_sckt.connect(("127.0.0.1", static_server_port))
    temp_sckt.send(fname.encode())
    data = temp_sckt.recv(max_data_to_be_recv)
    with open(fname, 'w') as content_file:
        content_file.write(data.decode())
    temp_sckt.close()
    print("File received. Transmitting to client")
else:
    print("File found. Transmitting it to client.")

data = read_file(fname)
conn.send(data.encode())
my_sckt.close()
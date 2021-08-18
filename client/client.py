import socket

print("[CLIENT]")
static_proxy_server_port = 44671
max_data_to_be_recv = 10240
fname = input("Enter filename to be downloaded: ")

my_sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sckt.connect(("127.0.0.1", static_proxy_server_port))
my_sckt.send(fname.encode())
data = my_sckt.recv(max_data_to_be_recv)

with open("abc.txt", 'w') as content_file:
    content_file.write(data.decode())

print("File received.")
my_sckt.close()
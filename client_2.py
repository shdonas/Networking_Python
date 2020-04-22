import socket

host = "192.168.56.1"
port = 13001

try:
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientSocket.connect((host, port))

	msg = "hello"
	clientSocket.send(msg.encode())
	clientSocket.close()

except Exception as E:
	print(E)

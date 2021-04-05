import socket

def Main():

	sock = socket.socket()
	sock.setblocking(1)
	print("Connecting to server..")
	sock.connect(('localhost', 9000))


	msg = input("Type in the data: ")
	while msg != "exit":
		print("Sending data...")
		sock.send(msg.encode())
		print("Accepting data...")
		data = sock.recv(1024)
		print(data.decode())
		msg = input()

	print("Closing connection..")
	sock.close()

if __name__ == '__main__':
	Main()


# import socket
# from time import sleep
#
# sock = socket.socket()
# sock.setblocking(1)
# sock.connect(('10.38.165.12', 9090))
#
# #msg = input()
# msg = "Hi!"
# sock.send(msg.encode())
#
# data = sock.recv(1024)
#
# sock.close()
#
# print(data.decode())
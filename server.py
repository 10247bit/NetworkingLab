import socket
import time
import os
import threading

def sendMsg(client):
	while True:
		msg=raw_input("TO SEND:")
		client.send(msg)

def recvMsg(client):
	while True:
		msg=client.recv(1024)
		#os.system('clear')
		print " "
		print "Message: ",msg

#Server Socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=2349

address=(host,port)

server.bind(address)

print "Server Started......"

server.listen(5)

print "Accepting Connection"

client,addr=server.accept()

print "Connected with ",client," at address ",addr

#Threads for the send and receive Function
sendThread=threading.Thread(target=sendMsg,args=(client,))
recvThread=threading.Thread(target=recvMsg,args=(client,))
#while True:

sendThread.start()
recvThread.start()
#sendThread.join()
#recvThread.join()
#server.close()


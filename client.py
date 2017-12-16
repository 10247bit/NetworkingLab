import socket
import threading
import os
def sendMsg(client):
	while True:
		msg=raw_input("Type:")
		client.send(msg)

def recvMsg(client):
	while True:
		msg=client.recv(1024)
		#os.system('clear')
		print " "
		print "Message: ",msg

client=socket.socket()

host=socket.gethostname()
port=2398

address=(host,port)

print "Client Started...."

client.connect(address)

print "Client is Connected to the server"


#Threads for the send and receive Function
sendThread=threading.Thread(target=sendMsg,args=(client,))
recvThread=threading.Thread(target=recvMsg,args=(client,))
#while True:

sendThread.start()
recvThread.start()
#sendThread.join()
#recvThread.join()
#client.close()
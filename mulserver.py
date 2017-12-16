import socket
import time
import os
import threading

def sendToAllMsg(msg,client,addr,clientsList):
	print " Message broadcasting is ''",msg,"'' from client ",client," and address ",addr
	preMess="Message broadcasted from the client "+str(client)+" at address "+str(addr)
	for i in clientsList:
		if not i[0] is client:
			i[0].send(preMess)
			i[0].send(" ")
			i[0].send(msg)

def recvMsg(client,addr,clientsList):
	while True:
		msg=client.recv(1024)
		#os.system('clear')
		if msg:
			sendToAllMsg(msg,client,addr,clientsList)

def newClientThread(client,addr,clientsList):
	recvThread=threading.Thread(target=recvMsg,args=(client,addr,clientsList))
	recvThread.start()
	return 1;

#Server Socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=2398

address=(host,port)

server.bind(address)

print "Server Started......"

server.listen(5)

clientsList=[]
while True:

	print "Accepting Connection"

	client,addr=server.accept()

	print "Connected with ",client," at address ",addr
	
	#Holding a list of the clients so that we can create a seperate a thread for each client
	clientsList.append([client,addr])

	#calling the thread creating function

	ack=newClientThread(client,addr,clientsList)

	if ack is True:
		print "Now the Client ",client," is ready to chat"
	time.sleep(1)



#Threads for the send and receive Function
#sendThread=threading.Thread(target=sendMsg,args=(client,))
#recvThread=threading.Thread(target=recvMsg,args=(client,))

#while True:

#sendThread.start()
#recvThread.start()
#sendThread.join()
#recvThread.join()
#server.close()


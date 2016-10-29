import socket      

def pythonFunction():
	return b"You called a function on Python"

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
host = "127.0.0.1"
port = 3715                
soc.bind((host, port))       
soc.listen(5)                 
while True:
	print "listening"
	conn, addr = soc.accept()     
	print "Got connection from"+ str(addr)
	msg = conn.recv(1024)
	print msg
	if msg == "Hello Server" :
		print "Hii everyone"
	else:
		print "Go away"
	data=pythonFunction()
	conn.sendall(data)
	conn.close()
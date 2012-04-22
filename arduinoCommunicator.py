import socket

#Jonathan Sumrall
#arduinoCommunicator.py
#This is a small program that talking over TCP from *eventually* 
#my WP app that sends simple button press information, etc, 
#out the serial port. The idea is that you will have an arduino connected,
#but really this can work for anything. Its EXTREMELY simplistic. 

def main():
	print "You must tell your phone what your IP address is."
	learnOwnIP()
	phone = makePhoneConnection()
	while(1):
		data = handleConnection(phone)
		print data
		



def learnOwnIP():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("gmail.com",80))
	print("Your IP Address is: ",s.getsockname()[0])
	s.close()
	
	
def handleConnection(phone):
	return phone.recv()
	
def makePhoneConnection():
	import socket
import sys

HOST = ''                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
	s = socket.socket(af, socktype, proto)
    except socket.error, msg:
	s = None
	continue
    try:
	s.bind(sa)
	s.listen(1)
    except socket.error, msg:
	s.close()
	s = None
	continue
    break
if s is None:
    print 'could not open socket'
    sys.exit(1)
conn, addr = s.accept()





print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
conn.close()
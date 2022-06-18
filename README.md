## Digispark reverse shell

The scripts creates either reverse shell python script or arduino sketch for digispark. The script is compatible with metasploit.</br>
This Digispark sketch is intended to run on OS X operating System.

## What is digispark?
Digispark is a Attiny85 based microcontroller

## Features

- Creates a reverse shell python script
- Creates a Arduino sketch for digispark

## Arduino Configuration

To flash the digispark module, you need to add this link to your boards maneger</br>
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
python3 payloadGenerator.py -i IP Address -p port -i IP Address -p port -py True
```






## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>


- [AngularJS] - HTML enhanced for web apps!
- [Ace Editor] - awesome web-based text editor
- [markdown-it] - Markdown parser done right. Fast and easy to extend.
- [Twitter Bootstrap] - great UI boilerplate for modern web apps
- [node.js] - evented I/O for the backend
- [Express] - fast node.js network app framework [@tjholowaychuk]
- [Gulp] - the streaming build system
- [Breakdance](https://breakdance.github.io/breakdance/) - HTML
to Markdown converter
- [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.


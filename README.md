# py_chatwork
python scirpt for senting message to chatwork.<br>
you need python 3 more.　　

# How to use
## Preparation
~~~~
$ git clone https://github.com/tadaken3/py_chatwork.git
~~~~

maybe you need <code>requests</code> library. Execute below command

~~~~
$ pip install requests
~~~~

## Setting
Customize below part of `chatwork.py` according to your chatwork setting

~~~~
psr.add_argument('-a', '--apikey', default='#Your Chatwork API KEY')
psr.add_argument('-r', '--roomid', default='Your Room ID')
psr.add_argument('-m', '--message', default='Your Message')
~~~~

## Usage
~~~~
usage: chatwork.py [-h] [-a APIKEY] [-r ROOMID] [-m MESSAGE] [--version]

optional arguments:
  -h, --help            show this help message and exit
  -a APIKEY, --apikey APIKEY
  -r ROOMID, --roomid ROOMID
  -m MESSAGE, --message MESSAGE
  --version             show program's version number and exit
~~~~

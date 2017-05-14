Listener
========
The listener (listen.py) takes three arguments, and is used to set up communications between involved devices. Usage: listen.py [-h] -a ADDRESS -u UPDATES -p PORT

Arguments:
    -h, --help 	show this help message and exit
    -a ADDRESS, --address ADDRESS
     	IP address of machine to listen to
    -u UPDATES, --updates UPDATES
     	IP address of machine to send updates to
    -p PORT, --port PORT
     	Target port of listening devices

In effect, –address points to the previous device in the chain, whilst –update points to the next one. The used port should be higher than 100 to avoid administrator privileges [default=9999].

.. function:: def listen(args)
  listen has two branches for incoming connections.
  Connections coming from the listening port --address are processed and verified from main.verifyBlock(x). Non-verification of block data results in returning an update request to the listening device.
  Connections from --update are assumed to be update requests, and respond with an update method on the target device.
  All other connections are dropped as a security measure.

Site
=====
The site host (site.py) takes two arguments, and hosts the digital voting application. Usage: site.py [-h] -a ADDRESS -p PORT

Arguments:
    -h, --help 	show this help message and exit
    -a ADDRESS, --address ADDRESS
     	Target IP address of next machine
    -p PORT, --port PORT
     	Target port on next machine

Here, –address points to the _next_ block in the chain, as this is where files will be sent. The port is _not_ that which hosts the site [default=8081], but rather the port on the listening device as above [default=9999].

.. function:: def send_static(filename)
  Returns a file from folder [static], such as images or stylesheets, for use in web pages

.. function:: def login()
  Prefaced with @get('/login'), this is the way web pages are served using bottle. Relevant calculations and variables are made, then served with a template from [views]

.. function:: def do_vote()
  Prefaced with @post('/vote'), this processes a post request from a page, such as the form on [/vote]. This request processes a user's vote based on the forms, and passes the information to main.makeBlock()

Main
=====
The (main.py) is the controller in a typical MVC/MOVE system. It contains the main functionality of the application. When running from the command line, use this instead of (site.py), with the same arguments. usage: main.py [-h] -a ADDRESS -p PORT

Arguments:
    -h, --help 	show this help message and exit
    -a ADDRESS, --address ADDRESS
     	Target IP address of next machine
    -p PORT, --port PORT
     	Target port on next machine

.. function:: def getPreviousBlock()
  Cycles through files in [../resources] to read their file height, finding the latest block in the chain. Returns the height as a string.

.. function:: def makeBlock(ballot, voterID)
  Takes variables from a form and generates a new block. Includes default information and calls getPreviousBlock() to find the height. Returns a block object.

.. function:: def hashBlockData(block)
  Calculates an MD5 hash based on key information in the block. Returns the hash as a string.

.. function:: def addBlockToChain(block)
  Writes a new block file into [../resources].

.. function:: def clearBlocks()
  Used in updating files, when called deletes all blocks in [../resources] other than the genesis block.

.. function:: def transmit(b, b_dict)
  Opens a TLS connection to the target host (stored in b_dict), and transmits a pickled dictionary containing block information.

.. function:: def verifyBlock(vblock)
  Given a received block, opens the latest block in the current repository and compares them for discrepencies.
  Returns an integer error code with the following pattern:
  #0 == Data is verified
  #1 == Host chain needs to update
  #2 == Source device needs to update (Unused)
  #3 == Block already processed (Chain is complete)
  #4 == File error; Kill application

.. function:: def main(block, r_ad, r_po)
  Main process chain. Given a block through either command line or site forms, generates a hash for the block, stores the file, then transmits to the next host.

Reader
======
The reader (reader.py) is a small script to enable easy access of blockchain files. When run, the reader will ask for a file number (this will have been provided by running the main application).

Entering the file number will return an output of the file’s contents, then the reader will exit. This is purely for testing purposes, although may later be expanded into a working application.

.. function:: def read(block)
  Takes an input from command line and returns information from a relevant file.
  Files are found in [../resources].

Static and Views
================
Files in these folders are static images, stylesheets, and templates for the web pages.

Bottle
======
This is the service used for hosting web pages using python. It is included with the project to reduce installation requirements. Bottle is available at: https://github.com/bottlepy/bottle

Voter
=====
This file contains sample information taken from a centralised voter database. As authentication is not yet implemented, this is currently unused.

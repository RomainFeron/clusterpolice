#!/usr/bin/python3

'''Send a message to a remote server

Usage:
    client.py MESSAGE [options]

Options:
    -h --help        Show this screen.
    -s --host HOST   Host (a domain, IPv4, or IPv6) [default: 0.0.0.0]
    -p --port PORT   Port [default: 4242]

'''

from docopt import docopt
from clusterpolice import Client

if __name__ == '__main__':

    arguments = docopt(__doc__, version='Naval Fate 2.0')
    host = arguments['--host']
    port = arguments['--port']
    message = arguments['MESSAGE']

    client = Client()
    client.connect(host=host, port=port)
    client.send(message)

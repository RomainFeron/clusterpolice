#!/usr/bin/python3

'''Run a listening server on a specific host and port

Usage:
    server.py [options]

Options:
    -h --help        Show this screen.
    -s --host HOST   Host (a domain, IPv4, or IPv6) [default: 0.0.0.0]
    -p --port PORT   Port [default: 4242]

'''

from docopt import docopt
from clusterpolice import Server


if __name__ == '__main__':

    arguments = docopt(__doc__, version='Naval Fate 2.0')
    host = arguments['--host']
    port = arguments['--port']

    server = Server()
    server.start(host=host, port=port)

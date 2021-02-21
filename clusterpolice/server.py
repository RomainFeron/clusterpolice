import logging
import socketserver
from .connected_object import ConnectedObject


class Handler(socketserver.StreamRequestHandler):
    '''
    '''

    def handle(self):
        '''
        '''
        for line in self.rfile:
            self.data = line.rstrip().decode('utf-8')
            print(f'{self.client_address[0]} wrote: {self.data}')


class Server(ConnectedObject):
    '''
    '''

    def __init__(self, host='0.0.0.0', port=4242):
        '''
        '''
        ConnectedObject.__init__(self, host=host, port=port)
        self._server = None

    @property
    def server(self):
        return self._server

    def __str__(self):
        '''
        '''
        info = f'host: {self.host}; port {self.port}'
        return info

    def start(self, host=None, port=None):
        '''
        '''
        if host:
            self.host = host
        if port:
            self.port = port
        self._server = socketserver.TCPServer((self._host, self._port), Handler)
        logging.info(f'Started server on {self._host}:{self._port}')
        self._server.serve_forever()

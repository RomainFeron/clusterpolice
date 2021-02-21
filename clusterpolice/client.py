import logging
import socket
from .connected_object import ConnectedObject


class Client(ConnectedObject):
    '''
    '''

    def __init__(self, host='0.0.0.0', port=4242):
        '''
        '''
        ConnectedObject.__init__(self, host=host, port=port)
        self._socket = None
        self._connected = False

    @property
    def connected(self):
        return self._connected

    def connect(self, host=None, port=None):
        '''
        '''
        if host:
            self.host = host
        if port:
            self.port = port
        assert self._host and self._port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self._host, self._port))
        logging.info(f'Connected to {self._host}:{self._port}')
        self._connected = True

    def disconnect(self):
        '''
        '''
        self._socket.disconnect()
        self._socket = None

    def send(self, data):
        '''
        '''
        if not self._connected:
            msg = ('Cannot send data from a client without open connection. '
                   'See Client.connect().')
            raise RuntimeError(msg)
        self._socket.send(bytes(data + "\n", "utf-8"))

import validators
from .logger import setup_logging


class ConnectedObject:
    '''
    '''

    def __init__(self, host='0.0.0.0', port=4242):
        '''
        '''
        setup_logging()
        self._host = None
        self._port = None

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        '''
        '''
        error_msg = (f'Invalid host "{value}". Value should be a '
                     f'domain, valid IPv4 address, or valid IPv6 address.')
        is_domain = validators.domain(value)
        is_ipv4 = validators.ip_address.ipv4(value)
        is_ipv6 = validators.ip_address.ipv6(value)
        if is_domain or is_ipv4 or is_ipv6:
            self._host = value
            return
        raise ValueError(error_msg)

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        '''
        '''
        error_msg = (f'Invalid port number "{value}". Value should be an '
                     f'integer between 1025 and 65535 (included).')
        try:
            value = int(value)
        except ValueError:
            raise ValueError(error_msg)
        if 1024 < int(value) < 65536:
            self._port = int(value)
            return
        raise ValueError(error_msg)

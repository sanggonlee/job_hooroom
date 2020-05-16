class ConfigError(Exception):
    def __init__(self, message):
        self.message = message


class UnknownDocTypeError(Exception):
    def __init__(self, type, message):
        self.message = ('Unknown doc type %s' % type) + message

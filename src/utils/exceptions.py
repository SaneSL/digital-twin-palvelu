


class CustomException(Exception):
    def __init__(self, message, status_code, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['Error'] = self.message
        return rv


class DatabaseError(CustomException):
    message = "Database error"
    def __init__(self, message=message, status_code=500):
        super().__init__(message, status_code)

class ApiAuthenticationError(CustomException):
    message = "Authentication error"
    def __init__(self, message=message, status_code=401):
        super().__init__(message, status_code)


class ArgMissingError(CustomException):
    message = "Missing argument(s)"
    def __init__(self, message=message, status_code=403):
        super().__init__(message, status_code)
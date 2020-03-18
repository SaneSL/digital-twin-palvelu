



class CustomException(Exception):
    def __init__(self, message, status_code, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message']: self.message
        return rv


class DatabaseError(CustomException):
    def __init__(self, message="Database Error", status_code=500):
        super().__init__(message, status_code)

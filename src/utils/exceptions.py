


class CustomException(Exception):
    def __init__(self, message, status_code, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['error'] = self.message
        return rv


class DatabaseError(CustomException):
    message = "Database error"
    def __init__(self, message=message, status_code=500):
        super().__init__(message, status_code)

class ApiAuthenticationError(CustomException):
    message = "Authentication error"
    def __init__(self, message=message, status_code=401):
        super().__init__(message, status_code)


class InvalidArgError(CustomException):
    message = "Invalid argument(s)"
    def __init__(self, message=message, status_code=400):
        super().__init__(message, status_code)


class ModuleError(CustomException):
    message = "Module error"
    def __init__(self, message=message, status_code=500):
        super().__init__(message, status_code)


class ModuleArgError(CustomException):
    message = "Invalid module arguments"
    def __init__(self, message=message, status_code=400):
        super().__init__(message, status_code)


class SubEndError(CustomException):
    message = "No active subscription"
    def __init__(self, message=message, status_code=400):
        super().__init__(message, status_code)
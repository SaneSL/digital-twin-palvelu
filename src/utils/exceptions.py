


class CustomException(Exception):
    def __init__(self, message, status_code):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        rv = dict()
        rv['error'] = {"code": self.status_code, "message": self.message}
        return rv


class DatabaseError(CustomException):
    message = "Database error"
    def __init__(self, message=message, status_code=500):
        super().__init__(message, status_code)


class AuthenticationError(CustomException):
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
    message = "Invalid module argument(s)"
    def __init__(self, message=message, status_code=400):
        super().__init__(message, status_code)


class ModuleNotFound(CustomException):
    message = "Invalid module ID"
    def __init__(self, message=message, status_code=400):
        super().__init__(message, status_code)


class NoResultsFound(CustomException):
    message = "No results found"
    def __init__(self, message=message, status_code=404):
        super().__init__(message, status_code)

class BaseError(Exception):
    def __init__(self, status_code, reason, look_for=""):
        self.status_code = status_code
        self.reason = reason
        self.look_for = "Where to start debugging? - " + look_for
        super().__init__(self.reason)


class InvalidDataFormatError(BaseError):
    pass


class InvalidFileFormatError(BaseError):
    pass

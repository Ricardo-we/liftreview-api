
class ResponseException(Exception):
    """Base class for exceptions that occur during response processing."""

    def __init__(self,exception: Exception, message: str, code: str):
        super().__init__(message)
        self.exception = exception
        self.message = message
        self.code = code
        
    def __dict__(self):
        return {
            "code": self.code,
            "message": self.message,
            "exception": repr(self.exception),
        }
        
    def get_status_code(self) -> int:
        return get_response_status_by_code(self.code)
        

class ResponseCodes:
    NOT_FOUND = "not_found"
    UNAUTHORIZED = "unauthorized"
    FORBIDDEN = "forbidden"
    INTERNAL_SERVER_ERROR = "internal_server_error"
    BAD_REQUEST = "bad_request"
    UNKNOWN_ERROR = "unknown_error"
    SUCCESS = "success"
    

def get_response_status_by_code(code=ResponseCodes.UNKNOWN_ERROR) -> str:
    return {
        ResponseCodes.NOT_FOUND: 404,
        ResponseCodes.UNAUTHORIZED: 401,
        ResponseCodes.FORBIDDEN: 403,
        ResponseCodes.INTERNAL_SERVER_ERROR: 500,
        ResponseCodes.BAD_REQUEST: 400,
        ResponseCodes.UNKNOWN_ERROR: 500,
        ResponseCodes.SUCCESS: 200,
    }.get(code, 500)
class OkResponse:
    """
    Class representing a successful response.
    """

    def __init__(self, message: str, code: int = 200):
        self.message = message
        self.code = code

    def __repr__(self):
        return f"OkResponse(message={self.message}, code={self.code})"
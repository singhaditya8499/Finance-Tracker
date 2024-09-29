class SimpleResponse:
    def __init__(self, status_code, message, data=None):
        self.status_code = status_code
        self.message = message
        self.data = data

    def __str__(self):
        return f"Response(status_code={self.statusCode}, message='{self.message}', data={self.data})"
    
    def to_dict(self):
        return {
            "status_code": self.status_code,
            "message": self.message,
            "data": self.data
        }

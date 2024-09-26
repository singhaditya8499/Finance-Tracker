class InvalidDBObject(Exception):
    """Raised when the DB object passed is incorrect"""
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return str(self.message)
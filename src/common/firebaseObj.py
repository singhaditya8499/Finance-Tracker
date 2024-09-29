from flask import json


class FireBaseObj:
    def __init__(self, collection_name: str, document_name: str, data: dict):
        if not isinstance(collection_name, str):
            raise TypeError("collection_name must be a string")
        if not isinstance(document_name, str):
            raise TypeError("document_name must be a string")
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")
        
        self.collection_name = collection_name
        self.document_name = document_name
        self.data = data
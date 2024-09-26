from flask import json


class FireBaseObj:
    def __init__(self, collection_name: str, document_name: str, data: dict):
        self.collection_name = collection_name
        self.document_name = document_name
        self.data = data
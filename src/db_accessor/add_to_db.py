from src.common.SimpleResponse import SimpleResponse
from src.common.enums import Collections
from src.common.firebaseObj import FireBaseObj
from src.common.exceptions import InvalidDBObject


def add_to_db(client, obj: FireBaseObj):
    try:
        _validate_db_object(obj)
        collection_name = obj.collection_name
        document_name = obj.document_name
        data = obj.data
        doc_ref = client.collection(collection_name).document(document_name)
        doc_ref.set(data)
        return SimpleResponse(status_code=200, message="OK")
    except InvalidDBObject as e:
        return SimpleResponse(
            status_code=400,
            message=e.message
        )

def _validate_db_object(obj: FireBaseObj):
    data = obj.data
    if data["id"] != obj.document_name:
        raise InvalidDBObject("Document name passed does'nt match the id of the data")
    
    if obj.collection_name not in {e.value for e in Collections}:
        raise InvalidDBObject("Collection name is not a valid collection")
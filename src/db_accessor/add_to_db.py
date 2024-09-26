from common import SimpleResponse
from common.enums import Collections
from common.firebaseObj import FireBaseObj
from common.exceptions import InvalidDBObject


def add_to_db(obj: FireBaseObj):
    try:
        _validate_db_object(obj)
    except InvalidDBObject as e:
        return SimpleResponse(
            status_code=400,
            message=e
        )

def _validate_db_object(obj: FireBaseObj):
    data = obj.data
    if data["id"] != obj.document_name:
        raise InvalidDBObject("Document name passed does'nt match the id of the data")
    
    if obj.collection_name not in {e.value() for e in Collections}:
        raise InvalidDBObject("Collection name is not a valid collection")
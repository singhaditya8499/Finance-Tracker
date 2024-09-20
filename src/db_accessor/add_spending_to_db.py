import firebase_admin
from firebase_admin import credentials, firestore

def add_to_db(collections, document_id, data):
    # Use the downloaded JSON file
    path = (
        
    )
    cred = credentials.Certificate(path)
    firebase_admin.initialize_app(cred)

    # Initialize Firestore DB
    db = firestore.client()

    try:
        doc_ref = db.collection(collections).document(document_id)
        doc_ref.set(data)
        print(f'Document {document_id} added to {collections} collection.')
    except Exception as e:
        print(f'Error adding document: {e}')
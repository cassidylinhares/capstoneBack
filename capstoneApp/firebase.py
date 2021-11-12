from firebase_admin import initialize_app, credentials, firestore
from datetime import datetime

# Use a service account
cred = credentials.Certificate('../ecohub-707c9-firebase-adminsdk-ctcaz-710ec24c6b.json')
initialize_app(cred)


def getLights():
    db = firestore.client()
    col_ref = db.collection(u'lights')
    docs = col_ref.stream()

    lights = []
    for doc in docs:
        vals = {}
        vals[doc.id] = doc.to_dict()
        lights.append(vals)

    return lights

def getLight(timestamp):
    db = firestore.client()
    doc_ref = db.collection(u'lights').document(timestamp)
    doc = doc_ref.get()

    light = {}
    light[timestamp]= doc.to_dict()

    return light

def insertLight(data):
    print(datetime.fromisoformat(data['time'][:-1]) )
    db = firestore.client()
    doc_ref = db.collection(u'lights').document(data['time'])
    doc_ref.set({
        u'name': data['name'],
        u'status': data['status'],
        u'time': datetime.fromisoformat(data['time'][:-1]) 
    })

    doc = doc_ref.get()

    light = {}
    light[data['time']]= doc.to_dict()

    return light
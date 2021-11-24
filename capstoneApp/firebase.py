from firebase_admin import initialize_app, credentials, firestore
from datetime import datetime

# Use a service account
cred = credentials.Certificate('../ecohub-707c9-firebase-adminsdk-ctcaz-710ec24c6b.json')
initialize_app(cred)

####### LIGHTS ######
def getLights(room):
    db = firestore.client()
    col_ref = db.collection(u'lights').document(room).collection(u'history')
    docs = col_ref.stream()

    lights = []
    for doc in docs:
        vals = {}
        vals[doc.id] = doc.to_dict()
        lights.append(vals)

    return lights

def getLight(room):
    db = firestore.client()
    doc_ref = db.collection(u'lights').document(room)
    doc = doc_ref.get()

    light = {}
    light[room]= doc.to_dict()

    return light

def insertLight(data):
    db = firestore.client()
    history_ref = db.collection(u'lights').document(data['name']).collection(u'history').document(data['time'])
    doc_ref = db.collection(u'lights').document(data['name'])

    doc_ref.set({
        u'status': data['status'],
        u'time': datetime.fromisoformat(data['time'][:-1]) 
    })

    history_ref.set({
        u'status': data['status'],
        u'time': datetime.fromisoformat(data['time'][:-1]) 
    })

    doc = doc_ref.get()

    light = {}
    light[data['time']]= doc.to_dict()

    return light

###### THERMOSTAT ######
def getTemps():
    db = firestore.client()
    col_ref = db.collection(u'thermostat')
    docs = col_ref.stream()

    temps = []
    for doc in docs:
        vals = {}
        vals[doc.id] = doc.to_dict()
        temps.append(vals)

    return temps

def getTemp(timestamp):
    db = firestore.client()
    doc_ref = db.collection(u'thermostat').document(timestamp)
    doc = doc_ref.get()

    temp = {}
    temp[timestamp]= doc.to_dict()

    return temp

def insertTemp(data):
    db = firestore.client()
    doc_ref = db.collection(u'thermostat').document(data['time'])
    doc_ref.set({
        u'temp': data['temp'],
        u'time': datetime.fromisoformat(data['time'][:-1]) 
    })

    doc = doc_ref.get()

    temp = {}
    temp[data['time']]= doc.to_dict()

    return temp
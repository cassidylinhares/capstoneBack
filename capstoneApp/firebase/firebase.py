from firebase_admin import initialize_app, credentials, firestore
from datetime import datetime, timedelta, date
import random

# Use a service account
cred = credentials.Certificate(
    '../../ecohub-707c9-firebase-adminsdk-ctcaz-710ec24c6b.json')
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
    light[room] = doc.to_dict()

    return light


def insertLight(data):
    db = firestore.client()
    history_ref = db.collection(u'lights').document(
        data['name']).collection(u'history').document(data['time'])
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
    light[data['time']] = doc.to_dict()

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
    temp[timestamp] = doc.to_dict()

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
    temp[data['time']] = doc.to_dict()

    return temp

###### DIET ########


def getDiet(userId, datestamp):
    db = firestore.client()
    doc_breakfast = db.collection(u'userDiet').document(
        userId).collection(u'breakfast').document(datestamp)
    doc_lunch = db.collection(u'userDiet').document(
        userId).collection(u'lunch').document(datestamp)
    doc_dinner = db.collection(u'userDiet').document(
        userId).collection(u'dinner').document(datestamp)

    doc1 = doc_breakfast.get()
    doc2 = doc_lunch.get()
    doc3 = doc_dinner.get()

    diet = {'date': datestamp}
    if doc1.exists:
        diet['breakfast'] = doc1.to_dict()
    if doc2.exists:
        diet['lunch'] = doc2.to_dict()
    if doc3.exists:
        diet['dinner'] = doc3.to_dict()

    return diet


def getDietPrevDay(userId):
    yesterday = date.today() - timedelta(days=1)

    return getDiet(userId, yesterday.strftime("%d-%m-%Y"))


def getDietPrevWeek(userId):
    diet = []

    # get previous 6 days
    for i in range(6, 0, -1):
        day = date.today() - timedelta(days=i)
        diet.append(getDiet(userId, day.strftime("%d-%m-%Y")))

    # get todays date
    diet.append(getDiet(userId, date.today().strftime("%d-%m-%Y")))

    return diet


def getDietPrevMonth(userId):
    diet = []

    for i in range(30, 0, -1):
        day = date.today() - timedelta(days=i)
        diet.append(getDiet(userId, day.strftime("%d-%m-%Y")))

    # get todays date
    diet.append(getDiet(userId, date.today().strftime("%d-%m-%Y")))
    return diet

###### Transportation #######


def getTransportation(userId, datestamp):
    db = firestore.client()
    doc_ref = db.collection(u'userTransportation').document(
        userId).collection(u'data').document(datestamp)
    doc = doc_ref.get()

    transportation = {'date': datestamp}
    if doc.exists:
        transportation['data'] = doc.to_dict()

    return transportation


def getTransportationPrevDay(userId):
    yesterday = date.today() - timedelta(days=1)

    return getTransportation(userId, yesterday.strftime("%d-%m-%Y"))


def getTransportationPrevWeek(userId):
    transportation = []

    # get previous 6 days
    for i in range(6, 0, -1):
        day = date.today() - timedelta(days=i)
        transportation.append(getTransportation(
            userId, day.strftime("%d-%m-%Y")))

    # get todays date
    transportation.append(getTransportation(
        userId, date.today().strftime("%d-%m-%Y")))

    return transportation


def getTransportationPrevMonth(userId):
    transportation = []

    # get previous 6 days
    for i in range(30, 0, -1):
        day = date.today() - timedelta(days=i)
        transportation.append(getTransportation(
            userId, day.strftime("%d-%m-%Y")))

    # get todays date
    transportation.append(getTransportation(
        userId, date.today().strftime("%d-%m-%Y")))

    return transportation


####### RECOMMENDATION #######


def insertRecommendation(userId, datestamp, data):
    db = firestore.client()
    doc_low_ref = db.collection(u'recommendation').document(
        userId).collection('lowest').document(datestamp)
    doc_low_ref.set({
        u'lowest': data['lowest'],
    })

    doc_high_ref = db.collection(u'recommendation').document(
        userId).collection('highest').document(datestamp)
    doc_high_ref.set({
        u'highest': data['highest'],
    })

    doc_thresh_ref = db.collection(u'recommendation').document(
        userId).collection('threshold').document(datestamp)
    doc_thresh_ref.set({
        u'threshold': data['threshold']
    })

    doc_low = doc_low_ref.get()
    doc_high = doc_high_ref.get()
    doc_thresh = doc_thresh_ref.get()

    recommendation = {}
    recommendation['date'] = datestamp
    recommendation['lowest'] = doc_low.to_dict()
    recommendation['highest'] = doc_high.to_dict()
    recommendation['threshold'] = doc_thresh.to_dict()

    return recommendation


def getSuggestion(category):  # get suggestion for provided data
    db = firestore.client()

    suggestions = {}
    recommendation = ''

    doc_ref = db.collection(u'suggestions').document(
        category)
    doc = doc_ref.get()

    suggestions = doc.to_dict()
    recommendation = random.choice(suggestions['suggestions'])

    return recommendation

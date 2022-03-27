from firebase_admin import auth
from firebase.firebase import getDietPrevWeek, getTransportationPrevWeek, getSuggestion


def executeRecommendations():
    # executing empty sample job
    for user in auth.list_users().iterate_all():
        # print(user.uid)
        print(lowestCategory(user.uid))
        # highestCategory()
        # threshold()


def calculateCarbonDiet(data):
    sum = 0

    if 'breakfast' in data:
        sum = sum([d['total'] for d in data])

    # return the carbon in grams or kg
    return sum


def calculateCarbonTransportation(data):
    # Average g CO2 per person KM (user inputs kilometre traveled and transportation)
    transportMode = {'Domestic Flight': 240, 'Long Haul Flight': 195, 'Car (1 passenger)': 194, 'Bus': 99,
                     'Car (4 passengers)': 48, 'Domestic Rail': 46, 'Coach Bus': 29, 'Eletric Vehicle': 80, 'Taxi/Uber': 244,
                     'Motorbike': 126, 'Bike': 8, 'Walk': 0}

    # calculate the carbon for that day
    # {date:29-01-2022, data:{bus:20, walk: 1.2}}
    carbonProduced = 0
    if 'data' in data:
        travel = list(data['data'].items())
        carbonProduced = sum([t[1] * transportMode[t[0]] for t in travel])

    # return the carbon in grams or kg
    return carbonProduced


def lowestCategory(userId):  # check for lowest producer/category
    # STEP1: get avg for each category over the Week
    # [{date: dksadkas, breakfast: {lamb:1}}, {date: dksadkas, breakfast: {lamb:1}}]
    diet = getDietPrevWeek(userId)
    dietCarbon = [calculateCarbonDiet(i) for i in diet]
    avgDiet = sum(dietCarbon)/len(dietCarbon)

    transportation = getTransportationPrevWeek(userId)
    transportationCarbon = [
        calculateCarbonTransportation(i) for i in transportation]
    avgTransportation = sum(transportationCarbon)/len(transportationCarbon)

    '''
    diet: [#carbonDay30, #carbonDay29, ...]
    transportation: [#carbonDay30, #carbonDay29, ...]
    '''
    # STEP2: find min of the avg
    category = {
        'diet': avgDiet,
        'transportation': avgTransportation,
    }
    minAverage = min(category.values())

    minCategory = list(category.values()).index(minAverage) if list(
        category.values()).index(minAverage) != 0 else ''

    '''
    check which category is the lowest using a Weeks worth of data
    run this each day
    '''
    return {'carbon': minAverage, 'category': minCategory, 'suggestion': getSuggestion(minCategory)}


def highestCategory(userId):  # check for highest producer
    # STEP1: get avg for each category over the Week
    # [{date: dksadkas, breakfast: {lamb:1}}, {date: dksadkas, breakfast: {lamb:1}}]
    diet = getDietPrevWeek(userId)
    dietCarbon = [calculateCarbonDiet(i) for i in diet]
    avgDiet = sum(dietCarbon)/len(dietCarbon)

    # transportation: getting the avg
    # [{date: dksadkas, breakfast: {lamb:1}}, {date: dksadkas, breakfast: {lamb:1}}]
    transportation = getTransportationPrevWeek(userId)
    transportationCarbon = [
        calculateCarbonTransportation(i) for i in transportation]
    avgTransportation = sum(transportationCarbon)/len(transportationCarbon)

    '''
    diet: [#carbonDay30, #carbonDay29, ...]
    transportation: [#carbonDay30, #carbonDay29, ...]
    '''
    # STEP2: find min of the avg
    category = {
        'diet': avgDiet,
        'transportation': avgTransportation,
    }
    maxAverage = max(category.values())

    maxCategory = list(category.values()).index(maxAverage)

    '''
    check which category is the highest using a Weeks worth of data
    run this each day
    '''
    return {'carbon': maxAverage, 'category': maxCategory, 'suggestion': getSuggestion(maxCategory)}

# check if above thresh hold

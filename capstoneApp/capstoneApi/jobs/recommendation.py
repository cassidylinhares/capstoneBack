from unicodedata import category
from firebase import getDietPrevMonth, getTransportationPrevMonth, getDiet


def calculateCarbonDiet(data):
    # CO2 produced in each food, per serving (g)
    foodCarbon = {'Beef': 7461, 'Chocolate': 1400, 'Lamb': 2979, 'Coffee': 4993, 'Shellfish': 2015, 'Cheese': 1194,
                  'Fish': 1022, 'Bacon': 923, 'Chicken': 740, 'Turkey': 740, 'Eggs': 560, 'Rice': 445, 'Nuts': 129,
                  'Tofu': 474, 'Milk': 756, 'Oatmeal': 248, 'Vegetables': 45, 'Beer': 518, 'Wine': 358,
                  'Bread': 133, 'Pasta': 133, 'Crackers': 133, 'Berries': 176, 'Fruit': 121, 'Peas': 147,
                  'Root Vegetables': 37, 'Juice': 121, 'Baked Goods': 63, 'Potatoes': 39}

    dict = getDiet('userId', 'timestamp')
    carbonProduced = 0

    breakfast = dict['breakfast']
    lunch = dict['lunch']
    dinner = dict['dinner']

    # calculate the carbon for that day
    for i in breakfast:
        serving = int(breakfast[i])
        carbonProduced += foodCarbon[i] * serving

    for j in lunch:
        serving = int(lunch[j])
        carbonProduced += foodCarbon[j] * serving

    for k in dinner:
        serving = int(dinner[k])
        carbonProduced += foodCarbon[k] * serving

    # return the carbon in grams or kg
    return carbonProduced


def calculateCarbonTransportation():
    # Average g CO2 per person KM (user inputs kilometre traveled and transportation)
    transportMode = {'Domestic Flight': 240, 'Long Haul Flight': 195, 'Car (1 passenger)': 194, 'Bus': 99,
                     'Car (4 passengers)': 48, 'Domestic Rail': 46, 'Coach Bus': 29, 'Eletric Vehicle': 80, 'Taxi/Uber': 244,
                     'Motorbike': 126, 'Bike': 8, 'Walk': 0}

    return

# check for lowest producer/category


def lowestCategory():
    # STEP1: get avg for each category over the month
    # [{date: dksadkas, breakfast: {lamb:1}}, {date: dksadkas, breakfast: {lamb:1}}]
    diet = getDietPrevMonth('userId')
    dietCarbon = [calculateCarbonDiet(i) for i in diet]
    avgDiet = sum(dietCarbon)/len(dietCarbon)

    # transportation: getting the avg
    # [{date: dksadkas, breakfast: {lamb:1}}, {date: dksadkas, breakfast: {lamb:1}}]
    transportation = getTransportationPrevMonth('userId')
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

    minCategory = list(category.values()).index(minAverage)

    '''
    check which category is the lowest using a months worth of data
    run this each day
    '''
    return minCategory

# check for highest producer (same as low but with highest)


def highestCategory():
 # STEP1: get avg for each category over the month
    # [{date: dksadkas, breakfast: {lamb:1}}, {date: dksadkas, breakfast: {lamb:1}}]
    diet = getDietPrevMonth('userId')
    dietCarbon = [calculateCarbonDiet(i) for i in diet]
    avgDiet = sum(dietCarbon)/len(dietCarbon)

    # transportation: getting the avg
    # [{date: dksadkas, breakfast: {lamb:1}}, {date: dksadkas, breakfast: {lamb:1}}]
    transportation = getTransportationPrevMonth('userId')
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
    check which category is the highest using a months worth of data
    run this each day
    '''
    return maxCategory

# check if above thresh hold

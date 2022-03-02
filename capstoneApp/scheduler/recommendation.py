from unicodedata import category
from firebase import getDietPrevMonth, getTransportationPrevMonth


def calculateCarbonDiet(data):
    #calculate the carbon for that day
    #return the carbon in grams or kg
    return

def calculateCarbonTransportation():
    return

# check for lowest producer/category
def lowestCategory():
    # STEP1: get avg for each category over the month
    diet = getDietPrevMonth('userId') #[{date: dksadkas, breakfast: {lamb:1}}, {date: dksadkas, breakfast: {lamb:1}}]
    dietCarbon = [calculateCarbonDiet(i) for i in diet]
    avgDiet = sum(dietCarbon)/len(dietCarbon)

    # transportation: getting the avg 
    transportation = getTransportationPrevMonth('userId') #[{date: dksadkas, breakfast: {lamb:1}}, {date: dksadkas, breakfast: {lamb:1}}]
    transportationCarbon = [calculateCarbonTransportation(i) for i in transportation]
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
    diet = getDietPrevMonth('userId') #[{date: dksadkas, breakfast: {lamb:1}}, {date: dksadkas, breakfast: {lamb:1}}]
    dietCarbon = [calculateCarbonDiet(i) for i in diet]
    avgDiet = sum(dietCarbon)/len(dietCarbon)

    # transportation: getting the avg 
    transportation = getTransportationPrevMonth('userId') #[{date: dksadkas, breakfast: {lamb:1}}, {date: dksadkas, breakfast: {lamb:1}}]
    transportationCarbon = [calculateCarbonTransportation(i) for i in transportation]
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

# check thresh hold

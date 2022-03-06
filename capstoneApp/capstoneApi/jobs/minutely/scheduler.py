from django_extensions.management.jobs import MinutelyJob
from firebase_admin import auth
from firebase.firebase import getDietPrevMonth, getTransportationPrevMonth, getSuggestion


class Job(MinutelyJob):

    def execute(self):
        # executing empty sample job
        for user in auth.list_users().iterate_all():
            # print(user.uid)
            self.lowestCategory(user.uid)
            # highestCategory()
            # threshold()

    def calculateCarbonDiet(self, data):
        # CO2 produced in each food, per serving (g)
        foodCarbon = {'Beef (Cows Meat)': 7461, 'Chocolate': 1400, 'Lamb': 2979, 'Coffee': 4993, 'Shellfish': 2015, 'Cheese and Yogurt': 1194,
                      'Fish': 1022, 'Bacon': 923, 'Chicken': 740, 'Turkey': 740, 'Eggs': 560, 'Rice': 445, 'Nuts': 129,
                      'Tofu': 474, 'Milk': 756, 'Oatmeal': 248, 'Vegetables': 45, 'Beer': 518, 'Wine': 358,
                      'Bread': 133, 'Pasta': 133, 'Crackers': 133, 'Berries': 176, 'Fruit': 121, 'Peas': 147,
                      'Root Vegetables': 37, 'Juice': 121, 'Baked Goods': 63, 'Potatoes': 39}

        # {date: dksadkas, breakfast: {lamb:1}, }
        print(data)
        # calculate the carbon for that day

        dailySumBreakfast, dailySumLunch, dailySumDinner = 0, 0, 0

        if 'breakfast' in data:
            breakfast = list(data['breakfast'].items())
            dailySumBreakfast = sum([b[1] * foodCarbon[b[0]]
                                    for b in breakfast])
        if 'lunch' in data:
            lunch = list(data['lunch'].items())
            dailySumLunch = sum([l[1] * foodCarbon[l[0]] for l in lunch])

        if 'dinner' in data:
            dinner = list(data['dinner'].items())
            dailySumDinner = sum([d[1] * foodCarbon[d[0]] for d in dinner])

        carbonProduced = sum(
            [dailySumBreakfast, dailySumLunch, dailySumDinner])
        # return the carbon in grams or kg
        return carbonProduced

    def calculateCarbonTransportation(self, data):
        # Average g CO2 per person KM (user inputs kilometre traveled and transportation)
        transportMode = {'Domestic Flight': 240, 'Long Haul Flight': 195, 'Car (1 passenger)': 194, 'Bus': 99,
                         'Car (4 passengers)': 48, 'Domestic Rail': 46, 'Coach Bus': 29, 'Eletric Vehicle': 80, 'Taxi/Uber': 244,
                         'Motorbike': 126, 'Bike': 8, 'Walk': 0}

        # calculate the carbon for that day
        # {date:29-01-2022, data:{bus:20, walk: 1.2}}
        carbonProduced = 0
        print(data)
        if 'data' in data:
            travel = list(data['data'].items())
            carbonProduced = sum([t[1] * transportMode[t[0]] for t in travel])

        # return the carbon in grams or kg
        return carbonProduced

    def lowestCategory(self, userId):  # check for lowest producer/category
        # STEP1: get avg for each category over the month
        # [{date: dksadkas, breakfast: {lamb:1}}, {date: dksadkas, breakfast: {lamb:1}}]
        diet = getDietPrevMonth(userId)
        dietCarbon = [self.calculateCarbonDiet(i) for i in diet]
        avgDiet = sum(dietCarbon)/len(dietCarbon)

        transportation = getTransportationPrevMonth(userId)
        transportationCarbon = [
            self.calculateCarbonTransportation(i) for i in transportation]
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
        print(minCategory)

        '''
        check which category is the lowest using a months worth of data
        run this each day
        '''
        return {'carbon': minAverage, 'category': minCategory, 'suggestion': getSuggestion(minCategory)}

    def highestCategory(self, userId):  # check for highest producer
        # STEP1: get avg for each category over the month
        # [{date: dksadkas, breakfast: {lamb:1}}, {date: dksadkas, breakfast: {lamb:1}}]
        diet = getDietPrevMonth(userId)
        dietCarbon = [self.calculateCarbonDiet(i) for i in diet]
        avgDiet = sum(dietCarbon)/len(dietCarbon)

        # transportation: getting the avg
        # [{date: dksadkas, breakfast: {lamb:1}}, {date: dksadkas, breakfast: {lamb:1}}]
        transportation = getTransportationPrevMonth(userId)
        transportationCarbon = [
            self.calculateCarbonTransportation(i) for i in transportation]
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
        return {'carbon': maxAverage, 'category': maxCategory, 'suggestion': getSuggestion(maxCategory)}

    # check if above thresh hold

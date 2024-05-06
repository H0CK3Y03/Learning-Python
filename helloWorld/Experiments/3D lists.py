non_alc_drinks = ["Soda", "Juice", "Water"]
alc_drinks = ["Wine", "Vodka", "Whiskey"]
dinner = ["Burger", "Pizza", "Hotdog"]
lunch = ["Steak", "Spaghetti", "Soup"]

food = [lunch, dinner]
beverages = [non_alc_drinks, alc_drinks]

edibles = [food, beverages]
print(edibles[1][0][2])
print(edibles[1][0][2][2])
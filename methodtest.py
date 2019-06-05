def fav_color(color, food):
    fav_food(food)
    print("My favorite color is " + color)
def fav_food(food):
    print("My favorite food is " + food)
foods = ["Apple", "Pear", "Strawberries"]
colors = ["Yellow", "Blue", "Green", "Orange"]
for color in colors:
    for food in foods:
        fav_color(color, food)

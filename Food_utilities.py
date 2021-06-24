"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  Michael Moriarty
ID:      170409170
Email:   mori9170@mylaurier.ca
Section: CP164 A
__updated__ = "2021-05-27"
-------------------------------------------------------
"""
from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    name = input("Name: ")
    origin = input("""Origin
 0 Canadian
 1 Chinese
 2 Indian
 …
: """)
    origin = int(origin)
    veg = input("Vegetarian (Y/N): ")
    if veg == "Y":
        veg = True
    else:
        veg = False
    calories = input("Calories: ")
    calories = int(calories)
    food = Food(name, origin, veg, calories)
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """

    # Your code here
    line = line.split("|")
    food = Food(line[0], int(line[1]), bool(line[2] == "True"), int(line[3]))
    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    foods = []
    while file_variable:
        line = file_variable.readline()
        if line == "":
            break
        line = line.split("|")
        food = Food(line[0], int(line[1]), bool(
            line[2] == "True"), int(line[3]))
        foods.append(food)
    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    for food in foods:
        name = food.name
        origin = str(food.origin)
        is_veg = str(food.is_vegetarian)
        calories = str(food.calories)

        w_food = (name + "|" + origin + "|" + is_veg + "|" + calories)

        file_variable.write(w_food + "\n")
    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    foods is unchanged.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """

    veggies = []
    for food in foods:
        is_veg = food.is_vegetarian
        if is_veg:
            veggies.append(food)

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    foods is unchanged.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    origins = []

    for food in foods:
        if food.origin == origin:
            origins.append(food)

    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """

    total = 0

    for food in foods:
        total += food.calories

    if len(foods) > 0:
        avg = total / len(foods)

    else:
        avg = 0

    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    total = 0
    count = 0

    for food in foods:
        if food.origin == origin:
            total += food.calories
            count += 1

    if count > 0:
        avg = total / count
    else:
        avg = 0

    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    foods.sort()

    print("""Food                                Origin       Vegetarian Calories
----------------------------------- ------------ ---------- --------""")

    for food in foods:
        print("{:<36}{:<13}{:>10}{:>9}".format(food.name, Food.ORIGIN[food.origin],
                                               str(food.is_vegetarian), food.calories))

    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))

    result = []

    if origin == -1:
        if max_cals == 0:
            for food in foods:
                if food.is_vegetarian == is_veg:
                    result.append(food)

        else:
            for food in foods:
                if max_cals >= food.calories and food.is_vegetarian == is_veg:
                    result.append(food)

    else:
        if max_cals == 0:
            for food in foods:
                if food.origin == origin and food.is_vegetarian == is_veg:
                    result.append(food)
        else:
            for food in foods:
                if food.origin == origin and max_cals >= food.calories and food.is_vegetarian == is_veg:
                    result.append(food)
    return result

def create_food_list(ilib):
    foodlist = []
    lunchlist = []
    ilib.PRINT("Type in 'yes' to begin.")
    decision = ilib.INPUT()
    while decision.lower() == "yes":
        ilib.PRINT("What did you eat for breakfast?")
        food = ilib.INPUT()
        foodlist.append(food)
        ilib.PRINT("Anything else? :(yes or no)")
        decision = ilib.INPUT()
    ilib.PRINT("You ate " + ' and '.join(foodlist)+' for breakfast. Do you want to make the lunch list?')
    answer = ilib.INPUT()
    while answer == "yes":
        ilib.PRINT("What did you eat for lunch?")
        lunch = ilib.INPUT()
        lunchlist.append(lunch)
        ilib.PRINT("Anything else? :(yes or no)")
        answer = ilib.INPUT()
    ilib.PRINT("You ate " + ' and '.join(lunchlist) + ' for lunch.')
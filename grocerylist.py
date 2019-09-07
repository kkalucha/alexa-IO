def makegrocerylist(ilib):
    grocerylist=[]
    decision = 'YES'
    while decision.upper() == 'YES':
        ilib.PRINT("Give me your item")
        item=ilib.INPUT()
        grocerylist.append(item)
        ilib.PRINT("Do you want to continue?:yes or no")
        decision=ilib.INPUT()
    #calljunkfoodcalculator
    ilib.PRINT("This is your grocery list:\n" + '\n'.join(grocerylist))
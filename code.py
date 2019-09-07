from grocerylist import *
from foodlist import *
from InterfaceLib import InterfaceLib

ilib = InterfaceLib()

ilib.PRINT("Type anything but no to start.")
x = ilib.INPUT()

while x != 'no':
    ilib.PRINT('Are you in the mood to talk?')
    x = ilib.INPUT()
    if x == 'no':
        break
    if x == 'yes':
        ilib.PRINT('Do you want to discuss your grocery list or the food you ate today? Type yes for the grocery list and no for the food.')
        x = ilib.INPUT()
        if x == 'yes':
            makegrocerylist(ilib)
            continue
        if x == 'no':
            create_food_list(ilib)
            continue
        elif x == '':
            noans()
            break
        else:
            idunno()
    elif x == '':
        noans()
    else:
        idunno()
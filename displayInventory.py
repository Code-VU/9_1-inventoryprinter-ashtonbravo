stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    stuff = {'rope':1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}
    for key in stuff:
        print(key, ':', stuff[key])
#displayInventory(stuff)
    
print('inventory: ')
displayInventory(stuff)
print('total number of items:', 62) 
from utils import helper


def search(item):
    # turn item into lower case so it can be found in helper.py dictionary
    item = item.lower()
    items = helper.battleItems
    found = False

    for x in items:

        #iterate through rarity (common, uncommon, rare, etc)
        for i in items[x]:

            #iterate through items inside of rarity
            if i == item:
                return items[x][i]
                    
    
    if not found:
        return None

def searchRarity(item):
    # turn item into lower case so it can be found in helper.py dictionary
    item = item.lower()
    items = helper.battleItems
    found = False

    for x in items:

        #iterate through rarity (common, uncommon, rare, etc)
        for i in items[x]:
            #iterate through items inside of rarity
            if i == item:
                return x
                    
    
    if not found:
        return None


def check_has_item_boolean(item, user):
    hasItem = False
    item = item.lower()
    for i in range(len(user["Items"])):
        for i in user["Items"][i]:
            if i == item:
                hasItem = True
                return hasItem
    if not hasItem:
        return False

def check_has_item_index(item, user):
    hasItem = False
    item = item.lower()
    for i in range(len(user["Items"])):
        for x in user["Items"][i]:
            if x == item:
                hasItem = True
                return i
    if not hasItem:
        return False

def check_equipped_boolean(item, user):
    equipped = False
    item = item.lower()
    for i in range((len(user["EquipedItems"]))):
        for i in user["EquipedItems"][i]:
            if i == item:
                equipped = True
                return equipped
    if not equipped:
        return False

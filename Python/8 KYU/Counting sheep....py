
def count_sheeps(sheep):
    amount = 0
    for s in sheep:
        if (s == True):
            amount += 1
    return amount

def count_sheeps(sheep):
    return sheep.count(True)
    pass
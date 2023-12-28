# Count-Long-and-short

def count_long_and_short(list2):
    length = {}
    length['long'] = 0
    length['short'] = 0
    for item in list2:
        if len(item) > 5:
            length['long'] += 1
        else:
            length['short'] += 1
    
    return length

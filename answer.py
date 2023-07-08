def friend(x):
    return [friend for friend in x if len(friend) == 4]

def friend(x):
    #Code
    names = []
    for name in x:
        if len(name) == 4:
            names.append(name)
    return names

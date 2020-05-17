def checkLuhn(purportedCC):
    
    # Drop the last digiit
    CC = purportedCC[:-1]
    card = []
    # Reverse the digits
    reversed(CC)
    # Multiple odd digits by 2 and Subtract 9 to numbers over 9:
    for i in range(0,len(CC)):
        if i % 2 == 0:
            number = int(CC[i]) * 2
            if number > 9:
                number -= 9
            card.append(number)
        else:
            card.append(int(CC[i]))
    total = 0
    for i in card:
        total += i

    if (total + int(purportedCC[-1])) % 10 == 0:
        return True
    else:
        return False


a = '4556737586899856'

if checkLuhn(a):
    print('True')
else:
    print('False')
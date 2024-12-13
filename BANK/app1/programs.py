import random

def ac():
    num="1234567890"
    return '64126' + (''.join(random.sample(num,6)))



def ot():
    num="1234567890"
    ad=""
    for i in range(4):
        ad+=random.choice(num)
    return ad




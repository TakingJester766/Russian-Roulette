from typing import Counter
import random

r1 = random.randint(1,101)
r2 = random.randint(1,101)
r3 = random.randint(1,101)
r4 = random.randint(1,101)
r5 = random.randint(1,101)


status = 'Alive'

def round_one():
    if (r1 <= 84):
        print('You survived the first round.')
    else:
        print('You died on the first round.')
        global status 
        status = 'Dead'

print()   
print('You take a deep breath and hope for the best...')    
round_one()

def round_two():
    if (r2 <= 80):
        print('You survived the second round.')
    else:
        print()
        print('You died in the second round.')
        global status
        status = 'Dead'
    

if status == 'Alive':
    print()
    print('You know your odds are being lowered with every round you take...')
    round_two()
else:
    print()
    print('You are still dead.')

def round_three():
    if (r3 <= 75):
        print('You survived the third round.')
    else:
        print('You died in the third round.')
        global status
        status = 'Dead'
    

if status == 'Alive':
    print()
    print('You sense the odds are getting worse for you.')
    round_three()
else:
    print()
    print('You are still dead.')


def round_four():
    if (r4 <= 66):
        print('You survived the fourth round.')
    else:
        print('You died in the fourth round.')
        global status
        status = 'Dead'


if status == 'Alive':
    print()
    print('You very well might soon die...')
    round_four()
else:
    print()
    print('You are still dead.')

def round_five():
    if (r5 <= 50):
        print('You survived the fifth round.')
    else:
        print('died in the fifth round.')
        global status
        status = 'Dead'


if status == 'Alive':
    print()
    print('This is it...You take a deep breath and:')
    round_five()
    print()
else:
    print()
    print('You are still dead.')
    print()
            
            

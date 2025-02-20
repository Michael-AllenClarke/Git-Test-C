letters = ['A', 'B', 'C', 'D']

for letter in letters:
    print(letter.lower())

numbers = ['1','2','3','4']

for number in numbers:
    print(number)

Clip = 30
import time

while Clip > 0:
    Clip -= 1
    if Clip < 30 and Clip > 1:
        print('Fa Fa Fa ... ' + str(Clip))
        time.sleep(1)
    if Clip == 0:
        print('Reloading...')
        time.sleep(3)
        Clip = 30 


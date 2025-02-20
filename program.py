letters = ['A', 'B', 'C', 'D']

for letter in letters:
    print(letter.lower())

numbers = ['1','2','3','45']

for number in numbers:
    print(number)

timer = 30
import time

while timer > 0:
    timer -= 1
    if timer < 30 and timer > 1:
        print('There is ' + str(timer) + " seconds left..." )
        time.sleep(1)
    if timer == 1:
        print('There is ' + str(timer) + " second left..." )
        time.sleep(1)
    if timer == 0:
        print('Resetting...')
        time.sleep(3)
        timer = 30 


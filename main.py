# Guess the number
from random import randint
print('You can choose between 3 difficulty levels!!!')
print('Press e for easy, m for medium and h for hard')
difficulty=input('Your difficulty level: ').lower().strip()

difficulty_levels={'e':100, 'm':500, 'h':1000}
target_number=randint(1,difficulty_levels[difficulty])
total_guesses=0
print('Your number is somewhere between 1 and',difficulty_levels[difficulty])
while True:
    guess=int(input('guess = '))
    if 1<=guess<=difficulty_levels[difficulty]:
        total_guesses+=1
        if guess==target_number:
            print('Congrats!!! You got it right.. your mamma will be proud of you :)')
            print('Total attempts =',total_guesses)
            break
        elif guess<target_number:
            print('Your guess was low. Try a higher number.')
        else:
            print('Your guess was high. Try a lower number.')
    else:
        print('Enter a valid input!!!!!')
        continue

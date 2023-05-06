import random
choices = ('rock', 'paper', 'scissors')
restart = True
playing = True
while True:
    lives = 5
    score = 0
    drew = 0
    computer_lives = 7
    print('Welcome to Rock, Paper, Scissors!')
    print(f'You start with {lives} lives')
    print('If you win you gain a point')
    print('If you lose you lose a life')
    print('If you draw the lives stay the same')
    print('------------------------------------------')
    print("MAKE SURE YOU DON'T USE CAPITALS")
    print('To see a list of rules type "rules"')
    print('------------------------------------------')
    print('At any point type "exit" to leave the game')
    print('------------------------------------------')
    print('The computer has lives as well')
    print('Can you beat the computer?')
    print('Good luck!')
    print('------------------------------------------')
    while True:
        rps = input('Rock, Paper, or Scissors?  ')
        computer_choice = random.choice(choices)
        # Rock if statements
        if rps == 'rock' and computer_choice == 'paper':
            print(f'The computer chose {computer_choice}')
            print('')
            print('You lose a life!')
            print('')
            print('')
            lives -= 1
        if rps == 'rock' and computer_choice == 'scissors':
            print(f'The computer chose {computer_choice}')
            print('')
            print('You gain a point!')
            print('')
            print('')
            computer_lives -= 1
            score += 1
        # Paper if statements
        if rps == 'paper' and computer_choice == 'rock':
            print(f'The computer chose {computer_choice}')
            print('')
            print('You gain a point!')
            print('')
            print('')
            computer_lives -= 1
            score += 1
        if rps == 'paper' and computer_choice == 'scissors':
            print(f'The computer chose {computer_choice}')
            print('')
            print('You lose a life!')
            print('')
            print('')
            lives -= 1
        # Scissors if statements
        if rps == 'scissors' and computer_choice == 'rock':
            print(f'The computer chose {computer_choice}')
            print('')
            print('You gain a point!')
            print('')
            print('')
            computer_lives -= 1
            score += 1
        if rps == 'scissors' and computer_choice == 'paper':
            print(f'The computer chose {computer_choice}')
            print('')
            print('You lose a life!')
            print('')
            print('')
            lives -= 1
        # Duplicates
        if rps == computer_choice:
            print(f'The computer chose {computer_choice}')
            print('')
            print('You drew')
            print('')
            print('')
            drew += 1
        # System
        if rps == 'rules':
            print('')
            print('******************************************')
            print('Rules')
            print('******************************************')
            print('-Rock beats Scissors')
            print('-Rock loses against Paper')
            print('-Paper beats Rock')
            print('-Paper loses against Scissors')
            print('-Scissors beats Paper')
            print('-Scissors loses against Rock')
            print('******************************************')
        if rps == 'display lives':
            print(lives)
        if rps == 'display score':
            print(score)
        if rps == 'display drew':
            print(drew)
        if lives == 0 or rps == 'test':
            print('Thanks for playing.')
            print('You have run out of lives')
            print(f'You got {score} points')
            print(f'You drew {drew} times')
            break
        if computer_lives == 0:
            print('Thanks for playing.')
            print('The computer lost all its lives. You win!')
            print(f'You got {score} points')
            print(f'You drew {drew} times')
            break
    play_again = input("Would you like to play again? Type no to exit, otherwise you're playing again :)")
    if play_again == 'no':
        break

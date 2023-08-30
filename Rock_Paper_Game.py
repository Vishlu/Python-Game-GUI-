from random import randint
    

game_data = ['Rock', 'Paper', 'Scissors']

computer = game_data[randint(0,2)]


start = True

while start:

    user = str(input('Rock, Paper, Scissors: '))

    if user == computer:
        print('computer choice:', computer)
        print('Game Draw!')

        
    elif user == 'Rock':
        if computer == 'paper':
            print('computer choice:', computer)
            print('You Lose, computer choice ', computer)
        
        else:
            print('computer choice:', computer)
            print('You Won, computer choice ', computer)


    elif user == 'Paper':
        if computer == 'Scissors':
            print('computer choice:', computer)
            print('You Lose, computer choice ', computer)
        
        else:
            print(computer)
            print('You Won, computer choice ', computer)


    elif user == 'Scissors':
        if computer =='Rock':
            print('computer choice:', computer)
            print('You Lose, computer choice ', computer)

        else:
            print(computer)
            print('You Won, computer choice ', computer)

    else:
        print('Your Spelling is Wrong.')
        
    
    
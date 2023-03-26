print('''Welcome to 3 in 1 Game
Press 1 to play Rock, Paper, Scissors
Press 2 to play Pakistan History Quiz
Press 3 to play Guess The Car Game
''')

select = int(input('Choose the game you want to play: '))
def quiz():
    print("Welcome to Pakistan History Quiz")
    answer = input('Are you ready to play the Pakistan History  Quiz ? (yes/no) : ')
    score = 0
    total_questions = 5

    if answer.lower() == 'yes':
        a = input('Question 1: In which year Pakistan gained Independence? : ')
        if a == '1947':
            score += 1
            print('Correct Answer')
        else:
            print('Wrong Answer ')

        b = input('Question 2: Independence day is Celebrated on Which date? : ')
        if b == '14 August'.lower() or b == '14 August'.upper():
            score += 1
            print('Correct Answer')
        else:
            print('Wrong Answer ')

        c = input('Question 3:Who was the Founder of Pakistan? : ')
        if c == 'Quaid-e-Azam'.lower() or b == 'Quaid-e-Azam'.upper():
            score += 1
            print('Correct Answer')
        else:
            print('Wrong Answer :(')

        d = input('Question 4: When was Pakistan resolution Passed ? : ')
        if d == '23 March 1940'.lower() or d == '23 March 1940'.upper():
            score += 1
            print('Correct Answer')
        else:
            print('Wrong Answer ')

        e = input('Question 5: Who is the Mother of Nation ? : ')
        if e == 'Fatima Jinnah'.lower() or e == 'Fatima Jinnah'.upper():
            score += 1
            print('Correct Answer')
        else:
            print('Wrong Answer ')
    if answer.lower == 'no':
        print('Bye!')
        
    print('Thank you for playing this Quiz Game, you attempted', score, "questions correctly!")
    mark = (score / total_questions) * 100
    print('Well Done ! You Obtained ', mark, '%', 'Marks')
    print('BYE , Have a Good Day')
    
    

def guess():
    import random
    answer = input('Are you ready to play Guess The Car Game ? (yes/no) :')
    if answer.lower() == 'yes':
        print("::::::::::::WELCOME TO GUESS THE CAR GAME::::::::::::")
        name = input("Your Name: ")
        print("Good Luck !", name)
        words = ["audi", "suzuki", "honda", "volkswagen", "bmw", "chevrolet", "mercedes", "ferrari", "porsche", "nissan", "tesla", "ford"]

        word = random.choice(words)
        print("guess the complete word")
        print('You have 5 lives to guess the correct car!')
        guess = ""
        guess_count = 0
        guess_limit = 5
        out_of_guesses = False
        while guess != word and not (out_of_guesses):
            if guess_count < guess_limit:
                guess = input("enter guess:")
                guess_count += 1
            else:
                out_of_guesses = True
        if out_of_guesses:
            print("Out Of Guesses,  YOU LOOSE!")
        else:
            print("YOU WIN!!!")
        print("the word is:", word)
        print("::::::THANK YOU FOR PLAYING GUESS THE CAR GAME::::::")
        print("WELL PLAYED, BYE!")

    if answer.lower() == 'no':
        print('GOODBYE!')


import random
# r means rock, p means paper, s means scissors
def game_rps(computer, you):
    def game2(computer, you):
        if computer == you:
            return None
        elif computer == 'r':
            if you == 'p' or you == 'P':
                return True
            elif you == 's' or you == 'S':
                return False

        elif computer == 's':
            if you == 'r' or you == 'R':
                return True
            elif you == 'p' or you == 'P':
                return False

        elif computer == 'p':
            if you == 's' or you == 'S':
                return True
            elif you == 'r' or you == 'R':
                return False

    print("Computer's turn: Rock(r), Paper(p), Scissors(s).")
    print('Computer has selected!')
    computer = random.choice(['r', 'p', 's'])

    you = input('Your turn: Rock(r), Paper(p), Scissors(s)? ')
    a = game2(computer, you)
    print(f'Computer chose {computer}')
    print(f'You chose {you}')
    if a == None:
      print('The game is a tie!')
    elif a == True:
      print('You Won!')
    else:
      print('You Lost!')


if select == 1:
    game_rps(computer="", you='')

if select == 2:
    quiz()

if select == 3:
    guess()

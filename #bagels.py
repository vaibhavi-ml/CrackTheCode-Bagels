#BAGELS
def playbagels():
    import time
    def selecting_number():
        import random
        digits=random.sample(range(0,9), 3)
        number=''.join(str(digit) for digit in digits)
        return number
    def check_guess(guessed_number):
        if len(guessed_number)==3 and guessed_number.isdigit() and len(set(guessed_number))==3:
            return guessed_number
        else:
            print("Please enter a three digit number having distinct digits")
            time.sleep(1)
            guessed_number=input(">")
            return guessed_number
    def get_clues(guessed_number, number):
        clues=[]
        for i in range(3):
            if guessed_number[i]==number[i]:
                clues.append("FERMI")
            elif guessed_number[i] in number:
                clues.append("PICO")
            elif guessed_number[i] not in number:
                clues.append("BAGELS")
        return clues
    max_guesses=10
    print(f'''Hey User
Welcome to the Bagels Game
Here you have to guess a three digit number.
If your digit is correct but at the wrong position... computer returns      PICO
If your digit is correct and at the right position...... computer returns     FERMI
If your digit is incorrect........................................................ computer returns     BAGELS
You will be getting {max_guesses} guesses.''')
    secret_number=selecting_number()
    
    guess_count=0
    while guess_count<max_guesses:
        time.sleep(1)
        print(f"Guess #{guess_count + 1}:")
        print("Enter a three digit number having distinct digits")
        guessed_number=input(">")
        guessed_number=check_guess(guessed_number)
        clues=get_clues(guessed_number, secret_number)
        print(','.join(clues))
        if guessed_number==secret_number:
            print("You got it!!!")
            break
        guess_count+=1
    else:
        print("Oops! You ran out of guesses. the number was", secret_number)
playbagels()

from random import randint

def main():
    print('Welcome to the number guessing game!')
    number = randint(1,10)
    while True:
        guess = input('Guess a number between one and ten: ')
        if int(guess) == number:
            print("That's right!")
            break
        else:
            print("That's not right. Sorry,guess again!")

if __name__ == '__main__':
    main()

import random

def get_user_guess():
    while True:
        try:
            return int(input("Please enter an int: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_guess(secret, guess):
    if guess == secret:
        print("Bingo! Secret number is: {secret}")
        return True
    elif abs(guess - secret) <= 5:
        print("Hot")
    else:
        print("Cold")
    return False

def main():
    secret_number = random.randint(1, 10)
    MAX_TRIES = 5
    tries = 0

    while tries < MAX_TRIES:
        guess = get_user_guess()
        if check_guess(secret_number, guess):
            break
        tries += 1

    if tries == MAX_TRIES:
        print(f"Sorry, you've used all your tries. The secret number was: {secret_number}")

if __name__ == "__main__":
    main()

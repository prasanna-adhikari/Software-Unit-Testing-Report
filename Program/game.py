"""Number Guessing Game"""
import random


def generate_random_number():
    """Generate a random four-digit number."""
    return random.sample(range(10), 4)


def get_user_guess():
    """Get user input for their guess."""
    error_msg = "Please enter a valid four-digit number or 'q' to quit."
    while True:
        try:
            guess = input("Enter your four-digit guess (or 'q' to quit): ")
            if guess.lower() == 'q':
                return None

            if len(guess) != 4 or not guess.isdigit():
                raise ValueError

            guess = [int(digit) for digit in guess]
            return guess
        except ValueError:
            print("Invalid input. ", error_msg)


def provide_hints(secret_number, guess):
    """Provide hints to the player about the accuracy of their guess."""
    hints = []
    used_positions = set()
    secret_digit_count = [secret_number.count(digit)
                          for digit in secret_number]
    for i in range(4):
        if guess[i] == secret_number[i]:
            hints.append("o")
            used_positions.add(i)
        elif guess[i] in secret_number:
            secret_index = secret_number.index(guess[i])
            if secret_digit_count[secret_index] == 1:
                hints.append("x")
            else:
                hints.append(" ")
        else:
            hints.append(" ")
    return hints


def main():
    """Run the Number Guessing Game."""
    print("Welcome to the Number Guessing Game!")
    play_again = True

    while play_again:
        secret_number = generate_random_number()
        attempts = 0

        while True:
            guess = get_user_guess()
            mapped_num = map(str, secret_number)
            if guess is None:
                print(f"The secret number was: {''.join(mapped_num)}")
                print(f"Number of attempts: {attempts}")
                break

            attempts += 1
            if guess == secret_number:
                congrats_msg = (
                    f"Congratulations! You've guessed the number "
                    f"{''.join(mapped_num)} in {attempts} attempts."
                )
                print(congrats_msg)
                break

            hints = provide_hints(secret_number, guess)
            print("Hints:", ' '.join(hints))

        play_again = input("Do you want to play again? (y/n): ").lower() == 'y'

    print("Thank you for playing!")


if __name__ == "__main__":
    main()

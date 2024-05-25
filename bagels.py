import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def get_secret_num():
    """Returns a string mad up of NUM_DIGITS unique random digits."""
    # numbers = ['0', '1'....]
    numbers = list('0123456789')
    random.shuffle(numbers)  # shuffle them into random order

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secret_retrieved_num = ''
    for i in range(NUM_DIGITS):
        secret_retrieved_num += str(numbers[i])
    return secret_retrieved_num


def get_clues(guess, secret_num):
    """ Returns a string with PICO, FERMI, BAGELS clues for a guess
    and secret number pair."""
    if guess == secret_num:
        return "You got it!"
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # a correct digit is in the first place.
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place.
            clues.append('PICO')
    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)


def main():
    print("""
    I am thinking of a {}- digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    when I say:  That means:
    PICO        One digit is correct but in the wrong position
    FERMI       One digit is correct and in the right position 
    BAGELS      No digit is correct.
    
    For example, if the secret number was 248 and your guess was 843,
    the clues would be Fermi Pico.""".format(NUM_DIGITS))

    while True:
        # stores the secret number that the player needs to guess
        secret_num = get_secret_num()
        print('"I have thought up a number.')
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            # keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(num_guesses))
                guess = input("> ")
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # the player is correct, break out of the loop
            if num_guesses > MAX_GUESSES:
                print("You have ran out of guesses.")
                print("The answer was {}.".format(secret_num))

        # Ask the player if they want to play again
        print("Do you want to play again? (y/n)")
        if not input("> ").lower().startswith('y'):
            break
    print("Thank you for playing!!!")


if __name__ == '__main__':
    main()

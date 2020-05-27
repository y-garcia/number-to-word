from vocabulary import Vocabulary
from util import is_number
from majorsystem import MajorSystem

if __name__ == "__main__":
    major_system = MajorSystem()
    vocab = Vocabulary()

    prompt = "Enter a number (press enter to exit): "
    number = input(prompt)

    while number != "":
        if is_number(number):
            pattern = major_system.build_pattern(number)
            words = vocab.search(pattern)
            print(f'Words for {number}: {words}\n')
        else:
            print("That wasn't a valid number.")
        number = input(prompt)

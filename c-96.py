# C96
# Functions
import random


def count_words_from_file():
    fname = input('Enter name of file: ')
    file = open(fname, "r")
    no_of_words = 0
    for line in file:
        words = line.split()
        no_of_words = no_of_words + len(words)
    print('There are ' + str(no_of_words) + ' words in ' + fname)


count_words_from_file()


def print_random_number(min, max):
    print(random.randint(min, max))


print_random_number(10, 20)

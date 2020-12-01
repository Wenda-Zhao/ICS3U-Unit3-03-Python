#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Nov 2020
# This program guessing random number


import random


def main():
    # this function guessing random number
    some_variable = random.randint(0, 9)   # a number between 0 and 9

    # input
    your_number = int(input("Enter your number (between 0 and 9): "))
    print("")

    # process
    if your_number == some_variable:
        # output
        print("You are correct!")
    else:
        print("You are wrong, the answer is {0}".format(some_variable))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Sep 2021
# This program calculates the sum of two integers given from the user


def main():
    # this function calculates sum of two integers

    # input
    integer1 = int(input("Enter the first number to add (integer): "))
    integer2 = int(input("Enter the second number to add (integer) :"))

    # process
    sum = integer1 + integer2

    # output
    print("")
    print("The sum of the two integers is {0}.".format(sum))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# Created by Marc Coffi
# Created in May 2022
# This program converts celsius to fahrenheit


def fahrenheit():
    user_input = input("Enter a temperature in Celsius: ")
    try:
        user_num = float(user_input)
        fahrenheit = (9 / 5) * user_num + 32
        print("{}℃ = {}℉".format(user_num, fahrenheit))
    except:
        print("Invalid Input. Please enter a proper Celsius value.")


def main():
    fahrenheit()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: December 4, 2023
# This program simulates a calculator


def calculator(num1, num2, sign):
    # use a match case to show what operation to use on num1 and num 2
    match sign:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "%":
            return num1 % num2


def main():
    # get num1, num2, and the sign
    print("This program simulates a calculator")
    number1_str = input("What is your first number?")
    number2_str = input("What is your second number?")
    sign_user = input("Enter a sign (ex. +)")
    try:
        # convert num1 to float
        number1_float = float(number1_str)

        try:
            # convert num2 to float
            number2_float = float(number2_str)

            # if the user enters a valid sign call the calculator function
            if (
                sign_user == "+"
                or sign_user == "-"
                or sign_user == "*"
                or sign_user == "/"
                or sign_user == "%"
            ):
                solution = calculator(number1_float, number2_float, sign_user)

                # display the solution
                print(
                    "{0} {1} {2} = {3}".format(
                        number1_float, sign_user, number2_float, solution
                    )
                )
            else:
                # otherwise, tell the to enter a valid sign
                print("Please enter a valid sign.")

        except:
            # if num2 cannot become a number, then tell the user to enter a number.
            print("{} is not a valid number.".format(number2_str))
    except:
        # if num1 cannot become a number, then tell the user to enter a number.
        print("{} is not a valid number.".format(number1_str))


if __name__ == "__main__":
    main()

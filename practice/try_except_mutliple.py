
# Add a while loop to iteratively ask the user for two numbers until they enter a valid input
while True:
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        print(num1 / num2)
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
    except ZeroDivisionError:
        print("Can't divide by zero.")
    else:
        print(f"No errors were raised, result is: {num1/num2}")
# try:

#     input_1 = input('Enter a number: ')
#     input_2 = input('Enter another number: ')
#     int_1 = int(input_1)
#     int_2 = int(input_2)
#     print(int_1 / int_2)

# # Add an exception for ValueError so when the user enters a string instead of a number, the program will not crash.
# except ValueError:
#     print("You must enter a number")

# # Add an exception for ZeroDivisionError so when the user enters 0 as the second number, the program will not crash.
# except ZeroDivisionError:
#     print("You cannot divide by zero")
# # Add an exception for KeyboardInterrupt so when the user presses Ctrl+C, the program will not crash.
# except KeyboardInterrupt:
#     print("You pressed Ctrl+C")

# else:
#     print(f"No errors were raised, result is: {int_1/int_2}")


# ask the user for width and
# loop until they enter a number that is greater than zero

def int_checker(question, low):

    error = f"Please enter an integer that is greater than or equal to {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is greater than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine goes here
for item in range(0, 2):
    integer = int_checker("Integer: ", 0)
    print (integer)

print()

for item in range(0, 2):
    width = int_checker("Width: ", 1)
    print (width)
print()

for item in range(0, 2):
    height = int_checker("Height: ", 1)
    print (height)
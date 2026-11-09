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

def image_calc():
    # get the image dimensions
    width = int_checker("Width: ", 1)
    height = int_checker("Height: ", 1)

    # calculate the number of pixels and multiply by 24 to ge the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # set up answer and return it
    answer = (f"Number of pixels: {width} x {height} = {num_pixels}. "
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")
    return answer


# main routine goes here
image_ans = image_calc()
print (image_ans)

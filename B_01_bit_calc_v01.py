# Generate headings, e.g. ----- Heading -----
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Display instructions
def instructions():
    statement_generator("Instructions", "-")

    print ('''
    Instructions: When asked for a file type, enter 
    - "xxx" to exit,
    - "integer", "int" for an integer file type
    - "text", "t", "txt" for a text file type
    - "image", "p", "picture", "img" for an image file type
    - "music" for a music file type
    ''')

# ask the user for width and loop until they enter a number that is greater than zero
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

# calculate how many bits are needed to represent an integer
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

# calculate how many bits to represent an integer
def integer_calc():
    # ask the user to enter an integer (greater than or equal to 0)
    integer = int_checker("Integer: ", 0)

    # convert the integer to binary and work out the number of bits needed
    raw_binary = bin(integer)

    # remove the leading '0b' from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    # set up answer and return it
    answer = f"{integer} in binary is {binary}. We need {num_bits} bits to represent it. "
    return answer

# calculate number of bits needed to represent text in ascii
def calc_text_bits():

    # get text from user
    response = input ("Enter some text: ")

    # calculate bits needed
    num_char = len(response)
    num_bits = num_char * 8

    # set up answer and return it
    answer = (f"{response} has {num_char} characters. "
              f"\nWe need {num_char} x 8 to represent it, "
              f"\nwhich is {num_bits} bits. ")
    return answer

# ask users for file type (integer / image / text / xxx)
def get_filetype():
    while True:
        response = input("File type: ").lower()

        # check for 'i' or the exist code 'xxx'
        if response == "xxx" or response == "i":
                return response

        # check if it is an integer
        elif response in ["integer", "int"]:
            return "integer"

        # check if it is text
        elif response in ["text", "t", "txt"]:
            return "text"

        # check if it is an image
        elif response in ["image", "p", "picture", "img"]:
            return "image"

        # check if it is music
        elif response == "music":
            return "music"

        else:
            print ("Please enter a valid file type")


# main routine goes here

# display the instructions if requested
want_instructions = input("Press <enter> to read the instructions or any key to continue ")

if want_instructions == "":
    instructions()

print("program continues")

while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break

    # if user chose 'i', ask if they want an image or an integer
    if file_type == "i":
        want_image = input ("Press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)

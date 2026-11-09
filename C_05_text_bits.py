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



# main routine goes here
text_ans = calc_text_bits()
print (text_ans)



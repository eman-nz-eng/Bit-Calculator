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
while True:
    file_type = get_filetype()

    # if user chose 'i', ask if they want an image or an integer
    if file_type == "i":
        want_image = input ("Press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"You chose {file_type}")

    if file_type == "xxx":
        break
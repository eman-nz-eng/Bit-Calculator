# Generate headings, e.g. ----- Heading -----

def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Display instructions
def instructions():
    statement_generator("Instructions", "-")

    print ('''
    Instructions go here
    - instruction 1
    - instruction 2
    - instruction 3    
    etc
    ''')

# main routine goes here

# display the instructions if requested
want_instructions = input("Press <enter> to read the instructions or any key to continue ")

if want_instructions == "":
    instructions()

print("program continues")

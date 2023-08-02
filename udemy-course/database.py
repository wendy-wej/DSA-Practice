
print("Welcome to Nweje's Tech Hub. This code has two code choices. Press 1 or 2 to select a choice \n\nTo generate the ASCII code from a given number, Press 1.\n\nTo generate a character from an ASCII value, Press 2 \n")

selection = input("Enter your selected number: ")
if selection == str(1):                        # Program to find the ASCII value from an input character.
    word = input("Enter any character of your choice: ")      # getting character from user.
    ascii_value = ord(word)                                   # Get the ASCII value of the character
    print("The ASCII value of '" + word + "' is: " + str(ascii_value)) # Print the ASCII value of the character

elif selection == str(2):       # Program to find the character from an input ASCII value
    ascii_num = int(input("Enter any ASCII value of your choice: "))  # getting ASCII value from user
    character = chr(ascii_num)         #getting the character corresponding to that ASCII value
    print("The ASCII value '"+ str(ascii_num) +"' corresponds to the character: '"+ chr(ascii_num) +"'.")

else:
    print("INVALID SELECTION CHOICE!, Try Again")


print("Welcome again to Nweje's Tech Hub. This code has two code choices. Press 1 or 2 to select a choice \n\nTo convert any number in any base to base 10, Press 1.\n\nTo convert any number in base 10 to its eqivalent in any base, Press 2 \n")
selection = input("Enter your selected number: ")
if selection == str(1):   
    selection = input("Enter your selected number: ")
    base = int(input("Enter the base of the number: ")) # Input the base of the number
    number = input("Enter the number: ")  # Input the number
    base10_equivalent = int(number, base) # Convert the number to its base 10 equivalent
    print("The base 10 equivalent of " + number + " is: " + str(base10_equivalent)) # Print the base 10 equivalent of the number

elif selection == str(2):
    # Accept the base to which you want to convert the number
    base = int(input("Enter the base to which you want to convert the number: "))
# Accept the number
    number = int(input("Enter the number: "))
    # Convert the number to its equivalent in the desired base
    if base == 2:
        base_equivalent = bin(number)
        print("The equivalent of " + str(number) + " in base " + str(base) + " is: " + base_equivalent)
    elif base == 8:
        base_equivalent = oct(number)
        print("The equivalent of " + str(number) + " in base " + str(base) + " is: " + base_equivalent)
    elif base == 16:
        base_equivalent = hex(number)
        print("The equivalent of " + str(number) + " in base " + str(base) + " is: " + base_equivalent)
    elif base > 16:
        print('Invalid base!!')
    else:
        def other_base(number, base):
            assert base>0 and int(base)==base, "Base must be a positive whole number number!"
            assert number>0 and int(number)==number, "Number must be a positive whole number!"

            carry = number//base
            rem = number%base

            if carry == 0:
                return str(rem)

            return other_base(carry, base) + str(rem)
        print(other_base(number, base))

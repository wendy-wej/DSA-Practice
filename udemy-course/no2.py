print("Welcome again to Nweje's Tech Hub. This code has two code choices. Press 1 or 2 to select a choice \n\nTo convert any number in any base to base 10, Press 1.\n\nTo convert any number in base 10 to its eqivalent in any base, Press 2 \n")
selection = input("Enter your selected number: ")
if selection == str(1):   
    selection = input("Enter the number you want to convert: ")
    base = int(input("Enter the base of the number: ")) # Input the base of the number
    number = input("Enter the number: ")  # Input the number
    base10_equivalent = int(number, base) # Convert the number to its base 10 equivalent
    print("The base 10 equivalent of " + number + " is: " + str(base10_equivalent)) # Print the base 10 equivalent of the number

elif selection == str(2):
    # Accept the base to which you want to convert the number
    base = int(input("Enter the base to which you want to convert the number: "))
# Accept the number
    number = int(input("Enter the number you want to convert: "))
    # Convert the number to its equivalent in the desired base
    if base >=1 and base <= 10:
        def other_base(number, base):
            assert base>0 and int(base)==base, "Base must be a positive whole number!"
            assert number>0 and int(number)==number, "Number must be a positive whole number!"

            carry = number//base
            rem = number%base

            if carry == 0:
                return str(rem)

            return other_base(carry, base) + str(rem)
        print("The equivalent of " + str(number) + " in base " + str(base) + " is: " + other_base(number, base))
    elif base == 16:
        base_equivalent = hex(number)
        print("The equivalent of " + str(number) + " in base " + str(base) + " is: " + base_equivalent)
    elif base > 16:
        print('Invalid base!!')
    else:
        print('Invalid base!!')
      
else:
    print("You selected the wrong value!")

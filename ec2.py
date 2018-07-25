'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
'''

while True:
    try:
        number = raw_input("Enter the number: ");
        a = int(number) % 2;
        if a :
            print "Odd number!";
        else:
            print "Even number!";
        break;
    except Exception as e:
        print "Enter Valid number!"

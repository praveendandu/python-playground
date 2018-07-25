'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

import re
import datetime

while True:
    try:
        name = raw_input("Enter your name: ");
        isValid = re.match('[A-Za-z\s]+\Z',name);
        if isValid:
            print(name);
            break;
        else:
            print "Yo! not a valid name! ";
            continue;
    except Exception as e:
        print "Something wrong .."

while True:
    try:
        age = raw_input("Enter your age: ");
        print int(age);
        break;
    except Exception as e:
        print "Yo! not a valid age! ";

num = datetime.datetime.now().year+100-int(age);
print "Hey! ",name,"! You will turn 100 in the year: "+str(num)

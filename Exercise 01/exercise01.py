''' Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
Add on to the previous program by asking the user for another number and printing out that
many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string \n is the same as pressing the ENTER button)
'''
print("Hello");
print("Please enter your name: ")
name = input();
print("Please enter your age: ")
age = input();
print("Please enter the number of times you want the expression to print: ");
numOfexpressions = int(input());

hun = (int(age) + 100);
name = str(name);
age = str(age);
hun = str(hun);

while(numOfexpressions > 0):
    print('Your name is ' + name + ' and your age is ' + age + ' and you will be ' + hun + ' in a hundred years.');
    numOfexpressions = numOfexpressions - 1;

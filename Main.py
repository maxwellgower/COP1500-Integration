# Max Gower
# COP 1500
# This program is simply a showcase of what we have learned in COP1500

print("")
print("Forewarning; ")
print("")
profInput1 = input("I have had to not only work from home, but my role in my company has switched from water treatment system sales to basically a 24/7 on-call emergency phone answering service. That doesn't sound like fun, does it? :( y/n ")
if (profInput1 == "y"):
    print("Actually yeah there is some merit in helping those in need :) ")
    print("Regardless, I have no complaints, you reinforced the idea that anything can be done if I apply myself 100% ")
elif (profInput1 == "n"):
    print("It certainly has challenged me more than before. And having to learn the second half of Discrete Mathmatics without a very helpful professor has its own challenges. ")
    print("That shit is hard. ")
    print("But no complaints, you reinforced the idea that anything can be done if I apply myself 100% ")
profInput2 = input("Anyways, bottom line is that there's mixes of snake case and camel case, and some variable naming that gets a little messy. Hope that's okay? y/n ")
if (profInput2 == "y"):
    print("Thank you for being generous, I know this won't fly when I develop projects for a company in the future so hopefully by then I'll iron out the flaws in my time management skills. ")
elif (profInput2 == "n"):
    print("Well I understand. Whatever path I take with this degree certainly will expect clean code and syntax. Better learn my lesson now while I can. ")
def main():
    name = input("Welcome to my program. What is your name? ")
    print("Hello", name+"." )
    age = input("How old are you? ")
    print("You are", age, "years old.")
    print("You are about to order fast food. Prepare your body. ")
    num_hamburgers = int(input("Enter the number of hamburgers: "))
    num_fries = int(input("Enter the number of fries: "))
    num_drinks = int(input("Enter the number of drinks: "))
    price_hamburger = float(2.00)
    price_fries = float(1.50)
    price_drinks = float(1.00)
    cost_hamburger = (num_hamburgers * price_hamburger)
    cost_fries = (num_fries * price_fries)
    cost_drinks = (num_drinks * price_drinks)
    total_cost = float(cost_hamburger + cost_fries + cost_drinks)
    print("Thank you for ordering, your total is: $" + format(total_cost, "0.2f"))
    math = input("Are you ready for math? ")
    if (math == "yes"):
        print("Good. Now for some numeric operators. ")
    else: print("Too bad.")
    answer =  6 ** 2 + 3 * 4 // 2
    print("6 ** 2 + 3 * 4 // 2 " ,answer)
    final = answer%4
    print(final)
    print("16 + 3 = " ,16 + 3)
    print("16 - 3 = " ,16 - 3)
    print("16 * 3 = " ,16 * 3)
    print("16 ** 3 = " ,16 ** 3)
    print("16 / 3 = " ,16 / 3)
    print("16 // 3 = " ,16 // 3)
    print("16 % 3 = " ,16 % 3)
    color = input("What is your favorite color? ")
    food = input("What is your favorite food? ")
    sport = input("What is your favorite sport? ")
    hobby = input("Do you have a hobby, and if so, what is it? ")
    car = input("What is your favorite car? ")
    job = input("What is your job title? ")
    location = input("What place have you always wanted to visit? ")
    idol = input("Who is someone you look up to? ")
    print("Your favorite color is:", color)
    print("Your favorite food is:", food)
    print("Your favorite sport is:", sport)
    print("Your hobby is:", hobby)
    print("Your favorite car is:", car)
    print("Your job title is:", job)
    print("A place you want to visit is:", location)
    print("A person you idolize is:", idol)
    num1 = int(input("Give me any whole number: "))
    num2 = int(input("Give me another whole number: "))
    if (num1 == num2):
        print("The numbers are equal! ")
    elif (num1 != num2):
        print("The numbers are not equal! ")
        while (num1 != num2):
            if (num1 > num2):
                print("The first number is greater! ")
            elif (num1 < num2):
                print("The second number is greater! ")
            elif (num1 >= num2):
                print("The first numbner is greater than or equal to the second! ")
            elif (num1 <= num2):
                print("The second number is greater than or equal to the first! ")
            break
main()
def getSmaller(num1, num2):
    if num1<num2:
        smaller = num1
    else:
        smaller = num2
    return smaller
def main2():
    userInput1 = int(input("Time for one more relational operator that also incorporates ELSE and RETURN, so I can meet the Sprint 2 requirements. (hopefully) Enter any integer: "))
    userInput2 = int(input("Enter a second integer: "))
    smallerNumber = getSmaller(userInput1, userInput2)
    print("The smaller of the two integers is", smallerNumber)
main2()
def addNumbers(num1, num2):
    print(num1, "+", num2, "=",num1+num2)
def subtractNumbers(num1,num2):
    print(num1, "-", num2, "=",num1-num2)
def main3():
    firstNumber = int(input("Enter a number between 1 and 10: "))
    secondNumber = int(input("Enter another number between 1 and 10: "))
    operator = input("Enter a '+' to add or a '-' to subtract: ")
    if operator == '+':
        addNumbers(firstNumber, secondNumber)
    elif operator == '-':
        subtractNumbers(firstNumber,secondNumber)
    else:
        print("Invalid operator!")
main3()
def main4():
    program = input("Do you think this program ran correctly? y/n ")
    if(program == "y"):
        print("You think the program ran correctly. Thank you. ")
        print("")
        print("I'll put in a good word to Rate My Professors. ")
        print("Because you deserve it, no brown-nosing here. ")
    elif(program == "n"):
        print("Thank you for any feedback you provide. I will make sure to correct any mistakes. ")
        print("")
        print("I'll put in a good word to Rate My Professors. ")
        print("Because you deserve it, no brown-nosing here. ")
main4()


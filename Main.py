"""Integration Project for COP1500"""
__author__ = "Max Gower"

print()
print("This program requires interaction to run all functions. \n")
print("Astrix prompts require any key press to continue. \n")
input("* Prompts will appear like this. Continue? * \n")
name = input("What is your name? \n")
print(name + ", welcome. I'm sure you already know my name. \n")
dive_in = input("Take a seat. Are you ready to free yourself? (y/n) \n")
if dive_in == 'y':
    print("Excellent. Let us begin. \n")
else:
    print("Very well. When your mind changes, we'll find you. \n")


def walk_away():
    input("* You walk away, choosing to remain in the dark * \n")
    x = 0
    while x <= 10:
        print(".")
        x += 1
    try_again = input("Return? (y/n) \n")
    if try_again == 'y':
        print()
        intro()
    else:
        print("The end.")


def pill_color():
    pill_info = input("* choose red or blue pill * \n")
    if pill_info == 'blue':
        print("You take the blue pill and the story ends. \n")
        print("You wake in your bed, ")
        print("and believe whatever you want to believe. \n")
    elif pill_info == 'red':
        print("You take the red pill and you stay in Wonderland, \n")
        print("and I show you how deep the rabbit-hole goes. \n")
    pill_choice = input("* Choose a pill * \n")
    if pill_choice == 'blue':
        walk_away()
    if pill_choice == 'red':
        print("Wow this was complicated. \n")
        input("* Let's run my main function now. * \n")
        main()


def find_truth():
    input("* places in your right hand a red pill * \n")
    input("* places in your left hand a blue pill * \n")
    print("This is your last chance. After this there is no going back. \n")
    stay_blind = input("* Leave and stay blind to the truth? * (y/n) \n")
    if stay_blind == 'y':
        print()
        print("Very well. When your mind changes, we'll find you. \n")
        walk_away()
    while stay_blind != 'y':
        if stay_blind == 'n':
            print()
            print("Good. Pick either pill to learn more. \n")
            pill_color()
        else:
            print()
            print("You seem undecided", name + ". \n")
            print("Very well. When your mind changes, we'll find you. \n")
            walk_away()
        break


def intro():
    open_hand = input(name + ", hold out your hands. (y/n) \n")
    if open_hand == 'y':
        print()
        find_truth()
    while open_hand != 'y':
        if open_hand == 'n':
            print()
            print("Very well. When your mind changes, we'll find you. \n")
            walk_away()
        break


def compare_values(num1, num2):
    """This function compares the value of two integers using operators.
    == - checks for equality
    != - checks for inequality
    > - determines if 1st value is larger than 2nd
    >= - determines if 1st value is larger than or equal to 2nd
    < - determines if 1st value is smaller than 2nd
    <= - determines if 1st value is smaller than or equal to 2nd
    return result - returns string based on operator result"""
    if num1 == num2:
        result = "The numbers are equal! "
    elif num1 != num2:
        result = "The numbers are not equal! "
        while num1 != num2:
            if num1 > num2:
                result = "The first number is greater! "
            elif num1 < num2:
                result = "The second number is greater! "
            elif num1 >= num2:
                result = "The number 1 is greater than or equal to the second! "
            elif num1 <= num2:
                result = "The number 2 is greater than or equal to the first! "
            break
    return result


def integer_comparison():
    """This function runs user input through compare_values and prints result.
    input_1 - 1st user input integer
    input_2 - 2nd user input integer
    answer - variable representing result of compare_values function."""
    input_1 = int(input("Give me any whole number: "))
    input_2 = int(input("Give me another whole number: "))
    answer = compare_values(input_1, input_2)
    print(answer)


def get_smaller(num1, num2):
    """This function finds the smallest of two integers.
    < - determines if 1st value is smaller than 2nd
    return smaller - returns string based on operator result"""
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    return smaller


def smallest_integer():
    """This function runs user input through get_smaller and prints result.
    user_input_1 - 1st user input integer
    user_input_2 - 2nd user input integer
    smaller_number - variable representing result of get_smaller function."""
    user_input_1 = int(input("Enter any integer: "))
    user_input_2 = int(input("Enter a second integer: "))
    smaller_number = get_smaller(user_input_1, user_input_2)
    print("The smaller of the two integers is", smaller_number)


def add_numbers(num1, num2):
    """This function adds two integers and prints the result."""
    print(num1, "+", num2, "=", num1 + num2)


def subtract_numbers(num1, num2):
    """This function subtracts two integers and prints the result."""
    print(num1, "-", num2, "=", num1 - num2)


def integer_operations():
    """This function asks user input to add/subtract two numbers.
    first_number - 1st user integer between 1 and 10
    second_number - 2nd user integer between 1 and 10
    operator - user input determines operand to be used"""
    first_number = int(input("Enter a number between 1 and 10: "))
    second_number = int(input("Enter another number between 1 and 10: "))
    operator = input("Enter a '+' to add or a '-' to subtract: ")
    if operator == '+':
        add_numbers(first_number, second_number)
    elif operator == '-':
        subtract_numbers(first_number, second_number)
    else:
        print("Invalid operator!")


def program_evaluation():
    """This function asks the user their opinion of this program.
    program - y/n/other input to determine printed response"""
    program = input("Do you think this program ran correctly? y/n ")
    if program == "y":
        print("You think the program ran correctly. Thank you. ")
        print("")
        print("I'll put in a good word to Rate My Professors. ")
        print("Because you deserve it, no brown-nosing here. ")
    elif program == "n":
        print("Thank you. I will make sure to correct any mistakes. ")
        print("")
        print("I'll put in a good word to Rate My Professors. ")
        print("Because you deserve it, no brown-nosing here. ")


def main():
    """This is my main function, a showcase of COP1500 topics,
    and as each line runs a different topic is showcased."""
    print("")
    print("Forewarning; \n")
    print("Before the virus I enjoyed a rewarding sales position.")
    print("Working from home I'm now fielding our customer complaints.")
    print("Pissed off customers get to yell at me for 8 hours a day.")
    prof_input_1 = input("Does this job sound fun at all? :( y/n ")
    if prof_input_1 == "y":
        print("It's not. But I guess I'm lucky to still have a job. ")
        print("It is what it is, a paycheck is a paycheck. ")
    elif prof_input_1 == "n":
        print("It's definitely taught me better time management. ")
        print("Now I have 2 online classes but this one isn't an issue")
        print("But having to learn discrete math online really sucks! ")
        print("It's whatever, I'll just work even harder.")
    prof_input_2 = input("Will my project exceed your expectations? y/n ")
    if prof_input_2 == "y":
        print("Thank you for being optimistic, I tried my best. ")
    elif prof_input_2 == "n":
        print("Challenge accepted. Let's get ready to rumble. ")
    name = input("Welcome to The Matrix. What is your name again? ")
    print(name + ", that's right I forgot.")
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
    print("Thank you, your total is: $" + format(total_cost, "0.2f"))
    math = input("Are you ready for math? ")
    if math == "yes":
        print("Good. Now for some numeric operators. ")
    else:
        print("Too bad.")
    answer = 6 ** 2 + 3 * 4 // 2
    print("6 ** 2 + 3 * 4 // 2 ", answer)
    final = answer % 4
    print(final)
    print("16 + 3 = ", 16 + 3)
    print("16 - 3 = ", 16 - 3)
    print("16 * 3 = ", 16 * 3)
    print("16 ** 3 = ", 16 ** 3)
    print("16 / 3 = ", 16 / 3)
    print("16 // 3 = ", 16 // 3)
    print("16 % 3 = ", 16 % 3)
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
    integer_comparison()
    smallest_integer()
    integer_operations()
    program_evaluation()


intro()
main()

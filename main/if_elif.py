"""
Assignment name: Basic if-elif Statement Assignment
Program: if_elif.py
Author: Colby Boell
Last date modified: 01/26/2022

The purpose is to prompt the user to sign up for programmer's toolkit monthly subscription box.
They must select level (platinum, gold, silver, bronze, free trial). Each month is something
different (t-shirts, stickers, figurines, even programming books). The program then outputs
the price of the selected subscription.
"""
# sequential
# print statement to describe info to user
print("Welcome to the Programmer's Toolkit subscription service!\nEach month is something different, t-shirts, stickers, figurines, even programming books!")
# variable for user input/ also prints out prompt for user input
user_choice = input('Which subscription would you like?\nEnter One of the Following:\nP for Platinum\nG for Gold\nS for Silver\nB for Bronze\nF for Free Trial\nChoice:')

"""
if else statement to decide what price to return to the user
if statement capitalizes input so user can put lower or uppercase input and still get proper info on subscription
if user input is P or Platinum then if statement prints out premium price
conditional
"""
if user_choice.capitalize() == 'P':
    print('Platinum subscription is $60.00 a month')
# else if the user input is G or Gold then it prints out the gold price
elif user_choice.capitalize() == 'G':
    print('Gold subscription is $50.00 a month')
# else if the user input is S then it prints out the silver price
elif user_choice.capitalize() == 'S':
    print('Silver subscription is $40.00 a month')
# else if the user input is B then it prints out the bronze price
elif user_choice.capitalize() == 'B':
    print('Bronze subscription is $30.00 a month')
# else if the user input is F then it prints out the free trial information
elif user_choice.capitalize() == 'F':
    print('Free trial subscription is free for one month (upgrade at any time)\nThen you can upgrade to a different subscription or cancel!')
# else statement if they enter in invalid choice /default to free trial
else:
    print('That choice was not valid! We will go ahead and give you a free trail!')
    print('Free trial subscription is free for one month (upgrade at any time)\nThen you can upgrade to a different subscription or cancel!')
# sequential
print('Thank you for subscribing!!!!')

"""
input and output result tests (tested each input)
inputs: p     output: Platinum subscription is $60.00 a month
        P             Thank you for subscribing!!!!
inputs: g     output: Gold subscription is $50.00 a month
        G             Thank you for subscribing!!!!
inputs: s     output: Silver subscription is $40.00 a month
        S            Thank you for subscribing!!!!
inputs: b     output: Bronze subscription is $30.00 a month
        B             Thank you for subscribing!!!!
inputs: f     output: Free trial subscription is free for one month(upgrade at any time)
        F             Then you can upgrade to a different subscription or cancel!
                      Thank you for subscribing!!!!
inputs: w     output: That choice was not valid! We will go ahead and give you a free trail!
        1             Free trial subscription is free for one month (upgrade at any time)
        C             Then you can upgrade to a different subscription or cancel!
                      Thank you for subscribing!!!!
"""

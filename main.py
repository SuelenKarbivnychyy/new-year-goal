import random


def give_tips():
    """Give a tip for the user to spend less money"""

    tips = ["Make a list of your fixed spends", "Take 30% of your earning and save it on a investing account", "Take $50 dolares per week to spend on fun activities", "Make a emergency reserve for the pets if you have one", "Make sure you dont have subscriptions plan that you are not using", "When you feel like you want to buy something, think tree times if you really need it"]    

    input("Press any key to receive a tip to achieve your goal: ")

    print(random.choice(tips))

give_tips()    





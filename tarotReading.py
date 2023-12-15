'''
Name: tarotReading.py

Purpose: Runs the tarot card reading session for the user

Last Updated: 14 Dec 2023
'''
import LCGTarot
import datetime

if __name__ == "__main__":
    # source: https://biddytarot.com/tarot-card-meanings/major-arcana/ 
    major_arcana = {
        "The Fool" : "Beginnings, innocence, spontaneity, a free spirit",
        "The Fool - Reversed" : "Holding back, recklessness, risk-taking"
    }
    major_arcana2 = [("The Fool","Beginnings, innocence, spontaneity, a free spirit"), ("The Fool - Reversed", "Holding back, recklessness, risk-taking")]

    print("\nWelcome to your tarot reading! We will only be using the 22 major arcana cards.\n")
    print("What would you like to do?\n")
    print("1: My Past, Present, and Future\n2: Answer My Question\n")
    selection = False
    # checks input and does corresponding action
    while(selection is False):
        input_reading = input("Type in the number that correspondes to what you want to do:")
        if (int(input_reading) == 1):
            past_present_future()
        elif (int(input_reading) == 2):
            question()
        else:
            print("Please enter a valid number.\n")
     


    def past_present_future():
        pass

    def question():
        pass
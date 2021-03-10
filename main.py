# This is a sample Python script.
# Ever wanted to make a DnD Encounter with no continuity or care for
# the world you are in?
#
# Gives me a good excuse to use a DnD API so there is that too
# https://www.dnd5eapi.co/
#

import requests


class Party:


    def __init__(self, goodEvil, lawChaos):
        self.goodEvil = goodEvil
        self.lawChaos = lawChaos
        self.currentCR = 1


class Path:

    start = True

    while (start):

        alignment1 = {0: "Neutral", 1: "Good", 2: "Evil"}
        alignment2 = {0: "Neutral", 1: "Lawful", 2: "Chaotic"}

        print("Lets get going with whether the part is Neutral (0), Good (1) or Evil (2)")
        print("Please enter a number for whether your party is a boringly neutral (0), bunch of goody two shoes (1), or devilishly evil (2): ")
        goodEvil = int(input("Well?.... "))

        while (goodEvil not in [0,1,2]):
            goodEvil = int(input("Come on now, you're only wasting your own time. Enter a valid... number. "))


        print("Incredible! Such talent and efficiency. Now then, is your party Neutral (0), Lawful (1), or Chaotic (2)")
        print("Please enter a number for whether your party is is lying to themselves about being neutral (0), upstanding lawful citizens (1), or honest (2): ")
        lawChaos = int(input("Well?.... "))

        while (lawChaos not in [0,1,2]):
            lawChaos = int(input("Pretty please enter a valid number <3 "))

        theParty = Party(alignment1[goodEvil], alignment2[lawChaos])

        check = input("So your party is %s %s? Y or N", theParty.goodEvil, theParty.lawChaos)

        while (check.upper() != "Y" or check.upper() != "N"):
            if (check.upper() == "Y"):
                start = False
            elif (check.upper() != "N"):
                check = input("Please enter a valid character, Y for 'Yes' or N for 'No' ")


    print("You did it! Lets get going now. Adventure. Awaits!")





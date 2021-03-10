# This is a sample Python script.
# Ever wanted to make a DnD Encounter with no continuity or care for
# the world you are in?
#
# Gives me a good excuse to use a DnD API so there is that too
# https://www.dnd5eapi.co/
#

import Party
import requests
import random

class AlignmentDecision:

    def __init__(self, theParty):
        self.alignment1 = theParty.lawChaos
        self.alignment2 = theParty.goodEvil
        self.currentCR = theParty.currentCR
        self.alignment = theParty.alignment

        self.listOfCreatureAlignments = []

    def selectAlignment(self):
        code = requests.get("https://www.dnd5eapi.co/api/alignments")

        if (code.status_code == 404):
            print("Error")
        else:
            results = code.json()["results"]

            for alignment in results:
                rand = random.randint(0, 10)

                split = alignment["name"].split()

                if (split[0] == "Neutral"):
                    split.append("Neutral")

                print(alignment["name"] + " " + str(rand))

                if (alignment["name"] == self.alignment.lower()):
                    if (rand > 4):
                        self.listOfCreatureAlignments.append(alignment["name"])
                elif (split[0] == self.alignment1.lower()):
                    if (rand > 7):
                        self.listOfCreatureAlignments.append(alignment["name"])
                elif (split[1] == self.alignment2.lower()):
                    if (rand > 7):
                        self.listOfCreatureAlignments.append(alignment["name"])
                else:
                    if (rand > 8):
                        self.listOfCreatureAlignments.append(alignment["name"])

        return self.listOfCreatureAlignments
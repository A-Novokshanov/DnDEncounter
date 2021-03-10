#
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

        self.listOfCreatureAlignments = {}

    def selectAlignment(self):
        code = requests.get("https://www.dnd5eapi.co/api/alignments")

        if (code.status_code == 404):
            print("Error")
        else:
            results = code.json()["results"]

            while (len(self.listOfCreatureAlignments) == 0):
                for alignment in results:
                    rand = random.randint(0, 20)

                    split = alignment["name"].split()

                    if (alignment["name"] == "Neutral"):
                        split.append("Neutral")

                    if ((str(split[0]) + " " + str([1])).lower() == self.alignment.lower()):
                        if (rand > 5):
                            self.listOfCreatureAlignments[alignment["name"]] = []
                    elif (split[0].lower() == self.alignment1.lower()):
                        if (rand > 12):
                            self.listOfCreatureAlignments[alignment["name"]] = []
                    elif (split[1].lower() == self.alignment2.lower()):
                        if (rand > 12):
                            self.listOfCreatureAlignments[alignment["name"]] = []
                    else:
                        if (rand > 16):
                            self.listOfCreatureAlignments[alignment["name"]] = []


        return self.listOfCreatureAlignments
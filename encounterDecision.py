#
# Ever wanted to make a DnD Encounter with no continuity or care for
# the world you are in?
#
# Gives me a good excuse to use a DnD API so there is that too
# https://www.dnd5eapi.co/api/
#

import random

class encounterDecision:

    def __init__(self, crList, alignmentList, beastiary):
        self.encounterCR = crList
        self.potentialMonsters = alignmentList
        self.alignmentList = alignmentList
        self.beastiary = beastiary
        self.monsterList = {}

    def getPotentialMonsters(self):

        for monster in self.beastiary:

            for alignment in self.alignmentList:

                trueAlignment = alignment

                if (alignment == "Neutral"):
                    trueAlignment = "unaligned"

                if (self.beastiary[monster]["alignment"].lower() == trueAlignment.lower()
                        or (self.beastiary[monster]["alignment"].lower() == alignment.lower())):
                    self.potentialMonsters[alignment].append(monster)
        return self.potentialMonsters

    def getEncounter(self):
        encounterNum = 1
        potentialList = self.getPotentialMonsters()

        for encounter in self.encounterCR:
            self.monsterList[encounter + " " + str(encounterNum)] = None
            goalCR = self.encounterCR[encounter]

            #currentECR = 0

            while ((goalCR != 0) and (len(potentialList[encounter]) > 0)):
                checkMonster = potentialList[encounter][random.randint(0, len(self.potentialMonsters[encounter]) - 1)]

                if (self.beastiary[checkMonster]["challenge_rating"] <= goalCR):

                    goalCR -= self.beastiary[checkMonster]["challenge_rating"]
                    if (self.monsterList[encounter + " " + str(encounterNum)] == None):
                        self.monsterList[encounter + " " + str(encounterNum)] = self.beastiary[checkMonster]["name"]
                    else:
                        self.monsterList[encounter + " " + str(encounterNum)] = self.monsterList[encounter + " "
                                                                                + str(encounterNum)] + ", " + \
                                                                                self.beastiary[checkMonster]["name"]

                #for mob in self.monsterList[encounter + " " + str(encounterNum)].split(", "):
                #    currentECR += self.beastiary[mob]


                #for (mob in self.monsterList):
                #currentECR +=

                potentialList[encounter].remove(checkMonster)
            encounterNum += 1

        return self.monsterList
#
# Ever wanted to make a DnD Encounter with no continuity or care for
# the world you are in?
#
# Gives me a good excuse to use a DnD API so there is that too
# https://www.dnd5eapi.co/api/
#

import random

class crDecision:

    def __init__(self, theParty, alignmentList):
        self.currentCR = theParty.currentCR + 1
        self.monsterAlignments = alignmentList

        self.crList = {}

    def selectCR(self):

        numList = []

        for num in range(self.currentCR - 1):
            if (self.currentCR < 4):
                numList.append(random.randint(1, self.currentCR - 1))
            else:
                numList.append(random.randint(1, self.currentCR))

        return (max(numList))

    def createCRDict(self):

        for alignment in self.monsterAlignments:
            self.crList[alignment] = crDecision.selectCR(self)

        return self.crList
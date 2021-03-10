#
# Ever wanted to make a DnD Encounter with no continuity or care for
# the world you are in?
#
# Gives me a good excuse to use a DnD API so there is that too
# https://www.dnd5eapi.co/api/
#

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

                if (alignment == "Neutral"):
                    alignment = (alignment + " Neutral")

                if (self.beastiary[monster]["alignment"].lower() == alignment.lower()):
                    self.potentialMonsters[alignment].append(monster)

        return self.potentialMonsters

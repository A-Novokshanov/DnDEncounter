# This is a sample Python script.
# Ever wanted to make a DnD Encounter with no continuity or care for
# the world you are in?
#
# Gives me a good excuse to use a DnD API so there is that too
# https://www.dnd5eapi.co/
#

class Party:

    def __init__(self, goodEvil, lawChaos):
        self.goodEvil = goodEvil
        self.lawChaos = lawChaos
        self.currentCR = 1
        self.alignment = lawChaos + goodEvil


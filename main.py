#
# Ever wanted to make a DnD Encounter with no continuity or care for
# the world you are in?
#
# Gives me a good excuse to use a DnD API so there is that too
# https://www.dnd5eapi.co/api/
#

import GameStart
import AlignmentDecision
import crDecision
import encounterDecision
import Beastiary
import Party
import requests
import random

class main:

    beastiary = Beastiary.Beastiary().getBeastiary()

    start = GameStart.GameStart()

    theHeroes = start.setup()

    alDec = AlignmentDecision.AlignmentDecision(theHeroes).selectAlignment()

    crDec = crDecision.crDecision(theHeroes, alDec).createCRDict()

    encounter = encounterDecision.encounterDecision(crDec, alDec, beastiary).getPotentialMonsters()

    print(encounter)

    #print(alDec)
    #print(crDec)

    #print()
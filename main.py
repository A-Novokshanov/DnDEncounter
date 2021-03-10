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
import Party
import requests
import random

class main:

    start = GameStart.GameStart()

    theHeroes = start.setup()

    alDec = AlignmentDecision.AlignmentDecision(theHeroes).selectAlignment()

    crDec = crDecision.crDecision(theHeroes, alDec).createCRDict()

    print(crDec)

    #print(alDec)
    #print(crDec)

    #print()
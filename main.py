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

class main:

    # creates the bestiary to make encounter building faster
    beastiary = Beastiary.Beastiary().getBeastiary()

    # has the user create their party (pretty much just alignment)
    start = GameStart.GameStart()

    # creates a party with relevant alignment
    theHeroes = start.setup()

    # used to create a random selection of alignments weighted towards party's alignment
    alDec = AlignmentDecision.AlignmentDecision(theHeroes).selectAlignment()

    # determines the 'total CR' that a particular encounter will have
    crDec = crDecision.crDecision(theHeroes, alDec).createCRDict()

    # chooses the creates for each encounter
    encounter = encounterDecision.encounterDecision(crDec, alDec, beastiary).getEncounter()

    print(str(theHeroes.currentCR) + " : " + str(encounter))

    theHeroes.currentCR = theHeroes.currentCR + 1


    while (theHeroes.currentCR < 50):
        alDec = AlignmentDecision.AlignmentDecision(theHeroes).selectAlignment()

        crDec = crDecision.crDecision(theHeroes, alDec).createCRDict()

        encounter = encounterDecision.encounterDecision(crDec, alDec, beastiary).getEncounter()

        print(str(theHeroes.currentCR) + " : " + str(encounter))

        theHeroes.currentCR = theHeroes.currentCR + 1

    #print(alDec)
    #print(crDec)

    #print()
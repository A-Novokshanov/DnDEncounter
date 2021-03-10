#
# Ever wanted to make a DnD Encounter with no continuity or care for
# the world you are in?
#
# Gives me a good excuse to use a DnD API so there is that too
# https://www.dnd5eapi.co/api/
#

import requests
import Party
import AlignmentDecision
import random

class Beastiary:

    def __init__(self):
        self.monsterDict = {}


    def getBeastiary(self):

        code = requests.get("https://www.dnd5eapi.co/api/monsters")

        if (code.status_code == 404):
            print("Error")
        else:
            total = code.json()["count"]
            current = 1
            results = code.json()["results"]

        for monster in results:

            if ((current / total) > 1.5):

                return self.monsterDict

            code2 = requests.get("https://www.dnd5eapi.co" + monster["url"])
            if (code.status_code == 404):
                print("Error")
                return
            else:
                specificMonster = code2.json()

            self.monsterDict[specificMonster["name"]] = specificMonster



            print(str(round((current / total) * 100, 2)) + "% done")
            current += 1

        return self.monsterDict

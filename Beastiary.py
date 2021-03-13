#
# Ever wanted to make a DnD Encounter with no continuity or care for
# the world you are in?
#
# Gives me a good excuse to use a DnD API so there is that too
# https://www.dnd5eapi.co/api/
#

import requests
import BeastiaryDatabase

import Party
import AlignmentDecision
import random

class Beastiary:

    def __init__(self):
        self.monsterDict = {}

    def decideUpdate(self):
        toReturn = "x"
        while((toReturn.lower() != "y") and (toReturn.lower() != "n")):
            toReturn = input("Recreate database? Y (for Yes) or N (for No) ")
            if ((toReturn.lower() != "y") and (toReturn.lower() != "n")):
                print("Invalid input")
            elif ((toReturn.lower() == "y")):
                return True
            elif ((toReturn.lower() == "n")):
                return False

    def getBeastiary(self):
        restore = self.decideUpdate()
        if (restore):
            return self.rebuildBeastiary()


    def rebuildBeastiary(self):

        code = requests.get("https://www.dnd5eapi.co/api/monsters")

        if (code.status_code == 404):
            print("Error")

        else:
            total = code.json()["count"]
            current = 1
            results = code.json()["results"]

        conn = BeastiaryDatabase.BeastiaryDatabase.create_connection(self, "BeastiaryDatapath.db")

        BeastiaryDatabase.BeastiaryDatabase.createBeastiaryDatabase(self, conn)

        for monster in results:

            if ((current / total) > 0.15):
                conn.close()

                return self.monsterDict

            code2 = requests.get("https://www.dnd5eapi.co" + monster["url"])
            if (code.status_code == 404):
                print("Error")
                return
            else:
                specificMonster = code2.json()

            self.monsterDict[specificMonster["name"]] = specificMonster

            BeastiaryDatabase.BeastiaryDatabase.addToDatabase(self, conn, self.monsterDict[specificMonster["name"]]["name"],
                                                              self.monsterDict[specificMonster["name"]]["alignment"],
                                                              self.monsterDict[specificMonster["name"]]["challenge_rating"])



            print(str(round((current / total) * 100, 2)) + "% done")
            current += 1

        return self.monsterDict

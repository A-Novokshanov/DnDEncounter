#
# Ever wanted to make a DnD Encounter with no continuity or care for
# the world you are in?
#
# Gives me a good excuse to use a DnD API so there is that too
# https://www.dnd5eapi.co/api/
#

import sqlite3
from sqlite3 import Error

class BeastiaryDatabase:

    def create_connection(self, path):
        connection = None

        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    def createBeastiaryDatabase(self, conn):

        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS BEASTIARY")
        sql = '''CREATE TABLE beastiary(
           ID CHAR(20),
           NAME CHAR(20),
           ALIGNMENT CHAR(20),
           CHALLENGE_RATING INT
        )'''
        cursor.execute(sql)
        print("Table has been rebuilt")
        conn.commit()

    def addToDatabase(self, conn, id, name, alignment, challengeRating):
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO beastiary VALUES (?, ?, ?, ?)""", (id, name, alignment, challengeRating))
        conn.commit()
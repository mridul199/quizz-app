import mysql.connector

class DBconnect:
    def __init__(self):
        try:
            self._conn=mysql.connector.connect(host= "127.0.0.1",user="root",password="",database="quizadda")
            self._mycursor = self._conn.cursor()
        except:

            print("Could Not Connect To Database")
            exit()

    def enter_user(self, name, email):
        self._mycursor.execute("SELECT * FROM participants WHERE NAME LIKE '{}' AND  email LIKE '{}'".format(name, email))
        data=self._mycursor.fetchall()
        if len(data) == 0:
            try:
                self._mycursor.execute(
                    "INSERT INTO participants(id,name,email)VALUES(NULL,'{}','{}')".format(name, email))
                self._conn.commit()

                return 1
            except:

                return 0
        else:
            return 1

    def score_entry(self, score, email):
        try:
            self._mycursor.execute("UPDATE participants SET score = {} WHERE email LIKE '{}'".format(score, email))
            self._conn.commit()

            return 1
        except:

            return 0




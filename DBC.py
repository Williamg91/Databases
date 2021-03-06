import mysql.connector as db

class Database:

    def __init__(self,user,passwd):
        self.user=user
        self.passwd = passwd
        connection = self.createConnection()
        global cursor
        cursor = connection.cursor()
    def createConnection(self):
        user = self.user
        passwd = self.passwd
        try:
            global connection
            connection = db.connect(
                host="localhost",
                user=user,
                passwd=passwd,
                database=user
            )
            print("ok")
            global cursor
            cursor = connection.cursor()
        except:
            print("Fejl i forbindelse")
        return connection
    def getConnection(self):

        return connection
    def createTable(self):

        cursor.execute("CREATE TABLE IF NOT EXISTS person2("
                       "id int(100) auto_increment primary key,"
                       "fornavn varchar(255),"
                       "efternavn varchar(255),"
                       "adresse varchar(500),"
                       "mail varchar(50),"
                       "password varchar(100)"
                       ")" #til tabellen
                       )#til funktionskaldet for execute

        print("Tabel oprettet")
        pass
    def createUser(self,*values):

        sql = "insert into person2(fornavn,efternavn,adresse,mail,password) values(%s,%s,%s,%s,%s)"

        cursor.execute(sql,values)
        connection.commit()
        print(cursor.rowcount,"værdier indsat:")
        pass

    def findUser(self,navn):
        user = []
        navn = "'" + navn + "'"
        sql = "select * from person2 where mail =" + navn +";"
        #vælg * fra tabel hvor kolonne = indtastet værdi
        print("Søger efter" +navn)
        cursor.execute(sql)
        #Her får vi en rækk eresultater tilbage.
        results = cursor.fetchall()
        for row in results:
            print(" ID:"+str(row[0]))
            print(" Fornavn:" + str(row[1]))
            print(" Efternavn:" + str(row[2]))
            print(" Adresse:" + str(row[3]))
            print(" Mail:" + str(row[4]))
            user.append(str(row))

        return user







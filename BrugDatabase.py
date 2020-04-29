
import mysql.connector as db
from DBC import Database
forb = Database("eksport00","hestehest")

forbindelse = forb.createConnection()

forb.createTable()

#createuser = forb.createUser("William","Geismar","export.eduhost.dk","wilge@dtu.dk","Coronafnis")
user = forb.findUser("wilge")
print(user)
#print(lokaltobjekt.user,lokaltobjekt.database,lokaltobjekt.cursor())

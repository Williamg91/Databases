import mysql.connector as db
try:
    conn = db.connect(
        host = "80.198.171.108",
        user ="eksport00",
        passwd = "hestehest"

    )
    print(conn.server_host,conn.user)
except:
    print("Fuck")


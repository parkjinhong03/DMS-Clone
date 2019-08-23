import pymysql


def connect():
    con = pymysql.connect(host="localhost", user="root", password="jinhong", db="DMS_DB", charset="utf8")
    cur = con.cursor()

    return con, cur
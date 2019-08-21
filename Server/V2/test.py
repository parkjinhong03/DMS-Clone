import pymysql

con = pymysql.connect(host="localhost", user="root", password="jinhong", db="test_db", charset="utf8")

cur = con.cursor()

sql = "create table test_table(" \
      "title varchar(100)," \
      "content text," \
      "primary key (title))"

try:
    cur.execute(sql)
except:
    print("이미 존재하는 테이블")

con.commit()

con.close()
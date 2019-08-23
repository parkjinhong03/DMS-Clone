import pymysql

def music_exist(con, cur, id):
    sql = f'select EXISTS (select * from music where user_id="{id}") as success'

    cur.execute(sql)
    con.commit()

    if cur.fetchone()[0] == 1:
        return True
    else:
        return False

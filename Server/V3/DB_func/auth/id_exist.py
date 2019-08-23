import pymysql


def id_exist(con, cur, id):
    sql = f'select EXISTS (select * from userlog where user_id="{id}") as success'

    cur.execute(sql)
    con.commit()

    if cur.fetchone()[0] == 1:
        return True

    return False

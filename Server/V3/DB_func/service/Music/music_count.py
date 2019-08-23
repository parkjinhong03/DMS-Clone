import pymysql

def music_count(con, cur, date):
    sql = f'SELECT COUNT(*) as count FROM music where date="{date}";'

    cur.execute(sql)
    return cur.fetchone()[0]

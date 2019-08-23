'''
기상 음악 신청 모듈
'''

from Server.V2.DB_func.service.Music.music_count import music_count
from Server.V2.DB_func.service.Music.music_exist import music_exist
from Server.V2.api.cookie_decorator import login_required
from Server.V2.DB_func.connect import connect
from flask import request


@login_required
def music_apply():
    '''
    :parameter: date(Mon, Tue, Wed, Thu, Fri), title, artist
    :return: status code
    403 - 로그인 상태가 아님
    411 - 해당 사용자가 한 주에 이미 기상 음악을 신청함
    412 - 당일 날에 이미 5개의 기상 음악이 신청됨
    400 - date의 VALUE에 정해진 값으로 들어오지 않음 (client 입력 오류)
    200 - 기상 음악 신청 성공
    '''

    con, cur = connect()

    sql = "CREATE TABLE Music (" \
          "     id BIGINT(20) unsigned NOT NULL AUTO_INCREMENT," \
          "     user_id TEXT NOT NULL," \
          "     date TEXT NOT NULL," \
          "     title TEXT NOT NULL," \
          "     artist TEXT NOT NULL," \
          "     PRIMARY KEY (id)" \
          ") DEFAULT CHARSET=utf8 COLLATE utf8_general_ci;"

    try:
        cur.execute(sql)
    except:
        pass

    date_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

    data = request.json

    date = data['date']
    title = data['title']
    artist = data['artist']
    my_name = request.cookies.get('user')

    # 413 예외처리
    if date not in date_list:
        return 'date의 VALUE으로 정해진 문구를 넣어 주세요.(Mon, Tue, Wed, Thu, Fri)', 400

    # 412 예외처리
    if  music_count(con, cur, date) >= 5:
        return f"음악 신청이 만료되었습니다.", 412

    # 411 예외처리
    if music_exist(con, cur, my_name) == True:
        return '이미 음악신청을 하셨습니다.', 411

    # 200 처리
    sql = f'INSERT INTO music (user_id, date, title, artist) VALUES("{my_name}", "{date}", "{title}", "{artist}")'

    cur.execute(sql)
    con.commit()

    con.close()

    return '기상 음악 신청 완료!', 200
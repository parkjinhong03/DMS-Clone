'''
로그인 모듈
'''

from Server.V2.DB_func.connect import connect
from Server.V2.DB_func.auth.id_exist import id_exist
from flask import request, make_response

def login():
    '''
    :parameter: id, pw
    :return: status code
    200 - 로그인 성공
    403 - 이미 로그인이 되어 있음
    410 - 아이디 입력 오류
    411 - 비밀번호 입력 오류
    '''
    data = request.json

    id = data['id']
    pw = data['pw']

    con, cur = connect()

    if 'user' in request.cookies:
        return '이미 로그인이 되어 있습니다.', 403

    if id_exist(con, cur, id) == False:
        return '일치하지 않는 아이디입니다.', 410

    sql = f'SELECT user_id, user_pw FROM UserLog WHERE user_id = "{id}"'

    cur.execute(sql)
    log_data = cur.fetchone()
    con.close()

    if pw == log_data[1]:
        resp = make_response("로그인 성공")
        resp.set_cookie('user', id)

        return resp, 200

    elif pw != log_data[1]:
        return '일치하지 않는 비밀번호 입니다.', 411
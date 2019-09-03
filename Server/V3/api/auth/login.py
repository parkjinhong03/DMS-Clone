'''
로그인 모듈
'''

from Server.V2.DB_func.connect import connect
from Server.V2.DB_func.auth.id_exist import id_exist
from flask import request, make_response
from flask_restful import reqparse
from flask_jwt_extended import create_access_token


def login():
    '''
    :parameter: id, pw
    :return: status code
    200 - 로그인 성공
    403 - 이미 로그인이 되어 있음
    410 - 아이디 입력 오류
    411 - 비밀번호 입력 오류
    '''
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=str)
    parser.add_argument('pw', type=str)
    args = parser.parse_args()

    _id = args['id']
    _pw = args['pw']

    con, cur = connect()


    if id_exist(con, cur, _id) == False:
        return {"message": "아이디가 이미 존재합니다.", "code": 410}, 410

    sql = f'SELECT user_id, user_pw FROM UserLog WHERE user_id = "{_id}"'

    cur.execute(sql)
    log_data = cur.fetchone()
    con.close()

    if _pw == log_data[1]:
        access_token = create_access_token(identity=_id)
        return {"access_token": access_token, "code": 200}, 200

    elif _pw != log_data[1]:
        return {"message": "일치하지 않는 비밀번호", "code": 411}, 411
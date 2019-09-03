'''
비밀번호 변경 모듈
'''

from Server.V2.DB_func.connect import connect
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import reqparse


@jwt_required
def pw_edit():
    '''
    :parameter: pw, pw_check
    :return: status code
    200 - 비밀번호 변경 완료
    410 - 로그인 상태 아님
    411 - 비밀번호와 비밀번호 확인 값이 다름
    '''

    parser = reqparse.RequestParser()
    parser.add_argument('pw', type=str)
    parser.add_argument('pw_check', type=str)
    args = parser.parse_args()

    _pw = args['pw']
    _pwCheck = args['pw_check']

    if _pw != _pwCheck:
        return '비밀번호와 비밀번호 확인이 서로 같지 않습니다.', 411

    user_id = get_jwt_identity()

    con, cur = connect()

    sql = f'UPDATE UserLog SET user_pw = "{_pw}" WHERE user_id = "{user_id}"'
    cur.execute(sql)

    con.commit()
    con.close()

    return '비밀번호 변경 완료!', 200
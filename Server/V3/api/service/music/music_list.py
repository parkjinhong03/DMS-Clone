'''
기상 음악 신청 조회 모듈
'''

from Server.V2.DB_func.connect import connect
from Server.V2.api.cookie_decorator import login_required
from flask import jsonify, request
from flask_restful import reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required
def music_list():
    '''
    :parameter: X
    :return: status code
    200 - 조회(데이터 반환) 성공
    403 - 로그인 상태 아님
    '''

    con, cur = connect()

    date_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    return_dict = {}

    my_user = get_jwt_identity()

    for date in date_list:
        date_dict = {}

        sql = f'SELECT user_id, artist, title FROM music WHERE date="{date}"'

        cur.execute(sql)
        music_data = list(cur.fetchall())

        for i in music_data:
            user_dict = {}
            user_dict['artist'] = i[1]
            user_dict['title'] = i[2]

            date_dict[i[0]] = user_dict

        return_dict[date] = date_dict

    con.close()

    return return_dict, 200

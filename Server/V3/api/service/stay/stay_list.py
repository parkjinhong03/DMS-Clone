'''
전체 잔류 신청 조회 모듈
'''

from Server.V2.DB_func.connect import connect
from flask import Flask, request, make_response, jsonify
from flask_jwt_extended import jwt_required


@jwt_required
def stay_list():
    '''
    :parameter: X
    :return:
    403 - 로그인 상태 아님
    200 - 전체 잔류 신청 조회 성공 및 반환
    '''

    count = 1
    return_dict = {}
    user_list=[]
    stay_list = {'1': '금요귀가',
                 '2': '토요귀가',
                 '3': '토요귀사',
                 '4': '잔류'}

    con, cur = connect()

    sql = f'SELECT user_id FROM stay;'
    cur.execute(sql)

    for i in cur.fetchall():
        user_list.append(i[0])

    for i in user_list:
        user_dict = {}
        sql = f'SELECT stay FROM stay WHERE user_id = "{i}"'
        cur.execute(sql)

        user_dict['id'] = i
        user_dict['stay'] = stay_list[cur.fetchone()[0]]

        return_dict[str(count)] = user_dict
        count += 1

    return return_dict, 200
'''
내 잔류 신청 조회 모듈
'''

from Server.V2.DB_func.connect import connect
from Server.V2.DB_func.service.Stay.stay_exist import stay_exist
from Server.V2.api.cookie_decorator import login_required
from flask import request, jsonify


@login_required
def stay_list_my():
    '''
    :parameter: X
    :return: status code
    403 - 로그인 상태 아님
    410 - 아직 잔류 신청을 안함
    200 - 내 잔류 신청 조회 성공 및 반환
    '''

    stay_list = {'1': '금요귀가',
                 '2': '토요귀가',
                 '3': '토요귀사',
                 '4': '잔류'}
    dict = {}
    user = request.cookies.get('user')

    con, cur = connect()

    if stay_exist(con, cur, user) == False:
        return "아직 잔류 신청을 하지 않았네요", 410

    sql = f'SELECT stay FROM stay WHERE user_id="{user}"'
    cur.execute(sql)

    dict['stay'] = stay_list[cur.fetchone()[0]]

    return jsonify(dict)
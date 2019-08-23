'''
잔류 신청 모듈
'''

from Server.V2.DB_func.service.Stay.stay_exist import stay_exist
from Server.V2.DB_func.connect import connect
from Server.V2.api.cookie_decorator import login_required
from flask import Flask, request, make_response
import os
import json

@login_required
def stay_apply():
    '''
    :parameter: stay(금요귀가, 토요귀가, 토요귀사, 잔류)
    :return: status code
    403 - 로그인 상태 아님
    400 - stay의 VALUE에 정해진 값으로 들어오지 않음 (client 입력 오류)
    410 - 이미 잔류 신청을 함
    200 - 잔류 신청 완료
    '''

    con, cur = connect()

    user = request.cookies.get('user')
    stay = request.json['stay']
    stay_list = {'금요귀가': '1',
                 '토요귀가': '2',
                 '토요귀사': '3',
                 '잔류': '4'}

    if stay not in ['금요귀가', '토요귀가', '토요귀사', '잔류']:
        return 'stay의 VALUE 값으로 정해진 문구를 넣어 주세요.(금요귀가, 토요귀가, 토요귀사, 잔류)', 400

    if stay_exist(con, cur, user) == True:
        return '이미 잔류 신청을 하셨네요!', 410

    sql = "CREATE TABLE Stay (" \
          "     id BIGINT(20) unsigned NOT NULL AUTO_INCREMENT," \
          "     user_id TEXT NOT NULL," \
          "     stay TEXT NOT NULL," \
          "     PRIMARY KEY (id)" \
          ") DEFAULT CHARSET=utf8 COLLATE utf8_general_ci;"

    try:
        cur.execute(sql)
    except:
        pass

    sql = f'INSERT INTO stay (user_id, stay) VALUES("{user}", "{stay_list[stay]}")'
    cur.execute(sql)

    con.close()

    return '잔류 신청 완료!', 200
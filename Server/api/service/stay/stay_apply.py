'''
잔류 신청 모듈
'''

from flask import Flask, request, make_response
import os
import json

def stay_apply():
    '''
    :parameter: stay(금요귀가, 토요귀가, 토요귀사, 잔류)
    :return: status code
    410 - 로그인 상태 아님
    411 - stay의 VALUE에 정해진 값으로 들어오지 않음 (client 입력 오류)
    200 - 잔류 신청 완료
    '''

    if 'user' not in request.cookies:
        return '로그인을 먼저 해주세요.', 410

    user = request.cookies.get('user')
    stay = request.form['stay']
    stay_list = ['금요귀가', '토요귀가', '토요귀사', '잔류']

    if stay not in stay_list:
        return 'stay의 VALUE 값으로 정해진 문구를 넣어 주세요.(금요귀가, 토요귀가, 토요귀사, 잔류)', 411

    with open('data/Stay/' + user, 'w') as f:
        f.write(stay)

    return '잔류 신청 완료!', 200
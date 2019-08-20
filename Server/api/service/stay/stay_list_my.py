'''
내 잔류 신청 조회 모듈
'''

from flask import Flask, request, make_response
import os
import json


def stay_list_my():
    '''
    :parameter: X
    :return: status code
    410 - 로그인 상태 아님
    411 - 잔류 신청을 아직 안함
    200 - 내 잔류 신청 조회 성공 및 반환
    '''

    if 'user' not in request.cookies:
        return '로그인을 먼저 해주세요', 410

    dict = {}
    user = request.cookies.get('user')

    try:
        with open('data/Stay/'+user) as f:
            data = f.readline()

        dict['my_stay'] = data
        return json.dumps(dict), 200

    except FileNotFoundError:
        return '아직 잔류 신청을 하지 않았네요!', 411
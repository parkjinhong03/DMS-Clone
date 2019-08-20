'''
내 잔류 신청 조회 모듈
'''

from flask import Flask, request, make_response, jsonify
import os
import json


def stay_list_my():
    '''
    :parameter: X
    :return: status code
    403 - 로그인 상태 아님
    200 - 내 잔류 신청 조회 성공 및 반환
    '''

    if 'user' not in request.cookies:
        return '로그인을 먼저 해주세요', 403

    dict = {}
    user = request.cookies.get('user')

    try:
        with open('V1/data/Stay/'+user) as f:
            data = f.readline()

        dict['my_stay'] = data
        return jsonify(dict), 200

    except FileNotFoundError:
        return '아직 잔류 신청을 하지 않았네요!', 200
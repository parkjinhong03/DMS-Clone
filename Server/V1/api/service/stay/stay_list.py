'''
전체 잔류 신청 조회 모듈
'''

from flask import Flask, request, make_response, jsonify
import os
import json

def stay_list():
    '''
    :parameter: X
    :return:
    403 - 로그인 상태 아님
    200 - 전체 잔류 신청 조회 성공 및 반환
    '''

    if 'user' not in request.cookies:
        return '로그인을 먼저 해주세요', 403

    return_dict = {}
    for data in os.listdir('V1/data/Stay'):
        with open('V1/data/Stay/'+data, 'r') as f:
            return_dict[data] = f.readline()

    return jsonify(return_dict), 200
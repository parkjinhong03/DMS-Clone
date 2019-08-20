'''
기상 음악 신청 조회 모듈
'''

from flask import Flask, request, make_response, jsonify
import os
import json

def music_list():
    '''
    :parameter: X
    :return: status code
    200 - 조회(데이터 반환) 성공
    403 - 로그인 상태 아님
    '''

    if 'user' not in request.cookies:
        return '로그인을 먼저 해주세요.', 403

    date_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    return_dict = {}

    for i in date_list:
        date_dict = {}

        for j in os.listdir('V1/data/Music/'+i):
            with open('V1/data/Music/'+i+'/'+j, 'r') as f:
                user_dict = {}
                data = json.loads(f.readline())
                user_dict['title'] = data['title']
                user_dict['artist'] = data['artist']
                date_dict[j] = user_dict

        return_dict[i] = date_dict

    return jsonify(return_dict), 200

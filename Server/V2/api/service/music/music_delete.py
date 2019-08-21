'''
기상 음악 취소 모듈
'''

from flask import Flask, request, make_response
import os

def music_delete():
    '''
    :parameter: X
    :return: status code
    403 로그인 상태 아님
    200 기상 음악 신청 취소 완료
    '''

    if 'user' not in request.cookies:
        return '로그인을 먼저 해주세요.', 403
    my_name = request.cookies.get('user')

    date_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

    count = 0
    for i in date_list:
        if os.path.exists('V1/data/Music/'+i+'/'+my_name):
            os.remove('V1/data/Music/'+i+'/'+my_name)
            count += 1
            return '기상 음악 취소 완료!', 200

    if count == 0:
        return '전에 신청해준 기상 음악이 없습니다.', 200
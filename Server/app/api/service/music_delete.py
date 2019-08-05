'''
기상 음악 취소 모듈
'''

from flask import Flask, request, make_response
import os

def music_delete():
    '''
    :parameter: X
    :return: status code
    410 로그인 상태 아님
    411 기상 음악 신청 X
    200 기상 음악 신청 취소 완료
    '''

    if 'user' not in request.cookies:
        return 'login first', 410
    my_name = request.cookies.get('user')

    date_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

    count = 0
    for i in date_list:
        if os.path.exists('data/Music/'+i+'/'+my_name):
            os.remove('data/Music/'+i+'/'+my_name)
            count += 1
            return 'music delete complete', 200

    if count == 0:
        return 'You have never applied music.', 411

    os.remove('data/Music')
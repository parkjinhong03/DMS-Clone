'''
기상 음악 신청 모듈
'''

from flask import Flask, request, make_response
import os
import json

def music_apply():
    '''
    :parameter: date(Mon, Tue, Wed, Thu, Fri), title, artist
    :return: status code
    410 - 로그인 상태가 아님
    411 - 해당 사용자가 한 주에 이미 기상 음악을 신청함
    412 - 당일 날에 이미 5개의 기상 음악이 신청됨
    413 - date의 VALUE에 정해진 값으로 들어오지 않음 (client 입력 오류)
    200 - 기상 음악 신청 성공
    '''

    date_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

    # 410 예외 처리
    if 'user' not in request.cookies:
        return 'login first', 410

    data = request.form

    date = data['date']
    title = data['title']
    artist = data['artist']
    my_name = request.cookies.get('user')

    # 413 예외처리
    if date not in date_list:
        return 'Please give the setted value of the date.(Mon, Tue, Wed, Thu, Fri)', 413

    # 411 예외처리
    for i in date_list:
        if os.path.exists('data/Music/'+i+'/'+my_name):
            return 'you already apply music', 411

    # 412 예외처리
    count = 0
    for _ in os.listdir('data/Music/'+date):
        count += 1
    if count == 5:
        return 'Your application for the day has already been closed.', 412

    # 200 처리
    with open('data/Music/'+date+'/'+my_name, 'w') as f:
        music_dict = {}
        music_dict["title"] = title
        music_dict["artist"] = artist
        f.write(json.dumps(music_dict))

    return 'apply music complete', 200
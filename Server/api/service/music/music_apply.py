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
    403 - 로그인 상태가 아님
    411 - 해당 사용자가 한 주에 이미 기상 음악을 신청함
    412 - 당일 날에 이미 5개의 기상 음악이 신청됨
    400 - date의 VALUE에 정해진 값으로 들어오지 않음 (client 입력 오류)
    200 - 기상 음악 신청 성공
    '''

    date_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

    # 410 예외 처리
    if 'user' not in request.cookies:
        return '로그인을 먼저 해주세요.', 403

    data = request.form

    date = data['date']
    title = data['title']
    artist = data['artist']
    my_name = request.cookies.get('user')

    # 413 예외처리
    if date not in date_list:
        return 'date의 VALUE으로 정해진 문구를 넣어 주세요.(Mon, Tue, Wed, Thu, Fri)', 400

    # 411 예외처리
    for i in date_list:
        if os.path.exists('data/Music/'+i+'/'+my_name):
            return '이미 기상 음악 신청을 하셨네요!', 411

    # 412 예외처리
    count = 0
    for _ in os.listdir('data/Music/'+date):
        count += 1
    if count == 5:
        return f'아쉽게도 {data}은 기상 음악 신청이 마감됬어요ㅜㅜ', 412

    # 200 처리
    with open('data/Music/'+date+'/'+my_name, 'w') as f:
        music_dict = {}
        music_dict["title"] = title
        music_dict["artist"] = artist
        f.write(json.dumps(music_dict))

    return '기상 음악 신청 완료!', 200
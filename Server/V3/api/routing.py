from flask_restful import Resource, reqparse
from Server.V3.api.auth import login, pw_edit, signup
from Server.V3.api.service.music import music_apply, music_delete, music_list
from Server.V3.api.service.stay import stay_list, stay_list_my, stay_apply


class user(Resource):
    '''
    유저 관리 class
    '''
    def post(self):
        '''
        login: 로그인 POST method
        signup: 회원가입 POST Method
        '''
        reqp = reqparse.RequestParser()
        reqp.add_argument('func', type=str)
        args = reqp.parse_args()

        if args['func'] == 'login':
            return login.login()

        elif args['func'] == 'signup':
            return signup.signup()

    def put(self):
        return pw_edit.pw_edit()


class music(Resource):
    def get(self):
        return music_list.music_list()

    def post(self):
        return music_apply.music_apply()

    def delete(self):
        return music_delete.music_delete()


class stay(Resource):
    def get(self):
        return stay_list.stay_list()

    def post(self):
        return stay_apply.stay_apply()


class my_stay(Resource):
    def get(self):
        return stay_list_my.stay_list_my()
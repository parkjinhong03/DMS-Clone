from flask import Flask

app = Flask(__name__)

from Server.api.auth.signup import signup
from Server.api.auth.login import login
from Server.api.auth.logout import logout
from Server.api.auth.pw_edit import pw_edit
from Server.api.service.music.music_apply import music_apply
from Server.api.service.music.music_delete import music_delete
from Server.api.service.music.music_list import music_list
from Server.api.service.stay.stay_apply import stay_apply
from Server.api.service.stay.stay_list_my import stay_list_my
from Server.api.service.stay.stay_list import stay_list

app.add_url_rule('/auth/signup',  'signup', signup, methods=['POST'])
app.add_url_rule('/auth/login', 'login', login, methods=['POST'])
app.add_url_rule('/auth/logout', 'logout', logout, methods=['POST'])
app.add_url_rule('/auth/pw_edit', 'pw_edit', pw_edit, methods=['POST'])

app.add_url_rule('/service/music', 'music_apply', music_apply, methods=['POST'])
app.add_url_rule('/service/music', 'music_delete', music_delete, methods=['DELETE'])
app.add_url_rule('/service/music', 'music_list', music_list, methods=['GET'])

app.add_url_rule('/service/stay', 'stay_apply', stay_apply, methods=['POST'])
app.add_url_rule('/service/my-stay', 'stay_list_my', stay_list_my, methods=['GET'])
app.add_url_rule('/service/stay', 'stay_list', stay_list, methods=['GET'])

if __name__ == '__main__':
    app.run(host= '10.156.147.138', port= 5000, debug= True)
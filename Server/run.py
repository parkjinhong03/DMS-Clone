from flask import Flask

app = Flask(__name__)

from Server.app.api.auth.signup import signup
from Server.app.api.auth.login import login
from Server.app.api.auth.logout import logout
from Server.app.api.auth.pw_edit import pw_edit
from Server.app.api.service.music.music_apply import music_apply
from Server.app.api.service.music.music_delete import music_delete
from Server.app.api.service.music.music_list import music_list
from Server.app.api.service.stay.stay_apply import stay_apply
from Server.app.api.service.stay.stay_list_my import stay_list_my
from Server.app.api.service.stay.stay_list import stay_list

app.add_url_rule('/auth/signup',  'signup', signup, methods=['POST'])
app.add_url_rule('/auth/login', 'login', login, methods=['POST'])
app.add_url_rule('/auth/logout', 'logout', logout, methods=['POST'])
app.add_url_rule('/auth/pw_edit', 'pw_edit', pw_edit, methods=['POST'])
app.add_url_rule('/service/music/apply', 'music_apply', music_apply, methods=['POST'])
app.add_url_rule('/service/music/delete', 'music_delete', music_delete, methods=['POST'])
app.add_url_rule('/service/music/list', 'music_list', music_list, methods=['POST'])
app.add_url_rule('/service/stay/apply', 'stay_apply', stay_apply, methods=['POST'])
app.add_url_rule('/service/stay/list_my', 'stay_list_my', stay_list_my, methods=['POST'])
app.add_url_rule('/service/stay/list', 'stay_list', stay_list, methods=['POST'])

if __name__ == '__main__':
    app.run(host= '172.30.1.59', port= 5000, debug= True)
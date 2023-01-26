from flask import Flask, render_template,request
from user_agents import parse
from werkzeug.user_agent import UserAgent

app = Flask(__name__)


@app.route("/")
@app.route("/test")
def test():
    return render_template('test.html')

def redirect(button_id='Install'):
    ua = request.headers.get('User_Agent')
    ua_os = ua.os.family 
    if (ua.is_mobile == True):
        match ua_os:
            case "iOS":
               button_id.href = "https://apps.apple.com/us/app/menutium/id1170811326"
            case "Android":
               button_id.href = "https://apps.apple.com/us/app/menutium/id1170811326"
            case "HarmonyOS":
               button_id.href = "https://apps.apple.com/us/app/menutium/id1170811326"
    elif (ua.is_pc == True):
        button_id.href = "{{ url_for('test') }}"
    else :
        button_id.href ="{{ url_for('test') }}"


@app.route('/Install_Now')
def Install_Now():
    return render_template('Install_Now.html')


def redirect(button_id='button'):
         return render_template("https://www.youtube.com/watch?v=ku5Zfa3KTWg")



if __name__ == "__main__":
    app.run(debug=True)



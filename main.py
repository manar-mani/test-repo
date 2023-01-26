from flask import Flask, render_template, request
from user_agents import parse
from werkzeug.user_agent import UserAgent
import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)

app = Flask(__name__)

# TODOs:
# - Add requirements.txt file in order to install the required packages easily. 
# - Check out the follwoing links to send data from Python to HTML and vice-versa:
#   - https://pythonbasics.org/flask-template-data/
#   - https://stackoverflow.com/questions/51669102/how-to-pass-data-to-html-page-using-flask
#   - https://www.youtube.com/watch?v=aDOSQAq8cls&ab_channel=PythonProgramming

# README
# - In each file, you need to use sinigfic names
# - Always add logger service !!!


@app.route("/")
def init():
    logging.info('***** Server running *****')
    ua = request.headers.get('User_Agent')
    logging.info(ua)
    user_agent = parse(ua)
    # Accessing user agent's browser attributes
    logging.info('Browser full data: '+str(user_agent.browser))
    logging.info('Browser familly: '+str(user_agent.browser.family))
    logging.info('Browser version: '+str(user_agent.browser.version))

    # Accessing user agent's operating system properties
    logging.info('OS full data: '+str(user_agent.os))
    logging.info('OS familly: '+str(user_agent.os.family))
    logging.info('OS version: '+str(user_agent.os.version))

    # Accessing user agent's device properties
    logging.info('Device full data: '+str(user_agent.device))
    logging.info('Device familly: '+str(user_agent.device.family))
    logging.info('Device brand: '+str(user_agent.device.brand))
    logging.info('Device model: '+str(user_agent.device.model))
    return render_template('index.html')



# Why you do this? (what is the utility of button id?)
def redirect(button_id='Install'):
    ua = request.headers.get('User_Agent')
    logging.info(ua)
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
        button_id.href = "{{ url_for('index') }}"
    else:
        button_id.href = "{{ url_for('index') }}"


# Where is this file?
# @app.route('/Install_Now')
# def Install_Now():
#    return render_template('Install_Now.html')


def redirect(button_id='button'):
    return render_template("https://www.youtube.com/watch?v=ku5Zfa3KTWg")


if __name__ == "__main__":
    app.run(debug=True)

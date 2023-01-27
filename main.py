from flask import Flask, render_template, request, redirect, url_for
from user_agents import parse
from werkzeug.user_agent import UserAgent
import logging
from os import path

logging.basicConfig(filename='example.log', level=logging.DEBUG)

app = Flask(__name__)

# TODOs:
# - Add requirements.txt file in order to install the required packages easily. (Done)
# - Check out the follwoing links to send data from Python to HTML and vice-versa:
#   - https://pythonbasics.org/flask-template-data/ (Done)
#   - https://stackoverflow.com/questions/51669102/how-to-pass-data-to-html-page-using-flask (Done)
#   - https://www.youtube.com/watch?v=aDOSQAq8cls&ab_channel=PythonProgramming (Done)

# README
# - In each file, you need to use sinigfic names
# - Always add logger service !!!


@app.route('/')
def index():
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

#def Install_Now():
    #return render_template('Install_Now.html')



# Why you do this? (what is the utility of button id?)
@app.route('/install',methods = ['POST', 'GET'])
def redirect():
    user_agent = parse(request.headers.get('user_agent'))
    logging.info(user_agent)
    user_agent_os = user_agent.os.family
    if (user_agent.is_mobile == True):
        match user_agent_os :
            case "iOS":
                return redirect(url_for('iOS'))
            case "Android":
                 return redirect(url_for('Android'))
            case "HarmonyOS":
                return redirect(url_for('HarmonyOS'))
    elif (user_agent.is_pc == True):
        return render_template('Install_Now.html')
    else:
        return render_template('Install_Now.html')


# Where is this file?

def iOS():
    return '<a>https://www.apple.com/app-store/</a>'
def Android():
    return '<a>https://www.apple.com/app-store/</a>'
def HarmonyOS():
    return '<a>https://www.apple.com/app-store/</a>'

@app.route('/Install_Now')
def Install_Now():
    return render_template('Install_Now.html')
    

if __name__ == "__main__":
    app.run(host='192.168.31.218', port=8080, debug=True)

from flask import Flask, request, redirect
from twilio import twiml
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>flaskin like a baw$$</h1>"

# @application.route("/twilio", methods=['GET', 'POST'])
# def twilio():
#     resp = twiml.Response()
#     resp.say("Welcome to twilio!")
#     print(str(resp))
#
#
# vxml_xml2 = """
# <?xml version="1.0" encoding="UTF-8"?><vxml version="2.1">
# <form>
# <block>
# <prompt xml:lang="en-in-female">
# <break time="2s"/>
# Welcome to You Report! Please tell us what district you live in.
# </prompt>
# </block>
# </form>
# </vxml>
# """
#
# @application.route("/nexmo")
# def nexmo():
#     return vxml_xml2

if __name__ == "__main__":
    application.run(host='127.0.0.1', port='8000')
    #application.run(debug=False, host='0.0.0.0')
    #application.run(debug=False)

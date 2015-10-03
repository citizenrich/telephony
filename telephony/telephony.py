from flask import Flask, request, redirect
import twilio.twiml

application = Flask(__name__)

@application.route("/twilio", methods=['GET', 'POST'])
def hello_monkey():
    resp = twilio.twiml.Response()
    resp.reject(reason="busy")
    return str(resp)

vxml_xml = '<?xml version="1.0" encoding="UTF-8"?><vxml version="2.1"><form><block><prompt xml:lang="en-in-female"><break time="2s"/>Welcome to You Report! Please tell us what district you live in.</prompt></block></form></vxml>'

vxml_xml2 = """
<?xml version="1.0" encoding="UTF-8"?><vxml version="2.1">
<form>
<block>
<prompt xml:lang="en-in-female">
<break time="2s"/>
Welcome to You Report! Please tell us what district you live in.
</prompt>
</block>
</form>
</vxml>
"""

@application.route("/nexmo")
def hello():
    return vxml_xml2

if __name__ == "__main__":
    application.run(debug=False, host='0.0.0.0')
    application.run(debug=False)

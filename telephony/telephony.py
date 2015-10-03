from flask import Flask, request, redirect
import twilio.twiml
from PyVXML import PyVXML

application = Flask(__name__)

@application.route("/twilio", methods=['GET', 'POST'])
def hello_monkey():
    resp = twilio.twiml.Response()
    resp.reject(reason="busy")
    return str(resp)

#vxml = PyVXML(version='2.0')
#vxml.start_form(fid='indian english demo')
#vxml.start_block()
#vxml.start_disconnect()
#vxml.start_prompt('Hello', xml_lang='en-in-female')
#vxml.end_prompt()
#vxml.end_block()
#vxml.end_form()
#vxml_xml = vxml.generate()

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
    app.run(debug=False, host='0.0.0.0')

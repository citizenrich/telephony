import anymarkup

y = """
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

z = anymarkup.serialize(y, 'json')
print z


x = anymarkup.serialize({'foo': 'bar'}, 'xml')
print x

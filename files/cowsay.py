import subprocess
from flask import Response

from flask import Flask
app = Flask(__name__)

@app.route('/<what>')
#@app.route('/', defaults={'what': 'moo'})
def cowsay(what):
    return Response(subprocess.check_output('cowsay %s' % what, stderr=subprocess.STDOUT, shell=True), mimetype = 'text/plain')
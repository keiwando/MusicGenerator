'''
Music Generator Web Application
Copyright (C) 2016 Keiwan Donyagard

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.
'''

from flask import Flask, render_template, request, url_for, send_from_directory, json
from werkzeug import secure_filename
import webbrowser
import os
import compileFile
import random
import MusicGenerator as MG

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/Lilypond-Files')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] == "ly"

def compileToPDF(file):
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],"Sheet.ly"))
    compileFile.compile()

def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir,'musicgenerator','mysite', 'static', 'Lilypond-Files'), filename)

@app.route('/')
def default():
    return render_template('home.html')


@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        #return str(request.form['hidden-major-minor'])
        if 'file' in request.files:
            file = request.files['file']
            if allowed_file(file.filename):
                compileToPDF(file)
                return serve_static("Sheet.pdf")
            else:
                return render_template('home.html', result=False, invalid=True)
        elif 'randomFile' in request.form:
            #return str(request.form)
            title = request.form['title']
            rhyCompl = request.form['rhythm-complexity']
            melCompl = request.form['melody-complexity']
            expCompl = request.form['expression-complexity']
            rhythmTreble = request.form['hidden-rhythm-treble']
            rhythmBass = request.form['hidden-rhythm-bass']
            melodyTreble = request.form['hidden-melody-treble']
            melodyBass = request.form['hidden-melody-bass']
            expTreble = request.form['hidden-expression-treble']
            expBass = request.form['hidden-expression-bass']

            keyAcc = request.form['key-accidental']
            keyTone = request.form['base-key']
            keyMinMaj = request.form['hidden-major-minor']
            MG.writeSheet(title,rhyCompl,melCompl,expCompl,rhythmTreble,rhythmBass,melodyTreble,melodyBass,expTreble,expBass,keyAcc,keyTone,keyMinMaj)
            compileFile.compile()
            return serve_static("Sheet.pdf")
        else:
            return str(request.form)
    else:
        return render_template('home.html')

@app.route('/test/')
def test():
    return compileFile.test()


if __name__ == '__main__':
    url = "http://127.0.0.1:5000"
    webbrowser.open_new(url)
    app.run(debug=True)



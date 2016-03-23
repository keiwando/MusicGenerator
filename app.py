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

from flask import Flask, render_template, request, url_for, send_from_directory
from werkzeug import secure_filename
import webbrowser
import os
import compileFile

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/Lilypond-Files')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    #url = "http://127.0.0.1:5000"
    #webbrowser.open_new(url)
    app.run(debug=True)

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
        if 'external' in request.form:
            if 'file' in request.files:
                file = request.files['file']
                if allowed_file(file.filename):
                    compileToPDF(file)
                    return serve_static("Sheet.pdf")
            else:
                return "file not allowed"
        elif 'file' in request.files:
            file = request.files['file']
            if allowed_file(file.filename):
                compileToPDF(file)
                return serve_static("Sheet.pdf")
            else:
                return render_template('home.html', result=False, invalid=True)
        else:
            return str(request.files.keys())
    else:
        return render_template('home.html')

@app.route('/test/')
def test():
    return compileFile.test()
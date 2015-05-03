from flask import Flask, render_template, redirect, url_for, request, session, Response, json
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
import os


#config
app = Flask(__name__)
DEBUG = True

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test2.db'
# create the sqlalchemy object
db = SQLAlchemy(app)

import models
from models import *





@app.route('/', methods=['GET','POST'])
def index():
    if request.method =='POST':
        
        new_post=BlogPost(
            request.form['title'],
            request.form['content']
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        posts = db.session.query(BlogPost).all()
        return render_template('index.html', posts=posts)





@app.route('/upload_image', methods=['POST'])
def upload_image():
    """Froala img upload"""
    
    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']
        
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.static_folder,'img',filename))
            
        link = url_for('static', filename='%s/%s' % ('img', filename))

    return Response(json.dumps({'link': link}), content_type="application/json")






if __name__ == '__main__':
    app.run()
    

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#import psycopg2

app = Flask(__name__)

app.config.update(
    SECRET_KEY='password',
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost:5433/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return "Hello world"


#using templates
@app.route('/temp')
def using_templates():
    return render_template('hello.html')

if __name__=='__main__':
    app.run(debug=True)
from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Test12312#@localhost/height_collector'
db = SQLAlchemy(app)

class Data(db.Model):
	__tablename__ = 'data'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True)
	height = db.Column(db.Integer)

	def __init__(self, email, height):
		self.email = email
		self.height = height

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/success/', methods=['POST'])
def success():
	if request.method == 'POST':
		email = request.form["email_name"]
		height = request.form["height_name"]
		if db.session.query(Data).filter(Data.email == email).count() == 0:
			data = Data(email, height)
			db.session.add(data)
			db.session.commit()
			height_avg = db.session.query(func.avg(Data.height)).scalar()
			height_avg = round(height_avg)
			count = db.session.query(Data.email).count()
			send_email(email, height, height_avg, count)
			return render_template('success.html')
		return render_template('index.html', text='Email already exist, please enter a new one')

if __name__=="__main__":
    app.run(debug=True)
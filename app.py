from flask import (Flask,
	render_template,
	request,
	url_for,
	redirect,
	flash,
	jsonify)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def showHomepage():
	return render_template('home.html')

@app.route('/check', methods=['GET','POST'])
def checkMed():
	# check medications
	# does not need to be logged in
	return render_template('check.html')

@app.route('/admin', methods=['GET','POST'])
def showAdmin():
	# admin panel for medications CRUD
	# and users CRUD
	return render_template('admin.html')


if __name__ == '__main__':
	print('app started')
	app.secret_key = 'secretkey'
	app.run(debug=True)

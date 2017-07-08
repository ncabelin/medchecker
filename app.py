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

if __name__ == '__main__':
	print('app started')
	app.secret_key = 'secretkey'
	app.run(host='0.0.0.0', port = 15000)
import os

from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('template.html')

@app.route('/user/<username>/')
# Show the gists for an user
def showUserGists(username):
	# Llamada a github con el usuario
	# Parseo de gists
	return "User %s" % username

@app.route('/search', methods=['POST'])
# Redirect to the correct URL
def redirectToUser():
	if request.form['username']:
		return redirect(url_for('showUserGists', username=request.form['username']))
	else:
		return 'Error'

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)

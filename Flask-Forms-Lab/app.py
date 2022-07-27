
from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "yuval"
password = "Ariel124"
facebook_friends=["noam","roei","mohamed"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method=='POST':
		if username == request.form['username'] and password == request.form['password']:
			return render_template('home.html',facebook_friends=facebook_friends)
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')

@app.route('/friend_exist/<string:friend>' ,methods=['GET', 'POST'])
def friends_exist(friend):
	if friend in facebook_friends:
		return render_template('friend_exists.html')
	else:
		return render_template('friend_exists.html')
		

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
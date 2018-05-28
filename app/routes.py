from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Rafael'}
	posts = [
		{
			'author':{'username': 'John'},
			'body': 'kicking ass today!'
		},
		{
			'author':{'username': 'Susan'},
			'body': 'Get`em John!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)
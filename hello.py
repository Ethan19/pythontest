from flask import Flask,url_for,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'hello world'


@app.route('/index')
def index():
	return render_template('index.html',name='python')



@app.route('/index/<username>')
def showname(username):
	return '%s' % username


@app.route('/index/<int:post_id>')
def showid(post_id):
	return 'nihao %d' % post_id
if __name__ == '__main__':
	app.run(debug=True)
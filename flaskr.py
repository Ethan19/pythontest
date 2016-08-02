import sqlite3,os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing


app = Flask(__name__)
app.config.from_envvar('FALSKR_SETTINGS',silent=True)

# configuration
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='root',
    PASSWORD='root'
))


def connect_db():
	return sqlite3.connect(app.config['DATABASE'])
def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql',mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()


@app.before_request
def before_request():
	g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
	db = getattr(g,'db',None)
	if db is not None:
		db.close()

@app.route('/')
def show_entries():
	cur = g.db.execute('select title,text from entries order by id desc')
	entries = [dict(title=row[0],text=row[1]) for row in cur.fetchall()]
	return render_template('show_entries.html',entries=entries)

@app.route('/add',methods=['post'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)

	g.db.execute('insert into entries (title,text) values (?,?)',[request.form['title'],request.form['text']])
	g.db.commit()
	flash("insert success")
	return redirect(url_for('show_entries'))


@app.route('/logout')
def logout():
	session.pop('logged_in',None)
	flash('you were logout')
	return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')









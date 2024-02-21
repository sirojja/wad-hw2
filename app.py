from flask import Flask, render_template, request, redirect, url_for, current_app, session
import psycopg2

app = Flask(__name__)
app.secret_key = b'jnc4!jncdjscjsjc4r4fejcn'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_login(username, password):
            session['username'] = username
            return redirect(url_for('profile'))
    
    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'username' in session:
        return render_template('profile.html', username=session['username'])
    else:
        return redirect(url_for('login'))



@app.route('/static/<string:name>')
def send_static(name):
    return current_app.send_static_file(name)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


def check_login(username, password):
    conn = psycopg2.connect(dbname='postgres', host='127.0.0.1')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE name=%s AND pass=%s', (username, password))
    users = cur.fetchall()
    cur.close()
    conn.close()
    if (users != []):
        return True
    else:
        return False


if __name__ == '__main__':
    app.run(port=5000)
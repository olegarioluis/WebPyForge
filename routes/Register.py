from flask import Blueprint, render_template, request, url_for, redirect
from bank import conn, cur
import time

register_route = Blueprint('register', __name__)


@register_route.route('/Register')
def register():
    return render_template('register.html')


@register_route.route('/submit', methods=['POST'])
def submit():
    try:
        name_ = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        password_ = request.form['password']

        cur.execute("INSERT INTO (your table) (name_, surname, email, password_) VALUES (%s, %s, %s, %s)",
                    (name_, surname, email, password_))
        conn.commit()

        return render_template('success.html')

    except KeyError:
        return 'Missing form fields.', 400
    finally:

        cur.close()
        conn.close()


@register_route.route('/redirect')
def redirect_page():

    time.sleep(2)
    return redirect(url_for('login.login'))

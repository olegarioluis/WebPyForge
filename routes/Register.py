from flask import Blueprint, render_template, request, url_for, redirect
from bank import conn, cur

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

        #Insert data into the Database
        cur.execute("INSERT INTO (your_table) (name_, surname, email, password_) VALUES (%s, %s, %s, %s)", (name_, surname, email, password_))
        conn.commit()

        return redirect(url_for('login.login'))
    except KeyError:
        return 'Campos do formulário ausentes.', 400
    finally:
        
        # Close Connection
        cur.close()
        conn.close()

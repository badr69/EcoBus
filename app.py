from flask import Flask, render_template, request, url_for, redirect
from config import Config
from db import get_db_connection
from forms import *


app = Flask(__name__)




# TODO: afficher tous les trajets possibles
@app.route('/')
def index():
    return render_template('index.html')

    # conn = get_db_connection()
    # cur = conn.cursor()
    # cur.execute('SELECT * FROM trips')
    # trips = cur.fetchall()
    # cur.close()
    # conn.close()
    # return render_template('index.html', trips=trips)


# TODO: create a new trip
@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    if request.method == 'POST':
        depart = request.form['depart']
        destination = request.form['destination']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO trips (depart, destination) VALUES (%s, %s))', (depart, destination))
        conn.commit()
        conn.close()
        cur.close()
        return redirect(url_for('index'))
    render_template('create_trip.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    contactform = ContactForm()
    return render_template('contact.html', form=contactform)

# TODO: routes for auth
@app.route("/register", methods=['GET', 'POST'])
def register():
    registerform = RegisterForm()
    return render_template("auth/register.html", form=registerform)

@app.route("/login", methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    return render_template("auth/login.html", form=LoginForm())



# TODO: edit a specific trip
# TODO: update a specific trip

if __name__ == '__main__':
    app.run(debug=True)

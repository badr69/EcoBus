from flask import Flask, render_template, request, url_for, redirect, session, flash

from db import get_db_connection
from forms import RegisterForm, LoginForm, ContactForm, TripForm


app = Flask(__name__)



#TODO: afficher tous les trajets
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM trips')
    trips = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', trips=trips)


# TODO: ajouter un nouveau trajet
@app.route('/add_trip', methods=['GET', 'POST'])
def add_trip():
    tripform = TripForm()
    if request.method == 'POST':
        departure = request.form['departure']
        destination = request.form['destination']
        departure_time = request.form['departure_time']
        available_seats = request.form['available_seats']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO trips (departure, destination, departure_time_date, available_seats) VALUES (%s, %s, %s, %s)', (departure, destination, departure_time, available_seats))
        conn.commit()
        conn.close()
        cur.close()
        return redirect(url_for('index'))
    return render_template('add_trip.html', form=tripform)

# TODO: edit a specific trip
# TODO: update a specific trip
#
# TODO: route pour la page  de contact


# TODO: routes for auth

@app.route("/register", methods=['GET', 'POST'])
def register():
    registerform = RegisterForm()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO passengers (name, email, role, password) VALUES (%s, %s, %s, %s)',
                    (name, email, role, password))
        conn.commit()
        conn.close()
        cur.close()
        flash('Inscription réussie!', 'success')
        return redirect(url_for('login'))
    return render_template("auth/register.html", form=registerform)


@app.route("/login", methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM passengers WHERE email = %s AND password = %s', (email, password))
        passenger = cur.fetchone()
        conn.close()
        cur.close()

        if passenger:
            session['passenger_id'] = passenger[0]
            return redirect(url_for('index'))
        else:
            return "nom d'utilisateur incorrect", 401
    return render_template("auth/login.html", form=loginform)


@app.route("/logout")
def logout():
    return redirect(url_for('index'))

@app.route("/contact", methods=["GET", "POST"])
def contact():
    contactform = ContactForm()
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        content = request.form["content"]
        submit = request.form['submit']
    return render_template("contact.html", form=contactform)


if __name__ == '__main__':
    app.run(debug=True)

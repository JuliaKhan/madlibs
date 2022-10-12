"""A madlib game that compliments its users."""

from crypt import methods
from random import choice

from flask import Flask, render_template, request, session, redirect, url_for

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def index():
    """Display homepage."""
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'
    # return "Hi! This is the home page."


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet", methods=['post'])
def greet_person():
    """Greet user with compliment."""

    # person = request.form.get("person")   #uses form answer
    person = session['username']            #uses session username

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=person, compliment=compliment)

@app.route("/game")
def show_madlib_form():
    """Shows a madlib form"""
    answer = request.args.get('play_game')
    
    if answer == "True":
        return render_template("game.html")
    else:
        return render_template("goodbye.html", person=session['username'])

@app.route("/madlib", methods=['POST'])
def show_madlib():
    """Shows the output from the madlib form"""

    adj1 = request.form.get('adj1')
    adj2 = request.form.get('adj2')
    adj3 = request.form.get('adj3')
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')
    n3 = request.form.get('n3')
    pn1 = request.form.get('pn2')
    pn2 = request.form.get('pn1')
    pn3 = request.form.get('pn3')
    pn4 = request.form.get('pn4')
    game = request.form.get('game')
    vbing1 = request.form.get('vbing1')
    vbing2 = request.form.get('vbing2')
    vbing3 = request.form.get('vbing3')
    vbing4 = request.form.get('vbing4')
    plant = request.form.get('plant')
    bodypart = request.form.get('bodypart')
    place = request.form.get('place')
    num = request.form.get('num')
    

    return render_template("madlib.html", 
    adj1=adj1, adj2=adj2, adj3=adj3, n1=n1, n2=n2, n3=n3, pn1=pn1,
    pn2=pn2, pn3=pn3, pn4=pn4, bodypart=bodypart, plant=plant, game=game,
    vbing1=vbing1, vbing2=vbing2, vbing3=vbing3, vbing4=vbing4, place=place,
    num=num
    )
    

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")

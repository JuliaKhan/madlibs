"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

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
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():
    """Shows a madlib form"""
    answer = request.args.get('play_game')
    
    if answer == "True":
        return render_template("game.html") #show madlib
    else:
        return render_template("goodbye.html")

@app.route("/madlib")
def show_madlib():
    """Shows the output from the madlib form"""

    adj1 = request.args.get('adj1')
    adj2 = request.args.get('adj2')
    adj3 = request.args.get('adj3')
    n1 = request.args.get('n1')
    n2 = request.args.get('n2')
    n3 = request.args.get('n3')
    pn1 = request.args.get('pn2')
    pn2 = request.args.get('pn1')
    pn3 = request.args.get('pn3')
    pn4 = request.args.get('pn4')
    game = request.args.get('game')
    vbing1 = request.args.get('vbing1')
    vbing2 = request.args.get('vbing2')
    vbing3 = request.args.get('vbing3')
    vbing4 = request.args.get('vbing4')
    plant = request.args.get('plant')
    bodypart = request.args.get('bodypart')
    place = request.args.get('place')
    num = request.args.get('num')
    

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

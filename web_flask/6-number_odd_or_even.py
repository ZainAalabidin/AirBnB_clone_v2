#!/usr/bin/python3
""" starts a Flask web application """

from flask  import Flask, render_template
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """ Return hello HBNB """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display “HBNB” """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ display “C ” followed by the value of the text """
    text = text.replace("_", " ")
    return f"C {text}"

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def ptyhon_text(text="is cool"):
    """ display “Python ”, followed by the value of the text """
    text = text.replace("_", " ")
    return f"Python {text}"

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"{n}"

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template("5-number.html", o=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """display a HTML page only if n is an intege"""
    result = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

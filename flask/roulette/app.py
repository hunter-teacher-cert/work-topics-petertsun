from flask import Flask, render_template, request, session

import random

app = Flask(__name__)
app.secret_key="you_will_never_guess_it"

@app.route('/')
def index():
    country = {'name': 'USA'}
    return render_template('index.html', nation = country)

@app.route('/farm')
def farm():
    return render_template('farm.html')

@app.route("/form_wheel", methods=['GET','POST'])
def form_wheel():
    # GET is when we just load the page in our browser
    #POST is when we click the button
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] = session['count'] + 1
    if request.method=="GET":
        return render_template("form_wheel.html")
    else:
        integer_value = request.form['maxPositiveInteger']
        print(integer_value)
        i = random.randrange(1, int(integer_value) + 1)
        return render_template("form_wheel.html", wholeValue = i, count = session['count'])

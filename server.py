import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'steal the ninjas gold!'


@app.route("/")
def index():
    if 'total_gold' not in session:
        session['total_gold'] = 0
        session['rounds']= ''
    return render_template("index.html")


@app.route("/process_money", methods=['POST'])
def process_money():
    if request.form['property'] == 'farm':
        session['property']= request.form['property']
        number = random.randint(10,20)
        session['total_gold'] += number
    elif request.form['property'] == 'cave':
        session['property']= request.form['property']
        number = random.randint(5,10)
        session['total_gold'] += number
    elif request.form['property'] == 'house':
        session['property']= request.form['property']
        number = random.randint(2,5)
        session['total_gold'] += number
    elif request.form['property'] == 'casino':
        session['property']= request.form['property']
        number = random.randint(-50,50)
        session['total_gold'] += number
    if number < 0:
        message = f"<p class='text-danger'>Ninja drunkenly stumbled into the {session['property']} and lost {number*-1} gold, leaving with a total of {session['total_gold']} gold!</p>"
    else:
        message = f"<p class='text-success'>Ninja snuck around the {session['property']} and obtained {number} gold, thickening his wallet to a total amount of {session['total_gold']} gold!</p>"
    if session['total_gold'] >= 200:
        session['total_gold'] = 200
    print(number)
    session['rounds'] += message
    print(message)
    return redirect("/")


@app.route("/clearSession")
def clearSession():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port = 5001)
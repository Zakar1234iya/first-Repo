from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry = request.form['strawberry']
    blackberry = request.form['blackberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    firstName = request.form['first_name']
    lastname = request.form['last_name']
    student_id = request.form['student_id']
    total = int(strawberry) + int(blackberry) + int(raspberry) + int(apple)
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M")
    return render_template("checkout.html", 
    strawberry = strawberry, blackberry = blackberry, raspberry = raspberry, apple = apple,
    firstName = firstName, lastname = lastname, student_id = student_id, total = total , x=date_time , time = now)
      

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
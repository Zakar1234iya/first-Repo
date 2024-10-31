from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    email = request.form['email']
    Gender = request.form['Gender']
    favorite_language = request.form['favorite_language']
    dojo_location = request.form['dojo_location']
    comment = request.form['comment']
    return render_template('result.html', name=name, email=email, Gender=Gender ,  favorite_language=favorite_language ,dojo_location=dojo_location ,comment=comment )

if __name__ == "__main__":
    app.run(debug=True)

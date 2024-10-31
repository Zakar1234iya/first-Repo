from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def func1():
    return render_template('index.html', x=8, y=8, color1='red', color2='black')

@app.route('/<int:x>')
def func2(x):
    return render_template('index.html', x=x, y=8, color1='white', color2='green')

@app.route('/<int:x>/<int:y>')
def func3(x, y):
    return render_template('index.html', x=x, y=y, color1='white', color2='black')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def func4(x, y, color1, color2):
    return render_template('index.html', x=x, y=y, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)

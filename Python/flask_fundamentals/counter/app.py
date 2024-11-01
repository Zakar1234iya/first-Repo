from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/increment_by_2')
def increment_by_2():
    if 'counter' in session:
        session['counter'] += 2
    else:
        session['counter'] = 2
    return redirect('/')

@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

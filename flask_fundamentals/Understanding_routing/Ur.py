from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')         
def hello_world():
    return 'Hello World!'  

@app.route('/Champion')
def champ():
    return 'Champion!'

@app.route('/say/Flask')
def say_flask():
    return 'Hi Flask!'

@app.route('/say/Micheal')
def say_micheal():
    return 'Hi Micheal!'

@app.route('/say/John')
def say_john():
    return 'Hi John'

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return (word + ' ') * num

    
# @app.route('/repeat/<int:num>/bye')
# def repeat(num):
#     return "bye" * num

# @app.route('/repeat/<int:num>/dogs')
# def repeat(num):
#     return "dogs" * num


@app.errorhandler(404)
def page_not_found(error):
    return 'Sorry! No response. Try again\n 404' 

if __name__=="__main__":   
    app.run(debug=True)    # Run the app in debug mode.
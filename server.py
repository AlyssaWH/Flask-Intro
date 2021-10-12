"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = ['this website judges you', 'go back to Party City where you belong', 
'Nsync said it best: bye bye bye', 'I was today years old when I realized I didnt like you']


@app.route('/')
def start_here():
    """Home page."""

    return """
      <!doctype html>
      <html>Hi! This is the home page. <a href= "/hello">Click here to say hello </a> </html>
      """
     


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")
    

    return  f"""
    <!doctype html>
    
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
        

      </body>
      
    </html>
    """


@app.route('/diss')
def insult_person():
    """Get user by name."""

    player = request.args.get("person")

    insult = choice(INSULTS)
    

    return  f"""
    <!doctype html>
    
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        {player}! {insult}!
        

      </body>
      
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")

from flask import Flask,render_template

app=Flask(__name__)

@app.route('/login')
def index():
    return "Hello"

@app.route('/yo/<name>')
def yo(name):
    return f"Yo {name}"

@app.route('/')
def Home():
    return render_template('index.html',title="Home")
if __name__== '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lion')
def lion():
    return render_template('lion.html')

@app.route('/giraffe')
def giraffe():
    return render_template('giraffe.html')

if __name__ == "__main__":
    app.run(debug=True)
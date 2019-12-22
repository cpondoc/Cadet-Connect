from flask import Flask, render_template
from data import get_data

app = Flask(__name__)

Articles = get_data()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/clubs')
def clubs():
    return render_template('clubs.html', articles = Articles)

@app.route('/clubs/<string:id>/')
def club(id):
    index = int(id) - 1
    return render_template('club.html', id = id, article = Articles[index])

if __name__ == '__main__':
    app.run(debug=True)
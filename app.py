from flask import Flask, render_template
import os

# Configuration

app = Flask(__name__)

# Routes 

@app.route('/')
def root():
    return render_template("index.j2")

@app.route('/index.j2')
def home():
    return render_template("index.j2")

@app.route('/about.j2')
def about():
    return render_template("about.j2")

@app.route('/view.j2')
def view():
    return render_template("view.j2")

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 2000))
    app.run(port=port, debug=True)
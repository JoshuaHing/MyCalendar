#!/usr/bin/python3
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("base.html")



if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, use_reloader=True, port=5000)

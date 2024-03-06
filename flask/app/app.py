import os

from flask import Flask, render_template
from dotenv import load_dotenv
from detection_module import print_env

load_dotenv()
app = Flask(__name__)

@app.route('/')
def hello():
	abc = print_env()
	return render_template("index.html", data=abc)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
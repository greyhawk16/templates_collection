#!/usr/bin/env python
import os

from flask import Flask, render_template
from detection_module import *
# from pymongo import MongoClient


app = Flask(__name__)

# client = MongoClient("mongo:27017")

@app.route('/')
def todo():
    from_outer_module = print_true()
    env_from_file = os.getenv("VIRUSTOTAL_API_KEY")
    return render_template("index.html", var1 = from_outer_module, var2 = env_from_file)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)


import os
import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def healthcheck():
    return jsonify({"heathcheck": "Everything is Fine, Houston"})
    

if __name__ == '__main__':
    app.run(debug=True)
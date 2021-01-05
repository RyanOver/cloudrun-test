from flask import Flask, render_template
import sys
import time
import requests
import json
# import pytemperature
import threading
# import googlemaps
from datetime import datetime
import pprint
import os

app = Flask(__name__)


@app.route('/')

def home():

  return render_template('index.html')

'''
sudo docker build . --tag gcr.io/ryan-cicd/test-run

PORT=8080 && sudo docker run -p 9090:${PORT} -e PORT=${PORT} gcr.io/ryan-cicd/test-run
'''

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))

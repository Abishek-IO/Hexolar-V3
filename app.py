from flask import Flask,render_template,url_for,request,redirect
import sys, os
from utils.get_data import get_data
 
sys.path.insert(0, os.getcwd())

app = Flask(__name__)

# For testing purpose only
# TODO: Delete once function is complete

date = 10
month = 12

get_data(28.42, 77.148, date, month)

# Main Route
@app.route('/', methods=['POST', 'GET'])
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask 
import numpy as np
import pandas as pd 


from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

## Route for home Page 
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
  if request.method=='GET':
    return render_template('Home.html')
  else:
    pass


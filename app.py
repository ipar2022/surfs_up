from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Fun Fact'

#    return 'Test Website'
#    return 'Hello World'

# enter this in the terminal FLASK_APP=app.py
# export FLASK_APP=app.py              page 9.4.3
# set FLASK_APP=app.py                 page 9.4.3



#import datetime as dt
#import numpy as np
#import pandas as pd
#import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
#from sqlalchemy import create_engine, func
#from flask import Flask, jsonify
#engine = creat#Measurement = Base.classes.measurement
#Station = Base.classes.station
#session = Session(engine)
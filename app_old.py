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

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_fly():
    return '<!-- POC by pdelteil -->'

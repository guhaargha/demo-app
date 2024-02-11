import os
from flask import Flask
app = Flask(__name__)

tenant = os.environ.get("TENANT") or "default"
environment = os.environ.get("ENVIRONMENT") or "default env"

@app.route('/')
def example():
    return "<h1>MCaaS Example App on " +  tenant + " shared " + environment + " cluster.</h1>"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)

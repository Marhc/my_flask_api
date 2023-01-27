from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def index():
  message = {"message": "Hello from Flask!"}
  return json.dumps(message)


app.run(host='0.0.0.0', port=81)

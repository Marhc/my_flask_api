from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
  message = {"message": "Hello from Flask!"}
  return jsonify(message)


app.run(host='0.0.0.0', port=81)

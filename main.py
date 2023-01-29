from app import app
from config.server import SERVER_PORT


app.run(host='0.0.0.0', port=SERVER_PORT)

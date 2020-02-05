from flask import Flask
from routes.routes import routes

app = Flask(__name__, static_folder="static")
app.secret_key = "my_secret_key"
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
from flask import Flask
from ab_test_suite.routes.routes import routes

app = Flask(__name__, static_folder="static")
app.secret_key = "my_secret_key"
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

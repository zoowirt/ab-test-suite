from flask import Flask
from ab_test_suite.proportions.routes_means import routes_means
from ab_test_suite.proportions.routes_proportions import routes_proportions

app = Flask(__name__, static_folder="static", static_url_path="/static")
app.secret_key = "my_secret_key"
app.register_blueprint(routes_proportions)
app.register_blueprint(routes_means)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=False)

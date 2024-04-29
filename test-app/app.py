from api import api_v0
from environs import Env
from flask import Flask
from flask_bootstrap import Bootstrap5
from views import views

env = Env()
env.read_env()

app = Flask(__name__, static_folder="static")

bootstrap = Bootstrap5(app)

app.register_blueprint(views)
app.register_blueprint(api_v0)


if __name__ == "__main__":
    app.run(
        debug=env.str("DEBUG", default="True"),
        host="0.0.0.0",
        port=env.str("PORT", default="5000"),
    )

from flask import render_template
import config
from flask_cors import CORS
from connexion.middleware import MiddlewarePosition
from starlette.middleware.cors import CORSMiddleware


app = config.connex_app
CORS(app.app, resources={r"/*": {"origins": "*"}})
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

app.add_middleware(
    CORSMiddleware,
    position=MiddlewarePosition.BEFORE_ROUTING,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
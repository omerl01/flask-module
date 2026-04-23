from flask import Flask
from routes.tasks import tasks_bp
from errors import errors_bp
from flask import render_template
from db import init_db

# initialize app and db
app = Flask(__name__)
init_db(app)

# get routes for tasks/lists and errors
app.register_blueprint(tasks_bp)
app.register_blueprint(errors_bp)

# load home page
@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")
# run app
if __name__ == "__main__":
    app.run(debug=True)
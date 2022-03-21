import flask_sqlalchemy
from flask import Flask, render_template, request
from sqlalchemy.sql import func
from send_email import send_email


HOST = "0.0.0.0"
PORT = "8080"
USERNAME = "postgres"
PASSWORD = "agoodpassword"
DBNAME = "postgres"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}'
db = flask_sqlalchemy.SQLAlchemy(app)

class Data(db.Model):
    """Connects to and communicates with our database."""
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    email_ = db.Column(db.String(120), unique = True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    """Function that displays homepage html."""
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    """Function that displays the success page and
    retrieves user info"""
    if request.method == "POST":
        email = request.form["email_name"]
        height = request.form["height_name"]

        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height,1)
            count = db.session.query(Data.height_).count()
            send_email(email, height, average_height, count)
            return render_template("success.html")
    return render_template('index.html',
    text="Seems like we've got something from that email address already!")

if __name__ == "__main__":
    app.debug = True
    app.run()

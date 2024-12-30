from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cars.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
# id
# title
# year
# description
# rating
# ranking
# review
# img_url

class Car(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# with app.app_context():
#     db.create_all()
#
# new_car = Car(
#     name="McLaren P1",
#     year=2013,
#     description="The McLaren P1 is a hybrid hypercar produced from 2013-2015, featuring a twin-turbo 3.8L V8 engine paired with an electric motor for 903 total horsepower. It reaches 60 mph in 2.8 seconds and tops out at 217 mph. Notable features include an active rear wing, carbon fiber construction, and advanced aerodynamics generating 600kg of downforce. Only 375 units were built, priced at $1.15M. The P1 formed part of the hybrid hypercar 'Holy Trinity' alongside the LaFerrari and Porsche 918.",
#     rating=10,
#     ranking=2,
#     review="add comment",
#     img_url="https://wallpapercrafter.com/desktop/454057-Vehicles-McLaren-P1-Phone-Wallpaper.jpg"
# )
# with app.app_context():
#     db.session.add(new_car)
#     db.session.commit()


@app.route("/")
def home():
    result = db.session.execute(db.select(Car).order_by(Car.ranking))
    all_cars = list(result.scalars())
    return render_template("index.html", cars=all_cars)


if __name__ == '__main__':
    app.run(debug=True)

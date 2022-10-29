import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')
API_KEY = os.getenv("API_KEY")

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

def retrieve_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ city }&units=metric&appid={ API_KEY }'
    payload = requests.get(url).json()
    return payload

@app.route('/')
def index_get_city():
    cities = City.query.all()

    weather_data = []

    for city in cities:

        r = retrieve_weather_data(city.name)
        print(r)

        weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(weather)

    return render_template('weather.html', weather_data=weather_data)

@app.route('/', methods=['POST'])
def index_post_city():
    err_msg = ''
    new_city_post = request.form.get('city')

    if new_city_post:
        existing_city = City.query.filter_by(name=new_city_post).first()

        if not existing_city:
            new_city_data = retrieve_weather_data(new_city_post)

            if new_city_data['cod'] == 200:
                new_city_object = City(name=new_city_post)

                if new_city_data['main']['temp'] != None and new_city_data['main']['temp'] > 38:
                    flash('Yeah, you should definitely wear some sunscreen.')
                else:
                    flash('Just wear some sunscreen anyway.')

                db.session.add(new_city_object)
                db.session.commit()
            else:
                err_msg = 'Not sure where that is, but wear sunscreen anyway!'
        else:
            err_msg = 'Whoops! Think you tried this city already.'

    if err_msg:
        flash(err_msg, 'error')
    # else:
    #     flash('Just wear some sunscreen anyway!')

    return redirect(url_for('index_get_city'))


@app.route('/delete/<name>')
def delete_city_from_db(name):
    city = City.query.filter_by(name=name).first()
    db.session.delete(city)
    db.session.commit()

    flash(f'You successfully removed { city.name }.', 'success')
    return redirect(url_for('index_get_city'))
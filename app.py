from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    # Render the main page template.
    return render_template('main.html')


@app.route('/routes')
def routes():
    routes_data = [
  {
    "departure_station": "Київ",
    "destination": "Львів",
    "departure_frequency": "щоденно",
    "carrier": "Мерседес-18",
    "departure_time": "08:00",
    "arrival_time": "15:30"
  },
  {
    "departure_station": "Харків",
    "destination": "Одеса",
    "departure_frequency": "щоденно",
    "carrier": "Мерседес 50",
    "departure_time": "8:30",
    "arrival_time": "21:00"
  },
  {
    "departure_station": "Київ",
    "destination": "Херсон",
    "departure_frequency": "щоденно",
    "carrier": "Автолюкс",
    "departure_time": "12:00",
    "arrival_time": "18:30"
  },
  {
    "departure_station": "Київ",
    "destination": "Полтава",
    "departure_frequency": "щоденно",
    "carrier": "Мерседес-18",
    "departure_time": "09:30",
    "arrival_time": "12:00"
  },
  {
    "departure_station": "Одеса",
    "destination": "Харків",
    "departure_frequency": "щоденно",
    "carrier": "Автолюкс",
    "departure_time": "9:00",
    "arrival_time": "21:30"
  }
]
    # Render the routes page template.
    return render_template('routes.html', routes=routes_data)

@app.route('/prices')
def prices():
    prices_data = [
  {
    "departure_station": "Київ",
    "destination": "Львів",
    "departure_time": "08:00",
    "arrival_time": "15:30",
    "price": "500грн"
  },
  {
    "departure_station": "Київ",
    "destination": "Одеса",
    "departure_time": "15:30",
    "arrival_time": "21:00",
    "price": "400грн"
  },
  {
    "departure_station": "Київ",
    "destination": "Херсон",
    "departure_time": "12:00",
    "arrival_time": "18:30",
    "price": "500грн"
  },
  {
    "departure_station": "Київ",
    "destination": "Полтава",
    "departure_time": "09:30",
    "arrival_time": "12:00",
    "price": "300грн"
  },
  {
    "departure_station": "Київ",
    "destination": "Харків",
    "departure_time": "9:00",
    "arrival_time": "21:30",
    "price": "200грн"
  }
]
    # Render the prices page template.
    return render_template('prices.html', prices=prices_data)


@app.route('/contacts')
def contacts():
    # Render the contacts page template.
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)

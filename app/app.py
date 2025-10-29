from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            params = {
                'q': city,
                'appid': API_KEY,
                'units': 'metric'
            }
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'humidity': data['main']['humidity'],
                    'wind_speed': data['wind']['speed'],
                    'description': data['weather'][0]['description'].capitalize()
                }
            else:
                error = 'City not found or API error.'
    return render_template('index.html', weather=weather_data, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
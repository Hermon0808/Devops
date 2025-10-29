from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Get API key from environment variable
API_KEY = os.getenv('OPENWEATHER_API_KEY', 'YOUR_OPENWEATHERMAP_API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            if API_KEY == 'YOUR_OPENWEATHERMAP_API_KEY':
                error = 'API key not configured. Please set OPENWEATHER_API_KEY environment variable.'
            else:
                params = {
                    'q': city,
                    'appid': API_KEY,
                    'units': 'metric'
                }
                try:
                    response = requests.get(BASE_URL, params=params, timeout=10)
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
                        error = f'API error: {response.status_code} - {response.text}'
                except requests.exceptions.RequestException as e:
                    error = f'Network error: {str(e)}'
        else:
            error = 'Please enter a city name.'
    return render_template('index.html', weather=weather_data, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
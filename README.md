# Weather-App
A simple, user-friendly weather application built with Python, KivyMD, and WeatherAPI. Enter a city name to get real-time weather information, displayed on the UI and spoken aloud using text-to-speech.

# Features
* Real-Time Weather Data: Fetches current weather details including temperature, condition, humidity, and wind speed.
* Text-to-Speech: Weather information is narrated aloud using the pyttsx3 library.
* Responsive UI: Built with KivyMD for a modern, Material Design-inspired interface.
* Error Handling: Gracefully handles invalid inputs, network issues, and API errors.

# Prerequisites
Before running the app, ensure you have the following installed:
* Python 3.x
* A WeatherAPI key (sign up at WeatherAPI to get your free API key)

# Usage
1. Run the App: python weather_app.py
2. Interact with the App:
* Launch the app to see a simple interface.
* Enter a city name (e.g., "London") in the text field.
* Click the "Get Weather" button to fetch and display the weather data.
* Listen as the weather details are spoken aloud.

# Dependencies
* kivy: For the app’s graphical interface.
* kivymd: For Material Design components.
* requests: To fetch weather data from the WeatherAPI.
* pyttsx3: For text-to-speech functionality.

# Example Output
Upon entering "New York":\
City: New York\
Temperature: 15°C\
Condition: Partly cloudy\
Humidity: 60%\
Wind Speed: 12 km/h\
The app will also narrate: **"The weather in New York is partly cloudy. The temperature is 15 degrees Celsius, with 60 percent humidity, and wind speed of 12 kilometers per hour."**

# Note
* The app requires an active internet connection to fetch weather data.

# License
This project is licensed under the [MIT License](https://opensource.org/license/MIT).

# Authors
[Divya HS](https://github.com/DivyaHS26)

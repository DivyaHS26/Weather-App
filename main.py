from kivy.lang import Builder
from kivymd.app import MDApp
import requests
import json
import pyttsx3  # Import text-to-speech engine
from kivy.clock import Clock

KV = '''
BoxLayout:
    orientation: 'vertical'
    spacing: dp(10)
    padding: dp(20)

    MDLabel:
        text: "Weather App"
        theme_text_color: "Primary"
        halign: "center"
        font_style: "H4"

    MDTextField:
        id: city_input
        hint_text: "Enter city name"
        size_hint_x: 0.9
        pos_hint: {"center_x": 0.5}

    MDRaisedButton:
        text: "Get Weather"
        size_hint_x: 0.5
        pos_hint: {"center_x": 0.5}
        on_release: app.get_weather()

    MDLabel:
        id: weather_output
        text: "Weather info will appear here"
        halign: "center"
        theme_text_color: "Secondary"
        font_style: "H6"
'''

class WeatherApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.engine = pyttsx3.init()  # Initialize TTS engine
        return Builder.load_string(KV)

    def speak(self, text):
        """Speaks the given text."""
        self.engine.say(text)
        self.engine.runAndWait()

    def get_weather(self):
        city = self.root.ids.city_input.text.strip()
        if city:
            url = f"https://api.weatherapi.com/v1/current.json?key=55939d48a00b4ce9ba3220347230406&q={city}"

            try:
                response = requests.get(url)
                if response.status_code == 200:
                    weather_data = json.loads(response.text)
                    temp = weather_data["current"]["temp_c"]
                    condition = weather_data["current"]["condition"]["text"]
                    humidity = weather_data["current"]["humidity"]
                    wind_speed = weather_data["current"]["wind_kph"]

                    # Prepare weather details
                    weather_text = (
                        f"City: {city}\n"
                        f"Temperature: {temp}°C\n"
                        f"Condition: {condition}\n"
                        f"Humidity: {humidity}%\n"
                        f"Wind Speed: {wind_speed} km/h"
                    )

                    # Update the UI with weather details first
                    self.root.ids.weather_output.text = weather_text

                    # Use Clock.schedule_once to schedule the speaking action after the UI update
                    Clock.schedule_once(lambda dt: self.speak_weather(city, temp, condition, humidity, wind_speed), 0.1)

                else:
                    self.root.ids.weather_output.text = "Error: Could not fetch data."
                    self.speak("Sorry, I couldn't fetch the weather data.")

            except Exception as e:
                self.root.ids.weather_output.text = "Network Error!"
                self.speak("Network error! Please check your internet connection.")

        else:
            self.root.ids.weather_output.text = "Please enter a city name."
            self.speak("Please enter a city name.")

    def speak_weather(self, city, temp, condition, humidity, wind_speed):
        """Speak the weather details."""
        speech_text = (
            f"The weather in {city} is {condition}. "
            f"The temperature is {temp} degrees Celsius, "
            f"with {humidity} percent humidity, "
            f"and wind speed of {wind_speed} kilometers per hour."
        )
        self.speak(speech_text)

if __name__ == "__main__":
    WeatherApp().run()

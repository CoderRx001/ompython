import forecastio
from geopy.geocoders import Nominatim

def get_current_weather(address):
    location = Nominatim(user_agent="my-app").geocode(address)
    api_key = "ab1cd78dc8ddb7081901341c244ed941"

    if location:
        forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude).currently()
        return f"Today is {forecast.time} currently {forecast.summary} {forecast.icon} at {forecast.temperature} degrees, with a chance for rain of {forecast.precipProbability}."
    else:
        return "Location not found"

print(get_current_weather("New York, NY"))
print(get_current_weather("Los Angeles, CA"))
print(get_current_weather("Hong Kong, CN"))
print(get_current_weather(""))


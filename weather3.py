
import forecastio
#dark sky import 
from geopy.geocoders import Nominatim
#geopy imports


def get_current_weather(address):
    location = Nominatim(user_agent="my-app").geocode(address)
    api_key = "ab1cd78dc8ddb7081901341c244ed941"
    lat = location.latitude
    lng = location.longitude
    forecast = forecastio.load_forecast(api_key, lat, lng).currently()
    return f"Today is {forecast.time} currently {forecast.summary} {forecast.icon} at {forecast.temperature} degrees, with a chance for rain of {forecast.precipProbability}."

print(get_current_weather("New York, NY"))
print(get_current_weather("Los Angeles, CA"))
print(get_current_weather("Hong Kong, CN"))

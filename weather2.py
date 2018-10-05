
import forecastio
#dark sky import 
from geopy.geocoders import Nominatim
#geopy imports

location = Nominatim(user_agent="my-app").geocode("1300 north dearborn st. chicago,IL")
# Please specify a custom `user_agent` with `Nominatim(user_agent="my-application") do to violation apparently

api_key = "ab1cd78dc8ddb7081901341c244ed941"
# api-key for dark sky
lat = location.latitude
lng = location.longitude
#chicago lat & lng coordinates

forecast = forecastio.load_forecast(api_key, lat, lng).currently()
print(f"Today is {forecast.time} currently {forecast.summary} {forecast.icon} at {forecast.temperature} degrees, with a chance for rain of {forecast.precipProbability}.")
# terminal info requested


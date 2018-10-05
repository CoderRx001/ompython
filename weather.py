
import forecastio

api_key = "ab1cd78dc8ddb7081901341c244ed941"
# api-key for dark sky
lat = 41.8781
lng = -87.6298
#chicago lat & lng coordinates

forecast = forecastio.load_forecast(api_key, lat, lng).currently()
print(forecast.time, forecast.summary, forecast.temperature, forecast.icon, forecast.precipProbability)
# terminal info requested

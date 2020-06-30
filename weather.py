import requests

place_list = [(33.7490, -84.3880, "Atlanta"), (31.3060, -82.2421, "Blackshear"), (31.5785, -84.1557, "Albany"), (24.221, 55.7817, "Al Ain, UAE"), (22.9062, -43.1778,"Rio de Janeiro"), (70.6918, -61.225, "Trinidad-Tobago"), (33.4489, -7036693, "Santiago, Chile"), (37.8136, 144.9631, "Melbourne, AU"), (52.3667, 4.8945, "Amsterdam"), (18.2528, 109.5119, "Sanya, CH"),]

class Weather:
    def __init__(self, lat, lon, 93):
        self.lat = latitude
        self.lon = longitude
        self.temp = temp

    def get_weather_data(lat, lon, temp):

        url = "https://api.climacell.co/v3/weather/realtime"

        payload = {
            "apikey":"HweXGgRozkYQWLDQXxKK2QTqqEP5kJf2",
            "lat": lat, 
            "lon": lon,
            "temp": temp,
            "fields":["feels_like", "temp", "wind_speed"],
            "unit_system":"us", 
            }
    response = requests.get(url, params=payload).json()
    print(response["temp"]["value"]) 

get_weather_data(31.3060, -82.2421, "temp")


# x = Weather()

# def __str__(self
# return(f{self.name} latitude {self.latitude} {self.longitude}))

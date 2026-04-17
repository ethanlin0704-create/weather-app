import requests

api_key = "YOUR_API_KEY"
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
#print(response)
data = response.json()
#print(data)

if response.status_code == 200:
    city_name = data["name"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print(f"\nWeather in {city_name}")
    print(f"Temperature: {temperature}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Condition: {weather}")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed} m/s")
else:
    print("City not found or API request failed.")
import requests

def display_weather(city):
    api_key = "60955c8f131f9dc48b5acbc7ef62b022"  # ✅ Your API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(complete_url, timeout=10)
        
        # Check HTTP response status
        if response.status_code == 200:
            data = response.json()

            city_name = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_desc = data["weather"][0]["description"]

            print(f"\nCity: {city_name}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {weather_desc.capitalize()}")

        else:
            print("Error:", response.json().get("message", "Unknown error"))

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please check your internet connection.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your network connection.")
    except Exception as e:
        print("Error:", str(e))

# ---- Run the function ----
city_name = input("Enter city name: ")
display_weather(city_name)

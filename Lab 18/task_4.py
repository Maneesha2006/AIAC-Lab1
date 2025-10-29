import requests

def display_weather(city):
    api_key = "60955c8f131f9dc48b5acbc7ef62b022"  # ✅ Your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"

    try:
        # Send GET request
        response = requests.get(complete_url, timeout=10)
        response.raise_for_status()  # Raises an error for bad HTTP responses (4xx, 5xx)

        # Convert response to JSON
        data = response.json()

        # Extract and display key details
        city_name = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]

        print(f"\nCity: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_desc.capitalize()}")

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please check your internet connection.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your network connection.")
    except requests.exceptions.HTTPError:
        print("Error: Invalid API request. Please check your API key or city name.")
    except KeyError:
        print("Error: Unexpected data format from API.")
    except Exception as e:
        print("Error:", str(e))


# ---- Run the function ----
city_name = input("Enter city name: ")
display_weather(city_name)

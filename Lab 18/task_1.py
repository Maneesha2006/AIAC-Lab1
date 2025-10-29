import requests
import json

def display_weather(city):
    api_key = "60955c8f131f9dc48b5acbc7ef62b022"  
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Create full API request URL
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    
    # Send GET request to the API
    response = requests.get(complete_url)
    
    # Convert response to JSON
    weather_data = response.json()
    
    # Display formatted JSON output
    print(json.dumps(weather_data, indent=4))

# Example usage
city_name = input("Enter city name: ")
display_weather(city_name)

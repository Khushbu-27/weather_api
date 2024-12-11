
from fastapi import  HTTPException
import requests
from app.src.weather_api.v1.city_weather.model.weather_model import WeatherResponse
import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

class weather:
    
    def get_weather(city: str):
        
        if not OPENWEATHERMAP_API_KEY:
            raise HTTPException(status_code=500, detail="API Key not configured")

        try:
            response = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
            )

            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail=response.json())
            
            data = response.json()

            weather_data = {
                "city": data["name"],
                "temperature_max": data["main"]["temp_max"],
                "temperature_min": data["main"]["temp_min"],
                "wind_speed": data["wind"]["speed"]
            }
            
            return WeatherResponse(**weather_data)

        except requests.RequestException as e:
            raise HTTPException(status_code=500, detail=str(e))
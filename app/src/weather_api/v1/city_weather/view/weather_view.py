
from fastapi import APIRouter
from app.src.weather_api.v1.city_weather.model.weather_model import WeatherResponse
from app.src.weather_api.v1.city_weather.services.weather_services import weather


weather_router = APIRouter()

@weather_router.get("/weather/", response_model=WeatherResponse)
def get_weather(city: str):
    return weather.get_weather(city)
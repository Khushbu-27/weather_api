
from fastapi import APIRouter
from app.src.weather_api.v1.city_weather.view.weather_view import weather_router

router = APIRouter()

router.include_router(weather_router)

from pydantic import BaseModel

class Weather(BaseModel):
    
    city: str
    temperature_max: float
    temperature_min: float
    wind_speed: float
    
class WeatherResponse(BaseModel):
    
    city: str
    temperature_max: float
    temperature_min: float
    wind_speed: float
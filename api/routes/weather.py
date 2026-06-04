from fastapi import APIRouter 
import requests 

from api.config import CLE_METEO 

router= APIRouter() 

@router.get("/weather/{city}")

def get_weather(city: str):
    url = (
        "https://api.weatherapi.com/v1/current.json"
        f"?key={CLE_METEO}"
        f"&q={city}"
    )

    response = requests.get(url)

    data = response.json()

    return {
        "city": data["location"]["name"],
        "temperature": data["current"]["temp_c"]
    }
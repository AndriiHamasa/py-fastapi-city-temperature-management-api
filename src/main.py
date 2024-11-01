from fastapi import FastAPI

from src.city import router as city_router
from src.temperature import router as temperature_router


app = FastAPI()

app.include_router(city_router.router)
app.include_router(temperature_router.router)
from pydantic import BaseModel


class VehicleEvent(BaseModel):
    id: str
    lat: float
    lon: float
    speed: float

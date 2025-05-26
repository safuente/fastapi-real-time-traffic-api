from fastapi import APIRouter, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.models.schemas import VehicleEvent
from app.services.vehicle_service import handle_vehicle_event
import time

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)


@router.post("/events")
@limiter.limit("100/second")
async def post_vehicle_event(event: VehicleEvent, request: Request):
    start_time = time.perf_counter()
    await handle_vehicle_event(event)
    duration = time.perf_counter() - start_time
    return {"status": "received", "duration_ms": round(duration * 1000, 2)}

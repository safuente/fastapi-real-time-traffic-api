from fastapi import FastAPI
from app.api.routes import router as api_router, limiter
from app.api.websocket import websocket_endpoint
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.core.event_bus import start_event_listener
import asyncio


app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded,
    lambda r, e: JSONResponse(status_code=429, content={"error": "Too Many Requests"}),
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
app.add_api_websocket_route("/ws/vehicles", websocket_endpoint)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_event_listener())

import json
import asyncio
from redis.asyncio import Redis
from app.ws_manager import manager

REDIS_CHANNEL = "vehicle_events"
redis = Redis(host="redis", port=6379, decode_responses=True)


async def publish_event(event):
    await redis.publish(REDIS_CHANNEL, event.json())


async def start_event_listener():
    pubsub = redis.pubsub()
    await pubsub.subscribe(REDIS_CHANNEL)
    async for message in pubsub.listen():
        if message["type"] == "message":
            await manager.broadcast(message["data"])

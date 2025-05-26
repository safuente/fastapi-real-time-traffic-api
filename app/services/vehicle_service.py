from app.core.event_bus import publish_event


async def handle_vehicle_event(event):
    await publish_event(event)

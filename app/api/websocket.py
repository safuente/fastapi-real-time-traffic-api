from fastapi import WebSocket
from app.ws_manager import manager


async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except:
        await manager.disconnect(websocket)

# FastAPI Real-Time Traffic API

This project provides a real-time event broadcasting API for vehicle location updates.

### Features
- REST endpoint to ingest vehicle events
- WebSocket endpoint to broadcast updates
- Redis-backed Pub/Sub for scalability
- Dockerized

### Run Locally
```bash
make up
```

To stop the application:
```bash
make down
```

### Test WebSocket
Use browser or Postman to connect to:
```
ws://localhost:8000/ws/vehicles
```
Send a POST to `/events` with:
```json
{
  "id": "bus-42",
  "lat": 40.7128,
  "lon": -74.0060,
  "speed": 50
}
```
Clients will receive it live via Redis pub/sub.

### Load Test Example
Run:
```bash
make locust
```
Then open your browser at:
```
http://localhost:8089
```
Enter:
- Number of users: `100`
- Spawn rate: `10`

Observe how the app handles many POST events per second.

### API Timing
Each POST to `/events` will return the duration in milliseconds under key `duration_ms` so you can monitor response time directly.
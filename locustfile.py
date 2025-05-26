from locust import HttpUser, task, between
import random


class VehicleEventUser(HttpUser):
    wait_time = between(0.01, 0.2)
    host = "http://localhost:8000"

    @task
    def post_event(self):
        payload = {
            "id": f"bus-{random.randint(1, 100)}",
            "lat": round(random.uniform(-90, 90), 6),
            "lon": round(random.uniform(-180, 180), 6),
            "speed": round(random.uniform(0, 120), 2),
        }
        self.client.post("/events", json=payload)

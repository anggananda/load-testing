import os
from dotenv import load_dotenv
from locust import HttpUser, task, between

load_dotenv()


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    token = os.getenv("JWT_TOKEN")

    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}

    @task
    def get_agenda_mengajar(self):
        self.client.get("/api/v1/agenda-mengajar?tahun=2024")

    @task
    def get_agenda_mengajar_export_csv(self):
        self.client.get("/api/v1/agenda-mengajar/export-csv?tahun=2024")

    @task
    def get_unitkerja(self):
        self.client.get("/api/v1/unitkerja")

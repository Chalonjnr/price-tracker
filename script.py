import os
import requests

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]

mensaje = "✅ GitHub Actions ya puede mandar mensajes a Discord"

response = requests.post(WEBHOOK_URL, json={"content": mensaje})
response.raise_for_status()

print("Mensaje enviado a Discord")
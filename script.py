import os
import requests

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]

ITEM_ID = "MPE737220072"

url = f"https://api.mercadolibre.com/items/{ITEM_ID}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

data = response.json()

titulo = data["title"]
precio = data["price"]
moneda = data["currency_id"]
link = data["permalink"]

mensaje = (
    f"📦 {titulo}\n"
    f"💰 Precio: {moneda} {precio}\n"
    f"🔗 {link}"
)

requests.post(WEBHOOK_URL, json={"content": mensaje})

print("Precio enviado a Discord")
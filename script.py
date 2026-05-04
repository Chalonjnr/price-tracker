import os
import requests

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]

ITEM_ID = "MPE737220072"  # ID correcto del producto en Perú

url = f"https://api.mercadolibre.com/items/{ITEM_ID}"

response = requests.get(url)
response.raise_for_status()

data = response.json()

titulo = data["title"]
precio = data["price"]
moneda = data["currency_id"]
link = data["permalink"]

mensaje = (
    f"📦 {titulo}\n"
    f"💰 Precio actual: {moneda} {precio}\n"
    f"🔗 {link}"
)

discord_response = requests.post(
    WEBHOOK_URL,
    json={"content": mensaje}
)

discord_response.raise_for_status()

print("Precio enviado a Discord")
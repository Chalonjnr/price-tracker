import os
import requests

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]

QUERY = "xiaomi mi tv box s 3ra google tv 4k"
URL_OBJETIVO = "https://www.mercadolibre.com.pe/xiaomi-mi-tv-box-s-3ra-con-google-tv-4k-chromecast-no-stick/up/MPEU3235961795"

url = "https://api.mercadolibre.com/sites/MPE/search"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
}

params = {
    "q": QUERY,
    "limit": 5,
}

response = requests.get(url, headers=headers, params=params)

print("STATUS:", response.status_code)
print("BODY:", response.text[:500])

response.raise_for_status()

data = response.json()
results = data.get("results", [])

if not results:
    raise Exception("No encontré productos en Mercado Libre Perú.")

producto = results[0]

titulo = producto["title"]
precio = producto["price"]
moneda = producto["currency_id"]
link = producto["permalink"]

mensaje = (
    f"📦 {titulo}\n"
    f"💰 Precio actual: {moneda} {precio}\n"
    f"🔗 {link}"
)

discord_response = requests.post(WEBHOOK_URL, json={"content": mensaje})
discord_response.raise_for_status()

print("Precio enviado a Discord")
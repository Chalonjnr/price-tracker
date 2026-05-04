import os
import re
import requests
from bs4 import BeautifulSoup

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]

URL = "https://www.mercadolibre.com.pe/xiaomi-mi-tv-box-s-3ra-con-google-tv-4k-chromecast-no-stick/up/MPEU3235961795"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "es-PE,es;q=0.9,en;q=0.8",
}

response = requests.get(URL, headers=headers, timeout=20)

print("STATUS:", response.status_code)

if response.status_code in [403, 429]:
    raise Exception("Mercado Libre bloqueó la solicitud. No continuamos.")

response.raise_for_status()

html = response.text
soup = BeautifulSoup(html, "html.parser")

titulo = soup.find("h1")
titulo = titulo.get_text(strip=True) if titulo else "Producto Mercado Libre"

# Busca precios en el HTML
texto = soup.get_text(" ", strip=True)
match = re.search(r"S/\s*([\d.,]+)", texto)

if not match:
    raise Exception("No pude encontrar el precio en la página.")

precio = match.group(1)

mensaje = (
    f"📦 {titulo}\n"
    f"💰 Precio detectado: S/ {precio}\n"
    f"🔗 {URL}"
)

discord_response = requests.post(WEBHOOK_URL, json={"content": mensaje})
discord_response.raise_for_status()

print("Precio enviado a Discord")
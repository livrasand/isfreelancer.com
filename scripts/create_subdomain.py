import json
import requests
import os

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
DOMAIN = 'isfreelancer.com'

def create_subdomain(subdomain):
    headers = {
        'Authorization': f'sso-key {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json'
    }
    url = f'https://api.godaddy.com/v1/domains/{DOMAIN}/records'
    data = [{
        "type": "CNAME",
        "name": subdomain,
        "data": DOMAIN,
        "ttl": 600
    }]
    response = requests.patch(url, headers=headers, json=data)
    return response.status_code == 200

# Leer archivo subdominios.json
with open('subdominios.json', 'r') as file:
    subdominios = json.load(file)

# Buscar el último subdominio añadido
nuevo_subdominio = subdominios[-1]['subdomain']

# Crear subdominio
if create_subdomain(nuevo_subdominio):
    print(f"Subdominio {nuevo_subdominio}.{DOMAIN} creado con éxito.")
else:
    print("Error al crear el subdominio.")

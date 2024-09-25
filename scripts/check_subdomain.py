import dns.resolver
import json

DOMAIN = 'isfreelancer.com'

# Función para verificar el subdominio mediante una consulta DNS
def check_subdomain_dns(subdomain):
    try:
        result = dns.resolver.resolve(f'{subdomain}.{DOMAIN}', 'CNAME')
        for cnameval in result:
            if cnameval.target.to_text().strip('.') == DOMAIN:
                return True
    except dns.resolver.NXDOMAIN:
        return False
    except dns.resolver.NoAnswer:
        return False
    except Exception as e:
        print(f"DNS lookup failed: {e}")
        return False

# Leer el archivo subdominios.json
with open('subdomains.json', 'r') as file:
    subdomains = json.load(file)

# Buscar el último subdominio añadido
nuevo_subdominio = subdomains[-1]['subdomain']

# Verificación por DNS
if check_subdomain_dns(nuevo_subdominio):
    print(f"DNS verification successful: {nuevo_subdominio}.{DOMAIN} is active.")
    exit(0)  # Exit with success
else:
    print(f"Error: Subdomain {nuevo_subdominio}.{DOMAIN} was not found in DNS.")
    exit(1)  # Exit with failure

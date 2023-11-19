import socket
import dns.resolver

def probabilite(sous_domaine):
   seuil_risque = 1 - len(sous_domaine) / 20.0
   print(f"Sous-domaine trouvé avec un seuil de risque de {seuil_risque}: {sous_domaine}")
   return seuil_risque

def SubdomainSearch(domaine, dictionnaire, seuil_risque):
    for sous_domaine, valeur in dictionnaire.items():
        if valeur.endswith(domaine):
            risque = probabilite(sous_domaine)
            if risque > seuil_risque:
              return sous_domaine
    return None

    

dictionnaire = {
    "www": "example.com",
    "blog": "example1.com",
    "api": "example2.com"
}

domaine = "example2.com"
seuil_risque = 0.5

sous_domaine = SubdomainSearch(domaine, dictionnaire, seuil_risque)

print(sous_domaine)


def ReverseDNS(ip):
  try:
    information = socket.gethostbyaddr(ip)
    return information[0]
  except socket.gaierror:
    return None
  
ip_lookup = "8.8.8.8"
host_name = ReverseDNS(ip_lookup)

if host_name:
    print(f"Le nom d'hôte associé à l'adresse IP {ip_lookup} est {host_name}.")
else:
    print(f"Aucun nom d'hôte trouvé pour l'adresse IP {ip_lookup}.")



#1. Une requête DNS est envoyée par un client pour obtenir des info sur le domaine.
#   Pour ensuite traduire l'@IP en nom de domaine.


#2. Le reverse DNS permet de trouver quelle adresse ip est associé un domaine.
#   Cela permet également de filtrer les requêtes et empêcher les spams par exemple.


#3. Nous pouvons ajouter un seuil de risque pour éviter toute menace comme fait ci-dessus.


#4. Sécurité : les menaces extérieurs peuvent utilser le reverse DNS pour obtenir notre @IP.
#   Fiabilité : ne renvoie pas toujours les bonnes valeurs.
#   Temps de réponse : le temps de réponse est élevé ce qui provoque des baisse de performance.
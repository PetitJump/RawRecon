from dns import requette_dns
from https import requete_https

def domaine_vivant(domaine):
    if requette_dns(domaine) is None:
        return None
    return requete_https(domaine)


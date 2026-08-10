import json
from dns import requette_dns
from https import requete_https

def domaine_vivant(domaine):
    if requette_dns(domaine) is None:
        return False
    return True


def sous_domaine(domaine):
    try:
        rendu = []
        dico = json.loads(requete_https("crt.sh", f"/?q={domaine}&output=json"))
        for k in dico:
            print(k["name_value"])
            if k["name_value"] not in rendu:
                rendu.append(k["name_value"])
    except json.decoder.JSONDecodeError:
        print("Erreur JSONDecodeError")
        return []

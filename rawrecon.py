import socket
import ssl
import struct
from dns import encoder_nom

def requete_https(cible, chemin="/"):

    ### Création de l'emmeteur ###
    emetteur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    emetteur.connect((cible, 443)) # Connecte l'emetteur a la cible au port 443
    print(f"Connexion faite chez {cible} au port 443")
    ######

    ### Création du chiffrement ###
    context = ssl.create_default_context() # Crée l'objet qui va servir a chiffré
    securise = context.wrap_socket(emetteur, server_hostname=cible) # Sécurise ce que va envoyer l'emetteur
    print("Connexion sécurisé activé")
    ######

    ### Création et envoie de la requete DNS ###
    message = encoder_nom("sumply.fr") + struct.pack(">HH", 1, 1)
    securise.sendto(message, ("8.8.8.8", 53))
    ######

    ### Envoie de la requette ###
    requete = f"GET {chemin} HTTP/1.1\r\nHost: {cible}\r\nConnection: close\r\n\r\n" # Requete HTTP
    data = requete.encode() # Encode la requete en byts
    securise.sendall(data)
    print(f"Message envoyé chez {cible}")
    ######

    ### Recupération du message ###
    byts = b""
    while True: # Tant qu'il reste des messages a prendre
        recu = securise.recv(4096)
        if not recu: # Si il n'y a plus aucun message
            break
        byts += recu
        print("Message trop long -> rechargement de la demande")
    parties = byts.decode()
    parties = parties.split("\r\n\r\n", 1) # Coupe en deux (header et corp)
    header = parties[0]
    corps = parties[1]
    print(f"Message reçu de {cible} \r")
    ######
    return corps

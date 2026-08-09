import socket
import ssl


def requete_https(cible, chemin="/"):
    emetteur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crée l'objet emetteur qui va servir a envoyer les messages
    emetteur.connect((cible, 443)) # Connecte l'emetteur a la cible au port 443
    print("Connexion faite au port 443")

    context = ssl.create_default_context() # Crée l'objet qui va servir a chiffré
    securise = context.wrap_socket(emetteur, server_hostname=cible) # Sécurise ce que va envoyer l'emetteur
    print("Connexion sécurisé activé")


    requete = f"GET {chemin} HTTP/1.1\r\nHost: {cible}\r\nConnection: close\r\n\r\n" # Requete HTTPS
    data = requete.encode() # Encode la requete en byts
    securise.sendall(data)

    byts = b""
    while True: # Tant qu'il reste des messages a prendre
        recu = securise.recv(4096)
        if not recu: # Si il n'y a plus aucun message
            break
        byts += recu
    return byts

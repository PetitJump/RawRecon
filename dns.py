import socket
import struct

def dns(domaine):
    def en_tete(domaine: str):
        rendu =  b""
        parties = domaine.split('.')
        for k in parties:
            rendu += bytes([len(k)])
            rendu += k.encode()
        rendu += bytes([0])
        return struct.pack(">HHHHHH", 6769, 0x0100, 1, 0, 0, 0) + rendu + struct.pack(">HH", 1, 1) # Création de l'en-tete

    emetteur = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Création de l'emmeteur

    emetteur.sendto(en_tete(domaine), ("8.8.8.8", 53)) # Envoie de la requette DNS
    return emetteur.recvfrom(512)[0]

def extraire_ip(reponse):
    rendu = ""
    for k in reponse[-4:]: # On ne prend que l'adresse ip
        rendu += str(k) + "."
    return rendu[:-1] # On enlève le dernier point pour donné une vrai ip

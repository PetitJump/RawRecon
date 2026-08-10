import struct

def encoder_nom(domaine: str):
    rendu =  b""
    parties = domaine.split('.')
    for k in parties:
        rendu += bytes([len(k)])
        rendu += k.encode()
    rendu += bytes([0])
    return struct.pack(">HHHHHH", 1234, 0x0100, 1, 0, 0, 0) + rendu

# RawRecon
Un outil de reconnaissance de sous domaines codé entièrement avec la bibliothèque standard de Python. Pas de requests, pas de aiohttp, pas de dnspython : juste socket, ssl et struct...

## Statut
En cours de construction.

## Ce que ça fait (objectif)

RawRecon est un petit outil de reconnaissance pensé pour la découverte de sous domaines façon bug bounty.
 
* Récupère tous les sous domaines qui ont un jour eu un certificat HTTPS public pour un domaine cible, via les logs de Certificate Transparency (crt.sh)
* Vérifie lesquels sont encore actifs
* Sonde chaque host actif en HTTP et HTTPS pour récupérer son code de statut, son titre et son header serveur
* Repère ce qui ressemble à un vieux panneau d'admin oublié ou un environnement de test qui traîne

## Pourquoi pas de bibliothèque tierce
Franchement, pourquoi se faire chier à tout recoder soi même quand requests, dnspython et compagnie existent déjà, font le travail, et sont testés par des millions de gens ?
 
Parce que justement, c'est tout l'intérêt. N'importe qui peut coller import requests et obtenir un résultat sans jamais comprendre ce qui se passe entre l'appel de fonction et la réponse qui arrive. Ce projet fait l'inverse : chaque opération réseau (la poignée de main TCP, la poignée de main TLS, la requête DNS, la requête HTTP) est écrite directement avec les modules socket, ssl et struct de Python.
 
L'objectif n'est pas de réinventer subfinder ou httpx en mieux. C'est de comprendre ce que ces outils font vraiment sous le capot avant de les utiliser les yeux fermés, ce qui compte beaucoup plus en sécurité offensive que dans la plupart des autres domaines.

## Transparance
Chaque ligne de code de ce repo a été tapée à la main. Aucun outil IA n'a écrit, complété ou suggéré la moindre ligne de code. Ce README, en revanche, a été rédigé avec l'aide de l'IA.
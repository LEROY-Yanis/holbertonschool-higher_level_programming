#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:   # on vérifie si la clé existe
        del a_dictionary[key] # on supprime la clé
    return a_dictionary       # on retourne le dictionnaire

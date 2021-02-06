import random

pies_en_millas = 5280
metros_en_km = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def get_nombre_archivo(archivo):
    return archivo[archivo.index(".") + 1:]

def tirar_dado(num):
    return random.randint(1, num)
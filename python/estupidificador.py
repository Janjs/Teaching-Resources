archivo_con_frase = open("frase.txt", "r")

def traductor_estupido(frase):
    traducción = ""
    for letra in frase:
        if letra.lower() in "aeiou":
            if letra.isupper():
                traducción = traducción + "I"
            else:
                traducción = traducción + "i"
        else:
            traducción = traducción + letra

    print(frase)
    return traducción

frase = input("Escribe algo inteligente: ")
print(traductor_estupido(frase))

#frase = archivo_con_frase.readline()
#print("Frase des de arxiu: "+traductor_estupido(frase))
parrafo = """
La logística Digital es un concepto que surge de la integración entre la logística tradicional y
la era digital. Con el auge del correo electrónico y las descargas digitales reemplazando
productos físicos, podríamos estar hablando de un golpe devastador para la industria de la
logística, pero, de hecho, ha ocurrido algo muy diferente. El sector de la logística ha
introducido las innovaciones digitales.
"""

palabra_buscada = "logística"


def convertir_a_minusculas(texto):
    resultado = ""
    for caracter in texto:
        if 'A' <= caracter <= 'Z':
            resultado += chr(ord(caracter) + 32)
        else:
            resultado += caracter
    return resultado

parrafo = convertir_a_minusculas(parrafo)
palabra_buscada = convertir_a_minusculas(palabra_buscada)

print(parrafo)
print(palabra_buscada)

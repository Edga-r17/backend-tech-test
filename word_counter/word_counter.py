parrafo = """
La logística Digital es un concepto que surge de la integración entre la logística tradicional y
la era digital. Con el auge del correo electrónico y las descargas digitales reemplazando
productos físicos, podríamos estar hablando de un golpe devastador para la industria de la
logística, pero, de hecho, ha ocurrido algo muy diferente. El sector de la logística ha
introducido las innovaciones digitales.
"""

palabra_buscada = "logística"

parrafo_prueba = """
En el vasto universo de la programación, Python brilla con luz propia. 
Python es versátil, fácil de aprender y poderoso. Muchos programadores 
aman Python porque les permite construir soluciones elegantes en poco tiempo.
"""
palabra_buscada_prueba = "python"



def convertir_a_minusculas(texto):
    resultado = ""
    for caracter in texto:
        if 'A' <= caracter <= 'Z':
            resultado += chr(ord(caracter) + 32)
        else:
            resultado += caracter
    return resultado

def es_letra(caracter):
    return ('a' <= caracter <= 'z') or ('á' <= caracter <= 'ú') or ('ñ' == caracter)

def contar_ocurrencias(parrafo, palabra):
    ocurrencias = 0
    i = 0

    while i <= len(parrafo) - len(palabra):
        match = True

        for j in range(len(palabra)):
            if parrafo[i + j] != palabra[j]:
                match = False
                break

        if match:
            antes = parrafo[i - 1] if i > 0 else ' '
            despues = parrafo[i + len(palabra)] if i + len(palabra) < len(parrafo) else ' '

            if not es_letra(antes) and not es_letra(despues):
                ocurrencias += 1
                i += len(palabra)  
            else:
                i += 1
        else:
            i += 1

    return ocurrencias

parrafo = convertir_a_minusculas(parrafo)
palabra_buscada = convertir_a_minusculas(palabra_buscada)
resultado = contar_ocurrencias(parrafo, palabra_buscada)

parrafo_prueba = convertir_a_minusculas(parrafo_prueba)
palabra_buscada_prueba = convertir_a_minusculas(palabra_buscada_prueba)
resultado_prueba = contar_ocurrencias(parrafo_prueba, palabra_buscada_prueba)


print(parrafo)
print(palabra_buscada)
print(f"'La palabra: {palabra_buscada}' aparece {resultado} veces.")

print(parrafo_prueba)
print(palabra_buscada_prueba)
print(f"'La palabra: {palabra_buscada_prueba}' aparece {resultado_prueba} veces.")

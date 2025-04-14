def convertir_a_minusculas(texto):
    resultado = ""
    for caracter in texto:
        if 'A' <= caracter <= 'Z':
            resultado += chr(ord(caracter) + 32)
        else:
            resultado += caracter
    return resultado


def es_letra(caracter):
    return ('a' <= caracter <= 'z') or ('á' <= caracter <= 'ú') or (caracter == 'ñ')


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


def main():
    parrafo_1 = """
    La logística Digital es un concepto que surge de la integración entre la logística tradicional y
    la era digital. Con el auge del correo electrónico y las descargas digitales reemplazando
    productos físicos, podríamos estar hablando de un golpe devastador para la industria de la
    logística, pero, de hecho, ha ocurrido algo muy diferente. El sector de la logística ha
    introducido las innovaciones digitales.
    """
    palabra_1 = "logística"

    parrafo_2 = """
    En el vasto universo de la programación, Python brilla con luz propia. 
    Python es versátil, fácil de aprender y poderoso. Muchos programadores 
    aman Python porque les permite construir soluciones elegantes en poco tiempo.
    """
    palabra_2 = "python"

    parrafo_1 = convertir_a_minusculas(parrafo_1)
    palabra_1 = convertir_a_minusculas(palabra_1)

    parrafo_2 = convertir_a_minusculas(parrafo_2)
    palabra_2 = convertir_a_minusculas(palabra_2)

    resultado_1 = contar_ocurrencias(parrafo_1, palabra_1)
    resultado_2 = contar_ocurrencias(parrafo_2, palabra_2)

    print(f"La palabra '{palabra_1}' aparece {resultado_1} veces.")
    print(f"La palabra '{palabra_2}' aparece {resultado_2} veces.")


if __name__ == "__main__":
    main()

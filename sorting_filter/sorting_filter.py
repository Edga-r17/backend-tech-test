def cumple_criterios(item, criterios):
    for campo, operador, valor in criterios:
        if operador == '=' and item[campo] != valor:
            return False
        elif operador == '>=' and item[campo] < valor:
            return False
        elif operador == '<=' and item[campo] > valor:
            return False
    return True

def ordenar_por_priority_desc(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]['priority'] < lista[j + 1]['priority']:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    return lista

def main():
    entry = [
        {'id': 12340, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
        125, 'priority': 2},
        {'id': 12341, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
        127, 'priority': 4},
        {'id': 12342, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
        129, 'priority': 6},
        {'id': 12343, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
        131, 'priority': 0},
        {'id': 12344, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
        133, 'priority': 0},
        {'id': 12345, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
        135, 'priority': 0},
        {'id': 12346, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
        137, 'priority': -1},
        {'id': 12347, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
        139, 'priority': 0},
        {'id': 12348, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
        141, 'priority': 2},
        {'id': 12349, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
        143, 'priority': 0},
        {'id': 12350, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost':
        145, 'priority': 0},
        {'id': 12351, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost':
        147, 'priority': 10},
        {'id': 12352, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost':
        149, 'priority': 0},
        {'id': 12353, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost':
        151, 'priority': 0},
        {'id': 12354, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost':
        153, 'priority': 0},
        {'id': 12355, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost':
        155, 'priority': 0},
        {'id': 12356, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost':
        157, 'priority': 0},
        {'id': 12357, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost':
        159, 'priority': 0},
        {'id': 12358, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost':
        161, 'priority': 0},
        {'id': 12359, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost':
        135, 'priority': 0},
        {'id': 12360, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
        137, 'priority': 0},
        {'id': 12361, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
        139, 'priority': 0},
        {'id': 12362, 'weight': 3, 'width': 3, 'height': 1, 'length': 10, 'cost':
        141, 'priority': -2},
        {'id': 12363, 'weight': 3, 'width': 3, 'height': 1, 'length': 10, 'cost':
        153, 'priority': -2},
        {'id': 12364, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
        145, 'priority': -6},
        {'id': 12366, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
        147, 'priority': 0},
        {'id': 12367, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
        149, 'priority': 0},
        {'id': 12365, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
        151, 'priority': 2},
        {'id': 12368, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
        181, 'priority': 2},
        {'id': 12369, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
        183, 'priority': 0},
    ]

    criterios = [('weight', '=', 3)]
    

    cumplen = []
    no_cumplen = []

    for item in entry:
        if cumple_criterios(item, criterios):
            cumplen.append(item)
        else:
            no_cumplen.append(item)
    cumplen_ordenados = ordenar_por_priority_desc(cumplen)

    resultado = cumplen_ordenados + no_cumplen

    print("Elementos que cumplen con los criterios:")
    for e in cumplen:
        print(e)

    print("\nElementos que NO cumplen:")
    for e in no_cumplen:
        print(e)

    print("\nResultado final:")
    for e in resultado:
        print(e)


if __name__ == "__main__":
    main()
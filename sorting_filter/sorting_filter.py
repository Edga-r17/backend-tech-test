def cumple_criterios(item, criterios):
    for campo, operador, valor in criterios:
        if operador == '=' and item[campo] != valor:
            return False
        elif operador == '>=' and item[campo] < valor:
            return False
        elif operador == '<=' and item[campo] > valor:
            return False
    return True

def main():
    entry = [
        {'id': 12340, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost': 125, 'priority': 2},
        {'id': 12341, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost': 127, 'priority': 4},
        {'id': 12342, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost': 129, 'priority': 6},
        {'id': 12360, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost': 137, 'priority': 0},
        {'id': 12368, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost': 181, 'priority': 2},
        {'id': 12365, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost': 151, 'priority': 2},
        {'id': 12364, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost': 145, 'priority': -6}
    ]

    criterios = [('weight', '=', 3)]

    cumplen = []
    no_cumplen = []

    for item in entry:
        if cumple_criterios(item, criterios):
            cumplen.append(item)
        else:
            no_cumplen.append(item)

    print("Elementos que cumplen con los criterios:")
    for e in cumplen:
        print(e)

    print("\nElementos que NO cumplen:")
    for e in no_cumplen:
        print(e)


if __name__ == "__main__":
    main()
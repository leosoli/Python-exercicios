
def find_num(lista, n) -> int:
    """Encontrar qual número está ausente em uma lista de inteiros

    Args:
        lista (list(int)): lista de inteiros de comprimento n-1 (1 inteiro faltante)
        n (int): total de múmeros que a lista deveria possuir

    Returns:
        int: n_falta -> inteiro faltante
    """
    lista.sort()
    for i in range(len(lista)):
        if i == 0:
            if lista[i] != 1:
                n_falta = 1
                break
        else:
            if lista[i]-lista[i-1] != 1:
                n_falta = lista[i] - 1
                break
    return n_falta

def main():
    n = int(input()) # input de inteiro n que pertence a [2 , 1000]3
    lista_n = [int(i) for i in input().split(' ')] # lista com n-1 inteiros inseridos

    print(find_num(lista_n, n))

if __name__ == '__main__':
    main()

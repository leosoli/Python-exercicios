def teste_pares_sapatos(total_sapatos: int, lista_sapatos: list) -> int:
    """Teste de verificação de pares de calçados

    Args:
        total_sapatos (int): total de sapatos a verificar
        lista_sapatos (list): lista de sapatos a verificar

    Returns:
        int: total_pares -> total de pares formados encontrado
    """
    total_pares = 0
    i = 0 # deverá ir até total_sapatos-1 no máximo
    while len(lista_sapatos)>1 and i<total_sapatos:
        sapato = lista_sapatos[0] # separa o 1º sapato da lista para comparação
        len_lista_antes = len(lista_sapatos)

        for k in range(1,len(lista_sapatos)):
            if sapato[:2]==lista_sapatos[k][:2] and \
                                        sapato[3]!=lista_sapatos[k][3]:\
                                        # mesmo número, mas pés diferentes
                lista_sapatos.pop(k); lista_sapatos.pop(0) # par eliminado
                total_pares = total_pares + 1 # total de pares incrementado
                break # par foi eliminado -> novo lista_sapatos[0] definido
        if len(lista_sapatos)==len_lista_antes: # correspondente do 1º sapato não encontrado
            lista_sapatos.pop(0) # elimina o 1º sapato
        i = i+1
    return total_pares


def main():
    n = input() # número de sapatos em string

    while n != '': # n == '' -> EOF
        n_int = int(n) # número inteiro de sapatos
        lista_s = [input() for i in range(n_int)]

        total_pares = teste_pares_sapatos(n_int, lista_s)

        print(total_pares)
        n = input()

if __name__ == '__main__':
    main()

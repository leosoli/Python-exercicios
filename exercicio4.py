def elimina_zeros_esquerda(texto_num: str) -> str:
    if texto_num == []:
        return False
    
    eliminado = False
    chegou_fim = False
    pos_inicio = 0
    for pos, c in enumerate(texto_num):
        if c != '0':
            pos_inicio = pos
            break
        if pos == len(texto_num)-1:
            chegou_fim = True
    texto_num = texto_num[pos_inicio:] if not chegou_fim else []
    return texto_num


def elimina_digito(texto_num: str, dig: str) -> str:
    texto_num = texto_num.replace(dig, '')
    return texto_num

def main():
    entrada = input()

    while entrada != '0 0':
        params = [p for p in entrada.split(' ')]
        digito = params[0]
        texto_numero = params[1]
        
        texto_numero = elimina_digito(texto_numero, digito)
        texto_numero = elimina_zeros_esquerda(texto_numero)

        print('0') if len(texto_numero) == 0 else print(texto_numero)

        entrada = input()

if __name__ == '__main__':
    main()

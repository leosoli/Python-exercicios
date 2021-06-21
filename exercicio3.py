
def inicializa_dict_andares(n: int) -> dict:
    """Inicializa dicionário de andares
    Args:
        n (int): total de andares do prédio
    Returns:
        dict: dicionário de andares com 0 pessoas para cada andar
    """
    return dict(zip(range(1,n+1),[0 for i in range(n)]))

def alimentar_andares(andares: dict, pessoa_andar: list) -> dict:
    """Alimenta o dicionário de andares com o número de pessoas
    para cada andar.
    Args:
        andares (dict): dicionário de andares zerado
        pessoa_andar (list): lista com o andar desejado para cada pessoa
    Returns:
        dict: dicionário com a relação de nº pessoas por andar desejado
    """
    for andar in pessoa_andar:
        andares[andar] = andares[andar] + 1
    return andares

def pessoas_mais_alto(andares: dict) -> int:
    """Andar mais alto que querem ir pessoas
    Args:
        andares (dict): dicionário com a relação de pessoas por andar desejado
    Returns:
        int: andar mais alto que querem ir
    """
    encontrado = False
    for andar, num_p in reversed(andares.items()):
        if num_p > 0:
            encontrado = True
            break
    
    return (andar if encontrado else 0)

def remove_pessoas_and_altos(dicio_andares: dict, cap: int) -> None:
    """Remover as pessoas dos andares quando há mais de 1 andar que pode ser visitado
    Args:
        dicio_andares (dict): dicionário com a relação de nº pessoas por andar desejado
        cap (int): capacidade total do elevador
    """
    remove_pessoas_and_altos_recursivo(dicio_andares, cap)
    return 

def remove_pessoas_and_altos_recursivo(dic_and: dict, c_rest: int) -> None:
    """Chamada pela função remove_pessoas_and_alto() para recursivamente 
    deixar as pessoas nos andares do topo para a base até todas as pessoas 
    no elevador serem deixadas nos seus andares (eliminadas) do dicionário
    Args:
        dic_and (dict): dicionário com a relação de nº pessoas por andar desejado
        c_rest (int): restante de pessoas no elevador
    """
    andar_alto = pessoas_mais_alto(dic_and) # andar mais alto para pessoas no momento

    if andar_alto == 0:
        return

    if dic_and[andar_alto] >= c_rest: # se tem mais ou igual gente que quer ir para aquele andar do que cap restante do elevador
        dic_and[andar_alto] = dic_and[andar_alto] - c_rest
        return
    else:
        novo_c_rest = c_rest - dic_and[andar_alto]
        dic_and[andar_alto] = 0
    remove_pessoas_and_altos_recursivo(dic_and, novo_c_rest)



def simulacao_elevador() -> None:
    """Simulação de energia do elevador para parâmentros pergutados ao usuário
    """
    params_str = input()
    params = [int(p) for p in params_str.split(' ')]
    N = params[0]; C = params[1]; M = params[2]

    pessoa_andar_str = input()
    pessoa_andar = [int(num) for num in pessoa_andar_str.split(' ')]

    energia = 0

    dict_andares = alimentar_andares(inicializa_dict_andares(N), pessoa_andar)

    while ( dict_andares != inicializa_dict_andares(N) ):
        andar_mais_alto = pessoas_mais_alto(dict_andares)
        situacao = C - dict_andares[andar_mais_alto] # pos: cabe mais; zero: no limite; neg: passou do limite

        if situacao == 0: # todas as pessoas que vão pro mais alto sobem e enchem o elevador
            energia = energia + 2*andar_mais_alto # elevador sobe até o mais alto
            dict_andares[andar_mais_alto] = 0 # zera as pessoas para subirem para esse andar
        elif situacao < 0: # faltou espaço pra todas as pessoas que iam pro mais alto
            energia = energia + 2*andar_mais_alto # elevador sobe até o mais alto
            dict_andares[andar_mais_alto] = dict_andares[andar_mais_alto] - C
        else: # sobrou espaço no elevador
            energia = energia + 2*andar_mais_alto # elevador sobe até o mais alto
            remove_pessoas_and_altos(dict_andares, C) # recursivamente eliminando as pessoas dos andares até acabar a capacidade

    print(energia)

def main():
    num_testes = int(input()) # número de testes desejados
    for t in range(num_testes):
        simulacao_elevador()

if __name__ == '__main__':
    main()

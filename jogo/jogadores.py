def cria_jogador(id_jogador):
    nome = input(f'Nome do jogador {id_jogador} ')
    return {
        'id': id_jogador,
        'nome': nome,
        'pontos': 0,
        'vez': True
    }

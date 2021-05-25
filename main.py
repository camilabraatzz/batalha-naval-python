from jogo.jogadas import posicao_navios
from jogo.jogadores import cria_jogador
from jogo.tabuleiro import cria_tabuleiro
from jogo.validacoes import valida_posicao_bombas
from telas.tabuleiro import mostrar_tabuleiro


def main():
    jogador1 = cria_jogador(1)
    jogador2 = cria_jogador(2)

    tabuleiro1 = cria_tabuleiro(jogador1)
    mostrar_tabuleiro(tabuleiro1)
    posicao_navios(tabuleiro1)

    tabuleiro2 = cria_tabuleiro(jogador2)
    mostrar_tabuleiro(tabuleiro2)
    posicao_navios(tabuleiro2)

    valida_posicao_bombas(jogador1, jogador2, tabuleiro1, tabuleiro2)


main()

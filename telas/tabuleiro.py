from time import sleep

from utils.cores import adiciona_cor
from utils.texto import gera_texto


def mostrar_indice_coluna(tamanho_linha):
    for count in range(0, tamanho_linha):
        end = '\n' if count == tamanho_linha - 1 else ' '
        espaco_extra = '  ' if count == 0 else ''
        if count == 6 or count == 7:
            print(f'{espaco_extra} {adiciona_cor("33m", count)}', end=end)
        else:
            print(f'{espaco_extra} {adiciona_cor("33m", count)} ', end=end)


def mostrar_indice_linha(indice):
    print(adiciona_cor("33m", indice), end=': ')


def mostrar_tabuleiro(tabuleiro):
    area = tabuleiro['area']
    for j, linha in enumerate(area):
        if j == 0:
            mostrar_indice_coluna(len(linha))
        mostrar_indice_linha(j)
        for posicao in linha:
            print(f'{adiciona_cor("1;94m", gera_texto("🌊 "))}', end=' ')
        print()
        sleep(0.05)


def tabuleiro_final(tabuleiro):
    area = tabuleiro['area']
    for j, linha in enumerate(area):
        for posicao in linha:
            if posicao is None:
                print(f'{adiciona_cor("1;94m", gera_texto("🌊"))}', end=' ')
            if posicao == '🚢':
                print(f'{adiciona_cor("1;33m", gera_texto("🚢"))}', end=' ')
            elif posicao == '💥':
                print(f'{adiciona_cor("1;31m", gera_texto("💥"))}', end=' ')
        print()
        sleep(0.05)
    print(f'Nome: {tabuleiro["jogador"]["nome"]}, Pontos: {tabuleiro["jogador"]["pontos"]}')
    return tabuleiro
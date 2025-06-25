import pygame
import sys

pygame.init()

#mostrando a tela 
LARGURA, ALTURA = 300, 300
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Velha")

#Dando cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
LINHA_COLOR = (0, 0, 0)


tabuleiro = [['' for _ in range(3)] for _ in range(3)]

jogador_atual = 'X'
game_over = False

# Desenhando o tabuleiro
def desenhar_tabuleiro():
    TELA.fill(BRANCO)
    # Linhas verticais
    pygame.draw.line(TELA, LINHA_COLOR, (100, 0), (100, 300), 2)
    pygame.draw.line(TELA, LINHA_COLOR, (200, 0), (200, 300), 2)
    # Linhas horizontais
    pygame.draw.line(TELA, LINHA_COLOR, (0, 100), (300, 100), 2)
    pygame.draw.line(TELA, LINHA_COLOR, (0, 200), (300, 200), 2)


    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == 'X':
                pygame.draw.line(TELA, PRETO, (coluna * 100 + 15, linha * 100 + 15), (coluna * 100 + 85, linha * 100 + 85), 2)
                pygame.draw.line(TELA, PRETO, (coluna * 100 + 85, linha * 100 + 15), (coluna * 100 + 15, linha * 100 + 85), 2)
            elif tabuleiro[linha][coluna] == 'O':
                pygame.draw.circle(TELA, PRETO, (coluna * 100 + 50, linha * 100 + 50), 35, 2)

def verificar_vitoria():
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != '':
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != '':
            return tabuleiro[0][i]
        

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != '':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != '':
        return tabuleiro[0][2]
    return None


def verificar_empate():
    for linha in tabuleiro:
        if '' in linha:
            return False
    return True



while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if not game_over and evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            linha, coluna = y // 100, x // 100 
            
            if tabuleiro[linha][coluna] == '':
                tabuleiro[linha][coluna] = jogador_atual
                
                vencedor = verificar_vitoria()
                if vencedor:
                    print(f"Jogador {vencedor} venceu!")
                    game_over = True
                elif verificar_empate():
                    print("Empate!")
                    game_over = True
                else:
                    jogador_atual = 'O' if jogador_atual == 'X' else 'X'
    
    desenhar_tabuleiro()
    pygame.display.update()

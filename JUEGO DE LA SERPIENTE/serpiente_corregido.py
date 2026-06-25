import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Tamaño de la ventana
ANCHO, ALTO = 600, 400
TAM = 20

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Serpiente")

reloj = pygame.time.Clock()
fuente = pygame.font.SysFont(None, 35)


def mostrar_puntaje(puntaje):
    texto = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    pantalla.blit(texto, (10, 10))


def dibujar_serpiente(lista_serpiente):
    for bloque in lista_serpiente:
        pygame.draw.rect(pantalla, VERDE, (bloque[0], bloque[1], TAM, TAM))


def crear_comida(serpiente):
    while True:
        comida = [
            random.randrange(0, ANCHO, TAM),
            random.randrange(0, ALTO, TAM)
        ]
        if comida not in serpiente:
            return comida


def menu():
    while True:
        pantalla.fill(NEGRO)

        textos = [
            ("JUEGO DE LA SERPIENTE", VERDE, 120, 60),
            ("1 - Nivel Facil", BLANCO, 180, 150),
            ("2 - Nivel Dificil", BLANCO, 180, 200),
            ("Q - Salir", ROJO, 180, 250),
        ]

        for texto, color, x, y in textos:
            pantalla.blit(fuente.render(texto, True, color), (x, y))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1 or evento.key == pygame.K_KP1:
                    juego(10)

                elif evento.key == pygame.K_2 or evento.key == pygame.K_KP2:
                    juego(18)

                elif evento.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


def juego(velocidad):
    x = ANCHO // 2
    y = ALTO // 2

    # La serpiente inicia moviéndose hacia la derecha
    dx = TAM
    dy = 0

    serpiente = [[x, y]]
    longitud = 1
    comida = crear_comida(serpiente)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and dx != TAM:
                    dx, dy = -TAM, 0
                elif evento.key == pygame.K_RIGHT and dx != -TAM:
                    dx, dy = TAM, 0
                elif evento.key == pygame.K_UP and dy != TAM:
                    dx, dy = 0, -TAM
                elif evento.key == pygame.K_DOWN and dy != -TAM:
                    dx, dy = 0, TAM

        x += dx
        y += dy

        # Verificar choque con los bordes
        if x < 0 or x >= ANCHO or y < 0 or y >= ALTO:
            volver_menu = game_over(longitud - 1)
            if volver_menu:
                return

        cabeza = [x, y]

        # Verificar choque con el propio cuerpo
        if cabeza in serpiente:
            volver_menu = game_over(longitud - 1)
            if volver_menu:
                return

        serpiente.append(cabeza)

        if len(serpiente) > longitud:
            serpiente.pop(0)

        # Comer comida
        if cabeza == comida:
            longitud += 1
            comida = crear_comida(serpiente)

        pantalla.fill(NEGRO)
        pygame.draw.rect(pantalla, ROJO, (comida[0], comida[1], TAM, TAM))
        dibujar_serpiente(serpiente)
        mostrar_puntaje(longitud - 1)

        pygame.display.update()
        reloj.tick(velocidad)


def game_over(puntaje):
    while True:
        pantalla.fill(NEGRO)

        texto1 = fuente.render(f"GAME OVER - Puntaje: {puntaje}", True, ROJO)
        texto2 = fuente.render("C - Menu", True, BLANCO)
        texto3 = fuente.render("Q - Salir", True, BLANCO)

        pantalla.blit(texto1, (100, 120))
        pantalla.blit(texto2, (210, 170))
        pantalla.blit(texto3, (220, 220))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_c:
                    return True

                elif evento.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


# Ejecutar el menú principal
menu()

import pygame
import random

# Inicializar Pygame
pygame.init()

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Tamaño de la ventana
ANCHO = 600
ALTO = 400

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Serpiente")

reloj = pygame.time.Clock()

# Tamaño de los bloques
tam_bloque = 20
velocidad = 10

fuente = pygame.font.SysFont(None, 35)

def mostrar_puntaje(puntaje):
    texto = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    pantalla.blit(texto, [10, 10])

def dibujar_serpiente(tam_bloque, lista_serpiente):
    for bloque in lista_serpiente:
        pygame.draw.rect(pantalla, VERDE, [bloque[0], bloque[1], tam_bloque, tam_bloque])

def juego():
    fin_juego = False
    game_over = False

    x = ANCHO / 2
    y = ALTO / 2

    cambio_x = 0
    cambio_y = 0

    serpiente = []
    longitud = 1

    comida_x = round(random.randrange(0, ANCHO - tam_bloque) / 20.0) * 20
    comida_y = round(random.randrange(0, ALTO - tam_bloque) / 20.0) * 20

    while not fin_juego:

        while game_over:
            pantalla.fill(NEGRO)

            mensaje = fuente.render(
                "Perdiste. Presiona C para continuar o Q para salir",
                True,
                ROJO
            )

            pantalla.blit(mensaje, [20, ALTO / 2])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fin_juego = True
                    game_over = False

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fin_juego = True
                        game_over = False
                    if evento.key == pygame.K_c:
                        juego()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fin_juego = True

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    cambio_x = -tam_bloque
                    cambio_y = 0
                elif evento.key == pygame.K_RIGHT:
                    cambio_x = tam_bloque
                    cambio_y = 0
                elif evento.key == pygame.K_UP:
                    cambio_y = -tam_bloque
                    cambio_x = 0
                elif evento.key == pygame.K_DOWN:
                    cambio_y = tam_bloque
                    cambio_x = 0

        if x >= ANCHO or x < 0 or y >= ALTO or y < 0:
            game_over = True

        x += cambio_x
        y += cambio_y

        pantalla.fill(NEGRO)

        pygame.draw.rect(
            pantalla,
            ROJO,
            [comida_x, comida_y, tam_bloque, tam_bloque]
        )

        cabeza = []
        cabeza.append(x)
        cabeza.append(y)
        serpiente.append(cabeza)

        if len(serpiente) > longitud:
            del serpiente[0]

        for bloque in serpiente[:-1]:
            if bloque == cabeza:
                game_over = True

        dibujar_serpiente(tam_bloque, serpiente)
        mostrar_puntaje(longitud - 1)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, ANCHO - tam_bloque) / 20.0) * 20
            comida_y = round(random.randrange(0, ALTO - tam_bloque) / 20.0) * 20
            longitud += 1

        reloj.tick(velocidad)

    pygame.quit()

juego()
Algoritmo JuegoSerpiente
    Definir juegoActivo Como Logico
    Definir puntaje Como Entero
    
    // Inicialización de variables
    puntaje <- 0
    juegoActivo <- Verdadero
    
    // Llamadas a los subprocesos (¡Ya no darán error 106!)
    InicializarSerpiente()
    InicializarComida()
    
    Mientras juegoActivo = Verdadero Hacer
        
        LeerTecla() 
        ActualizarPosicion() 
        
        // Evaluamos las funciones que devuelven Verdadero/Falso
        Si ChocaConBorde() Entonces
            juegoActivo <- Falso
            Escribir "¡Game Over! Chocaste con la pared."
        Sino
            Si ChocaConCuerpo() Entonces
                juegoActivo <- Falso
                Escribir "¡Game Over! Te mordiste."
            Sino
                Si ComeComida() Entonces
                    puntaje <- puntaje + 1
                    GenerarNuevaComida()
                FinSi
                
                DibujarPantalla()
            FinSi
        FinSi
        
        Esperar 100 Milisegundos // Comando nativo de PSeInt para la velocidad
        
    FinMientras
    
    Escribir "Puntaje Final: ", puntaje
FinAlgoritmo

// =======================================================
//  AQUÍ DECLARAMOS LOS SUBPROCESOS PARA QUE PSeINT LOS RECONOZCA
// =======================================================
Subproceso InicializarSerpiente
    // Aquí iría la lógica para posicionar la serpiente
    Escribir "Serpiente lista..."
FinSubproceso

Subproceso InicializarComida
    // Aquí iría la lógica para colocar la primera comida
    Escribir "Comida lista..."
FinSubproceso

Subproceso LeerTecla
    // Lógica para capturar movimiento
FinSubproceso

Subproceso ActualizarPosicion
    // Lógica para mover coordenadas
FinSubproceso

Funcion choque <- ChocaConBorde
    Definir choque Como Logico
    choque <- Falso // Por defecto no choca
FinFuncion

Funcion choque <- ChocaConCuerpo
    Definir choque Como Logico
    choque <- Falso
FinFuncion

Funcion come <- ComeComida
    Definir come Como Logico
    come <- Falso
FinFuncion

Subproceso GenerarNuevaComida
    // Lógica para reubicar la comida
FinSubproceso

Subproceso DibujarPantalla
    // Lógica para "limpiar pantalla" y redibujar
    Borrar Pantalla
    Escribir "Moviendo la serpiente..."
FinSubproceso

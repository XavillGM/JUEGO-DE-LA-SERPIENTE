Algoritmo Sin_Titulo
    // Aquí va el flujo principal de tu juego (Menú, llamadas, etc.)
    Escribir "Iniciando juego simulado..."
    
    // Llamamos al subproceso de ejemplo pasando un puntaje de 15
    GameOver(15) 
    
FinAlgoritmo // <-- El FinAlgoritmo principal va AQUÍ, cerrando el bloque principal

// =======================================================
// LOS SUBPROCESOS VAN AFUERA DEL ALGORITMO PRINCIPAL
// =======================================================
Subproceso GameOver(puntaje)
    Definir tecla_usuario Como Caracter
    Definir opcion_valida Como Logico
    
    opcion_valida <- Falso
    
    // Mostrar Puntaje y opciones
    Escribir "=== ¡GAME OVER! ==="
    Escribir "Puntaje final: ", puntaje
    Escribir "C = Volver al Menú"
    Escribir "Q = Salir del juego"
    
    // Bucle para: "No -> Volver a leer tecla"
    Mientras opcion_valida = Falso Hacer
        
        // Leer Tecla
        Leer tecla_usuario
        
        // ¿Tecla = C? (Acepta mayúscula y minúscula)
        Si tecla_usuario = "C" o tecla_usuario = "c" Entonces
            opcion_valida <- Verdadero
            Escribir "Regresando al Menú..." 
            
        Sino
            // ¿Tecla = Q?
            Si tecla_usuario = "Q" o tecla_usuario = "q" Entonces
                opcion_valida <- Verdadero
                Escribir "Gracias por jugar. ¡Adiós!"
            Sino
                // No -> Volver a leer tecla (el bucle se repite)
                Escribir "Opción no válida. Presiona C para Menú o Q para Salir: "
            FinSi
        FinSi
        
    FinMientras
FinSubproceso // <-- Cierre correcto del subproceso
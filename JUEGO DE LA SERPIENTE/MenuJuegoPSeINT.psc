Algoritmo MenuJuego
		Definir opcion Como Caracter
		Definir velocidad Como Entero
		Definir salir Como Logico
		
		salir <- Falso
		
		Mientras salir = Falso Hacer
			// Mostrar Menú
			Escribir "--- MENÚ PRINCIPAL ---"
			Escribir "1. Nivel Fácil (Velocidad 10)"
			Escribir "2. Nivel Difícil (Velocidad 18)"
			Escribir "Q. Salir"
			Escribir "Selecciona una opción: "
			
			// Leer Opción
			Leer opcion
			
			// ¿Opción = 1?
			Si opcion = "1" Entonces
				velocidad <- 10
				Escribir "Iniciando juego... Velocidad establecida en ", velocidad
				// Aquí iría la llamada a la función/subproceso IrAJuego()
				
			Sino
				// ¿Opción = 2?
				Si opcion = "2" Entonces
					velocidad <- 18
					Escribir "Iniciando juego... Velocidad establecida en ", velocidad
					// Aquí iría la llamada a la función/subproceso IrAJuego()
					
				Sino
					// ¿Opción = Q?
					Si opcion = "Q" o opcion = "q" Entonces
						// Sí -> FIN
						salir <- Verdadero
						Escribir "Fin del programa."
					Sino
						// No -> Volver al Menú
						Escribir "Opción no válida. Inténtalo de nuevo."
					FinSi
				FinSi
			FinSi
		FinMientras
FinAlgoritmo

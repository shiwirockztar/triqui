import pyfiglet
import triquy as tr
introfile = "intro.txt"

# 1. Mostrar mensaje de bienvenida
tr.printIntro(introfile)


turn = tr.whoGoesFirst() # Indica quién tiene el turno para jugar, el usuario o la computadora.


while True:
    board = [" ", " ", " ", " ", " ", " " ," ", " ", " " ]
    tr.drawBoard(board) # 2. Crear el tablero
    print("\n")  # línea en blanco
    letterP = tr.inputPlayerLetter()[0] # 3. El usuario debe seleccionar la marca
    letterM = tr.inputPlayerLetter()[1] 
    print(turn,' va primero.') # 4. Quién va primero el usuario o la computadora?

    jugando = True # El juego ha iniciado
    victoria = False
    empate = False
    while jugando:

        if turn == 'Usuario': # 5. Turno del usuario

            tr.drawBoard(board) # a. Mostrar tablero
            print("\n")  # línea en blanco
            move = tr.getPlayerMove(board)# b. Pedir jugada al usuario
            print("\n")  # línea en blanco

            # c. Actualizar el tablero
            board = tr.makeMove(board, letterP, move)
            tr.drawBoard(board)

            victoria = tr.isWinner(board, letterP) # d. Verificar si el usuario ha ganado el juego.

            if victoria : #    Si si, mostrar tablero, mostrar mensaje de felicitación y terminar el juego.
                print("¡Felicidades! ¡Has ganado el juego!")
                mensaje = pyfiglet.figlet_format("¡VICTORIA!")
                print(mensaje)
                jugando = False
                continue

            empate = tr.isBoardFull(board) # e. Verificar si hay empate.
            if empate : #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.
                mensaje = pyfiglet.figlet_format("EMPATE")
                jugando = False
                continue
            # f. Si el usuario no ha ganado y no hay empate, la computadora
            #    toma el siguiente turno

            turn = 'Computadora'


        else: # 6. Turno de la computadora.

            move = tr.getComputerMove(board, letterM)# a. Computadora hace jugada.
            board = tr.makeMove(board, letterM, move)# b. Actualizar el tablero.
            print("move : ", move)
            print("board : ", board)
            print("victoria :", victoria)
            print("empate :", empate)  
            victoria = tr.isWinner(board, letterM)# c. Verificar si la computadora ha ganado el juego.
            
            if victoria : #    Si si, mostrar tablero, mostrar mensaje indicando al usuario que ha perdido y terminar el juego.
                print("¡Lo siento! ¡Vuelve a intentarlo!")
                mensaje = pyfiglet.figlet_format("¡DERROTA!")
                print(mensaje)
                jugando = False
                continue

            empate = tr.isBoardFull(board)# d. Verificar si hay empate.
            if empate : #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.
                mensaje = pyfiglet.figlet_format("EMPATE")
                jugando = False
                continue

            # f. Si la computadora no ha ganado y no hay empate, el usuario
            #    toma el siguiente turno.

            turn = 'Usuario'

    jugando = input("Quieres seguir jugando : (Y|N) : ").lower() # 7. Preguntar si el usuario quiere jugar una vez mas
    if jugando in ["n", "no"]: #    Si no, finalizar el programa.
      break
    else: #    Si si, reiniciar el juego.
      continue  
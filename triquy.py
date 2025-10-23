import random
#import numpy as np

def printIntro(introFile):
    '''
        Firma:
            (string) -> ()

        Sinopsis:
            función que imprime el contenido de un archivo en pantalla, en este
    		caso, el mensaje de bienvenida al juego

        Entradas y salidas:
            - inputFile: Nombre del archivo que contiene la presentación del juego
            - returns: None, solo imprime el archivo leído en pantalla

        Ejemplos de uso:

            >>> printIntro("intro.txt")

            ████████╗██████╗ ██╗ ██████╗ ██╗   ██╗██╗
            ╚══██╔══╝██╔══██╗██║██╔═══██╗██║   ██║██║
               ██║   ██████╔╝██║██║   ██║██║   ██║██║
               ██║   ██╔══██╗██║██║▄▄ ██║██║   ██║██║
               ██║   ██║  ██║██║╚██████╔╝╚██████╔╝██║
               ╚═╝   ╚═╝  ╚═╝╚═╝ ╚══▀▀═╝  ╚═════╝ ╚═╝
        '''

    with open(introFile, 'r') as f:
        print(f.read())

    pass

def whoGoesFirst():
    # Esta función escoge de forma aleatoria quien inicial el juego.

    # Retorna el string "Usuario" si el usuario inicia el juego o
    # el string "Computadora" si la computadora inicia el juego.

    turno = random.choice(['Usuario', 'Computadora'])
    print("Empieza el juego: ",turno)
    return turno

def drawBoard(board):
    # Esta función imprime el tablero en la consola
    # Argumentos:
    # Board: Lista de strings que representa el estado del tablero

    print()
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---+---+---')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---+---+---')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print()

simbolo = ['X', 'O']
def inputPlayerLetter():
    # Esta función le permite escoger al usuario entre la letra "X" y la letra "O".

    # retorna una lista de strings donde la letra escogida por el usuario
    # ocupa la primera posición y la letra que le corresponde a la computadora
    # ocupa la segunda posición.

   
    #seleccion = input("Selecciona la marca que usarás (X o O): ")
    seleccion = 'O'
    if simbolo[0] != seleccion.upper():
            simbolo.reverse()

    print("Jugaras con la : ",simbolo[0])
    return simbolo


def isSpaceFree(board, move):
    # Esta función verifica si hay una casilla vacía en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # move: Es el número de la casilla que se desea verificar.

    # Esta función debe retornar el valor lógico True, si la casilla está vacía
    # en caso contrario, debe retornar el valor lógico False.

    index = int(move) - 1

    if board[index] != " ":
        print("Esa casilla ya fue jugada. Elige otra.")
        return False
    else:
        return True


  

def getPlayerMove(board):
    # Esta función le pide al usuario que ingrese el número de la casilla
    # que quiere marcar.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función retorna el número de la casilla seleccionada por el usuario.


    Board = ["1", "2", "3", "4", "5", "6" ,"7", "8", "9" ]
    drawBoard(Board)
    
    while True:
        casilla = input("Selecciona la casilla a jugar (1-9): ")

        if casilla not in "123456789":
            print("Entrada inválida. Debes elegir un número del 1 al 9.")
        
        else:
          index = int(casilla) - 1
          vacio = isSpaceFree(board, casilla)  
          if vacio :
              return index+1  # Casilla válida: se devuelve y se sale del bucle

def makeMove(board, letter, move):
    # Esta función actualiza el estado del tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # letter: Es la marca que se desea poner en el tablero ("X" o "O").
    # move: Es el número de la casilla donde se desea poner la marca.
    
    board[move - 1] = letter
    return board

def isWinner(board, letter):
    # Esta función debe verificar si hay una jugada ganadora en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # letter: La marca que se desea verificar ("X" o "O").

    # Esta función debe retornar el valor lógico True, si hay una jugada ganadora o
    # debe retornar el valor lógico False, si no hay una jugada ganadora.

     # Combinaciones ganadoras (filas, columnas, diagonales)
    triqui = [
        [0, 1, 2],  # Fila 1
        [3, 4, 5],  # Fila 2
        [6, 7, 8],  # Fila 3
        [0, 3, 6],  # Columna 1
        [1, 4, 7],  # Columna 2
        [2, 5, 8],  # Columna 3
        [0, 4, 8],  # Diagonal 1
        [2, 4, 6]   # Diagonal 2
    ]

    # Verificamos si alguna combinación está llena con la misma letra
    for combinacion in triqui:
        if board[combinacion[0]] == board[combinacion[1]] == board[combinacion[2]] == letter:
            return True

    return False

def isBoardFull(board):
    # Esta función verifica si el tablero está lleno.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función debe retorna el valor lógico True, si el tablero está lleno.
    # En caso contrario debe retornar el valor lógico False.

    return board.count(' ') == 0

def getComputerMove(board, computerLetter):
    # Esta función implementa la estrategia de juego de la computadora.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # computerLetter: La marca que está usando la computadora.

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'


    # 1. Verificar si la computadora puede ganar...
    for i in range(9):
        if board[i] == ' ':
            board_copy = board.copy()
            board_copy = makeMove(board_copy, computerLetter, i+1)
            if isWinner(board_copy, computerLetter):
                return i+1

    # 2. Si no, verificar si el usuario puede ganar en la siguiente jugada, si si, bloquear esta jugada...
    for i in range(9):
        if board[i] == ' ':
            board_copy = board.copy()
            board_copy = makeMove(board_copy, playerLetter, i+1)
            if isWinner(board_copy, playerLetter):
                return i+1

    # 3. Si no, tratar de poner una marca en alguna de las esquinas, si alguna está vacía...
    for i in [0, 2, 6, 8]:
        if board[i] == ' ':
            return i+1

    # 4. Si no, tratar de marcar la casilla del centro, si esta está vacía...
    if board[4] == ' ':
        return 5

    # 5. Si no, tratar de poner una marca en alguna de las casillas de los lados...
    for i in [1, 3, 5, 7]:
        if board[i] == ' ':
            return i+1

    pass
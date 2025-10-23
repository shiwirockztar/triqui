# Triqui (Tres en raya) - Juego en Python

Este repositorio contiene una implementación simple del juego "Triqui" (Tres en raya / Tic-Tac-Toe) en Python.

## Descripción

El juego permite jugar una partida entre un usuario y la computadora (IA básica). El programa muestra un tablero 3x3 en la consola, permite al usuario escoger su marca (X u O), y alterna turnos entre el usuario y la computadora. La computadora tiene una estrategia básica: intenta ganar, bloquea al jugador si puede ganar en la siguiente jugada, busca esquinas, centro y luego lados.

Archivos principales:

- `main.py`: Lógica principal de ejecución y flujo de juego.
- `triquy.py`: Funciones auxiliares del juego (dibujar tablero, validar movimientos, lógica de la IA, comprobaciones de victoria/empate, etc.).
- `intro.txt`: Texto de bienvenida mostrado al iniciar el juego.
- `requirements.txt`: Dependencias del proyecto (`pyfiglet` para banners ASCII).

## Requisitos

- Python 3.11 (se ha probado con Python 3.11).
- Paquetes listados en `requirements.txt`.

## Instalación

En Windows (cmd):

```cmd
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

En GitHub Codespaces o cualquier contenedor DevContainer, el archivo `.devcontainer/devcontainer.json` está configurado para ejecutar `pip install -r requirements.txt` automáticamente al crear el contenedor.

## Uso

Ejecuta el juego desde la raíz del proyecto:

```cmd
python main.py
```

Flujo básico:
- Al iniciar se muestra el mensaje de introducción (desde `intro.txt`).
- El usuario elige su marca (X u O).
- Se decide aleatoriamente quién inicia la partida.
- El tablero se muestra en la consola; el usuario introduce un número (1-9) para jugar en la casilla correspondiente.
- El juego detecta victoria, derrota o empate y muestra un banner ASCII usando `pyfiglet`.
- Al terminar la partida se pregunta si quieres jugar otra vez.

## Notas

- Si ves problemas con la codificación al leer `intro.txt` en sistemas Windows, puedes convertir `intro.txt` a UTF-8 o ajustar la función `printIntro` en `triquy.py` para abrir el archivo con `encoding='utf-8'` y manejar un fallback.
- La IA es deliberadamente simple para mantener el código didáctico.

## Contribuciones

Si quieres mejorar la IA, agregar tests automatizados o mejorar la interfaz, crea un fork y un pull request. Agradezco correcciones en el manejo de entradas y la robustez del juego.

---

¡Disfruta jugando!

## Trabajando con ramas (Git)

Si quieres trabajar en una copia del proyecto sin tocar la rama principal, puedes crear una nueva rama y cambiarte a ella con:

```bash
git checkout -b readme
```

Esto hace dos cosas:

- Crea una nueva rama llamada `readme`.
- Te cambia automáticamente a esa rama, por lo que cualquier commit que hagas irá a `readme`.

Cuando quieras volver a la rama principal (`master`), usa:

```bash
git checkout master
```

Esto cambia tu copia de trabajo a la rama `master`.

Nota: en muchos repositorios modernos la rama por defecto se llama `main` en vez de `master`. Si tu repositorio usa `main`, sustituye `master` por `main` en los comandos anteriores.
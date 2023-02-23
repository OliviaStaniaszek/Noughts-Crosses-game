from cx_Freeze import setup, Executable

files = ["game.py", "GUI.py", "main.py", "menu.py", "tic-tac-toe.ico", "fonts/Kreon-Medium.ttf", "fonts/Marmelad-Regular.ttf", "fonts/Numans-Regular.ttf", "imgs/darkbkg.png", "imgs/lightbkg.png"]

target = Executable(
    script="game.py",
    base="Win32GUI",
    icon="tic-tac-toe.ico"
)

setup(
    name = "Noughts and Crosses",
    version = "1.0",
    description = "",
    author = "Olivia Staniaszek",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
)
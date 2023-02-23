import os


def QArgv(arguments: list, menu):
    if len(arguments) >= 2:
        if os.path.exists(arguments[1]):
            menu.openFile(arguments[1])

import json
import os
import sys

from . import configurate

from PySide6.QtWidgets import QApplication, QWidget, QErrorMessage


class QAbstractApplication(QApplication):
    def __init__(self, init: str, *args, **kwargs):
        super(QAbstractApplication, self).__init__(*args, **kwargs)

        self._init = init
        self._widgets = []
        self._bar = None

        with open(init, mode="r", encoding="utf-8") as file:
            self._settings = json.load(file)
            self._langs = configurate.LANGS[self._settings["interface"]["lang"][-3:-1]]

        self.setStyleSheet(configurate.THEMES[self._settings["interface"]["theme"]].QApplication)

    def language(self):
        return self._langs

    def settings(self):
        return self._settings

    def theme(self):
        return "dark" if \
            configurate.THEMES[self._settings["interface"]["theme"]] == configurate.QDarkStyleSheet() else "light"

    def addWidget(self, widget):
        self._widgets.append(widget)

    def setStatusBar(self, widget: QWidget):
        self._bar = widget

    def updateStatusBar(self, text: str):
        if self._settings["general"]["status-bar"]:
            self._bar.setText(text)

    def applySettings(self, settings: dict):
        with open(self._init, mode="w", encoding="utf-8") as file:
            json.dump(settings, file, ensure_ascii=False, indent=2)

        self._settings = settings
        self._langs = configurate.LANGS[settings["interface"]["lang"][-3:-1]]
        self._bar.setText("")

        self.setStyleSheet(configurate.THEMES[settings["interface"]["theme"]].QApplication)

        for widget in self._widgets:
            widget.applySettings()

    def plugin(self, *plugin):
        import csv
        import json
        import os
        import subprocess
        import sys
        import threading
        import webbrowser

        import PySide6

        for path in os.listdir("./plugins"):
            if path[0] == "_":
                continue

            if os.path.exists(f"./plugins/{path}/main.py"):
                with open(f"./plugins/{path}/main.py", mode="r", encoding="utf-8") as _plugin:
                    try:
                        exec(f"sys.path.append(r'{os.path.abspath(f'./plugins/{path}')}')\n\n{_plugin.read()}")
                    except Exception as error:
                        QErrorMessage(self._widgets[0]).showMessage(self.language()["plugin_err"].format(error))

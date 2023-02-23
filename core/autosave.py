import sqlite3

from threading import Timer

from .ui.widgets import QAbstractTabWidget, QAbstractTextEdit, QAbstractApplication


class QAutoSave(Timer):
    def __init__(self, app: QAbstractApplication, tabs: QAbstractTabWidget, path: str, interval: int = 1):
        super(QAutoSave, self).__init__(interval, self._save)

        self._path = path

        interval = app.settings()["other"]["backup"]
        if interval != "-":
            self.interval = int(interval[:-1])
            self._enable = True
        else:
            self._enable = False

        self._app = app
        self._tabs = tabs

        self._extensionsR = {"html": self._readHtml}
        self._extensionsS = {"html": self._saveHtml}

    def addRestoreExtension(self, extension: str, reader):
        self._extensionsR[extension] = reader

    def addSaveExtension(self, extension: str, dumper):
        self._extensionsS[extension] = dumper

    def start(self):
        self._app.aboutToQuit.connect(self._quit)
        self._app.addWidget(self)

        for title, text in self._restore(self._path):
            widget = QAbstractTextEdit(self._app)

            if title.split("/")[-1].split(".")[-1] in self._extensionsR:
                self._extensionsR[title.split("/")[-1].split(".")[-1]](
                    text.replace("\\n", "\n"), widget, title.split("/")[-1].split(".")[-1]
                )
            else:
                widget.setPlainText(text.replace("\\n", "\n"))

            self._tabs.addTab(widget, title.replace("\\", "/").split("/")[-1], title)

        return super(QAutoSave, self).start()

    def run(self):
        while not self.finished.wait(self.interval) and self._enable:
            self.function(*self.args, **self.kwargs)

    def applySettings(self):
        interval = self._app.settings()["other"]["backup"]
        if interval != "-":
            self.interval = int(interval[:-1])
            self._enable = True
        else:
            self._enable = False

    def _quit(self):
        self._save()
        self.cancel()

    def _save(self):
        data = []
        for index in range(self._tabs.count()):
            widget = self._tabs.widget(index)
            if not hasattr(widget, "toPlainText") or widget.isReadOnly():
                continue
            filename = self._tabs.keyAt(widget)
            extension = filename.split(".")[-1]

            if extension in self._extensionsS:
                data.append((filename, self._extensionsS[extension](widget, extension)))
            else:
                data.append((filename, widget.toPlainText()))

        self._backup(data, self._path)

    @staticmethod
    def _readHtml(text: str, widget: QAbstractTextEdit, _):
        return widget.setHtml(text)

    @staticmethod
    def _saveHtml(widget: QAbstractTextEdit, _):
        return widget.toHtml()

    @staticmethod
    def _backup(data: list[tuple[str, str]], file: str = r"autosave.db"):
        db = sqlite3.connect(file)

        db.execute("CREATE TABLE IF NOT EXISTS saves (path STRING, [data] BLOB)")
        db.execute("CREATE UNIQUE INDEX IF NOT EXISTS index_title ON saves (path)")
        db.execute("DELETE FROM saves")
        if data:
            for chunk in data:
                db.execute("INSERT OR REPLACE INTO saves (path, data)\nVALUES (?, ?)", chunk)

        db.commit()

    @staticmethod
    def _restore(file: str = r"autosave.db"):
        db = sqlite3.connect(file)

        db.execute("CREATE TABLE IF NOT EXISTS saves (path STRING, [data] BLOB)")
        db.execute("CREATE UNIQUE INDEX IF NOT EXISTS index_title ON saves (path)")
        db.commit()

        return db.execute("SELECT * FROM saves").fetchall()

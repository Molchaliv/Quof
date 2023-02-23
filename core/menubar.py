import json
import os

from .ui.widgets import (
    QAbstractApplication, QAbstractMenu, QAbstractTabWidget, QAbstractTextEdit
)
from .find import QFindDialog
from .settings import QSettings

from PySide6.QtGui import QFont, Qt
from PySide6.QtWidgets import QFileDialog, QErrorMessage
from PySide6.QtPrintSupport import QPrintDialog, QPrinter


class QFileMenu(QAbstractMenu):
    def __init__(self, app: QAbstractApplication, tabs: QAbstractTabWidget, *args, **kwargs):
        super(QFileMenu, self).__init__(*args, **kwargs)

        self._app = app
        self._tabs = tabs
        self._files = {}
        self._extensionsO = {"html": self._readHtml}
        self._extensionsR = {}

        self._app.addWidget(self)
        self.aboutToShow.connect(self.load)

        self.applySettings()

    def addOpenExtension(self, extension: str, reader):
        self._extensionsO[extension] = reader

    def addSaveExtension(self, extension: str, dumper):
        self._extensionsR[extension] = dumper

    def applySettings(self):
        self.setTitle(self._app.language()["file"])

    def load(self):
        self.clear()

        self.addAction(self._app.language()["new"], "Ctrl+N", self._new)
        self.addAction(self._app.language()["open"], "Ctrl+O", self._open)
        self.addAction(self._app.language()["save"], "Ctrl+S", self._save).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))
        self.addAction(self._app.language()["save_as"], "Ctrl+Shift+S", self._save_as).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))

        self.addSeparator()

        self.addAction(self._app.language()["print"], self._print).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))
        self.addAction(self._app.language()["settings"], self._settings)

        self.addSeparator()

        self.addAction(self._app.language()["exit"], "Ctrl+E", self._exit)

    def _new(self):
        self._tabs.addTab(
            QAbstractTextEdit(self._app),
            f"{self._app.language()['untitled']} {self._tabs.currentIndex() + 2}",
            f"{self._app.language()['untitled']} {self._tabs.currentIndex() + 2}"
        )

    def _open(self):
        filename = QFileDialog.getOpenFileName(
            self, self._app.language()["open_file"], "", self._app.language()["text_files"])[0]

        if filename:
            try:
                self.openFile(filename)
            except Exception as error:
                QErrorMessage(self._tabs.parent()).showMessage(
                    self._app.language()["read_err"].format(error))

    def _save(self):
        if os.path.exists(self._tabs.currentKey()):
            filename = self._tabs.currentKey()
            extension = filename.split(".")[-1]

            with open(filename, mode="w", encoding="utf-8") as file:
                if extension == "html":
                    file.write(self._tabs.widgetAt(filename).toHtml())
                else:
                    file.write(self._tabs.widgetAt(filename).toPlainText())
        else:
            self._save_as()

    def _save_as(self):
        filename = QFileDialog.getSaveFileName(
            self, self._app.language()["save_file"], self._app.language()["untitled"],
            self._app.language()["text_files"])[0]

        if filename:
            self._files[self._tabs.currentWidget()] = filename
            self._tabs.addKey(filename)
            self._tabs.setTabText(self._tabs.currentIndex(), filename.split("/")[-1])

            extension = filename.split(".")[-1]

            with open(filename, mode="w", encoding="utf-8") as file:
                if extension == "html":
                    file.write(self._tabs.currentWidget().toHtml())
                else:
                    file.write(self._tabs.currentWidget().toPlainText())

            if extension in self._extensionsR:
                self._extensionsR[extension](self._tabs.currentWidget(), extension)

    def _print(self):
        printer = QPrinter(QPrinter.HighResolution)

        if not QPrintDialog(printer, self).exec():
            return

        self._tabs.currentWidget().print_(printer)

    def _settings(self):
        self._tabs.addTab(QSettings(self._app), self._app.language()["settings"], ":settings:")

    def _exit(self):
        self._app.exit()

    def openFile(self, filename):
        extension = filename.split(".")[-1]
        widget = QAbstractTextEdit(self._app)

        if extension in self._extensionsO:
            self._extensionsO[extension](filename, widget, extension)
        else:
            self._readPlaiText(filename, widget, extension)

        self._files[self._tabs.addTab(widget, os.path.normpath(filename).split("\\")[-1], filename)] = filename

    @staticmethod
    def _readHtml(filename: str, widget: QAbstractTextEdit, _):
        with open(filename, mode="r", encoding="utf-8") as file:
            widget.setHtml(file.read())

    @staticmethod
    def _readPlaiText(filename: str, widget: QAbstractTextEdit, _):
        with open(filename, mode="r", encoding="utf-8") as file:
            widget.setPlainText(file.read())


class QEditMenu(QAbstractMenu):
    def __init__(self, app: QAbstractApplication, tabs: QAbstractTabWidget, *args, **kwargs):
        super(QEditMenu, self).__init__(*args, **kwargs)

        self._app = app
        self._tabs = tabs

        self._app.addWidget(self)
        self.aboutToShow.connect(self.load)

        self.applySettings()

    def applySettings(self):
        self.setTitle(self._app.language()["edit"])

    def load(self):
        self.clear()

        self.addAction(self._app.language()["undo"], "Ctrl+Z", self._undo).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))
        self.addAction(self._app.language()["redo"], "Ctrl+Y", self._redo).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))

        self.addSeparator()

        self.addAction(self._app.language()["cut"], "Ctrl+X", self._cut).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))
        self.addAction(self._app.language()["copy"], "Ctrl+С", self._copy).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))
        self.addAction(self._app.language()["paste"], "Ctrl+V", self._paste).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))
        self.addAction(self._app.language()["del"], self._delete).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))

        self.addSeparator()

        self.addAction(self._app.language()["select_all"], "Ctrl+A", self._select_all).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))

        self.addSeparator()

        self.addAction(self._app.language()["find"], "Ctrl+F", self._find).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))

    def _undo(self):
        self._tabs.currentWidget().undo()

    def _redo(self):
        self._tabs.currentWidget().redo()

    def _cut(self):
        self._tabs.currentWidget().cut()

    def _copy(self):
        self._tabs.currentWidget().copy()

    def _paste(self):
        self._tabs.currentWidget().paste()

    def _delete(self):
        self._tabs.currentWidget().textCursor().removeSelectedText()

    def _select_all(self):
        self._tabs.currentWidget().selectAll()

    def _find(self):
        QFindDialog(self._app, self._tabs.currentWidget(), self._tabs.parent()).exec()


class QStyleMenu(QAbstractMenu):
    def __init__(self, app: QAbstractApplication, tabs: QAbstractTabWidget, *args, **kwargs):
        super(QStyleMenu, self).__init__(*args, **kwargs)

        self._app = app
        self._tabs = tabs

        self._app.addWidget(self)
        self.aboutToShow.connect(self.load)

        self.applySettings()

    def applySettings(self):
        self.setTitle(self._app.language()["style"])

    def load(self):
        self.clear()

        self.addAction(self._app.language()["bold"], "Ctrl+Shift+1", self._bold).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))
        self.addAction(self._app.language()["italic"], "Ctrl+Shift+2", self._italic).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))
        self.addAction(self._app.language()["underline"], "Ctrl+Shift+3", self._underline).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))

        self.addSeparator()

        self.addAction(self._app.language()["left"], "Ctrl+Shift+4", self._left).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))
        self.addAction(self._app.language()["right"], "Ctrl+Shift+5", self._right).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))
        self.addAction(self._app.language()["center"], "Ctrl+Shift+6", self._center).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))
        self.addAction(self._app.language()["both"], "Ctrl+Shift+7", self._both).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))

        self.addSeparator()

        self.addAction(self._app.language()["clear_style"], "Ctrl+Shift+8", self._clear_style).setEnabled(
            hasattr(self._tabs.currentWidget(), "toPlainText"))

    def _bold(self):
        if self._tabs.currentWidget().fontWeight() != QFont.Bold:
            self._tabs.currentWidget().setFontWeight(QFont.Bold)
        else:
            self._tabs.currentWidget().setFontWeight(QFont.Normal)

    def _italic(self):
        if not self._tabs.currentWidget().fontItalic():
            self._tabs.currentWidget().setFontItalic(True)
        else:
            self._tabs.currentWidget().setFontItalic(False)

    def _underline(self):
        if not self._tabs.currentWidget().fontUnderline():
            self._tabs.currentWidget().setFontUnderline(True)
        else:
            self._tabs.currentWidget().setFontUnderline(False)

    def _right(self):
        self._tabs.currentWidget().setAlignment(Qt.AlignRight)

    def _left(self):
        self._tabs.currentWidget().setAlignment(Qt.AlignLeft)

    def _center(self):
        self._tabs.currentWidget().setAlignment(Qt.AlignCenter)

    def _both(self):
        self._tabs.currentWidget().setAlignment(Qt.AlignJustify)

    def _clear_style(self):
        self._tabs.currentWidget().setPlainText(self._tabs.currentWidget().toPlainText())


class QHelpMenu(QAbstractMenu):
    def __init__(self, app: QAbstractApplication, tabs: QAbstractTabWidget, *args, **kwargs):
        super(QHelpMenu, self).__init__(*args, **kwargs)

        self._app = app
        self._tabs = tabs

        self._app.addWidget(self)
        self.aboutToShow.connect(self.load)

        self.applySettings()

    def applySettings(self):
        self.setTitle(self._app.language()["help"])

    def load(self):
        self.clear()

        self.addAction(self._app.language()["about"], self._about)

    def _about(self):
        widget = QAbstractTextEdit(self._app)
        widget.setReadOnly(True)
        widget.setHtml(open(r".\res\help.html", mode="r", encoding="utf-8").read())

        self._tabs.addTab(widget, self._app.language()["about"], ":about:")

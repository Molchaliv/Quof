import re

from .ui.widgets import QAbstractApplication, QAbstractTextEdit

from PySide6.QtCore import Qt
from PySide6.QtGui import QResizeEvent, QTextCursor
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QCheckBox, QListWidget, QDialog, QWidget


class QFindDialog(QDialog):
    def __init__(self, app: QAbstractApplication, text: QWidget, *args, **kwargs):
        super(QFindDialog, self).__init__(*args, **kwargs)

        self._app = app
        self._text: QAbstractTextEdit = text

        self._find_lbl = QLabel(app.language()["find"], self)
        self._find_set = QLineEdit(self)

        self._replace_lbl = QLabel(self._app.language()["replace"], self)
        self._replace_set = QLineEdit(self)

        self._match_case = QCheckBox(self._app.language()["match_case"], self)

        self._find_btn = QPushButton(self._app.language()["find"], self)
        self._replace_btn = QPushButton(self._app.language()["replace"], self)

        self._find_list = QListWidget(self)

        self._back_btn = QPushButton(self._app.language()["back"], self)
        self._next_btn = QPushButton(self._app.language()["next"], self)

        self.ui()

    def ui(self):
        self.setWindowTitle(f"{self._app.language()['find']} & {self._app.language()['replace']}")
        self.setMinimumSize(290, 350)

        self._find_lbl.move(20, 10)
        self._find_set.move(10, 35)
        self._find_set.setContextMenuPolicy(Qt.NoContextMenu)

        self._replace_lbl.move(20, 70)
        self._replace_set.move(10, 95)
        self._replace_set.setContextMenuPolicy(Qt.NoContextMenu)

        self._match_case.move(20, 135)

        self._find_btn.resize(100, 30)
        self._find_btn.clicked.connect(self.findText)
        self._replace_btn.resize(100, 30)
        self._replace_btn.clicked.connect(self.replaceText)

        self._find_list.move(10, 180)
        self._find_list.currentItemChanged.connect(self.selectText)

        self._back_btn.resize(100, 30)
        self._back_btn.setShortcut(Qt.Key.Key_Left)
        self._back_btn.clicked.connect(self.previousItem)
        self._next_btn.resize(100, 30)
        self._next_btn.setShortcut(Qt.Key.Key_Right)
        self._next_btn.clicked.connect(self.nextItem)

    def findText(self):
        self._find_list.clear()
        if self._match_case.isChecked():
            for word in re.finditer(self._find_set.text(), self._text.toPlainText()):
                self._find_list.addItem(f"{self._find_set.text()} - {word.start()}:{word.end()}")
        else:
            for word in re.finditer(self._find_set.text().lower(), self._text.toPlainText().lower()):
                self._find_list.addItem(f"{self._find_set.text()} - {word.start()}:{word.end()}")

    def replaceText(self):
        self._find_list.clear()
        self._text.setText(
            self._text.toPlainText().replace(self._find_set.text(), self._replace_set.text()))

        for word in re.finditer(self._replace_set.text(), self._text.toPlainText()):
            self._find_list.addItem(f"{self._replace_set.text()} - {word.start()}:{word.end()}")

    def selectText(self, item):
        start, end = map(int, item.text().split(" - ")[-1].split(":"))
        cursor = self._text.textCursor()

        cursor.setPosition(start)
        cursor.setPosition(end, QTextCursor.KeepAnchor)

        self._text.setTextCursor(cursor)

    def nextItem(self):
        if self._find_list.currentRow() >= self._find_list.count() - 1:
            self._find_list.setCurrentRow(0)
        else:
            self._find_list.setCurrentRow(self._find_list.currentRow() + 1)

    def previousItem(self):
        if self._find_list.currentRow() <= 0:
            self._find_list.setCurrentRow(self._find_list.count() - 1)
        else:
            self._find_list.setCurrentRow(self._find_list.currentRow() - 1)

    def resizeEvent(self, event: QResizeEvent):
        if event.size().width() <= 400:
            self._find_set.resize(event.size().width() - 140, 30)
            self._replace_set.resize(event.size().width() - 140, 30)

        self._find_btn.move(event.size().width() - 110, 35)
        self._replace_btn.move(event.size().width() - 110, 95)

        self._find_list.resize(event.size().width() - 20, event.size().height() - 240)

        self._back_btn.move(event.size().width() - 220, event.size().height() - 40)
        self._next_btn.move(event.size().width() - 110, event.size().height() - 40)

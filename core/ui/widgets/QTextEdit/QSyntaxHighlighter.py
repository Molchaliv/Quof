import enchant
import re

from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QTextCharFormat, QTextFormat, QColor, QFont, QAction, QTextCursor, QSyntaxHighlighter
from PySide6.QtWidgets import QTextEdit, QFrame


def find(text: str, pos: int):
    index = 0
    for word in re.split(r"(\W+)", text):
        if "_" in word:
            for chunk in word.split("_"):
                if index <= pos < index + len(chunk):
                    return chunk, index, len(chunk)
                index += len(chunk) + 1
            continue

        if index <= pos < index + len(word):
            return word, index, len(word)
        index += len(word)

    return None, -1, 0


class QSpellingHighlighter(QSyntaxHighlighter):
    def __init__(self, app, parent: QTextEdit, language: str = "en_US"):
        super(QSpellingHighlighter, self).__init__(parent.document())

        self._app = app
        self._enabled = True
        self._textEdit = parent
        self._baseDict = enchant.Dict("en_US")
        self._wordDict = enchant.Dict(language)

        self._textEdit.setContextMenuPolicy(Qt.CustomContextMenu)
        self._textEdit.customContextMenuRequested.connect(self.contextMenu)

    def enabled(self):
        return self._enabled

    def setEnabled(self, enabled: bool):
        self._enabled = enabled

    def highlightBlock(self, text: str):
        if not text or not self._enabled:
            return

        formatter = QTextCharFormat()
        formatter.setFontHintingPreference(QFont.HintingPreference.PreferNoHinting)
        formatter.setUnderlineColor(QColor(255, 0, 0))
        formatter.setUnderlineStyle(
            QTextCharFormat.SpellCheckUnderline
        )

        index = 0
        for word in re.split(r"(\W+)", text):
            if "_" in word:
                for chunk in word.split("_"):
                    if re.match(r"\w", chunk) and not (self._wordDict.check(chunk) or self._baseDict.check(chunk)):
                        self.setFormat(index, len(chunk), formatter)
                    index += len(chunk) + 1
                continue

            if re.match(r"\w", word) and not (self._wordDict.check(word) or self._baseDict.check(word)):
                self.setFormat(index, len(word), formatter)
            index += len(word)

    def contextMenu(self, point: QPoint):
        cursor = self._textEdit.textCursor()

        if not cursor.hasSelection():
            word = find(self._textEdit.toPlainText(), cursor.position())[0]
        else:
            word = cursor.selection().toPlainText()

        menu = self._textEdit.createStandardContextMenu()
        menu.clearStateActions()

        if word:
            spells = self._wordDict.suggest(word)
            if not spells:
                spells = self._baseDict.suggest(word)

            if not spells:
                menu.addStateAction(None)

            if not sum([self._wordDict.check(word), self._baseDict.check(word)]):
                for spell in spells:
                    act = QAction(spell, self)
                    act.triggered.connect(lambda __b=None, __r=spell: self.replaceWord(__r))

                    menu.addStateAction(act)

                add = QAction(self._app.language()["add_to_dict"], self)
                add.triggered.connect(lambda __b=None: self.addWord(word))

                menu.addStateSeparator()
                menu.addStateAction(add)
                menu.addStateSeparator()
        menu.exec(self._textEdit.mapToGlobal(point))

    def replaceWord(self, replace: str):
        cursor = self._textEdit.textCursor()

        word, index, length = find(self._textEdit.toPlainText(), cursor.position())

        cursor.beginEditBlock()
        cursor.setPosition(index)
        cursor.setPosition(index + length, QTextCursor.KeepAnchor)
        cursor.removeSelectedText()
        cursor.insertText(replace)
        cursor.endEditBlock()

    def addWord(self, add: str):
        self._wordDict.add(add)

        cursor = self._textEdit.textCursor()
        cursor.insertText(f"{cursor.selectedText()} ")
        cursor.deletePreviousChar()

import webbrowser
import pyperclip

from ..QMenu import QAbstractMenu
from .QSyntaxHighlighter import QSpellingHighlighter

from textblob.translate import Translator

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QIcon, QTextOption, QWheelEvent, QDragEnterEvent, QDropEvent, QAction, QResizeEvent, \
    QTextCursor, QTextFormat, QColor
from PySide6.QtWidgets import QTextEdit, QPushButton, QDialog, QComboBox, QGraphicsBlurEffect, QLabel


class QAbstractTranslateWindow(QDialog):
    def __init__(self, app, text: str, *args, **kwargs):
        super(QAbstractTranslateWindow, self).__init__(*args, **kwargs)

        self._app = app
        self._text = text

        self._langs = QComboBox(self)
        self._output = QTextEdit(self)

        self._copy = QPushButton(app.language()["copy_all"], self)
        self._translate = QPushButton(app.language()["translate"], self)

        self.ui()

    def ui(self):
        self.setWindowTitle(self._app.language()["translate"])
        self.setMinimumSize(500, 400)

        self._langs.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        self._langs.view().window().setAttribute(Qt.WA_TranslucentBackground)
        self._langs.addItems(
            ["Afrikaans (af)", "Беларуская (be)", "Български (bg)", "বাংলা (bn)", "Català (ca)", "Čeština (cs)",
             "Dansk (da)", "Deutsch (de)", "Ελληνικά (el)", "English (en)", "Español (es)", "Eesti keel (et)",
             "Suomi (fi)", "Français (fr)", "ગુજરાતી (gu)", "हिन्दी (hi)", "Hrvatski (hr)", "Magyar (hu)", "Հայ (hy)",
             "Bahasa Indonesia (id)", "Íslenska (is)", "Italiano (it)", "日本語 (ja)", "ភាសាខ្មែរ (km)", "ಕನ್ನಡ (kn)",
             "한국어 (ko)", "ລາວ (lo)", "Lietuvių (lt)", "Latviešu (lv)", "Македонски (mk)", "മലയാളം (ml)", "मराठी (mr)",
             "Bahasa Melayu (ms)", "नेपाली (ne)", "Nederlands (nl)", "Norsk (no)", "ਪੰਜਾਬੀ (pa)", "Polski (pl)",
             "Português (pt)", "Română (ro)", "Русский (ru)", "Slovenčina (sk)", "Slovenščina (sl)", "Shqip (sq)",
             "Српски (sr)", "Svenska (sv)", "தமிழ் (ta)", "తెలుగు (te)", "ไทย (th)", "Filipino (tl)", "Türkçe (tr)",
             "Українська (uk)", "Tiếng Việt (vi)", "Yiddish (yi)", "普通话 (zh)"]
        )
        self._langs.resize(150, 30)
        self._langs.move(10, 10)

        self._output.setReadOnly(True)
        self._output.setContextMenuPolicy(Qt.NoContextMenu)
        self._output.move(0, 50)

        self._copy.clicked.connect(self.copy_all)
        self._copy.resize(120, 30)

        self._translate.clicked.connect(self.translate)
        self._translate.resize(120, 30)

    def copy_all(self):
        pyperclip.copy(self._output.toPlainText())

    def translate(self):
        self._output.setPlainText(Translator().translate(self._text, to_lang=self._langs.currentText()[-3:-1]))

    def resizeEvent(self, event: QResizeEvent):
        self._output.resize(event.size().width(), event.size().height() - 50)

        self._copy.move(event.size().width() - 260, 10)
        self._translate.move(event.size().width() - 130, 10)


class QMenu(QAbstractMenu):
    def __init__(self, app, text: QTextEdit, *args, **kwargs):
        super(QMenu, self).__init__(*args, **kwargs)

        self._app = app
        self._app.addWidget(self)
        self._text = text
        self._actions = []

        self.aboutToShow.connect(self.load)
        self.load()

    def applySettings(self):
        self.load()

    def clearStateActions(self):
        self._actions.clear()

    def addStateAction(self, *args):
        self._actions.append(("act", args))

    def addStateSeparator(self):
        self._actions.append(("sep",))

    def load(self):
        self.clear()

        for action in self._actions:
            if action[0] == "act":
                self.addAction(*action[1])
            else:
                self.addSeparator()

        self.addAction(self._app.language()["undo"], "Ctrl+Z", self._undo)
        self.addAction(self._app.language()["redo"], "Ctrl+Y", self._redo)
        self.addSeparator()

        self.addAction(self._app.language()["cut"], "Ctrl+X", self._cut).setEnabled(
            bool(self._text.textCursor().selectedText()))
        self.addAction(self._app.language()["copy"], "Ctrl+С", self._copy).setEnabled(
            bool(self._text.textCursor().selectedText()))
        self.addAction(self._app.language()["paste"], "Ctrl+V", self._paste)
        self.addAction(self._app.language()["del"], self._delete).setEnabled(
            bool(self._text.textCursor().selectedText()))

        self.addSeparator()
        self.addAction(self._app.language()["select_all"], "Ctrl+A", self._select_all)
        self.addSeparator()

        self.addAction(self._app.language()["translate"], "Ctrl+T", self._translate).setEnabled(
            bool(self._text.textCursor().selectedText()))

        self.addAction(self._app.language()["search"], "Ctrl+W", self._search).setEnabled(
            bool(self._text.textCursor().selectedText()))

    def _undo(self):
        self._text.undo()

    def _redo(self):
        self._text.redo()

    def _cut(self):
        self._text.cut()

    def _copy(self):
        self._text.copy()

    def _paste(self):
        self._text.paste()

    def _delete(self):
        self._text.textCursor().removeSelectedText()

    def _select_all(self):
        self._text.selectAll()

    def _translate(self):
        QAbstractTranslateWindow(self._app, self._text.textCursor().selectedText(), self._text).exec()

    def _search(self):
        if self._app.settings()["other"]["search"] == "Yandex":
            webbrowser.open_new_tab(f"https://yandex.ru/search/?lr=10735&text={self._text.textCursor().selectedText()}")
        else:
            webbrowser.open_new_tab(f"https://www.google.com/search?q={self._text.textCursor().selectedText()}")


class QAbstractTextEdit(QTextEdit):

    zoomSignal = Signal(int)

    def __init__(self, app, *args, **kwargs):
        super(QAbstractTextEdit, self).__init__(*args, **kwargs)

        self._highlighter = QSpellingHighlighter(app, self, language="ru_RU")

        self._app = app
        self._app.addWidget(self)

        self._menu = QMenu(self._app, self)

        self._font = QFont("Consolas", 12)
        self._font.setHintingPreference(
            QFont.HintingPreference.PreferNoHinting
        )

        self.textChanged.connect(self.status)
        self.cursorPositionChanged.connect(self.status)
        self.zoomSignal.connect(self.status)

        self.setFont(self._font)
        self.setWordWrapMode(QTextOption.NoWrap)
        self.applySettings()

    def app(self):
        return self._app

    def applySettings(self):
        if not self._app.settings()["general"]["current-line"]:
            self.setExtraSelections([])

        self._font.setFamily(self._app.settings()["interface"]["font"])
        self._highlighter.setEnabled(self._app.settings()["general"]["spelling-enable"])

        self.setFont(self._font)
        self.status()

    def status(self):
        if self._app.settings()["general"]["current-line"]:
            selection = self.ExtraSelection()

            selection.format.setBackground(
                QColor(30, 30, 30) if self._app.theme() == "dark" else QColor(225, 225, 225)
            )
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()

            self.setExtraSelections([selection])

        self._app.updateStatusBar(
            self._app.language()["status"].format(
                self.textCursor().positionInBlock() + 1,
                self.textCursor().blockNumber() + 1,

                int(self.font().pointSize() / 12 * 100)
            )
        )

    def zoom(self, delta: int):
        if delta < 0 and self.font().pointSize() > 6:
            self.zoomOut(1)
        elif delta > 0 and self.font().pointSize() < 60:
            self.zoomIn(1)

    def update(self):
        self.status()

        return super(QAbstractTextEdit, self).update()

    def createStandardContextMenu(self):
        return self._menu

    def wheelEvent(self, event: QWheelEvent):
        if event.modifiers() & Qt.ControlModifier and self._app.settings()["general"]["zoom-enable"]:
            self.zoom(event.angleDelta().y())

            self.zoomSignal.emit(int(self.font().pointSize() / 12 * 100))
        else:
            super(QAbstractTextEdit, self).wheelEvent(event)

    def insertFromMimeData(self, source):
        return self.insertPlainText(source.text())

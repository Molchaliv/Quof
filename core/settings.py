from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox, QLabel, QPushButton, QFrame, QScrollArea

from .ui.widgets import QAbstractComboBox, QAbstractApplication


class QSettingsBase(QScrollArea):
    def __init__(self, *args, **kwargs):
        super(QSettingsBase, self).__init__(*args, **kwargs)

        self._header_font = QFont("Roboto Black", 16)
        self._header_font.setBold(True)
        self._header_font.setHintingPreference(
            QFont.HintingPreference.PreferNoHinting
        )

        self._base_font = QFont("Roboto", 12)
        self._base_font.setHintingPreference(
            QFont.HintingPreference.PreferNoHinting
        )

        self._frame = QFrame()

        self.general = QLabel("General", self._frame)

        self.status_bar_lbl = QLabel("Status bar", self._frame)
        self.status_bar_set = QCheckBox("", self._frame)
        self.current_line_lbl = QLabel("Current line", self._frame)
        self.current_line_set = QCheckBox("", self._frame)
        self.zoom_enable_lbl = QLabel("Zoom enable", self._frame)
        self.zoom_enable_set = QCheckBox("", self._frame)
        self.spelling_enable_lbl = QLabel("Spelling highlight enable", self._frame)
        self.spelling_enable_set = QCheckBox("", self._frame)

        self.interface = QLabel("Interface", self._frame)

        self.language_lbl = QLabel("Language", self._frame)
        self.language_set = QAbstractComboBox(self._frame)
        self.theme_lbl = QLabel("Theme", self._frame)
        self.theme_set = QAbstractComboBox(self._frame)
        self.font_lbl = QLabel("Font", self._frame)
        self.font_set = QAbstractComboBox(self._frame)

        self.other = QLabel("Other", self._frame)

        self.auto_save_lbl = QLabel("Auto-save", self._frame)
        self.auto_save_set = QAbstractComboBox(self._frame)
        self.search_lbl = QLabel("Search", self._frame)
        self.search_set = QAbstractComboBox(self._frame)

        self.apply = QPushButton("Apply", self._frame)

        self.ui()

    def ui(self):
        self._frame.resize(350, 500)

        self.general.move(10, 10)
        self.general.setFont(self._header_font)

        self.status_bar_lbl.move(20, 50)
        self.status_bar_lbl.setFont(self._base_font)
        self.status_bar_set.move(200, 50)

        self.current_line_lbl.move(20, 85)
        self.current_line_lbl.setFont(self._base_font)
        self.current_line_set.move(200, 85)

        self.zoom_enable_lbl.move(20, 120)
        self.zoom_enable_lbl.setFont(self._base_font)
        self.zoom_enable_set.move(200, 120)

        self.spelling_enable_lbl.move(20, 155)
        self.spelling_enable_lbl.setFont(self._base_font)
        self.spelling_enable_set.move(200, 155)

        self.interface.move(10, 195)
        self.interface.setFont(self._header_font)

        self.language_lbl.move(20, 230)
        self.language_lbl.setFont(self._base_font)
        self.language_set.move(200, 230)
        self.language_set.resize(150, 30)
        self.language_set.addItems(["English (en)", "Русский (ru)"])

        self.theme_lbl.move(20, 265)
        self.theme_lbl.setFont(self._base_font)
        self.theme_set.move(200, 265)
        self.theme_set.resize(150, 30)
        self.theme_set.addItems(["System", "Dark", "Light"])

        self.font_lbl.move(20, 300)
        self.font_lbl.setFont(self._base_font)
        self.font_set.move(200, 300)
        self.font_set.resize(150, 30)
        self.font_set.addItems(QFontDatabase.families())

        self.other.move(10, 340)
        self.other.setFont(self._header_font)

        self.auto_save_lbl.move(20, 375)
        self.auto_save_lbl.setFont(self._base_font)
        self.auto_save_set.move(200, 375)
        self.auto_save_set.resize(150, 30)
        self.auto_save_set.addItems(["-", "5s", "10s", "15s", "30s", "60s"])

        self.search_lbl.move(20, 410)
        self.search_lbl.setFont(self._base_font)
        self.search_set.move(200, 410)
        self.search_set.resize(150, 30)
        self.search_set.addItems(["Google", "Yandex"])

        self.apply.move(100, 460)
        self.apply.resize(150, 30)

        self.resize(600, 500)
        self.setWidget(self._frame)


class QSettings(QFrame):
    def __init__(self, app: QAbstractApplication, *args, **kwargs):
        super(QSettings, self).__init__(*args, **kwargs)

        self._app = app
        self._base = QSettingsBase(self)

        self._app.addWidget(self)
        self._base.apply.clicked.connect(self.apply)

        self.setDefaultSettings()
        self.applySettings()

    def setDefaultSettings(self):
        self._base.status_bar_set.setChecked(self._app.settings()["general"]["status-bar"])
        self._base.current_line_set.setChecked(self._app.settings()["general"]["current-line"])
        self._base.zoom_enable_set.setChecked(self._app.settings()["general"]["zoom-enable"])
        self._base.spelling_enable_set.setChecked(self._app.settings()["general"]["spelling-enable"])

        self._base.language_set.setCurrentText(self._app.settings()["interface"]["lang"])
        self._base.theme_set.setCurrentText(self._app.settings()["interface"]["theme"])
        self._base.font_set.setCurrentText(self._app.settings()["interface"]["font"])

        self._base.auto_save_set.setCurrentText(self._app.settings()["other"]["backup"])
        self._base.search_set.setCurrentText(self._app.settings()["other"]["search"])

    def applySettings(self):
        self._app.updateStatusBar("")

        self._base.status_bar_lbl.setText(self._app.language()["status_bar"])
        self._base.status_bar_lbl.adjustSize()
        self._base.current_line_lbl.setText(self._app.language()["current_line"])
        self._base.current_line_lbl.adjustSize()
        self._base.zoom_enable_lbl.setText(self._app.language()["zoom_enable"])
        self._base.zoom_enable_lbl.adjustSize()
        self._base.spelling_enable_lbl.setText(self._app.language()["spelling_enable"])
        self._base.spelling_enable_lbl.adjustSize()
        self._base.language_lbl.setText(self._app.language()["lang"])
        self._base.language_lbl.adjustSize()
        self._base.theme_lbl.setText(self._app.language()["theme"])
        self._base.theme_lbl.adjustSize()
        self._base.font_lbl.setText(self._app.language()["font"])
        self._base.font_lbl.adjustSize()
        self._base.auto_save_lbl.setText(self._app.language()["auto_save"])
        self._base.auto_save_lbl.adjustSize()
        self._base.search_lbl.setText(self._app.language()["web_search"])
        self._base.search_lbl.adjustSize()

        self._base.general.setText(self._app.language()["general"])
        self._base.general.adjustSize()
        self._base.interface.setText(self._app.language()["interface"])
        self._base.interface.adjustSize()
        self._base.other.setText(self._app.language()["other"])
        self._base.other.adjustSize()
        self._base.apply.setText(self._app.language()["apply"])

    def apply(self):
        self._app.applySettings({
            "general": {
                "status-bar": self._base.status_bar_set.isChecked(),
                "current-line": self._base.current_line_set.isChecked(),
                "zoom-enable": self._base.zoom_enable_set.isChecked(),
                "spelling-enable": self._base.spelling_enable_set.isChecked()
            },
            "interface": {
                "lang": self._base.language_set.currentText(),
                "theme": self._base.theme_set.currentText(),
                "font": self._base.font_set.currentText()
            },
            "other": {
                "backup": self._base.auto_save_set.currentText(),
                "search": self._base.search_set.currentText()
            }
        })

    def update(self):
        self._app.updateStatusBar("")

        return super(QSettings, self).update()

    def resizeEvent(self, event):
        self._base.resize(370, event.size().height())
        self._base.move((event.size().width() // 2) - (self._base.width() // 2), 0)

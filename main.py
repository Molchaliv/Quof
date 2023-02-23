import core
import sys

from core.ui.widgets import QAbstractMenuBar, QAbstractStatusBar, QAbstractTabWidget, QAbstractApplication
from core import QAutoSave, QFileMenu, QEditMenu, QStyleMenu, QHelpMenu

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow


class QMain(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMain, self).__init__(*args, **kwargs)

        app.addWidget(self)

        self.setWindowTitle("Notepad")
        self.setWindowIcon(QIcon("res/icon.png"))
        self.setMinimumSize(500, 400)

        self.menuBar = QAbstractMenuBar(self)
        self.tabBar = QAbstractTabWidget(self)
        self.statusBar = QAbstractStatusBar(self)

        app.setStatusBar(self.statusBar)

        self.fileMenu = QFileMenu(app, self.tabBar, "file")
        self.editMenu = QEditMenu(app, self.tabBar, "edit")
        self.styleMenu = QStyleMenu(app, self.tabBar, "style")
        self.helpMenu = QHelpMenu(app, self.tabBar, "help")

        self.autoSave = QAutoSave(app, self.tabBar, r"res\backup.db", 10)

        self.fmIndex = self.menuBar.addMenu(self.fileMenu)
        self.emIndex = self.menuBar.addMenu(self.editMenu)
        self.smIndex = self.menuBar.addMenu(self.styleMenu)
        self.hmIndex = self.menuBar.addMenu(self.helpMenu)

        app.plugin(app, self, core)

        self.autoSave.start()
        self.setMenuBar(self.menuBar)

    def applySettings(self):
        ...

    def resizeEvent(self, event):
        self.tabBar.move(0, 35)
        self.tabBar.resize(event.size().width(), event.size().height() - 60)

        self.statusBar.move(0, event.size().height() - 25)
        self.statusBar.resize(event.size().width(), 25)


if __name__ == "__main__":
    app = QAbstractApplication(r".\res\config.json", sys.argv)

    main = QMain()
    main.show()

    sys.exit(app.exec())

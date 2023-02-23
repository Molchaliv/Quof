import darkdetect
import threading

from .dark import QDarkStyleSheet
from .light import QLightStyleSheet

from PySide6.QtWidgets import QApplication


class RepeatTimer(threading.Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


class QThemedApplication(QApplication):
    def __init__(self, *args, **kwargs):
        super(QThemedApplication, self).__init__(*args, **kwargs)

        self._current = self.theme()

        self._timer = RepeatTimer(1, self.update)
        self._timer.start()

        self.setStyleSheet(self._current.QApplication)

    def update(self):
        if (current := self.theme()) != self._current:
            self.setStyleSheet(current.QApplication)
        self._current = current

    @staticmethod
    def theme():
        return QDarkStyleSheet() if darkdetect.isDark() else QLightStyleSheet()

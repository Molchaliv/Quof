from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel


class QAbstractStatusBar(QLabel):
    def __init__(self, *args, **kwargs):
        super(QAbstractStatusBar, self).__init__(*args, **kwargs)

        self.setAlignment(Qt.AlignCenter)

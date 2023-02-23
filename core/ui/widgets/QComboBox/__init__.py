from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox


class QAbstractComboBox(QComboBox):
    def __init__(self, *args, **kwargs):
        super(QAbstractComboBox, self).__init__(*args, **kwargs)

        self.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        self.view().window().setAttribute(Qt.WA_TranslucentBackground)

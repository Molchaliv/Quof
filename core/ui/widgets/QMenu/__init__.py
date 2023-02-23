from PySide6.QtCore import Qt, QPropertyAnimation
from PySide6.QtWidgets import QMenu, QGraphicsBlurEffect, QWidget


class QAbstractMenu(QMenu):
    def __init__(self, *args, **kwargs) -> None:
        super(QAbstractMenu, self).__init__(*args, **kwargs)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.NoDropShadowWindowHint)

from PySide6.QtWidgets import QMenuBar


class QAbstractMenuBar(QMenuBar):
    def __init__(self, *args, **kwargs):
        super(QAbstractMenuBar, self).__init__(*args, **kwargs)

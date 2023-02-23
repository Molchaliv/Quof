from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QWidget


class QPos(object):
    Align: None = str

    TopCenter: None = "TopCenter"
    BottomCenter: None = "BottomCenter"
    BothCenter: None = "BothCenter"


class QAbstractDialog(QWidget):
    def __init__(self, *args, **kwargs):
        super(QAbstractDialog, self).__init__(*args, **kwargs)

        self._align = QPos.BothCenter

    def setPosition(self, align: QPos.Align):
        self._align = align

    def resizeEvent(self, event: QResizeEvent):
        if self._align == QPos.TopCenter:
            self.move(
                (event.size().width() // 2) - (self.width() // 2), 10
            )
        elif self._align == QPos.BothCenter:
            self.move(
                (event.size().width() // 2) - (self.width() // 2), event.size().height() - (self.height() + 10)
            )
        elif self._align == QPos.BothCenter:
            self.move(
                (event.size().width() // 2) - (self.width() // 2), (event.size().height() // 2) - (self.height() // 2)
            )

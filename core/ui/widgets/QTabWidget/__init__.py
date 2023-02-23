from PySide6.QtWidgets import QTabWidget, QWidget


class QAbstractTabWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        super(QAbstractTabWidget, self).__init__(*args, **kwargs)

        self._tabs = {}

        self.setMovable(True)
        self.setDocumentMode(True)
        self.setTabsClosable(True)

        self.currentChanged.connect(
            lambda index: self.widget(index).update() if self.widget(index) else self._tabs.clear()
        )
        self.tabCloseRequested.connect(
            lambda index: (self._tabs.pop(self.keyAt(self.widget(index))), self.removeTab(index))
        )

    def addTab(self, widget: QWidget, label: str, key: str = ""):
        if key not in self._tabs:
            index = super(QAbstractTabWidget, self).addTab(widget, label)

            self.setCurrentIndex(index)
            if key:
                self._tabs[key] = self.currentWidget()
        else:
            index = self.indexOf(self.widgetAt(key))

            self.setCurrentIndex(index)

        return index

    def addKey(self, key: str):
        self._tabs[key] = self.currentWidget()

    def keyAt(self, widget: QWidget):
        return {value: key for key, value in self._tabs.items()}[widget]

    def currentKey(self):
        return {value: key for key, value in self._tabs.items()}[self.currentWidget()]

    def widgetExist(self, widget: QWidget):
        return widget in self._tabs.values()

    def widgetAt(self, key: str):
        return self.widget(self.indexOf(self._tabs[key]))

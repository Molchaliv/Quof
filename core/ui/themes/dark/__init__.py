from PySide6.QtWidgets import QWidget


class QDarkStyleSheet(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(QDarkStyleSheet, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]

    def __init__(self, *args, **kwargs):
        super(QDarkStyleSheet, self).__init__(*args, **kwargs)

    @property
    def QCheckBox(self):
        return """
        QCheckBox {
            color: #F0F0F0;
            background: transparent;
            font-size: 10pt;
        }
        QCheckBox::indicator {
            background: #212121;
            width: 20px;
            height: 20px;
            border-radius: 5px;
            border: 1px solid #313131;
            margin: 1px;
        }
        QCheckBox::indicator:checked {
            background: #313131;
        }
        """

    @property
    def QComboBox(self):
        return """
        QComboBox {
            background: #212121;
            color: #F0F0F0;
            border-radius: 5px;
            border: 1px solid #313131;
            font-size: 9pt;
            padding: 5px;
            margin: 1px;
        }
        QComboBox::drop-down {
            border: none
        }
        QComboBox::down-arrow {
            image: url('res/dark-down-button.png');
            width: 12px;
            height: 12px;
        }
        """

    @property
    def QDialog(self):
        return """
        QDialog {
            background: #202020;
        }
        """

    @property
    def QFrame(self):
        return """
        QFrame {
            background: #1A1A1A;
        }
        """

    @property
    def QLabel(self):
        return """
        QLabel {
            color: #F0F0F0;
            background: transparent;
            font-size: 10pt;
        }
        """

    @property
    def QLineEdit(self):
        return """
        QLineEdit {
            background: #1A1A1A;
            color: #F0F0F0;
            selection-color: #1A1A1A;
            selection-background-color: #F0F0F0;
            border: 1px solid #313131;
            border-radius: 5px;
            padding: 5px;
            font-size: 9pt;
            margin: 1px;
        }
        """

    @property
    def QListView(self):
        return """
        QListView {
            background: #212121;
            color: #F0F0F0;
            border-radius: 5px;
            border: 1px solid #313131;
            font-size: 10pt;
            padding: 3px;
            margin: 1px;
            margin-top: 6px;
            outline: 0px;
        }
        QListView::item {
            border-radius: 3px;
        }
        QListView::item:hover {
            background: #313131;
        }
        QListView::item:selected {
            color: #F0F0F0;
            background: #313131;
        }
        """

    @property
    def QMainWindow(self):
        return """
        QMainWindow {
            background: #1A1A1A;
        }
        """

    @property
    def QMenu(self):
        return """
        QMenu {
            background: #212121;
            color: #F0F0F0;
            border: 1px solid #313131;
            border-radius: 5px;
            font-size: 10pt;
            padding: 3px;
        }
        QMenu::disabled {
            color: #888888;
        }
        QMenu::item {
            background: transparent;
            border: none;
            padding: 3px 15px 3px 15px;
        }
        QMenu::item:selected {
            background-color: #313131;
            border-radius: 3px;
        }
        QMenu::icon {
            padding-left: 5px;
        }
        QMenu::icon:disabled {
            color: #888888;
        }
        QMenu::separator {
            background: #313131;
            max-height: 1px;
            margin: 5px;
        }
        """

    @property
    def QMenuBar(self):
        return """
        QMenuBar {
            color: #F0F0F0;
            background: #202020;
            font-size: 10pt;
            padding: 3px;
        }
        
        QMenuBar::item {
            background: transparent;
            padding: 5px 10px 5px 10px;
            border-radius: 4px;
        }
        
        QMenuBar::item:selected {
            background: #222222;
        }
        
        QMenuBar::item:pressed {
            background: #222222;
        }
        """

    @property
    def QPushButton(self):
        return """
        QPushButton {
            background: #212121;
            color: #F0F0F0;
            border-radius: 5px;
            border: 1px solid #313131;
            font-size: 10pt;
            padding: 5px;
            margin: 1px;
        }
        QPushButton::hover {
            background: #313131;
        }
        QPushButton::pressed {
            background: #1A1A1A;
        }
        QPushButton::disabled {
            color: #888888;
        }
        """

    @property
    def QScrollBar(self):
        return """
        QScrollArea {
            border: none;
        }
        QScrollBar:horizontal {
            height: 15px;
            margin: 3px 15px 3px 15px;
            border: 1px transparent #2A2929;
            border-radius: 3px;
            background-color: #2A2929;
        }
        QScrollBar::handle:horizontal {
            background-color: #767676;
            min-width: 10px;
            border-radius: 3px;
        }
        QScrollBar::add-line:horizontal {
            background-color: transparent;
            color: transparent;
        }
        QScrollBar::sub-line:horizontal {
            background-color: transparent;
            color: transparent;
        }
        QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
            background: none;
        }
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
            background: none;
        }
        
        QScrollBar:vertical {
            background-color: #2A2929;
            width: 15px;
            margin: 15px 3px 15px 3px;
            border: 1px transparent #2A2929;
            border-radius: 3px;
        }
        QScrollBar::handle:vertical {
            background-color: #767676;
            min-height: 10px;
            border-radius: 3px;
        }
        QScrollBar::sub-line:vertical {
            background-color: transparent;
            color: transparent;
        }
        QScrollBar::add-line:vertical {
            background-color: transparent;
            color: transparent;
        }
        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
            background: none;
        }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }
        """

    @property
    def QTabBar(self):
        return """
        QTabBar {
            background: #202020;
        }
        QTabBar::tab {
            color: #F0F0F0;
            background: transparent;
            min-width: 75px;
            border-radius: 3px;
            padding: 5px;
            margin: 3px;
            font-size: 10pt;
        }
        QTabBar::tab:selected {
            background: #313131;
        }
        QTabBar::tab:selected:hover {
            background: #313131;
        }
        QTabBar::tab:hover {
            background: #252525;
        }
        QTabBar::close-button {
            image: url('res/dark-close-button.png');
        }
        QTabBar QToolButton {
            background: transparent;
            border: none;
        }
        QTabBar QToolButton::right-arrow:enabled {   
            image: url('res/dark-right-button.png');
        }
        QTabBar QToolButton::left-arrow:enabled {  
            image: url('res/dark-left-button.png');
        }
        QTabWidget::pane {
            border: none;
        }
        """

    @property
    def QTextEdit(self):
        return """
        QTextEdit {
            background: #1A1A1A;
            color: #F0F0F0;
            selection-color: #1A1A1A;
            selection-background-color: #F0F0F0;
            border: none;
        }
        """

    @property
    def QToolTip(self):
        return """
        QToolTip {
            background: #212121;
            background-clip: border;
            color: #F0F0F0;
            border-radius: 3px;
            border: 1px solid #313131;
            padding: 1px;
        }
        """

    @property
    def QApplication(self):
        return f"{self.QCheckBox}" \
               f"{self.QComboBox}" \
               f"{self.QDialog}" \
               f"{self.QFrame}" \
               f"{self.QLabel}\n" \
               f"{self.QLineEdit}\n" \
               f"{self.QListView}\n" \
               f"{self.QMainWindow}\n" \
               f"{self.QMenu}\n" \
               f"{self.QMenuBar}\n" \
               f"{self.QPushButton}" \
               f"{self.QScrollBar}\n" \
               f"{self.QTabBar}\n" \
               f"{self.QTextEdit}\n" \
               f"{self.QToolTip}\n"

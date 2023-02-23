from PySide6.QtWidgets import QWidget


class QLightStyleSheet(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(QLightStyleSheet, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]

    def __init__(self, *args, **kwargs):
        super(QLightStyleSheet, self).__init__(*args, **kwargs)

    @property
    def QCheckBox(self):
        return """
        QCheckBox::indicator {
            background: #DEDEDE;
            width: 20px;
            height: 20px;
            border-radius: 5px;
            border: 1px solid #CECECE;
            margin: 1px;
        }
        QCheckBox::indicator:checked {
            background: #CECECE;
        }
        """

    @property
    def QComboBox(self):
        return """
        QComboBox {
            background: #DEDEDE;
            color: #0F0F0F;
            border-radius: 5px;
            border: 1px solid #CECECE;
            font-size: 9pt;
            padding: 5px;
            margin: 1px;
        }
        QComboBox::drop-down {
            border: none
        }
        QComboBox::down-arrow {
            image: url('res/light-down-button.png');
            width: 12px;
            height: 12px;
        }
        QComboBox QListView {
            background: #DEDEDE;
            color: #0F0F0F;
            border-radius: 5px;
            border: 1px solid #CECECE;
            font-size: 10pt;
            padding: 3px;
            margin-top: 5px;
            outline: 0px;
        }
        QComboBox QListView::item {
            color: #0F0F0F;
            border-radius: 3px;
        }
        QComboBox QListView::item:hover {
            background: #CECECE;
        }
        QComboBox QListView::item:selected {
            background: #CECECE;
        }
        """

    @property
    def QDialog(self):
        return """
        QDialog {
            background: #DFDFDF;
        }
        """

    @property
    def QFrame(self):
        return """
        QFrame {
            background: #E5E5E5;
        }
        """

    @property
    def QLabel(self):
        return """
        QLabel {
            color: #0F0F0F;
            font-size: 10pt;
        }
        """

    @property
    def QLineEdit(self):
        return """
        QLineEdit {
            background: #E5E5E5;
            color: #0F0F0F;
            selection-color: #E5E5E5;
            selection-background-color: #0F0F0F;
            border: 1px solid #CECECE;
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
            background: #DEDEDE;
            color: #0F0F0F;
            border-radius: 5px;
            border: 1px solid #CECECE;
            font-size: 10pt;
            padding: 3px;
            margin: 1px;
            margin-top: 6px;
            outline: 0px;
        }
        QListView::item {
            color: #0F0F0F;
            border-radius: 3px;
        }
        QListView::item:hover {
            background: #CECECE;
        }
        QListView::item:selected {
            background: #CECECE;
        }
        """

    @property
    def QMainWindow(self):
        return """
        QMainWindow {
            background: #E5E5E5;
        }
        """

    @property
    def QMenu(self):
        return """
        QMenu {
            background: #DEDEDE;
            color: #0F0F0F;
            border: 1px solid #CECECE;
            border-radius: 5px;
            font-size: 10pt;
            padding: 3px;
        }
        QMenu::disabled {
            color: #777777;
        }
        QMenu::item {
            background: transparent;
            border: none;
            padding: 3px 15px 3px 15px;
        }
        QMenu::item:selected {
            background-color: #CECECE;
            border-radius: 3px;
        }
        QMenu::separator {
            background: #CECECE;
            max-height: 1px;
            margin: 5px;
        }
        """

    @property
    def QMenuBar(self):
        return """
        QMenuBar {
            color: #0F0F0F;
            background: #DFDFDF;
            font-size: 10pt;
            padding: 3px;
        }

        QMenuBar::item {
            background: transparent;
            padding: 5px 10px 5px 10px;
            border-radius: 4px;
        }

        QMenuBar::item:selected {
            background: #DDDDDD;
        }

        QMenuBar::item:pressed {
            background: #DDDDDD;
        }
        """

    @property
    def QPushButton(self):
        return """
        QPushButton {
            background: #DEDEDE;
            color: #0F0F0F;
            border-radius: 5px;
            border: 1px solid #CECECE;
            font-size: 10pt;
            padding: 5px;
            margin: 1px;
        }
        QPushButton::hover {
            background: #CECECE;
        }
        QPushButton::pressed {
            background: #E5E5E5;
        }
        QPushButton::disabled {
            color: #777777;
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
            border: 1px transparent #D5D6D6;
            border-radius: 3px;
            background-color: #D5D6D6;
        }
        QScrollBar::handle:horizontal {
            background-color: #898989;
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
            background-color: #D5D6D6;
            width: 15px;
            margin: 15px 3px 15px 3px;
            border: 1px transparent #D5D6D6;
            border-radius: 3px;
        }
        QScrollBar::handle:vertical {
            background-color: #898989;
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
            background: #DFDFDF;
        }
        QTabBar::tab {
            color: #0F0F0F;
            background: transparent;
            min-width: 75px;
            border-radius: 3px;
            padding: 5px;
            margin: 3px;
            font-size: 10pt;
        }
        QTabBar::tab:selected {
            background: #CECECE;
        }
        QTabBar::tab:selected:hover {
            background: #CECECE;
        }
        QTabBar::tab:hover {
            background: #DADADA;
        }
        QTabBar::close-button {
            image: url('res/light-close-button.png');
        }
        QTabBar QToolButton {
            background: transparent;
            border: none;
        }
        QTabBar QToolButton::right-arrow:enabled {   
            image: url('res/light-right-button.png');
        }
        QTabBar QToolButton::left-arrow:enabled {  
            image: url('res/light-left-button.png');
        }
        QTabWidget::pane {
            border: none;
        }
        """

    @property
    def QTextEdit(self):
        return """
        QTextEdit {
            background: #E5E5E5;
            color: #0F0F0F;
            selection-color: #E5E5E5;
            selection-background-color: #0F0F0F;
            border: none;
        }
        """

    @property
    def QToolTip(self):
        return """
        QToolTip {
            background: #DEDEDE;
            background-clip: border;
            color: #0F0F0F;
            border-radius: 3px;
            border: 1px solid #CECECE;
            padding: 1px;
        }
        """

    @property
    def QApplication(self):
        return f"{self.QCheckBox}" \
               f"{self.QComboBox}" \
               f"{self.QDialog}" \
               f"{self.QFrame}" \
               f"{self.QLabel}" \
               f"{self.QLineEdit}" \
               f"{self.QListView}" \
               f"{self.QMainWindow}\n" \
               f"{self.QMenu}\n" \
               f"{self.QMenuBar}\n" \
               f"{self.QPushButton}" \
               f"{self.QScrollBar}\n" \
               f"{self.QTabBar}\n" \
               f"{self.QTextEdit}\n" \
               f"{self.QToolTip}\n"

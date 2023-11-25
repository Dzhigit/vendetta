from PyQt6.QtWidgets import QWidget


class MessagesWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName('MessagesWidget')
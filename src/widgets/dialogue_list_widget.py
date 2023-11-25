from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QHBoxLayout, QLabel, QWidget
from PyQt6.QtGui import QShortcut, QKeySequence, QPixmap


class DialogueListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('DialogueListWidget')
        self.setMaximumWidth(200)

        self.change_visible_shortcut = QShortcut(QKeySequence('Ctrl+D'), parent)
        self.change_visible_shortcut.activated.connect(self.change_visible)

    def change_visible(self):
        self.setVisible(not self.isVisible())

    def add_chat(self, username):
        chat = QListWidgetItem()
        chat_info = socket_handler.get_chat()

        if not chat_info:
            return

        interior_widget = QWidget()
        icon_widget = QLabel(QPixmap(chat_info['icon']))
        name_widget = QLabel(username)

        h_box = QHBoxLayout()
        h_box.addWidget(icon_widget)
        h_box.addWidget(name_widget)
        interior_widget.setLayout(h_box)
        chat.setSizeHint(interior_widget.sizeHint())
        self.addItem(chat)


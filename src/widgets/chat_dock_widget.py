from PyQt6.QtWidgets import QDockWidget


class ChatDockWidget(QDockWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs, parent=parent)
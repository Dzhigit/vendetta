from PyQt6.QtWidgets import QDockWidget, QListWidget
from PyQt6.QtGui import QShortcut, QKeySequence


class SettingsDockWidget(QDockWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(*args, **kwargs, parent=parent)

        self.listWidget = QListWidget()
        self.listWidget.addItem('Item1')
        self.listWidget.addItem('Item2')
        self.listWidget.addItem('Item3')
        self.listWidget.addItem('Item4')

        self.setWidget(self.listWidget)

        self.change_visible_shortcut = QShortcut(QKeySequence('Ctrl+S'), parent)
        self.change_visible_shortcut.activated.connect(self.change_visible)

    def change_visible(self):
        self.setVisible(not self.isVisible())
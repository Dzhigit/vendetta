from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout
from PyQt6.QtCore import Qt
from dialogue_list_widget import DialogueListWidget
from messages_widget import MessagesWidget
from settings_dock_widget import SettingsDockWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Vendetta Alpha')
        self.setGeometry(200, 200, 900, 600)

        self.central_widget = QWidget()
        self.central_widget.setObjectName('CentralWidget')
        self.setCentralWidget(self.central_widget)

        self.dialogue_list_widget = DialogueListWidget(self)
        self.messages_widget = MessagesWidget()

        self.settings_dock_widget = SettingsDockWidget(self)
        self.settings_dock_widget.hide()

        grid = QGridLayout()
        grid.setAlignment(Qt.AlignmentFlag.AlignAbsolute)
        grid.addWidget(self.dialogue_list_widget, 0, 1)
        grid.addWidget(self.messages_widget, 0, 2)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.settings_dock_widget)
        self.central_widget.setLayout(grid)
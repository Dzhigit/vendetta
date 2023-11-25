from PyQt6.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QDockWidget, QListWidget, QTextEdit
from PyQt6.QtCore import Qt


class DockDemo(QMainWindow):
    def __init__(self,parent=None):
        super(DockDemo, self).__init__(parent)
        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('New')
        file.addAction('Save')
        file.addAction('quit')

        self.items = QDockWidget('Dockable', self)

        self.listWidget = QListWidget()
        self.listWidget.addItem('Item1')
        self.listWidget.addItem('Item2')
        self.listWidget.addItem('Item3')
        self.listWidget.addItem('Item4')

        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.items)

        self.setLayout(layout)
        self.setWindowTitle('Dock Demo with PyQt')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = DockDemo()
    window.show()
    sys.exit(app.exec())
from PyQt6.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QLineEdit, QFormLayout, QPushButton,
                             QStackedWidget)
from reg_widget import RegWidget


class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Vendetta Auth')
        self.setGeometry(100, 100, 400, 150)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.username_entry = QLineEdit()
        self.password_entry = QLineEdit()

        self.signin_btn = QPushButton('Sign In')
        self.signin_btn.clicked.connect(self.on_sign_in)

        self.reg_btn = QPushButton('Registration')
        self.reg_btn.clicked.connect(self.on_reg)

        self.auth_area = QWidget()
        self.f_box = QFormLayout()
        self.f_box.addRow('Login:', self.username_entry)
        self.f_box.addRow('Password:', self.password_entry)
        self.f_box.addRow(self.signin_btn)
        self.f_box.addRow(self.reg_btn)
        self.auth_area.setLayout(self.f_box)
        self.central_widget.addWidget(self.auth_area)

    def on_sign_in(self):
        pass

    def on_reg(self):
        self.central_widget.addWidget(RegWidget(self))
        self.central_widget.setCurrentIndex(1)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    auth_window = AuthWindow()
    auth_window.show()
    sys.exit(app.exec())
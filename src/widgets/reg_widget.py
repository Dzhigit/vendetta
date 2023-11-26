from PyQt6.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QDialog, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtNetwork import QTcpSocket
import requests


class RegWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.connection = QTcpSocket()
        self.parent = parent

        self.verify_code_widget = VerifyCodeWidget(self)

        self.username_entry = QLineEdit()
        self.password_entry = QLineEdit()
        self.re_password_entry = QLineEdit()
        self.email_entry = QLineEdit()
        self.verify_code_entry = QLineEdit()

        self.continue_btn = QPushButton('Continue')
        self.continue_btn.clicked.connect(self.on_continue)

        self.auth_btn = QPushButton('Authorization')
        self.auth_btn.clicked.connect(self.on_auth)

        self.f_box = QFormLayout()
        self.f_box.addRow('Username:', self.username_entry)
        self.f_box.addRow('Password:', self.password_entry)
        self.f_box.addRow('Re-password:', self.re_password_entry)
        self.f_box.addRow('Email', self.email_entry)
        self.f_box.addRow(self.continue_btn)
        self.f_box.addRow(self.auth_btn)
        self.setLayout(self.f_box)

    def on_continue(self):
        email = self.email_entry.text()
        username = self.username_entry.text()
        password = self.password_entry.text()
        re_password = self.re_password_entry.text()

        print(email)
        print(requests.get(f'http://localhost:5000/verification/{email}'))
        self.verify_code_widget.show()
        self.verify_code_widget.on_send(email, username, password, re_password)
        # if self.username_entry.text() and self.email_entry.text():
        #     if self.password_entry.text() == self.re_password_entry.text():
        #         self.verify_code_widget.setVisible(True)

    def on_auth(self):
        self.parent.central_widget.setCurrentIndex(0)


class VerifyCodeWidget(QDialog):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.resize(self.size().width() // 100 * 80, self.size().height() // 100 * 60)
        self.setWindowFlags(
            Qt.WindowType.Popup
        )

        self.code_entry = QLineEdit()
        self.send_btn = QPushButton('Send')
        self.send_btn.clicked.connect(self.on_send)

        v_box = QVBoxLayout()
        v_box.addWidget(QLabel('Enter your verification code on email'))
        v_box.addWidget(self.code_entry)
        v_box.addWidget(self.send_btn)
        self.setLayout(v_box)

    def on_send(self, email, username, password, re_password):
        response = requests.get(
            f'http://localhost:5000/registration/'
            f'email={email}&'
            f'username={username}&'
            f'password={password}&'
            f're_password={re_password}&'
            f'code={self.code_entry.text()}'
            ).json()

        if response['DONE']:
            print('YES')



if __name__ == '__main__':
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    reg_window = RegWidget()
    reg_window.show()
    sys.exit(app.exec())



from PyQt6.QtNetwork import QTcpSocket
import pickle


class SocketHandler(QTcpSocket):
    def __init__(self, parent):
        super().__init__(parent=parent)

    def set_up(self):
        self.connectToHost('localhost', 65044)

        if not self.waitForConnected(1000):
            return

    def get_chat(self):
        self.write(
            pickle.dumps({'event': 'GET_CHAT'})
        )
        data = self.readAll()
        if data:
            return pickle.loads(self.readAll())
        else:
            return

    def get_verify_code(self):
        self.write(
            pickle.dumps({'event': 'GET_VERIFY_CODE'})
        )
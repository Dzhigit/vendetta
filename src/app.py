from PyQt6.QtWidgets import QApplication
import sys

from src.data.styles import style_sheet
from src.widgets.main_window import MainWindow
from src.shandler.socket_handler import SocketHandler


connection = SocketHandler()


def on_startup(conn=connection):
    try:
        conn.set_up()
    except Exception as exc:
        conn.close()
    else:
        app = QApplication(sys.argv)
        main_window = MainWindow()
        main_window.setStyleSheet(style_sheet)
        main_window.show()
        sys.exit(app.exec())
    finally:
        conn.close()


if __name__ == '__main__':
    on_startup()
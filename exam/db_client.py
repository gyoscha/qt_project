import sys
from PySide2.QtWidgets import QApplication, QMainWindow

from exam.ui import ui_db


# import os
# os.environ['QT_MAC_WANTS_LAYER'] = '1'   # Прописываю, чтобы открывалось MainWindow на Mac OS


class MyDBClient(QMainWindow):
    def __init__(self, parent=None):   # Чтобы было отдельное окно parent = None
        super().__init__(parent)

        self.ui = ui_db.Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyDBClient()
    window.show()

    sys.exit(app.exec_())

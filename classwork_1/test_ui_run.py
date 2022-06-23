import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from classwork_1.UI.ui_cosmo import Ui_MainWindow

import os
os.environ['QT_MAC_WANTS_LAYER'] = '1'   # Прописываю, чтобы открывалось MainWindow на Mac OS


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

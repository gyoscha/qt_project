from PySide2 import QtCore, QtWidgets
from ui import P3_HardwareIndependentIO_QThread_design


class QThreadPractice(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = P3_HardwareIndependentIO_QThread_design.Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    myapp = QThreadPractice()

    myapp.show()

    app.exec_()

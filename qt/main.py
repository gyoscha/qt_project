from PySide2 import QtWidgets


import os
os.environ['QT_MAC_WANTS_LAYER'] = '1'   # Прописываю, чтобы открывалось MainWindow на Mac OS


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):   # Чтобы было отдельное окно parent = None
        super().__init__(parent)


if __name__ == '__main__':
    app = QtWidgets.QApplication()   # создали цикл приложения

    win = MyWindow()

    win.show()   # высветили окно

    app.exec_()   # запустили приложения

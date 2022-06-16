from datetime import time

from PySide2 import QtWidgets, QtCore, QtGui
from classwork_2.UI.ui_classwork_2 import Ui_MainWindow


# import os
# os.environ['QT_MAC_WANTS_LAYER'] = '1'   # Прописываю, чтобы открывалось MainWindow на Mac OS

# ToDo Переименовать все object names
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):   # Чтобы было отдельное окно parent = None
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox.addItems(["HEX", "DEC", "OCT", "BIN"])

        self.ui.pushButton_3.setShortcut(QtGui.QKeySequence("F1"))   # установка горячей клавиши на кнопку
        self.ui.pushButton_3.clicked.connect(self.getscreeninfo)

        # Установка сигналов на кнопки положения программы
        self.ui.pushButton_5.clicked.connect(self.onPBLTClicked)
        self.ui.pushButton_4.clicked.connect(self.onPBRTClicked)
        self.ui.pushButton.clicked.connect(self.onPBLBClicked)
        self.ui.pushButton_2.clicked.connect(self.onPBRBClicked)
        self.ui.pushButton_6.clicked.connect(self.onPBCClicked)

    def getscreeninfo(self):
        """Получение параметров экрана"""
        screens_count = QtWidgets.QApplication.screens()
        log = self.ui.plainTextEdit.appendPlainText

        log(f"{11*'='} SystemInfo {11*'='}")
        log(f"Кол-во экранов:           {len(screens_count)}")
        log(f"Основное окно:            {QtWidgets.QApplication.primaryScreen().name()}")
        for cur_screen in screens_count:
            log(f"Разрешение экрана         {cur_screen.name()} составляет {cur_screen.size().width()} на {cur_screen.size().height()}")
        log(f"Окно находится на экране  {QtWidgets.QApplication.screenAt(self.pos()).name()}")
        log(f"Размеры окна:")
        log(f"{' ' * 25} Ширина {self.size().width()} ")
        log(f"{' ' * 25} Высота {self.size().height()}")
        log(f"Минимальные размеры окна:")
        log(f"{' ' * 25} Ширина {self.minimumWidth()}")
        log(f"{' ' * 25} Высота {self.minimumHeight()}")
        log(f"Текущее положение:        x = {self.pos().x()}, y = {self.pos().y()}")
        log(f"Центр приложения:         x = {self.pos().x() + self.width()/2}, y = {self.pos().y() + self.height()/2}")
        log(f"{30 * '='}\n")

    def onPBLTClicked(self):
        """ ЛЕВО-ВЕРХ """
        self.move(0, 0)

    def onPBRTClicked(self):
        """ ПРАВО-ВЕРХ """
        # print(QtWidgets.QApplication.screenAt(self.pos()).size())
        # print(self.width())
        # print(self.height())
        screenWidth = QtWidgets.QApplication.screenAt(self.pos()).size().width()
        screenHeight = QtWidgets.QApplication.screenAt(self.pos()).size().height()
        self.move(screenWidth - self.width(), 0)

    def onPBLBClicked(self):
        """ ЛЕВО-НИЗ """
        screenWidth = QtWidgets.QApplication.screenAt(self.pos()).size().width()
        screenHeight = QtWidgets.QApplication.screenAt(self.pos()).size().height()
        self.move(0, screenHeight-self.height())

    def onPBRBClicked(self):
        """ ПРАВО-НИЗ """
        screenWidth = QtWidgets.QApplication.screenAt(self.pos()).size().width()
        screenHeight = QtWidgets.QApplication.screenAt(self.pos()).size().height()
        self.move(screenWidth - self.width(), screenHeight - self.height())

    def onPBCClicked(self):
        """ Центр """
        screenWidth = QtWidgets.QApplication.screenAt(self.pos()).size().width()
        screenHeight = QtWidgets.QApplication.screenAt(self.pos()).size().height()
        self.move(screenWidth/2 - self.width()/2, screenHeight/2 - self.height()/2)

    # EVENTS
    def changeEvent(self, event: QtCore.QEvent) -> None:
        """ Отслеживани состояния окна (свернуто/развёрнуто/активно/отображено + время) """
        # print(event.type())
        # ToDo Доделать
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.isMinimized():   # Для сворачивания окна
                self.ui.plainTextEdit.appendPlainText('Окно свернуто')

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        print(self.pos())

    def event(self, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.Resize:   # Можно было просто переопределить def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
            print(self.size())

        return QtWidgets.QWidget.event(self, event)


if __name__ == '__main__':
    app = QtWidgets.QApplication()   # создали цикл приложения

    win = MyWindow()

    win.show()   # высветили окно

    app.exec_()   # запустили приложения

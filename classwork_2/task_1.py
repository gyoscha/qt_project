import time
from PySide2 import QtWidgets, QtCore, QtGui
from classwork_2.UI.ui_classwork import Ui_MainWindow


import os
os.environ['QT_MAC_WANTS_LAYER'] = '1'   # Прописываю, чтобы открывалось MainWindow на Mac OS


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):   # Чтобы было отдельное окно parent = None
        super().__init__(parent)
        self.getSettingsValue()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox.addItems(["HEX", "DEC", "OCT", "BIN"])

        self.ui.window_data_button.setShortcut(QtGui.QKeySequence("A"))   # установка горячей клавиши на кнопку
        self.ui.window_data_button.clicked.connect(self.getscreeninfo)

        # Установка сигналов на кнопки положения программы
        self.ui.left_top_button.clicked.connect(self.onPBLTClicked)
        self.ui.right_top_button.clicked.connect(self.onPBRTClicked)
        self.ui.left_bottom_button.clicked.connect(self.onPBLBClicked)
        self.ui.right_bottom_button.clicked.connect(self.onPBRBClicked)
        self.ui.centre_button.clicked.connect(self.onPBCClicked)

        self.ui.dial.valueChanged.connect(self.showLCD)
        self.ui.slider.valueChanged.connect(self.showLCD)

        self.ui.dial.installEventFilter(self)
        self.ui.comboBox.currentIndexChanged.connect(self.changeLCDview)

        # SETTINGS
        self.lcd_value = self.settings_variables.value('lcd_value')
        self.ui.lcd.display(self.lcd_value)

        # ToDo доделать сохранение режима отображения чисел!!! Остальное сделано.
        # self.lcd_mode = self.settings_mode.value('lcd_mode')
        # if self.lcd_mode is not None:
        #     self.ui.lcd.setMode(self.lcd_mode)
        # else:
        #     self.ui.lcd.setHexMode()

    def getSettingsValue(self):
        self.settings_variables = QtCore.QSettings('MyWindow', 'Variables')
        self.settings_mode = QtCore.QSettings('MyWindow', 'Mode')

    def getscreeninfo(self):
        """Получение параметров экрана"""
        screens_count = QtWidgets.QApplication.screens()
        log = self.ui.text.appendPlainText

        log(f"{11*'='} SystemInfo {11*'='}")
        log(f"Кол-во экранов: {len(screens_count)}")
        log(f"Основное окно: {QtWidgets.QApplication.primaryScreen().name()}")
        for cur_screen in screens_count:
            log(f"Разрешение экрана {cur_screen.name()} составляет {cur_screen.size().width()} на {cur_screen.size().height()}")
        log(f"Окно находится на экране  {QtWidgets.QApplication.screenAt(self.pos()).name()}")
        log(f"Размеры окна:")
        log(f"{' ' * 25} Ширина {self.size().width()} ")
        log(f"{' ' * 25} Высота {self.size().height()}")
        log(f"Минимальные размеры окна:")
        log(f"{' ' * 25} Ширина {self.minimumWidth()}")
        log(f"{' ' * 25} Высота {self.minimumHeight()}")
        log(f"Текущее положение: x = {self.pos().x()}, y = {self.pos().y()}")
        log(f"Центр приложения: x = {self.pos().x() + self.width()/2}, y = {self.pos().y() + self.height()/2}")
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
        self.move(screenWidth - self.width(), 0)

    def onPBLBClicked(self):
        """ ЛЕВО-НИЗ """
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

    def showLCD(self):
        if self.sender().objectName() == "dial":
            value = self.ui.dial.value()
            self.ui.slider.setValue(value)
            self.ui.lcd.display(value)
        elif self.sender().objectName() == "slider":
            value = self.ui.slider.value()
            self.ui.dial.setValue(value)
            self.ui.lcd.display(value)

    def changeLCDview(self):

        a = {"HEX": self.ui.lcd.setHexMode, "BIN": self.ui.lcd.setBinMode,
             "OCT": self.ui.lcd.setOctMode, "DEC": self.ui.lcd.setDecMode}

        a[self.ui.comboBox.currentText()]()
        print(self.ui.lcd.mode())

        self.settings_mode.setValue('lcd_mode', self.ui.lcd.mode())  # SETTINGS

    # EVENTS
    def changeEvent(self, event: QtCore.QEvent) -> None:
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.isMinimized():   # Для сворачивания окна
                self.ui.text.appendPlainText(time.ctime() + ': Окно свернуто')
            elif self.isMaximized():
                self.ui.text.appendPlainText(time.ctime() + ': Окно развернуто')
        if event.type() == QtCore.QEvent.ActivationChange:
            self.ui.text.appendPlainText(time.ctime() + ': Окно активно')

        return QtWidgets.QWidget.changeEvent(self, event)

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        self.ui.text.appendPlainText(time.ctime() + ': Окно отображено')

        return QtWidgets.QWidget.showEvent(self, event)

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        print(self.pos())

        return QtWidgets.QWidget.moveEvent(self, event)

    def event(self, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.Resize:   # Можно было просто переопределить def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
            print(self.size())

        return QtWidgets.QWidget.event(self, event)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        print(f"{event.key()} нажата")

        return QtWidgets.QWidget.keyPressEvent(self, event)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent):

        if watched == self.ui.dial and event.type() == QtCore.QEvent.KeyPress:
            if event.text() == "+":
                self.ui.dial.setValue(self.ui.dial.value()+1)
            if event.text() == "-":
                self.ui.dial.setValue(self.ui.dial.value()-1)

            self.ui.text.appendPlainText(f"Значение dial: {self.ui.dial.value()}")

        return super(MyWindow, self).eventFilter(watched, event)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Закрыть окно",
                                                     "Вы хотите закрыть окно?",
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                     QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.settings_variables.setValue('lcd_value', self.ui.lcd.value())   # SETTINGS
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication()   # создали цикл приложения

    win = MyWindow()

    win.show()   # высветили окно

    app.exec_()   # запустили приложения

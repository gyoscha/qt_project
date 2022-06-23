from PySide2 import QtWidgets, QtCore
import time


class MyApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.initUi()

    def initUi(self):
        # init ui
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setPlaceholderText('Введите количество секунд')

        self.pbStart = QtWidgets.QPushButton()
        self.pbStart.setText('Старт')

        self.pbStop = QtWidgets.QPushButton()
        self.pbStop.setText('Стоп')
        self.pbStop.setEnabled(True)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.lineEdit)
        main_layout.addWidget(self.pbStart)
        main_layout.addWidget(self.pbStop)

        self.setLayout(main_layout)

        # init signals
        self.pbStart.clicked.connect(self.onPBStartClicked)
        self.pbStop.clicked.connect(self.onPBStopClicked)

    def onPBStartClicked(self):
        try:
            self.timerThread.timerCount = int(self.lineEdit.text())
            self.timerThread.start()
        except ValueError:
            self.lineEdit.setText('')
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Введено неправильное значение!')

    def onPBStopClicked(self):
        self.timerThread.status = False

    def initThreads(self):
        self.timerThread = TimerThread()

        # init signals
        self.timerThread.started.connect(self.timerThreadStarted)
        self.timerThread.finished.connect(self.timerThreadFinished)

        self.timerThread.timersignal.connect(self.timerSignalEmit)

    def timerThreadStarted(self):
        self.pbStart.setEnabled(False)
        self.pbStop.setEnabled(True)
        self.lineEdit.setEnabled(False)   # Блокируем поле ввода после старта

    def timerThreadFinished(self):
        self.pbStart.setEnabled(True)
        self.pbStop.setEnabled(False)
        self.lineEdit.setEnabled(True)

        self.lineEdit.setText('')

    def timerSignalEmit(self, emit_value):
        self.lineEdit.setText(emit_value)


class TimerThread(QtCore.QThread):
    timersignal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(TimerThread, self).__init__(parent)

        self.timerCount = None
        self.status = True

    def run(self) -> None:
        self.status = True
        while self.status:
            time.sleep(1)
            self.timerCount -= 1
            self.timersignal.emit(str(self.timerCount))

        # for i in range(self.timerCount, 0, -1):
        #     # print(i)
        #     self.timersignal.emit(str(i))
        #     time.sleep(1)


if __name__ == '__main__':
    app = QtWidgets.QApplication()  # создали цикл приложения

    win = MyApp()

    win.show()  # высветили окно

    app.exec_()  # запустили приложения



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_classwork.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 493)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_top_button = QPushButton(self.centralwidget)
        self.left_top_button.setObjectName(u"left_top_button")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_top_button.sizePolicy().hasHeightForWidth())
        self.left_top_button.setSizePolicy(sizePolicy)
        self.left_top_button.setMinimumSize(QSize(100, 30))

        self.horizontalLayout.addWidget(self.left_top_button)

        self.left_bottom_button = QPushButton(self.centralwidget)
        self.left_bottom_button.setObjectName(u"left_bottom_button")
        sizePolicy.setHeightForWidth(self.left_bottom_button.sizePolicy().hasHeightForWidth())
        self.left_bottom_button.setSizePolicy(sizePolicy)
        self.left_bottom_button.setMinimumSize(QSize(100, 30))

        self.horizontalLayout.addWidget(self.left_bottom_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.centre_button = QPushButton(self.centralwidget)
        self.centre_button.setObjectName(u"centre_button")
        sizePolicy.setHeightForWidth(self.centre_button.sizePolicy().hasHeightForWidth())
        self.centre_button.setSizePolicy(sizePolicy)
        self.centre_button.setMinimumSize(QSize(200, 30))

        self.verticalLayout.addWidget(self.centre_button)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.right_top_button = QPushButton(self.centralwidget)
        self.right_top_button.setObjectName(u"right_top_button")
        sizePolicy.setHeightForWidth(self.right_top_button.sizePolicy().hasHeightForWidth())
        self.right_top_button.setSizePolicy(sizePolicy)
        self.right_top_button.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.right_top_button)

        self.right_bottom_button = QPushButton(self.centralwidget)
        self.right_bottom_button.setObjectName(u"right_bottom_button")
        sizePolicy.setHeightForWidth(self.right_bottom_button.sizePolicy().hasHeightForWidth())
        self.right_bottom_button.setSizePolicy(sizePolicy)
        self.right_bottom_button.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.right_bottom_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.window_data_button = QPushButton(self.centralwidget)
        self.window_data_button.setObjectName(u"window_data_button")
        self.window_data_button.setMinimumSize(QSize(200, 30))
        self.window_data_button.setFlat(False)

        self.verticalLayout.addWidget(self.window_data_button)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QSize(100, 30))
        self.comboBox.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.comboBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setMinimumSize(QSize(50, 100))

        self.horizontalLayout_3.addWidget(self.dial)

        self.lcd = QLCDNumber(self.centralwidget)
        self.lcd.setObjectName(u"lcd")
        self.lcd.setMinimumSize(QSize(100, 200))

        self.horizontalLayout_3.addWidget(self.lcd)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.slider = QSlider(self.centralwidget)
        self.slider.setObjectName(u"slider")
        self.slider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.slider)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.text = QPlainTextEdit(self.centralwidget)
        self.text.setObjectName(u"text")

        self.horizontalLayout_4.addWidget(self.text)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.left_top_button.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.left_bottom_button.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0432\u043e/\u041d\u0438\u0437", None))
        self.centre_button.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.right_top_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.right_bottom_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043e/\u041d\u0438\u0437", None))
        self.window_data_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e\u043a\u043d\u0430", None))
    # retranslateUi


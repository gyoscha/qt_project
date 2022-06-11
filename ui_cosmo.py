# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cosmo.ui'
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
        MainWindow.setEnabled(True)
        MainWindow.resize(932, 673)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_12 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMouseTracking(False)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMouseTracking(False)
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(False)

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)


        self.horizontalLayout_2.addWidget(self.groupBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_6 = QCheckBox(self.groupBox_3)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_3.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.groupBox_3)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.verticalLayout_3.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.groupBox_3)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.verticalLayout_3.addWidget(self.checkBox_8)


        self.horizontalLayout_5.addWidget(self.groupBox_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.toolBox_2 = QToolBox(self.tab)
        self.toolBox_2.setObjectName(u"toolBox_2")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 442, 462))
        self.verticalLayout_5 = QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_7.addWidget(self.label)

        self.lineEdit_3 = QLineEdit(self.page_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_7.addWidget(self.lineEdit_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_8.addWidget(self.label_2)

        self.lineEdit_4 = QLineEdit(self.page_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_8.addWidget(self.lineEdit_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.lineEdit_5 = QLineEdit(self.page_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_9.addWidget(self.lineEdit_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.toolBox_2.addItem(self.page_3, u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 412, 425))
        self.horizontalLayout_4 = QHBoxLayout(self.page_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.page_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_10.addWidget(self.label_5)

        self.textEdit = QTextEdit(self.page_4)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_10.addWidget(self.textEdit)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_10)

        self.toolBox_2.addItem(self.page_4, u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 2")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_2 = QGroupBox(self.page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_2.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_2.addWidget(self.radioButton_4)

        self.radioButton_6 = QRadioButton(self.groupBox_2)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.verticalLayout_2.addWidget(self.radioButton_6)

        self.radioButton_5 = QRadioButton(self.groupBox_2)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.verticalLayout_2.addWidget(self.radioButton_5)

        self.radioButton_9 = QRadioButton(self.groupBox_2)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.verticalLayout_2.addWidget(self.radioButton_9)

        self.radioButton_10 = QRadioButton(self.groupBox_2)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.verticalLayout_2.addWidget(self.radioButton_10)


        self.horizontalLayout_6.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.page)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.radioButton_11 = QRadioButton(self.groupBox_4)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.verticalLayout_6.addWidget(self.radioButton_11)

        self.radioButton_12 = QRadioButton(self.groupBox_4)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.verticalLayout_6.addWidget(self.radioButton_12)

        self.radioButton_13 = QRadioButton(self.groupBox_4)
        self.radioButton_13.setObjectName(u"radioButton_13")

        self.verticalLayout_6.addWidget(self.radioButton_13)

        self.radioButton_14 = QRadioButton(self.groupBox_4)
        self.radioButton_14.setObjectName(u"radioButton_14")

        self.verticalLayout_6.addWidget(self.radioButton_14)

        self.radioButton_15 = QRadioButton(self.groupBox_4)
        self.radioButton_15.setObjectName(u"radioButton_15")

        self.verticalLayout_6.addWidget(self.radioButton_15)

        self.radioButton_16 = QRadioButton(self.groupBox_4)
        self.radioButton_16.setObjectName(u"radioButton_16")

        self.verticalLayout_6.addWidget(self.radioButton_16)

        self.radioButton_17 = QRadioButton(self.groupBox_4)
        self.radioButton_17.setObjectName(u"radioButton_17")

        self.verticalLayout_6.addWidget(self.radioButton_17)

        self.radioButton_18 = QRadioButton(self.groupBox_4)
        self.radioButton_18.setObjectName(u"radioButton_18")

        self.verticalLayout_6.addWidget(self.radioButton_18)


        self.horizontalLayout_6.addWidget(self.groupBox_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.toolBox_2.addItem(self.page, u" \u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 3")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.calendarWidget = QCalendarWidget(self.page_2)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMaximumSize(QSize(406, 16777215))

        self.verticalLayout_8.addWidget(self.calendarWidget)

        self.toolBox_2.addItem(self.page_2, u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 4")

        self.horizontalLayout_3.addWidget(self.toolBox_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_20 = QVBoxLayout(self.tab_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.groupBox_18 = QGroupBox(self.tab_2)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.groupBox_7 = QGroupBox(self.groupBox_18)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.groupBox_5 = QGroupBox(self.groupBox_7)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(131, 171))
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_11.addWidget(self.label_4)

        self.lineEdit = QLineEdit(self.groupBox_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(50, 22))

        self.horizontalLayout_11.addWidget(self.lineEdit)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_13.addWidget(self.label_6)

        self.lineEdit_2 = QLineEdit(self.groupBox_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(50, 22))

        self.horizontalLayout_13.addWidget(self.lineEdit_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_14.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(self.groupBox_5)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMaximumSize(QSize(50, 22))

        self.horizontalLayout_14.addWidget(self.lineEdit_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_15.addWidget(self.label_8)

        self.lineEdit_7 = QLineEdit(self.groupBox_5)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaximumSize(QSize(50, 22))

        self.horizontalLayout_15.addWidget(self.lineEdit_7)


        self.verticalLayout_9.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_16.addWidget(self.label_9)

        self.lineEdit_8 = QLineEdit(self.groupBox_5)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMaximumSize(QSize(50, 22))

        self.horizontalLayout_16.addWidget(self.lineEdit_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_18.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.groupBox_7)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMaximumSize(QSize(151, 191))
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_10 = QLabel(self.groupBox_6)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_17.addWidget(self.label_10)

        self.textEdit_2 = QTextEdit(self.groupBox_6)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(50, 22))
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_17.addWidget(self.textEdit_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_15 = QLabel(self.groupBox_6)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_22.addWidget(self.label_15)

        self.textEdit_7 = QTextEdit(self.groupBox_6)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setMaximumSize(QSize(50, 22))
        self.textEdit_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_22.addWidget(self.textEdit_7)


        self.verticalLayout_10.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_16 = QLabel(self.groupBox_6)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_23.addWidget(self.label_16)

        self.textEdit_8 = QTextEdit(self.groupBox_6)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setMaximumSize(QSize(50, 22))
        self.textEdit_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_23.addWidget(self.textEdit_8)


        self.verticalLayout_10.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_17 = QLabel(self.groupBox_6)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_24.addWidget(self.label_17)

        self.textEdit_9 = QTextEdit(self.groupBox_6)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setMaximumSize(QSize(50, 22))
        self.textEdit_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_24.addWidget(self.textEdit_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_18 = QLabel(self.groupBox_6)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_25.addWidget(self.label_18)

        self.textEdit_10 = QTextEdit(self.groupBox_6)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setMaximumSize(QSize(50, 22))
        self.textEdit_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_25.addWidget(self.textEdit_10)


        self.verticalLayout_10.addLayout(self.horizontalLayout_25)


        self.horizontalLayout_18.addWidget(self.groupBox_6)

        self.groupBox_8 = QGroupBox(self.groupBox_7)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMaximumSize(QSize(411, 151))
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tableWidget = QTableWidget(self.groupBox_8)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setBackground(QColor(0, 170, 0));
        __qtablewidgetitem2.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        brush1 = QBrush(QColor(0, 170, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setBackground(brush1);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_11.addWidget(self.tableWidget)


        self.horizontalLayout_18.addWidget(self.groupBox_8)


        self.verticalLayout_19.addWidget(self.groupBox_7)

        self.groupBox_17 = QGroupBox(self.groupBox_18)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.horizontalLayout_31 = QHBoxLayout(self.groupBox_17)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.groupBox_10 = QGroupBox(self.groupBox_17)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.groupBox_11 = QGroupBox(self.groupBox_10)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_11 = QLabel(self.groupBox_11)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_19.addWidget(self.label_11)

        self.textEdit_3 = QTextEdit(self.groupBox_11)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(50, 22))
        self.textEdit_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_19.addWidget(self.textEdit_3)


        self.verticalLayout_14.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_19 = QLabel(self.groupBox_11)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_26.addWidget(self.label_19)

        self.textEdit_11 = QTextEdit(self.groupBox_11)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setMaximumSize(QSize(50, 22))
        self.textEdit_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_26.addWidget(self.textEdit_11)


        self.verticalLayout_14.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_20 = QLabel(self.groupBox_11)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_27.addWidget(self.label_20)

        self.textEdit_12 = QTextEdit(self.groupBox_11)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setMaximumSize(QSize(50, 22))
        self.textEdit_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_27.addWidget(self.textEdit_12)


        self.verticalLayout_14.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_21 = QLabel(self.groupBox_11)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_28.addWidget(self.label_21)

        self.textEdit_13 = QTextEdit(self.groupBox_11)
        self.textEdit_13.setObjectName(u"textEdit_13")
        self.textEdit_13.setMaximumSize(QSize(50, 22))
        self.textEdit_13.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_28.addWidget(self.textEdit_13)


        self.verticalLayout_14.addLayout(self.horizontalLayout_28)


        self.verticalLayout_13.addWidget(self.groupBox_11)

        self.groupBox_9 = QGroupBox(self.groupBox_10)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.horizontalLayout_20 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalSlider_5 = QSlider(self.groupBox_9)
        self.verticalSlider_5.setObjectName(u"verticalSlider_5")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider_5.sizePolicy().hasHeightForWidth())
        self.verticalSlider_5.setSizePolicy(sizePolicy)
        self.verticalSlider_5.setMaximumSize(QSize(132, 16777213))
        self.verticalSlider_5.setOrientation(Qt.Vertical)

        self.horizontalLayout_20.addWidget(self.verticalSlider_5)

        self.verticalSlider = QSlider(self.groupBox_9)
        self.verticalSlider.setObjectName(u"verticalSlider")
        sizePolicy.setHeightForWidth(self.verticalSlider.sizePolicy().hasHeightForWidth())
        self.verticalSlider.setSizePolicy(sizePolicy)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_20.addWidget(self.verticalSlider)

        self.verticalSlider_2 = QSlider(self.groupBox_9)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        sizePolicy.setHeightForWidth(self.verticalSlider_2.sizePolicy().hasHeightForWidth())
        self.verticalSlider_2.setSizePolicy(sizePolicy)
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.horizontalLayout_20.addWidget(self.verticalSlider_2)

        self.verticalSlider_3 = QSlider(self.groupBox_9)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        sizePolicy.setHeightForWidth(self.verticalSlider_3.sizePolicy().hasHeightForWidth())
        self.verticalSlider_3.setSizePolicy(sizePolicy)
        self.verticalSlider_3.setOrientation(Qt.Vertical)

        self.horizontalLayout_20.addWidget(self.verticalSlider_3)

        self.horizontalSpacer_2 = QSpacerItem(55, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_2)

        self.verticalSlider_4 = QSlider(self.groupBox_9)
        self.verticalSlider_4.setObjectName(u"verticalSlider_4")
        sizePolicy.setHeightForWidth(self.verticalSlider_4.sizePolicy().hasHeightForWidth())
        self.verticalSlider_4.setSizePolicy(sizePolicy)
        self.verticalSlider_4.setOrientation(Qt.Vertical)

        self.horizontalLayout_20.addWidget(self.verticalSlider_4)


        self.verticalLayout_13.addWidget(self.groupBox_9)


        self.horizontalLayout_31.addWidget(self.groupBox_10)

        self.groupBox_16 = QGroupBox(self.groupBox_17)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_16)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.groupBox_12 = QGroupBox(self.groupBox_16)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.horizontalLayout_21 = QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.progressBar = QProgressBar(self.groupBox_12)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximum(1000)
        self.progressBar.setValue(200)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Vertical)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout_12.addWidget(self.progressBar)

        self.label_12 = QLabel(self.groupBox_12)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_12.addWidget(self.label_12)


        self.horizontalLayout_21.addLayout(self.verticalLayout_12)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.progressBar_2 = QProgressBar(self.groupBox_12)
        self.progressBar_2.setObjectName(u"progressBar_2")
        sizePolicy.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy)
        self.progressBar_2.setMaximum(1000)
        self.progressBar_2.setValue(300)
        self.progressBar_2.setOrientation(Qt.Vertical)

        self.verticalLayout_15.addWidget(self.progressBar_2)

        self.label_13 = QLabel(self.groupBox_12)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_15.addWidget(self.label_13)


        self.horizontalLayout_21.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.progressBar_3 = QProgressBar(self.groupBox_12)
        self.progressBar_3.setObjectName(u"progressBar_3")
        sizePolicy.setHeightForWidth(self.progressBar_3.sizePolicy().hasHeightForWidth())
        self.progressBar_3.setSizePolicy(sizePolicy)
        self.progressBar_3.setMaximum(1000)
        self.progressBar_3.setValue(500)
        self.progressBar_3.setOrientation(Qt.Vertical)

        self.verticalLayout_16.addWidget(self.progressBar_3)

        self.label_14 = QLabel(self.groupBox_12)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_16.addWidget(self.label_14)


        self.horizontalLayout_21.addLayout(self.verticalLayout_16)


        self.verticalLayout_18.addWidget(self.groupBox_12)

        self.groupBox_13 = QGroupBox(self.groupBox_16)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.groupBox_14 = QGroupBox(self.groupBox_13)
        self.groupBox_14.setObjectName(u"groupBox_14")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_14.sizePolicy().hasHeightForWidth())
        self.groupBox_14.setSizePolicy(sizePolicy1)
        self.horizontalLayout_29 = QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.pushButton = QPushButton(self.groupBox_14)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_29.addWidget(self.pushButton)


        self.verticalLayout_17.addWidget(self.groupBox_14)

        self.groupBox_15 = QGroupBox(self.groupBox_13)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.horizontalLayout_30 = QHBoxLayout(self.groupBox_15)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.pushButton_2 = QPushButton(self.groupBox_15)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_30.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.groupBox_15)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy3.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy3)

        self.horizontalLayout_30.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox_15)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy3.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy3)

        self.horizontalLayout_30.addWidget(self.pushButton_4)


        self.verticalLayout_17.addWidget(self.groupBox_15)


        self.verticalLayout_18.addWidget(self.groupBox_13)


        self.horizontalLayout_31.addWidget(self.groupBox_16)


        self.verticalLayout_19.addWidget(self.groupBox_17)


        self.verticalLayout_20.addWidget(self.groupBox_18)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout_12.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 932, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.toolBox_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">\u0433\u0440\u043f\u0430\u0432\u0433\u043f\u0438\u0444\u0433\u043f\u0438\u0432\u0433\u0444\u043f\u0438\u0432\u0433\u0444\u0432\u0444</span></p></body></html>", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 2", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_14.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_15.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_16.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_17.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_18.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page), QCoreApplication.translate("MainWindow", u" \u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 3", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0430\u043c\u043e\u043b\u0435\u0442", None))
        self.groupBox_7.setTitle("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"200 \u043a\u043c/\u0447", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0442\u043e-\u0442\u043e \u0435\u0449\u0435 ", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00ff00;\">500</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0431\u0430\u043a \u043e\u0431\u0449.", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00ff00;\">1000</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a 1", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00ff00;\">200</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a 2", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00ff00;\">300</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a 3", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00ff00;\">500</span></p></body></html>", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041e\u041a", None));
        ___qtablewidgetitem7 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u041a", None));
        ___qtablewidgetitem8 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u041a", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_17.setTitle("")
        self.groupBox_10.setTitle("")
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c 1", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00ff00;\">100</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c 2", None))
        self.textEdit_11.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00ff00;\">50</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c 3", None))
        self.textEdit_12.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00ff00;\">100</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c 4", None))
        self.textEdit_13.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00ff00;\">100</span></p></body></html>", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.groupBox_16.setTitle("")
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043f\u043b\u0438\u0432\u043e", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a 1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a 2", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a 3", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.groupBox_14.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.groupBox_15.setTitle("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
    # retranslateUi


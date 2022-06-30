import sqlite3
import sys

from PySide2.QtSql import QSqlDatabase, QSqlQuery
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtSql, QtCore, QtWidgets

from exam.ui import ui_db


# import os
# os.environ['QT_MAC_WANTS_LAYER'] = '1'   # Прописываю, чтобы открывалось MainWindow на Mac OS


class MyDBClient(QMainWindow):
    def __init__(self, parent=None):  # Чтобы было отдельное окно parent = None
        super().__init__(parent)

        self.ui = ui_db.Ui_MainWindow()
        self.ui.setupUi(self)

        self.initSQLModel()

    def initSQLModel(self):

        con = sqlite3.connect(db_path)
        # self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        # self.db.setDatabaseName('todo.db')

        self.model = QtSql.QSqlTableModel()
        self.model.setTable('note_note')

        self.model.select()

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnHidden(0, True)
        self.ui.tableView.horizontalHeader().setSectionsMovable(True)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyDBClient()
    window.show()

    sys.exit(app.exec_())

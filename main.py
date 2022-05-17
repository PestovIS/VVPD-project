"""from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import plates as p
import students as s
import studadd as sa
import mainmenu as m
import platesteam as t


if __name__ == "__main__":
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.show()"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class Wmainmenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupMainmenu(self)
        self.show()


    def setupMainmenu(self, Form):
        Form.setObjectName("Form")
        Form.resize(871, 458)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 370, 181, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.PushButton_2_wtd)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 50, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.PushButton_3_wtd)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 80, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.PushButton_3_wtd)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(45, 20, 191, 381))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(640, 30, 191, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(640, 90, 191, 61))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 180, 161, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textBrowser.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.textBrowser_2.raise_()
        self.textEdit.raise_()
        self.pushButton_5.raise_()

        self.retranslateMainmenu(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateMainmenu(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "Выйти"))
        self.pushButton_3.setText(_translate("Form", "Поток тест"))
        self.pushButton_4.setText(_translate("Form", "Поток пустой"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Выберите поток</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Добавить поток</p></body></html>"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Учебный год:</p></body></html>"))
        self.pushButton_5.setText(_translate("Form", "Добавить"))

    def PushButton_3_wtd(self):
        self.window = Wplates()
        self.close()
        self.window.show()

    def PushButton_2_wtd(self):
        self.hide()


class Wplates(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupPlates(self)
        self.show()


    def setupPlates(self, Form):
        Form.setObjectName("Form")
        Form.resize(871, 456)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 80, 161, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.PushButton_1_wtd)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 80, 161, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.PushButton_1_wtd)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 80, 161, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 80, 161, 81))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(690, 360, 161, 81))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.PushButton_5_wtd)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(90, 10, 131, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(340, 10, 131, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(590, 10, 131, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(90, 40, 131, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(340, 40, 131, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(690, 250, 161, 81))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslatePlates(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslatePlates(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Команда 1"))
        self.pushButton_2.setText(_translate("Form", "Команда 4"))
        self.pushButton_3.setText(_translate("Form", "Команда 3"))
        self.pushButton_4.setText(_translate("Form", "Команда 2"))
        self.pushButton_5.setText(_translate("Form", "Назад"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Название:</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Учебный год:</p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Команды:</p></body></html>"))
        self.pushButton_6.setText(_translate("Form", "Добавить команду"))

    def PushButton_5_wtd(self):
        self.window = Wmainmenu()
        self.close()
        self.window.show()

    def PushButton_1_wtd(self):
        self.window = Wplatesteam()
        self.close()
        self.window.show()


class Wplatesteam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupPlatesteam(self)
        self.show()

    def setupPlatesteam(self, Form):
        Form.setObjectName("Form")
        Form.resize(871, 464)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 256, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 180, 151, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.PushButton_2_wtd)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 280, 151, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(300, 20, 171, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(520, 20, 171, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 380, 151, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.PushButton_4_wtd)

        self.retranslatePlatesteam(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslatePlatesteam(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "№ коммитов"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "Откр. задач"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "Тек. задач"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "Закр. задач"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "Качество"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "Послед. релиз"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "Удалений"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "Добавлений"))
        self.pushButton_2.setText(_translate("Form", "Студенты"))
        self.pushButton_3.setText(_translate("Form", "Дополнительно"))
        self.textBrowser.setHtml(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Название:</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Form",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ссылка:</p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "Назад"))

    def PushButton_4_wtd(self):
        self.window = Wplates()
        self.close()
        self.window.show()

    def PushButton_2_wtd(self):
        self.window = Wstudents()
        self.close()
        self.window.show()


class Wstudents(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupStudents(self)
        self.show()


    def setupStudents(self, Form):
        Form.setObjectName("Form")
        Form.resize(870, 480)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 256, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(310, 20, 256, 192))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(710, 360, 151, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.PushButton_1_wtd)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 260, 151, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.PushButton_2_wtd)

        self.retranslateStudents(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateStudents(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "ФИО"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "Группа"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "Форма обуч."))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "ВК"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "Гитхаб"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Form", "ФИО"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("Form", "Группа"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("Form", "Форма обуч."))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("Form", "ВК"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("Form", "Гитхаб"))
        self.pushButton.setText(_translate("Form", "Назад"))
        self.pushButton_2.setText(_translate("Form", "Добавить студента"))

    def PushButton_1_wtd(self):
        self.window = Wplatesteam()
        self.close()
        self.window.show()

    def PushButton_2_wtd(self):
        self.window = Wstudadd()
        self.close()
        self.window.show()


class Wstudadd(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupStudadd(self)
        self.show()


    def setupStudadd(self, Form):
        Form.setObjectName("Form")
        Form.resize(869, 458)
        self.tableWidget_3 = QtWidgets.QTableWidget(Form)
        self.tableWidget_3.setGeometry(QtCore.QRect(30, 60, 371, 192))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(600, 370, 181, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.PushButton_6_wtd)
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(590, 110, 161, 81))
        self.pushButton_8.setObjectName("pushButton_8")

        self.retranslateStudadd(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateStudadd(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("Form", "ФИО"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("Form", "Группа"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("Form", "Форма обуч."))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("Form", "ВК"))
        item = self.tableWidget_3.verticalHeaderItem(4)
        item.setText(_translate("Form", "Гитхаб"))
        self.pushButton_6.setText(_translate("Form", "Назад"))
        self.pushButton_8.setText(_translate("Form", "Добавить"))

    def PushButton_6_wtd(self):
        self.window = Wstudents()
        self.close()
        self.window.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Wmainmenu()

# start the app
sys.exit(App.exec())

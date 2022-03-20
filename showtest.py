from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
from main import Tax_cal
from UI.newui import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.validator = QtGui.QIntValidator()
        self.ui.lineEdit.setValidator(self.validator)
        self.ui.lineEdit.textChanged.connect(self.text_changed)
        self.ui.lineEdit_2.setValidator(self.validator)
        self.ui.pushButton.setText('Calculate')
        self.ui.lineEdit_2.setEnabled(0)
        self.ui.pushButton.setEnabled(0)
        self.ui.pushButton.clicked.connect(self.button_clicked)
        self.ui.pushButton_2.clicked.connect(self.clear)
        self.ui.radioButton_2.toggled.connect(self.btn_single)
        self.ui.radioButton.toggled.connect(self.btn_marry)

    def text_changed(self,s):
        if not s:
            self.ui.pushButton.setEnabled(0)
        if s:
            self.ui.pushButton.setEnabled(1)

    def clear(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()

    def button_clicked(self):
        _translate = QtCore.QCoreApplication.translate
        text = self.ui.lineEdit.text()
        text2 = self.ui.lineEdit_2.text()
        Male = int(text)
        if self.ui.radioButton_2.isChecked():
            calculation = Tax_cal()
            data= calculation.single(Male)
            x = 0
            for i in data:
                item = self.ui.tableWidget.item(x, 0)
                item.setText(_translate("MainWindow", str(data[x])))
                x=x+1
            x = 0
            for i in data:
                item = self.ui.tableWidget.item(x, 1)
                item.setText(_translate("MainWindow", "N/A"))
                x=x+1
            x = 0
            for i in data:
                item = self.ui.tableWidget.item(x, 2)
                item.setText(_translate("MainWindow", "N/A"))
                x=x+1
        if self.ui.radioButton.isChecked():
            Female = int(text2)
            calculation = Tax_cal()
            data1 = calculation.single(Male)
            data2 = calculation.single(Female)
            data3 = calculation.joint(Male, Female)
            x = 0
            for i in data1:
                item = self.ui.tableWidget.item(x, 0)
                item.setText(_translate("MainWindow", str(data1[x])))
                x = x + 1
            x = 0
            for i in data2:
                item = self.ui.tableWidget.item(x, 1)
                item.setText(_translate("MainWindow", str(data2[x])))
                x = x + 1
            x = 0
            for i in data3:
                item = self.ui.tableWidget.item(x, 2)
                item.setText(_translate("MainWindow", str(data3[x])))
                x = x + 1
            noticestring = calculation.compare(data3[4],data1[4],data2[4])
            self.ui.label_4.setText(noticestring)

    def btn_single(self):
        self.ui.radioButton_2 = self.sender()
        if self.ui.radioButton_2.isChecked():
            self.ui.lineEdit_2.setEnabled(0)

    def btn_marry(self):
        self.ui.radioButton = self.sender()
        if self.ui.radioButton.isChecked():
            self.ui.lineEdit_2.setEnabled(1)
            self.ui.lineEdit_2.textChanged.connect(self.text_changed)
            self.ui.pushButton.setEnabled(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
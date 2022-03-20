from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1095, 528)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(140, 290, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 170, 113, 20))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(10, 220, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Nueva Std")
        font.setPointSize(16)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 150, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Nueva Std")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setTabletTracking(False)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 140, 47, 12))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 210, 47, 12))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 240, 113, 20))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(280, 60, 781, 291))
        font = QtGui.QFont()
        font.setFamily("PMingLiU")
        font.setPointSize(20)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.verticalHeader().setDefaultSectionSize(45)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 30, 471, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 290, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tax_calculation"))
        self.pushButton.setText(_translate("MainWindow", "Go"))
        self.radioButton.setText(_translate("MainWindow", "Married"))
        self.radioButton_2.setText(_translate("MainWindow", "Single"))
        self.label_2.setText(_translate("MainWindow", "Self"))
        self.label_3.setText(_translate("MainWindow", "Spouse"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Yearly Income"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "MPF Deduction"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Basic / Married Allowances"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Net Chargeable Income"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tax Payable"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Self"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Spouse"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Joint"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "\"\""))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "\"\""))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "\"\""))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "\"\""))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "\"\""))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "\"\""))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "\"\""))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "\"\""))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "\"\""))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "\"\""))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "\"\""))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("MainWindow", "\"\""))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "\"\""))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "\"\""))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("MainWindow", "\"\""))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
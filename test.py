# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(830, 414)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 631, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tabWidget.setIconSize(QtCore.QSize(2, 16))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 631, 301))
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 631, 301))
        self.tableWidget_2.setDragEnabled(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab_2, "")
        
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 110, 551, 171))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.layoutWidget = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 144, 62))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(430, 20, 140, 40))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_3.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_3.addWidget(self.radioButton_5)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 340, 811, 71))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(650, 20, 171, 318))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_10.setAutoDefault(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7, 0, QtCore.Qt.AlignTop)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tabWidget, self.radioButton_3)
        Dialog.setTabOrder(self.radioButton_3, self.radioButton_2)
        Dialog.setTabOrder(self.radioButton_2, self.radioButton)
        Dialog.setTabOrder(self.radioButton, self.radioButton_4)
        Dialog.setTabOrder(self.radioButton_4, self.radioButton_5)
        Dialog.setTabOrder(self.radioButton_5, self.plainTextEdit)
        Dialog.setTabOrder(self.plainTextEdit, self.pushButton_10)
        Dialog.setTabOrder(self.pushButton_10, self.pushButton_7)
        Dialog.setTabOrder(self.pushButton_7, self.pushButton_9)
        Dialog.setTabOrder(self.pushButton_9, self.pushButton_6)
        Dialog.setTabOrder(self.pushButton_6, self.pushButton_8)
        Dialog.setTabOrder(self.pushButton_8, self.plainTextEdit_2)
        Dialog.setTabOrder(self.plainTextEdit_2, self.tableWidget)
        Dialog.setTabOrder(self.tableWidget, self.tableWidget_2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "MQ_NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "MQ_STATUS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "MQ"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "No"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "S_NAME"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "S_STATUS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Service Schedule"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "Running SQL :"))
        self.radioButton_3.setText(_translate("Dialog", "EDI BATCH Channel"))
        self.radioButton_2.setText(_translate("Dialog", "EDI Receive Channel"))
        self.radioButton.setText(_translate("Dialog", "EDI Send Channel"))
        self.radioButton_4.setText(_translate("Dialog", "Active"))
        self.radioButton_5.setText(_translate("Dialog", "Inactive"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "DB schedule"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "WF Terminated"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "WF Restart"))
        self.plainTextEdit_2.setPlainText(_translate("Dialog", "~~ have been updated successfully."))
        self.pushButton_10.setText(_translate("Dialog", "Search"))
        self.pushButton_7.setText(_translate("Dialog", "Active"))
        self.pushButton_9.setText(_translate("Dialog", "Inactive"))
        self.pushButton_6.setText(_translate("Dialog", "Add"))
        self.pushButton_8.setText(_translate("Dialog", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

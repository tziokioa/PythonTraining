# Form implementation generated from reading ui file 'E:\python_course\examples\face.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(584, 450)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 20, 361, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 70, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 70, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(80, 120, 451, 321))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Dialog)
        self.pushButton_3.clicked.connect(Dialog.close)
        self.pushButton.clicked.connect(self.insert)
        self.pushButton_2.clicked.connect(self.remove)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Insert"))
        self.pushButton_2.setText(_translate("Dialog", "Delete"))
        self.pushButton_3.setText(_translate("Dialog", "Exit"))

    def insert(self):
        pass
        text=self.lineEdit.text()
        if len(text):
            self.listWidget.addItem(text)
            self.lineEdit.clear()
        
    def remove(self):
        pass
        row=self.listWidget.currentRow()
        self.listWidget.takeItem(row)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


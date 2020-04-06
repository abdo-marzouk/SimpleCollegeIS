from PyQt5 import QtCore, QtGui, QtWidgets
import icons

class Ui_DeleteForm(object):
    def setupUi(self, DeleteForm):
        DeleteForm.setObjectName("DeleteForm")
        DeleteForm.resize(260, 70)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DeleteForm.setWindowIcon(icon)
        self.DeleteInput = QtWidgets.QLineEdit(DeleteForm)
        self.DeleteInput.setGeometry(QtCore.QRect(190, 10, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.DeleteInput.setFont(font)
        self.DeleteInput.setPlaceholderText("")
        self.DeleteInput.setObjectName("DeleteInput")
        self.label = QtWidgets.QLabel(DeleteForm)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.SearchButton = QtWidgets.QPushButton(DeleteForm)
        self.SearchButton.setGeometry(QtCore.QRect(100, 40, 75, 23))
        self.SearchButton.setObjectName("SearchButton")

        self.retranslateUi(DeleteForm)
        QtCore.QMetaObject.connectSlotsByName(DeleteForm)

    def retranslateUi(self, DeleteForm):
        _translate = QtCore.QCoreApplication.translate
        DeleteForm.setWindowTitle(_translate("DeleteForm", "Delete student"))
        self.label.setText(_translate("DeleteForm", "Delete with ID"))
        self.SearchButton.setText(_translate("DeleteForm", "Delete"))
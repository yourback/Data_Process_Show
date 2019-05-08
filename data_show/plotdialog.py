# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotdialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(598, 529)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mplw = MatplotlibDialog(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplw.sizePolicy().hasHeightForWidth())
        self.mplw.setSizePolicy(sizePolicy)
        self.mplw.setObjectName("mplw")
        self.verticalLayout.addWidget(self.mplw)
        self.showydata = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showydata.sizePolicy().hasHeightForWidth())
        self.showydata.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.showydata.setFont(font)
        self.showydata.setAlignment(QtCore.Qt.AlignCenter)
        self.showydata.setObjectName("showydata")
        self.verticalLayout.addWidget(self.showydata)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "图形"))
        self.showydata.setText(_translate("Dialog", "TextLabel"))


from data_show.plot import MatplotlibDialog

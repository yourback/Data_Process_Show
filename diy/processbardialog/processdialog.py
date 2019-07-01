# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'processdialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(294, 104)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ll_process_text = QtWidgets.QLabel(dialog)
        self.ll_process_text.setAlignment(QtCore.Qt.AlignCenter)
        self.ll_process_text.setObjectName("ll_process_text")
        self.verticalLayout.addWidget(self.ll_process_text)
        self.pb_process = QtWidgets.QProgressBar(dialog)
        self.pb_process.setProperty("value", 24)
        self.pb_process.setObjectName("pb_process")
        self.verticalLayout.addWidget(self.pb_process)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_process_cancel = QtWidgets.QPushButton(dialog)
        self.btn_process_cancel.setObjectName("btn_process_cancel")
        self.horizontalLayout.addWidget(self.btn_process_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "程序执行中"))
        self.ll_process_text.setText(_translate("dialog", "当前状态"))
        self.btn_process_cancel.setText(_translate("dialog", "取消"))



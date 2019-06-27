# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainview.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(72, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.filename = QtWidgets.QLineEdit(self.centralwidget)
        self.filename.setEnabled(True)
        self.filename.setMinimumSize(QtCore.QSize(171, 0))
        self.filename.setMaximumSize(QtCore.QSize(267, 16777215))
        self.filename.setReadOnly(True)
        self.filename.setObjectName("filename")
        self.horizontalLayout_3.addWidget(self.filename)
        self.choosefile = QtWidgets.QPushButton(self.centralwidget)
        self.choosefile.setMaximumSize(QtCore.QSize(93, 16777215))
        self.choosefile.setObjectName("choosefile")
        self.horizontalLayout_3.addWidget(self.choosefile)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.layout_userprogramming = QtWidgets.QVBoxLayout()
        self.layout_userprogramming.setObjectName("layout_userprogramming")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.layout_userprogramming.addWidget(self.label_2)
        self.le_vars = QtWidgets.QLineEdit(self.centralwidget)
        self.le_vars.setMinimumSize(QtCore.QSize(364, 21))
        self.le_vars.setMaximumSize(QtCore.QSize(364, 16777215))
        self.le_vars.setObjectName("le_vars")
        self.layout_userprogramming.addWidget(self.le_vars, 0, QtCore.Qt.AlignHCenter)
        self.lines_worker_result = QtWidgets.QLabel(self.centralwidget)
        self.lines_worker_result.setObjectName("lines_worker_result")
        self.layout_userprogramming.addWidget(self.lines_worker_result)
        self.te_program = QtWidgets.QTextEdit(self.centralwidget)
        self.te_program.setObjectName("te_program")
        self.layout_userprogramming.addWidget(self.te_program)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_loadprogram = QtWidgets.QPushButton(self.centralwidget)
        self.btn_loadprogram.setObjectName("btn_loadprogram")
        self.horizontalLayout_4.addWidget(self.btn_loadprogram)
        self.btn_saveprogram = QtWidgets.QPushButton(self.centralwidget)
        self.btn_saveprogram.setObjectName("btn_saveprogram")
        self.horizontalLayout_4.addWidget(self.btn_saveprogram)
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run.setObjectName("btn_run")
        self.horizontalLayout_4.addWidget(self.btn_run)
        self.layout_userprogramming.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.layout_userprogramming)
        self.layout_varchoose = QtWidgets.QHBoxLayout()
        self.layout_varchoose.setObjectName("layout_varchoose")
        self.varslist = QtWidgets.QListWidget(self.centralwidget)
        self.varslist.setObjectName("varslist")
        self.layout_varchoose.addWidget(self.varslist)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setMidLineWidth(0)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.btn_novars = QtWidgets.QPushButton(self.centralwidget)
        self.btn_novars.setObjectName("btn_novars")
        self.verticalLayout_2.addWidget(self.btn_novars)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 3)
        self.layout_varchoose.addLayout(self.verticalLayout_2)
        self.varsselect = QtWidgets.QListWidget(self.centralwidget)
        self.varsselect.setObjectName("varsselect")
        self.layout_varchoose.addWidget(self.varsselect)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_o = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_o.setObjectName("cb_o")
        self.verticalLayout.addWidget(self.cb_o)
        self.btn_paint = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_paint.sizePolicy().hasHeightForWidth())
        self.btn_paint.setSizePolicy(sizePolicy)
        self.btn_paint.setObjectName("btn_paint")
        self.verticalLayout.addWidget(self.btn_paint)
        self.layout_varchoose.addLayout(self.verticalLayout)
        self.layout_varchoose.setStretch(0, 1)
        self.layout_varchoose.setStretch(1, 1)
        self.layout_varchoose.setStretch(2, 2)
        self.verticalLayout_4.addLayout(self.layout_varchoose)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.about = LabelClickable(self.centralwidget)
        self.about.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.about.setObjectName("about")
        self.horizontalLayout.addWidget(self.about)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 6)
        self.verticalLayout_4.setStretch(2, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据编程显示系统"))
        self.label.setText(_translate("MainWindow", "数据源："))
        self.choosefile.setText(_translate("MainWindow", "选择文件"))
        self.label_2.setText(_translate("MainWindow", "变量声明：（;分隔）"))
        self.lines_worker_result.setText(_translate("MainWindow", "逻辑处理："))
        self.btn_loadprogram.setText(_translate("MainWindow", "载入程序"))
        self.btn_saveprogram.setText(_translate("MainWindow", "保存程序"))
        self.btn_run.setText(_translate("MainWindow", "运行程序"))
        self.label_4.setText(_translate("MainWindow", "=>"))
        self.btn_novars.setText(_translate("MainWindow", "清空"))
        self.cb_o.setText(_translate("MainWindow", "数据描点"))
        self.btn_paint.setText(_translate("MainWindow", "生成\n"
"折线图"))
        self.about.setText(_translate("MainWindow", "当前版本号：V0.2"))


from diy.label_clickable import LabelClickable

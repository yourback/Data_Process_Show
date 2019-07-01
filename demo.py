import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QAbstractItemView

from data_show.mainview import Ui_MainWindow

# 文件操作
from data_process.varsprocess import vars_process
from diy.aboutdialog.amdialog import AMDialog
from diy.processbardialog.processbardialog import PROCESSDialog
from diy.settings import version_code, app_name
from file_operation.getlinesnum import GetLineWorker
from file_operation.loadprogram import load_program
from file_operation.saveprogram import save_program
from file_operation.selectsourcefile import get_source_data_file

# dialog
from data_show.mpldview import MPLDialog


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)
        self.lines_worker = GetLineWorker()
        # 界面初始化
        self.init_ui()
        # dialog初始化
        self.init_dialog()
        # 变量名与变量值的对应的字典
        self.name_value = {}
        # 软件名称
        self.setWindowTitle(app_name)
        # 软件版本
        self.about.setText(version_code)

    def init_ui(self):
        # 首先将后两个不布局设置隐藏
        # self.layout_userprogramming.setVisible(False)
        # self.layout_varchoose.setVisible(False)
        # 列表单项不可以编辑
        self.varslist.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.varsselect.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 各种监听的设置
        self.init_listener()

    # dialog初始化
    def init_dialog(self):
        self.about_dialog = AMDialog()
        # self.process_dialog = PROCESSDialog()

    def init_listener(self):
        self.choosefile.clicked.connect(self.choose_file)
        self.btn_loadprogram.clicked.connect(self.btn_load_program_click)
        self.btn_saveprogram.clicked.connect(self.btn_save_program_click)
        self.btn_run.clicked.connect(self.run_program)
        self.lines_worker.work_finish.connect(self.lines_worker_finish)

        self.varslist.itemDoubleClicked.connect(self.vars_list_doubleclick)
        self.varsselect.itemDoubleClicked.connect(self.vars_select_doubleclick)

        self.btn_novars.clicked.connect(self.btn_novars_click)

        # 生成折线图
        self.btn_paint.clicked.connect(self.btn_paint_click)

        # 更新日志
        self.about.clicked.connect(self.about_click)

    def about_click(self):
        '''查看升级日志'''
        self.about_dialog.exec()

    def btn_novars_click(self):
        '''清空选择变量'''
        self.name_value.clear()
        if self.varsselect.count() != 0:
            self.varsselect.clear()
        else:
            QMessageBox.information(self, '提示', '您还就没有选择变量')

    def btn_paint_click(self):
        '''生成折线图'''
        if self.varsselect.count() == 0:
            QMessageBox.information(self, '提示', '先选择变量')
        else:
            vars_name = []
            vars_value = []
            for i in range(self.varsselect.count()):
                nickname = self.varsselect.item(i).text()
                vars_name.append(nickname)
                # V0.2 有备注
                # vars_value.append(self.name_value[nickname[:nickname.rindex('(')]])
                # V0.3 无备注
                vars_value.append(self.name_value[nickname])
            # print('画图')
            ui = MPLDialog(title=vars_name.__str__())
            ui.start_plot(vars_name, vars_value, self.cb_o.isChecked())
            # ui.mpl.start_static_plot(vars_name, vars_value)
            ui.show()
            ui.exec_()

    def vars_list_doubleclick(self, item):
        # print('变量选择框，点击事件' + item.text())
        # 验证exec适用范围    验证结果只在本方法内生效
        # try:
        #     print(eval(item.text()))
        # except Exception as error:
        #     print('eval出错了：%s' % error)
        # 是否已经选择过了
        isSelected = False
        # V0.3 需求删除备注，直接添加到self.varsselect中
        if self.varsselect:
            for i in range(self.varsselect.count()):
                txt = self.varsselect.item(i).text()
                if txt == item.text():
                    isSelected = True
                    QMessageBox.information(self, '提示', '这个变量已经选择过了')
        if not isSelected:
            self.varsselect.addItem(item.text())
        # 以下是V0.2 有备注
        # if self.varsselect:
        #     for i in range(self.varsselect.count()):
        #         txt = self.varsselect.item(i).text()
        #         if txt[:txt.rindex('(')] == item.text():
        #             isSelected = True
        #             QMessageBox.information(self, '提示', '这个变量已经选择过了')
        # if not isSelected:
        #     text, ok = QInputDialog.getText(self, '名称设置', '输入%s的名称：' % item.text())
        #     if ok:
        #         if text:
        #             self.varsselect.addItem('%s(%s)' % (item.text(), text.strip()))
        #         else:
        #             QMessageBox.information(self, '提示', '请输入变量名称')

    def vars_select_doubleclick(self, item):
        # print('变量显示框，点击事件')
        # 删除item+数据
        self.varsselect.removeItemWidget(self.varsselect.takeItem(self.varsselect.row(item)))

    def choose_file(self):
        '''选择源文件'''
        file_name = get_source_data_file(self)
        if file_name:
            self.filename.setText(file_name)
            # 开线程获取文件行数
            self.lines_worker.getlines(file_name)

    def lines_worker_finish(self, num):
        '''统计行数完成'''
        self.linesnum = num
        self.lines_worker_result.setText('逻辑处理：（循环%s次）' % num)

    def btn_load_program_click(self):
        '''加载程序点击事件'''
        var, program = load_program(self)
        if var and program:
            self.le_vars.setText(var)
            self.te_program.setText(program)
            self.varsselect.clear()
            self.varslist.clear()

    def btn_save_program_click(self):
        '''保存程序点击事件'''
        var = self.le_vars.text()
        program = self.te_program.toPlainText()
        if var and program:
            save_program(self, self.le_vars.text(), self.te_program.toPlainText())
        else:
            QMessageBox.information(self, '错误', '请填写变量和程序', QMessageBox.Yes)

    def run_program(self):
        '''执行程序点击事件'''
        var = self.le_vars.text()
        program = self.te_program.toPlainText()
        if var and program:
            # 变量处理
            vars_name = self.le_vars.text().replace(' ', '')
            vars_name_list = vars_name.split(';')
            # 消除重复的变量
            vars_name_list = list(set(vars_name_list))
            # 获得变量数据
            vars_value_list = vars_process(vars_name_list, self.linesnum, self.filename.text())
            try:
                # 变量赋值
                self.update_status('变量赋值中')
                for i, _ in enumerate(vars_name_list):
                    sen = '%s=%s' % (vars_name_list[i], vars_value_list[i])
                    exec(sen)

                # 用户自定义程序运行
                self.update_status('程序运行')
                for i in range(self.linesnum):
                    self.update_status('进度 %s/%s' % (i, self.linesnum))
                    program = self.te_program.toPlainText()
                    exec(program)

                self.varslist.clear()
                self.varslist.addItems(vars_name_list)
                # V0.3 检查是否在变量列表中有这一项，没有的话就删除，有的话就保留这个已经选择的变量
                for i in range(self.varsselect.count()):
                    txt = self.varsselect.item(i).text()
                    print('已经选择变量：%s' % txt)
                    if txt not in vars_name_list:
                        print('%s在变量列表中不存在' % txt)
                        self.varsselect.takeItem(i)

                # 清空之前的运算结果
                self.name_value.clear()
                # 保存这次运算结果
                self.update_status('保存运行结果')
                for var_name in vars_name_list:
                    self.name_value[var_name] = eval(var_name)
                self.update_status('运行结束')
                QMessageBox.information(self, '提示', '执行完毕', QMessageBox.Yes)
            except Exception as error:
                QMessageBox.warning(self, '程序错误', error.__str__(), QMessageBox.Yes)
        else:
            QMessageBox.information(self, '错误', '请填写变量和程序', QMessageBox.Yes)

    def keyPressEvent(self, event):
        '''键盘点击'''
        if event.key() == Qt.Key_S:
            if self.te_program.hasFocus() or self.le_vars.hasFocus():
                self.btn_save_program_click()

    # 刷新状态栏
    def update_status(self, str_status_text):
        self.statusbar.showMessage('运行状态：%s' % str_status_text, 1000)
        QApplication.processEvents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QAbstractItemView, QInputDialog

from data_show.mainview import Ui_MainWindow

# 文件操作
from data_process.varsprocess import vars_process
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
        self.init_ui()
        # 变量名与变量值的对应的字典
        self.name_value = {}

    def init_ui(self):
        # 首先将后两个不布局设置隐藏
        # self.layout_userprogramming.setVisible(False)
        # self.layout_varchoose.setVisible(False)
        # 列表单项不可以编辑
        self.varslist.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.varsselect.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 各种监听的设置
        self.init_listener()

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
                vars_value.append(self.name_value[nickname[:nickname.rindex('(')]])
            # print('画图')
            ui = MPLDialog(title=vars_name.__str__())
            ui.start_plot(vars_name, vars_value)
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
        if self.varsselect:
            for i in range(self.varsselect.count()):
                txt = self.varsselect.item(i).text()
                if txt[:txt.rindex('(')] == item.text():
                    isSelected = True
                    QMessageBox.information(self, '提示', '这个变量已经选择过了')
        if not isSelected:
            text, ok = QInputDialog.getText(self, '名称设置', '输入%s的名称：' % item.text())
            if ok:
                if text:
                    self.varsselect.addItem('%s(%s)' % (item.text(), text.strip()))
                else:
                    QMessageBox.information(self, '提示', '请输入变量名称')

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
        self.le_vars.setText(var)
        self.te_program.setText(program)

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
            vars_name = self.le_vars.text()
            vars_name_list = vars_name.split(';')
            # print(vars_name_list)
            vars_name_list = list(set(vars_name_list))
            vars_value_list = vars_process(vars_name_list, self.linesnum, self.filename.text())
            # print(vars_value_list)
            try:
                for i, _ in enumerate(vars_name_list):
                    sen = '%s=%s' % (vars_name_list[i], vars_value_list[i])
                    # print(sen)
                    exec(sen)
                    # exec('''print('%s的值为%s')''' % (str(vars_name_list[i]), str(vars_value_list[i])))
                # 用户自定义程序运行
                for i in range(self.linesnum):
                    program = self.te_program.toPlainText()
                    # print(program)
                    exec(program)

                QMessageBox.information(self, '提示', '执行完毕', QMessageBox.Yes)
                # 执行成功，添加变量到下面的列表
                # print(vars_name_list)
                self.varslist.clear()
                self.varsselect.clear()
                self.varslist.addItems(vars_name_list)

                # 清空之前的运算结果
                self.name_value.clear()
                # 保存这次运算结果
                for var_name in vars_name_list:
                    self.name_value[var_name] = eval(var_name)
                # print("结果：%s" % self.name_value)
                # print(self.name_value)
            except Exception as error:
                print(error)
                QMessageBox.warning(self, '程序错误', error.__str__(), QMessageBox.Yes)
        else:
            QMessageBox.information(self, '错误', '请填写变量和程序', QMessageBox.Yes)

    def keyPressEvent(self, event):
        '''键盘点击'''
        if event.key() == Qt.Key_S:
            if self.te_program.hasFocus() or self.le_vars.hasFocus():
                self.btn_save_program_click()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

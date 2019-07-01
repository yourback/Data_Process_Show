from PyQt5.QtCore import QThread

from data_process.varsprocess import vars_process


class ExecWorker(QThread):
    def __init__(self):
        super().__init__()

    def update_data(self, var_name, list_var_value, str_program, run_num, data_file_name):
        self.var_name = var_name
        self.var_value = list_var_value
        self.program = str_program
        self.run_num = run_num
        self.data_file_name = data_file_name

    def run(self):
        vars_name_list = self.var_name.split(';')
        # 消除重复的变量
        vars_name_list = list(set(vars_name_list))
        # 获得变量数据
        vars_value_list = vars_process(vars_name_list, self.run_num, self.data_file_name)
        try:
            # 变量赋值
            for i, _ in enumerate(vars_name_list):
                sen = '%s=%s' % (vars_name_list[i], vars_value_list[i])
                # print(sen)
                exec(sen)
                # exec('''print('%s的值为%s')''' % (str(vars_name_list[i]), str(vars_value_list[i])))
                print('赋值完成')

            # 用户自定义程序运行
            self.process_dialog.update_status('执行程序')
            for i in range(self.linesnum):
                print('程序与运行%s遍' % i)
                program = self.te_program.toPlainText()
                # print(program)
                exec(program)

            # 保存这次运算结果
            for var_name in vars_name_list:
                self.name_value[var_name] = eval(var_name)

            return

            # V0.3 检查是否在变量列表中有这一项，没有的话就删除，有的话就保留这个已经选择的变量
            for i in range(self.varsselect.count()):
                txt = self.varsselect.item(i).text()
                print('已经选择变量：%s' % txt)
                if txt not in vars_name_list:
                    print('%s在变量列表中不存在' % txt)
                    self.varsselect.takeItem(i)
        except Exception as error:
            self.process_dialog.close()
            return ''

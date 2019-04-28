from PyQt5.QtWidgets import QFileDialog


def save_program(self, vars_content, program_content):
    f_name, _ = QFileDialog.getSaveFileName(self, '保存程序', '..', '*.txt')
    if f_name:
        with open(f_name, 'w') as f:
            f.write('varstart' + vars_content + 'varend' + '\n')
            f.write('programstart' + program_content + 'programend')

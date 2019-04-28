from PyQt5.QtWidgets import QFileDialog


def load_program(self):
    f_name, _ = QFileDialog.getOpenFileName(self, '选择程序', '..', "TXT files (*.txt)")
    if f_name:
        with open(f_name, 'r') as f:
            file_content = f.read()
        vars_start = file_content.index('varstart') + len("varstart")
        vars_end = file_content.rindex('varend')
        program_start = file_content.index('programstart') + len("programstart")
        program_end = file_content.rindex('programend')

        return file_content[vars_start: vars_end], file_content[program_start: program_end]
    else:
        return '', ''

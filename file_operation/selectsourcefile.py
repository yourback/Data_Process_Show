from PyQt5.QtWidgets import QFileDialog


def get_source_data_file(self):
    f_name, _ = QFileDialog.getOpenFileName(self, '选择数据源', '..', "TXT files (*.txt)")
    return f_name

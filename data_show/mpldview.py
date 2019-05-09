from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

from data_show.plotdialog import Ui_Dialog


class MPLDialog(QDialog, Ui_Dialog):
    def __init__(self, title, parent=None):
        super(MPLDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(title)
        self.mplw.mpl.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.setWindowFlag(Qt.WindowMinMaxButtonsHint)

    # mouse click
    def on_press(self, event):
        # print('点击事件触发')
        # print('坐标：（%s,%s）' % (event.xdata, event.ydata))
        try:
            var = event.xdata % 0.02
            if var > 0.01:
                x = round(event.xdata - var + 0.02, 2)
            else:
                x = round(event.xdata - var, 2)

            x_index = int(x / 0.02)

            if x_index > len(self.valuelist[0]):
                x_index = len(self.valuelist[0]) - 1

            # print('x_index:%s' % x_index)
            y_text = ''
            for i, v in enumerate(self.namelist):
                if y_text:
                    y_text = y_text + 'x:%s    %s：%s\n' % (x, v, self.valuelist[i][x_index if x_index > 0 else 0])
                else:
                    y_text = 'x:%s    %s：%s\n' % (x, v, self.valuelist[i][x_index if x_index > 0 else 0])
                # print(y_text)
            self.showydata.setText(y_text)
        except Exception as e:
            print(e)
            QMessageBox.information(self, '提示', '未点击坐标系区域内')

    # 绘图
    def start_plot(self, var_name_list, var_value_list):
        self.namelist = var_name_list
        self.valuelist = var_value_list
        self.mplw.mpl.start_static_plot(var_name_list, var_value_list)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = MPLDialog('gogog')
    ui.show()
    sys.exit(app.exec_())

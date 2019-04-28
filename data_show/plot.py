import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout, QApplication, QDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from numpy.ma import arange


class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # 设置中文
        plt.rcParams['font.family'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        # 新建一个绘制对象
        self.fig = Figure(figsize=(width, height), dpi=dpi, tight_layout=True)

        self.axes = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)

        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def start_static_plot(self, var_name_list, var_value_list):
        t = arange(0, len(var_value_list[0]) * 0.02, 0.02)
        for i, var_name in enumerate(var_name_list):
            self.axes.plot(t, var_value_list[i], '-', label=var_name)

        self.axes.grid(True)
        self.axes.legend()
        self.axes.set_xlabel('time(s)')


class MatplotlibDialog(QDialog):
    def __init__(self, title, parent=None):
        super(MatplotlibDialog, self).__init__(parent)
        self.title = title
        self.initUi()

    def initUi(self):
        self.setWindowTitle(self.title)
        self.layout = QVBoxLayout(self)
        # self.mpl = MyMplCanvas(self, width=5, height=4, dpi=100)
        self.mpl = MyMplCanvas(self)

        self.mpl_ntp = NavigationToolbar(self.mpl, self)

        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntp)

        # 窗口最大化
        # self.showMaximized()
        self.setWindowFlag(Qt.WindowMinMaxButtonsHint)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibDialog('绘图')
    varlist = [0 for _ in range(1000)]
    var_name_list = ['a', 'b', 'c']
    var_name_list1 = map(lambda n: n + 1, varlist)
    var_value_list = [varlist, list(map(lambda n: n + 1, varlist)), list(map(lambda n: n + 10, varlist))]
    ui.mpl.start_static_plot(var_name_list, var_value_list)
    ui.show()
    sys.exit(app.exec_())

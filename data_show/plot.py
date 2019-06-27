import sys
from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout, QApplication, QWidget
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

    def start_static_plot(self, var_name_list, var_value_list, is_show_o):
        t = arange(0, len(var_value_list[0]) * 0.02, 0.02)
        for i, var_name in enumerate(var_name_list):
            self.axes.plot(t, var_value_list[i], '-o' if is_show_o else '-', label=var_name)

        self.axes.grid(True)
        self.axes.legend()
        self.axes.set_xlabel('time(s)')


class MatplotlibDialog(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibDialog, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        # self.mpl = MyMplCanvas(self, width=5, height=4, dpi=100)
        self.mpl = MyMplCanvas(self)
        self.mpl_ntp = NavigationToolbar(self.mpl, self)
        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibDialog()
    ui.show()
    sys.exit(app.exec_())

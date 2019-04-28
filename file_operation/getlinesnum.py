# 为了不卡，增加线程读取文件行数
from PyQt5.QtCore import QThread, pyqtSignal


class GetLineWorker(QThread):
    work_finish = pyqtSignal(int)

    def __init__(self, parent=None):
        super(GetLineWorker, self).__init__(parent)
        self.num = 0

    def getlines(self, file):
        count = len(open(file, 'rU').readlines())
        self.work_finish.emit(count)

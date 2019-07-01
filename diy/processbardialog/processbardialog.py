from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication

from diy.processbardialog.processdialog import Ui_dialog


class PROCESSDialog(QDialog, Ui_dialog):
    def __init__(self, parent=None):
        super(PROCESSDialog, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_btn_process_cancel_clicked(self):
        self.close()

    def updata_process(self, process):
        print(process)

    def update_status(self, status_text):
        print(status_text)
        self.set_process_text(status_text)

    def set_process_text(self, str):
        self.ll_process_text.setText('当前状态：%s' % str)

    def closeEvent(self, QCloseEvent):
        self.pb_process.setValue(0)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = PROCESSDialog()
    ui.show()
    sys.exit(app.exec_())

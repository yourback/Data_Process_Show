from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QDialog, QApplication

from diy.aboutdialog.aboutme import Ui_Dialog
from diy.settings import update_log, version_code, app_name


class AMDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(AMDialog, self).__init__(parent)
        self.setupUi(self)
        self.textBrowser.setText(update_log)
        self.version_code.setText(version_code)
        self.app_name.setText('软件名称：%s' % app_name)

    def closeEvent(self, QCloseEvent):
        # 每次关闭的时候 滚动到开始
        self.textBrowser.moveCursor(QTextCursor.Start)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = AMDialog()
    ui.show()
    sys.exit(app.exec_())

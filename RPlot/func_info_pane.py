from PyQt5.Qt import *
from func_info import Ui_Dialog
from PyQt5 import  QtCore

class Func_info_Pane(QDialog, Ui_Dialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.textBrowser.setOpenExternalLinks(True)
        self.setWindowTitle("RPlot")

    def OK_btn_func_info_c(self):
        self.close()



if __name__ == '__main__':
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    window = Func_info_Pane()
    window.show()

    sys.exit(app.exec_())

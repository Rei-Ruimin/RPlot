from PyQt5.Qt import *
from progressbar import Ui_Dialog
import os
from func_plot import plot_and_save_func
from plot_and_save_scatter import plot_and_save_scatter
from PyQt5 import QtCore, QtWidgets

class ExecuteThread(QThread):

    def __init__(self, filename_d, filename_t, filename_s, utime, uaxis, ptitle,
                 data_ver, save_v, save_i):
        super(ExecuteThread, self).__init__()
        self.fd = filename_d
        self.ft = filename_t
        self.ds = filename_s
        self.ut = utime
        self.uax = uaxis
        self.pt = ptitle
        self.dv = data_ver
        self.sv = save_v
        self.si = save_i

    def run(self):
        # do something here
        plot_and_save_scatter(self.fd, self.ft, self.ds,
                              self.ut, self.uax, self.pt,
                              self.dv, self.sv, self.si)


class ExecuteThread2(QThread):

    def __init__(self, func_str, x1_i, x2_i, y1_i, y2_i, t1_i, t2_i, tnum, save_dir):
        super(ExecuteThread2, self).__init__()
        self.f = func_str
        self.x1 = x1_i
        self.x2 = x2_i
        self.y1 = y1_i
        self.y2 = y2_i
        self.t1 = t1_i
        self.t2 = t2_i
        self.tn = tnum
        self.sd = save_dir
        print("here")

    def run(self):
        # do something here
        print("f start")
        plot_and_save_func(self.f, self.x1, self.x2, self.y1, self.y2,
                           self.t1, self.t2, self.tn, self.sd)
        print("f end")


class Progressbar_Pane(QDialog, Ui_Dialog):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("RPlot")

    def pb_finished(self):
        print(1)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(100)
        self.ok_btn.setEnabled(True)
        self.msg.setText("Finished!")

    def open_folder(self):
        os.startfile(os.path.join(self.folder_dir, "Output"))
        self.close()

    def call_scatter_thread(self, filename_d, filename_t, filename_s, utime, uaxis, ptitle,
                         data_ver, save_v, save_i):
        self.test = ExecuteThread(filename_d, filename_t, filename_s, utime, uaxis, ptitle,
                                  data_ver, save_v, save_i)
        self.folder_dir = filename_s
        self.test.start()
        self.test.finished.connect(self.pb_finished)

    def call_func_thread(self, func_str, x1_i, x2_i, y1_i, y2_i, t1_i, t2_i, tnum, save_dir):
        self.test2 = ExecuteThread2(func_str, x1_i, x2_i, y1_i, y2_i, t1_i, t2_i, tnum, save_dir)
        self.folder_dir = save_dir
        self.test2.start()
        self.test2.finished.connect(self.pb_finished)


if __name__ == '__main__':
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    app = QApplication(sys.argv)

    window = Progressbar_Pane()
    #window.finished()
    window.show()

    sys.exit(app.exec_())

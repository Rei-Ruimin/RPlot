from PyQt5 import QtCore
from PyQt5.Qt import *
from myGUI_pane import MyGUIPane
from progressbar_pane import Progressbar_Pane
from func_info_pane import Func_info_Pane


if __name__ == '__main__':
    import sys
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    myGUI_pane = MyGUIPane()
    progressbar_pane = Progressbar_Pane(myGUI_pane)
    func_info_pane = Func_info_Pane(myGUI_pane)

    def open_func_info_pane():
        func_info_pane.show()

    myGUI_pane.function_info_signal.connect(open_func_info_pane)

    def handle_data(filename_d, filename_t, filename_s, utime, uaxis, ptitle,
                    data_ver, save_v, save_i):
        progressbar_pane.open()
        progressbar_pane.call_scatter_thread(filename_d, filename_t, filename_s,
                                              utime, uaxis, ptitle,
                                              data_ver, save_v, save_i)

    myGUI_pane.collect_all_data_signal.connect(handle_data)

    def handle_data2(func_str, x1_i, x2_i, y1_i, y2_i, t1_i, t2_i, tnum, save_dir):
        progressbar_pane.open()
        progressbar_pane.call_func_thread(func_str, x1_i, x2_i, y1_i, y2_i, t1_i, t2_i, tnum, save_dir)

    myGUI_pane.collect_all_data_signal2.connect(handle_data2)
    myGUI_pane.show()
    sys.exit(app.exec_())

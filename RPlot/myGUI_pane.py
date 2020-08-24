from final_GUI import Ui_Form
from PyQt5.Qt import *
import os
from PyQt5 import QtCore


class MyGUIPane(QWidget, Ui_Form):
    collect_all_data_signal = pyqtSignal(str, str, str, str, str, str, bool, bool, bool)
    collect_all_data_signal2 = pyqtSignal(str, str, str, str, str, str, str, str, str)
    function_info_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("RPlot")
        self.data_ver_rbtn.setToolTip("X Y T0 T1\n-  -  -  -\n-  -  -  -\n-  -  -  -")
        self.data_hor_rbtn.setToolTip("X  -  -  -  -\nY  -  -  -  -\nT0 -  -  -  -\nT1 -  -  -  -")

    # 设置子控件
    def collect_all_data(self):
        # collect all inputs
        filename_t = self.timeF_line.text()
        filename_d = self.dataF_line.text()
        filename_s = self.saveDir_line.text()
        utime = self.utime_line.text()
        uaxis = self.uaxis_line.text()
        ptitle = self.title_line.text()

        data_ver = self.data_ver_rbtn.isChecked()
        save_v = self.save_v_box.isChecked()
        save_i = self.save_i_box.isChecked()

        # check the data
        if filename_t == "" or filename_d == "" or filename_s == "":
            self.blank_file_error_msg()
        elif save_v == False and save_i == False:
            self.checkbox_error_msg()
        elif os.path.isdir(os.path.join(filename_s, "Output")):
            self.save_dir_error_msg()
        else:
            self.collect_all_data_signal.emit(filename_d, filename_t, filename_s,
                                              utime, uaxis, ptitle,
                                              data_ver, save_v, save_i)

    def dataF_btn_c(self):
        filename_d = QFileDialog.getOpenFileName(self, "Choose the data file", "", "TXT(*.txt)")
        self.dataF_line.setText(filename_d[0])

    def timeF_btn_c(self):
        filename_t = QFileDialog.getOpenFileName(self, "Choose the time parameter file", "", "TXT(*.txt)")
        self.timeF_line.setText(filename_t[0])

    def saveDir_btn_c(self):
        filedir_s = QFileDialog.getExistingDirectory(self, "Choose the save directory", "")
        self.saveDir_line.setText(filedir_s)

    def savedir_btn2_c(self):
        filedir_s = QFileDialog.getExistingDirectory(self, "Choose the save directory", "")
        self.savedir_line2.setText(filedir_s)

    def checkbox_error_msg(self):
        cb_msg = QMessageBox(QMessageBox.Warning, "RPlot",
                             "Please select at least one type of file you need.",
                             QMessageBox.Ok, self)
        cb_msg.open()

    def save_dir_error_msg(self):
        sd_msg = QMessageBox(QMessageBox.Warning, "RPlot",
                             "There is already a folder named 'Output'\nin the save directory you choose.",
                             QMessageBox.Ok, self)
        sd_msg.open()

    def blank_file_error_msg(self):
        bf_msg = QMessageBox(QMessageBox.Warning, "RPlot",
                             "Please select all required files and directory.",
                             QMessageBox.Ok, self)
        bf_msg.open()

    def blank_line_error_msg(self):
        bl_msg = QMessageBox(QMessageBox.Warning, "RPlot",
                             "Please fill every blank.",
                             QMessageBox.Ok, self)
        bl_msg.open()

    def invalid_input_msg(self):
        ii_msg = QMessageBox(QMessageBox.Warning, "RPlot",
                             "Please make sure the scales are valid numbers.",
                             QMessageBox.Ok, self)
        ii_msg.open()

    def collect_all_data2(self):
        # collect all inputs
        func_str = self.func_i_2.text()
        x1 = self.xmin_i_2.text()
        x2 = self.xmax_i_2.text()
        y1 = self.ymin_i_2.text()
        y2 = self.ymax_i_2.text()
        t1 = self.tmin_i_2.text()
        t2 = self.tmax_i_2.text()
        tnum = self.tnum_i_2.text()
        save_dir2 = self.savedir_line2.text()
        input_scale_list = [x1, x2, y1, y2, t1, t2]

        # check blank line
        if func_str == "" or x1 == "" or x2 == ""or\
                y1 == "" or y2 == "" or t1 == "" or\
                t2 == "" or tnum == "" or save_dir2 == "":
            self.blank_line_error_msg()
            return

        # make sure inputs are valid number
        for num in input_scale_list:
            if (not isinstance(num, int)) and (not isinstance(num, float)):
                self.invalid_input_msg()
                return

        if (not isinstance(tnum, int)) or (tnum <= 0):
            self.invalid_input_msg()
            return

        # if everything is good
        self.collect_all_data_signal2.emit(func_str, x1, x2, y1, y2, t1, t2, tnum, save_dir2)

    def function_info_c(self):
        self.function_info_signal.emit()


if __name__ == '__main__':
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    window = MyGUIPane()
    window.show()
    sys.exit(app.exec_())

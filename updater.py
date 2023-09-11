from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import *
from main_funcs.thread_class.update_version_class import *
import sys,os
import data.gui_data.file_rc

class UpdaterUi(QtWidgets.QDialog):
    def __init__(self):
        super(UpdaterUi, self).__init__()
        uic.loadUi('./data/gui_data/updater.ui', self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.pressing = False
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_start_update.clicked.connect(self.start_update)
        self.label.setVisible(False)
    
    def progress_val(self, value):
        self.label.setText(value)
        if value == "Yükleme Tamamlandı":
            os.startfile("GTO.exe")
            self.close()
    
    def start_update(self):
        self.thread = UpdateVersionClass(parent = None, index = 0)
        self.thread.start()
        self.thread.progress_signal.connect(self.pro_bar.setValue)
        self.thread.progress_info_signal.connect(self.progress_val)
        self.btn_start_update.setVisible(False)
        self.label.setVisible(True)
        
        

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(), 
                                self.mapToGlobal(self.movement).y(), 
                                self.width(), 
                                self.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def btn_close_clicked(self):
        self.close()

    def btn_min_clicked(self):
        self.showMinimized()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UpdaterUi()
    window.show()
    sys.exit(app.exec_())
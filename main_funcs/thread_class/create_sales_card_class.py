from PyQt5 import QtCore
class SalesCardClass(QtCore.QThread):
    label_69signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(SalesCardClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.tools.create_sales_card as csc
            if self.barcode:choice = 0
            elif self.no_barcode:choice = 1
            csc.create_sales_card(self.save_directory,self.institution,self.student_class,self.period,int(self.start_num),int(self.end_num),choice)
            self.label_69signal.emit("Oluşturuldu!")
        except:
            self.label_69signal.emit("Hata!")
        
        
    def stop(self):
        self.is_running = False
        self.terminate()
        

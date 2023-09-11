from PyQt5 import QtCore

class UploadIOPSPdfClass(QtCore.QThread):
    label_83signal = QtCore.pyqtSignal(str)

    def __init__(self, parent: None,index=0):
        super(UploadIOPSPdfClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        import main_funcs.tools.iops_file_separation as ifs
        try:
            if self.test_type_ps1 == True:
                test_type = "test_1step_1"
            elif self.test_type_ps2 == True:
                test_type = "test_1step_2"
            elif self.test_type_js == True:
                test_type = "test_3_standard"
            elif self.test_type_test_4 == True:
                test_type = "test_4"
            if self.score_report == True:
                ifs.all_sr_sep(self.upload_file,self.save_directory,test_type,self.upload_school,str(self.upload_date.toString('dd-MM-yyyy')))
                self.label_83signal.emit(self.upload_school+' IOPS Score Report bölündü.')
            elif self.certificate == True:
                if test_type == "test_1step_1" or test_type == "test_1step_2":
                    ifs.pri_c_sep(self.upload_file,self.save_directory,test_type,self.upload_school,str(self.upload_date.toString('dd-MM-yyyy')))
                elif test_type =="test_3_standard" or test_type == "test_4":
                    ifs.js_test_4_c_sep(self.upload_file,self.save_directory,test_type,self.upload_school,str(self.upload_date.toString('dd-MM-yyyy')))
                self.label_83signal.emit(self.upload_school+' IOPS Certificate bölündü.')
        except:
            self.label_83signal.emit('Belge oluşturulamadı!')

    def stop(self):
        self.is_running = False
        self.terminate()
        

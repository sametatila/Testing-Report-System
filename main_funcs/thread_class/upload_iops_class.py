from PyQt5 import QtCore

class UploadIOPSClass(QtCore.QThread):
    label_41signal = QtCore.pyqtSignal(str)
    all_result_list_signal = QtCore.pyqtSignal(list)
    def __init__(self, parent: None,index=0):
        super(UploadIOPSClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):        
        try:
            import main_funcs.db_student_post.main_iops as mi
            country = mi.get_school_info(self.upload_school)[0][0]
            city = mi.get_school_info(self.upload_school)[0][1]
            if self.test_type_ps1 == True:
                ps1_list = mi.ps1_db_aktar(self.upload_file,self.upload_form_code,country,city,str(self.upload_date.toString('dd-MM-yyyy')),self.upload_school)
                self.all_result_list_signal.emit(ps1_list)
                if len(ps1_list[1]) > 0: 
                    self.label_41signal.emit('Yüklenemedi!')
                else:
                    self.label_41signal.emit('Başarılı!')
            elif self.test_type_ps2 == True:
                ps2_list = mi.ps2_db_aktar(self.upload_file,self.upload_form_code,country,city,str(self.upload_date.toString('dd-MM-yyyy')),self.upload_school)
                self.all_result_list_signal.emit(ps2_list)
                if len(ps2_list[1]) > 0: 
                    self.label_41signal.emit('Yüklenemedi!')
                else:
                    self.label_41signal.emit('Başarılı!')
            elif self.test_type_js == True:
                js_list = mi.js_db_aktar(self.upload_file,self.upload_form_code,country,city,str(self.upload_date.toString('dd-MM-yyyy')),self.upload_school)
                self.all_result_list_signal.emit(js_list)
                if len(js_list[1]) > 0: 
                    self.label_41signal.emit('Yüklenemedi!')
                else:
                    self.label_41signal.emit('Başarılı!')
            if self.test_type_test_4 == True:
                try:
                    test_4_list = mi.test_4_db_aktar(self.upload_file,self.upload_form_code,country,city,str(self.upload_date.toString('dd-MM-yyyy')),self.upload_school)
                    self.all_result_list_signal.emit(test_4_list)
                    if len(test_4_list[1]) > 0: 
                        self.label_41signal.emit('Yüklenemedi!')
                    else:
                        self.label_41signal.emit('Başarılı!')
                except:
                    self.label_41signal.emit('Plan dışı öğrenci var!')
        except:
            self.label_41signal.emit('Yüklenemedi!')
        
    def stop(self):
        self.is_running = False
        self.terminate()

class UploadIOPStest_4Class(QtCore.QThread):
    label_41signal = QtCore.pyqtSignal(str)
    all_result_list_signal_1 = QtCore.pyqtSignal(list)
    def __init__(self, parent: None,index=0):
        super(UploadIOPStest_4Class, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.db_student_post.main_iops as mi
            country = mi.get_school_info(self.upload_school)[0][0]
            city = mi.get_school_info(self.upload_school)[0][1]
            test_4_list = mi.test_4_db_aktar_no_class(self.upload_file,self.upload_form_code,country,city,str(self.upload_date.toString('dd-MM-yyyy')),self.upload_school)
            self.all_result_list_signal_1.emit(test_4_list)
            if len(test_4_list[1]) == 0: 
                self.label_41signal.emit('Başarılı! Fakat TC son hane ve sınıf yok!')
            else:
                self.label_41signal.emit('Yüklenemedi!')
        except:
            self.label_41signal.emit('Yüklenemedi!')
        
    def stop(self):
        self.is_running = False
        self.terminate()
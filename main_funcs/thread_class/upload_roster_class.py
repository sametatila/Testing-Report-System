from PyQt5 import QtCore

class UploadRosterClass(QtCore.QThread):
    label_47signal = QtCore.pyqtSignal(str)
    all_result_list_signal2 = QtCore.pyqtSignal(list)
    def __init__(self, parent: None,index=0):
        super(UploadRosterClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.db_student_post.main_roster as mr
            country = mr.get_school_info(self.upload_school)[0][0]
            city = mr.get_school_info(self.upload_school)[0][1]
            if self.test_type_ps1 == True:
                ps1_list = mr.ps1_db_aktar(self.upload_file,self.upload_form_code,country,city,str(self.upload_date.toString('dd-MM-yyyy')),self.upload_school)
                self.all_result_list_signal2.emit(ps1_list)
                if len(ps1_list[1]) > 0: 
                    self.label_47signal.emit('Yüklenemedi!')
                else:
                    self.label_47signal.emit('Başarılı!')
            elif self.test_type_ps2 == True:
                ps2_list = mr.ps2_db_aktar(self.upload_file,self.upload_form_code,country,city,str(self.upload_date.toString('dd-MM-yyyy')),self.upload_school)
                self.all_result_list_signal2.emit(ps2_list)
                if len(ps2_list[1]) > 0: 
                    self.label_47signal.emit('Yüklenemedi!')
                else:
                    self.label_47signal.emit('Başarılı!')
            elif self.test_type_js == True:
                js_list = mr.js_db_aktar(self.upload_file,self.upload_form_code,country,city,str(self.upload_date.toString('dd-MM-yyyy')),self.upload_school)
                self.all_result_list_signal2.emit(js_list)
                if len(js_list[1]) > 0: 
                    self.label_47signal.emit('Yüklenemedi!')
                else:
                    self.label_47signal.emit('Başarılı!')
            if self.test_type_test_4 == True:
                try:
                    test_4_list = mr.test_4_db_aktar(self.upload_file,self.upload_form_code,country,city,str(self.upload_date.toString('dd-MM-yyyy')),self.upload_school)
                    self.all_result_list_signal2.emit(test_4_list)
                    if len(test_4_list[1]) > 0: 
                        self.label_47signal.emit('Yüklenemedi!')
                    else:
                        self.label_47signal.emit('Başarılı!')
                except:
                    self.label_47signal.emit('Plan dışı öğrenci var!')
            if self.test_type_pspk == True:
                pspk_list = mr.pspk_db_aktar(self.upload_file,self.upload_form_code,country,city,str(self.upload_date.toString('dd-MM-yyyy')),self.upload_school)
                self.all_result_list_signal2.emit(pspk_list)
                if len(pspk_list[1]) > 0: 
                    self.label_47signal.emit('Yüklenemedi!')
                else:
                    self.label_47signal.emit('Başarılı!')
            if self.test_type_jspk == True:
                jspk_list = mr.jspk_db_aktar(self.upload_file,self.upload_form_code,country,city,str(self.upload_date.toString('dd-MM-yyyy')),self.upload_school)
                self.all_result_list_signal2.emit(jspk_list)
                if len(jspk_list[1]) > 0: 
                    self.label_47signal.emit('Yüklenemedi!')
                else:
                    self.label_47signal.emit('Başarılı!')
        except:
            self.label_47signal.emit('Yüklenemedi!')
        
    def stop(self):
        self.is_running = False
        self.terminate()

class UploadRostertest_4Class(QtCore.QThread):
    label_47signal = QtCore.pyqtSignal(str)
    all_result_list_signal_3 = QtCore.pyqtSignal(list)
    def __init__(self, parent: None,index=0):
        super(UploadRostertest_4Class, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        import main_funcs.db_student_post.main_roster as mr
        country = mr.get_school_info(self.upload_school)[0][0]
        city = mr.get_school_info(self.upload_school)[0][1]
        try:
            test_4_list = mr.test_4_db_aktar_no_class(self.upload_file,self.upload_form_code,country,city,str(self.upload_date.toString('dd-MM-yyyy')),self.upload_school)
            self.all_result_list_signal_3.emit(test_4_list)
            if len(test_4_list[1]) == 0: 
                self.label_47signal.emit('Başarılı! Fakat TC son hane ve sınıf yok!')
            else:
                self.label_47signal.emit('Yüklenemedi!')
        except:
            self.label_47signal.emit('Yüklenemedi!')
        
    def stop(self):
        self.is_running = False
        self.terminate()
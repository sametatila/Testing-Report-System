from PyQt5 import QtCore

class GetDeleteSchoolResultClass(QtCore.QThread):
    all_result_2_signal = QtCore.pyqtSignal(object)

    def __init__(self, parent: None,index=0):
        super(GetDeleteSchoolResultClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        import main_funcs.score_docs.get_school_result as gsr
        if self.test_type_ps1 == True:
            all_result = gsr.get_school_result_list("test_1step_1","",self.institution,self.main_date,'')
            self.all_result_2_signal.emit(all_result)
        elif self.test_type_ps2 == True:
            all_result = gsr.get_school_result_list("test_1step_2","",self.institution,self.main_date,'')
            self.all_result_2_signal.emit(all_result)
        elif self.test_type_pspk == True:
            all_result = gsr.get_school_result_list("test_1speaking","",self.institution,self.main_date,'')
            self.all_result_2_signal.emit(all_result)
        elif self.test_type_js == True:
            all_result = gsr.get_school_result_list("test_3_standard","",self.institution,self.main_date,'')
            self.all_result_2_signal.emit(all_result)
        elif self.test_type_jspk == True:
            all_result = gsr.get_school_result_list("test_3_speaking","",self.institution,self.main_date,'')
            self.all_result_2_signal.emit(all_result)
        elif self.test_type_test_4 == True:
            all_result = gsr.get_school_result_list("test_4","",self.institution,self.main_date,'')
            self.all_result_2_signal.emit(all_result)
        
    def stop(self):
        self.is_running = False
        self.terminate()

class DeleteSchoolResultClass(QtCore.QThread):
    def __init__(self, parent: None,index=0):
        super(DeleteSchoolResultClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        import main_funcs.score_docs.delete_school_result as dsr
        dsr.delete_school_result_by_date(self.test_type,self.institution,self.main_date)

    def stop(self):
        self.is_running = False
        self.terminate()
        
class DeleteSelectedResultClass(QtCore.QThread):
    all_result_3_signal = QtCore.pyqtSignal(object)
    def __init__(self, parent: None,index=0):
        super(DeleteSelectedResultClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        import main_funcs.score_docs.delete_school_result as dsr
        dsr.delete_selected_result_by_date(self.test_type,self.institution,self.main_date,self.main_list)

    def stop(self):
        self.is_running = False
        self.terminate()
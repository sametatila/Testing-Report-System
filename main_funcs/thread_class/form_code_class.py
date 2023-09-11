from PyQt5 import QtCore
import main_funcs.mixed.form_code_funcs as fcf

class GetFormCodeInfoClass(QtCore.QThread):
    label_43signal = QtCore.pyqtSignal(str)
    edit_test_type_comboBoxsignal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(GetFormCodeInfoClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            form_code = self.form_code
            test_type_list = ['Test Type 1','Test Type 2','Test Type 3','Test Type 4','Test Type 5','Test Type 6']
            form_code_info = fcf.get_form_code(form_code)
            if form_code_info[1] in test_type_list:
                self.edit_test_type_comboBoxsignal.emit(form_code_info[1])
                self.label_43signal.emit(form_code_info[0]+' başarılı bir şekilde çekildi!')
            else:
                self.edit_test_type_comboBoxsignal.emit('Sonuç Bulunamadı!')
                self.label_43signal.emit(form_code_info[0]+' Form Code\'unun sınav türünde sorun var!')
        except:
            self.label_43signal.emit('Form Code çekilemedi!')
        
    def stop(self):
        self.is_running = False
        self.terminate()
        
class SaveFormCodeClass(QtCore.QThread):
    label_48signal = QtCore.pyqtSignal(str)
    edit_test_type_comboBoxsignal = QtCore.pyqtSignal(list)
    def __init__(self, parent: None,index=0):
        super(SaveFormCodeClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            try:
                form_code_info = fcf.create_form_code(self.form_code,self.test_type)
                all_form_codes = sorted(fcf.get_all_form_codes()[0])
                self.edit_test_type_comboBoxsignal.emit(all_form_codes)
                self.label_48signal.emit(str(form_code_info[0][0][0])+' '+str(form_code_info[0][0][1])+' sisteme kaydedildi!')
            except:
                if form_code_info != []:
                    self.label_48signal.emit(str(form_code_info[1][0][0])+' '+str(form_code_info[1][0][1])+' sisteme kaydedilemedi!')
                else:
                    self.label_48signal.emit('Sisteme kaydedilemedi!')
        except:
            self.label_48signal.emit("Hata!")
        
    def stop(self):
        self.is_running = False
        self.terminate()

class EditFormCodeClass(QtCore.QThread):
    label_43signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(EditFormCodeClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            try:
                form_code_info = fcf.edit_form_code(self.form_code,self.test_type)
                self.label_43signal.emit(str(form_code_info[0])+' '+str(form_code_info[1])+' olarak güncellendi!')
            except:
                self.label_43signal.emit(str(form_code_info[0])+' '+str(form_code_info[1])+' olarak güncellenemedi!')
        except:
            self.label_43signal.emit("Hata!")
        
    def stop(self):
        self.is_running = False
        self.terminate()
        
class DeleteFormCodeClass(QtCore.QThread):
    label_49signal = QtCore.pyqtSignal(str)
    edit_test_type_comboBoxsignal = QtCore.pyqtSignal(list)
    def __init__(self, parent: None,index=0):
        super(DeleteFormCodeClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            try:
                form_code_info = fcf.delete_form_code(self.form_code)
                all_form_codes = sorted(fcf.get_all_form_codes()[0])
                self.edit_test_type_comboBoxsignal.emit(all_form_codes)
                self.label_49signal.emit(str(form_code_info[0])+' silindi!')
            except:
                self.label_49signal.emit(str(form_code_info[0])+' silinemedi!')
        except:
            self.label_49signal.emit("Hata!")
        
    def stop(self):
        self.is_running = False
        self.terminate()
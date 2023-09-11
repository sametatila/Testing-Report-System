from PyQt5 import QtCore
import main_funcs.mixed.school_funcs as sm

class GetSchoolInfoClass(QtCore.QThread):
    label_38signal = QtCore.pyqtSignal(str)
    sch_country_3signal = QtCore.pyqtSignal(str)
    sch_city_3signal = QtCore.pyqtSignal(str)
    sch_address_3signal = QtCore.pyqtSignal(str)
    sch_teacher_3signal = QtCore.pyqtSignal(str)
    sch_teacher_tel_3signal = QtCore.pyqtSignal(str)
    sch_teacher_mail_3signal = QtCore.pyqtSignal(str)
    logo_signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(GetSchoolInfoClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            school_name = self.school_name
            schoolinfo = sm.get_school(school_name)
            self.sch_country_3signal.emit(schoolinfo[1])
            self.sch_city_3signal.emit(schoolinfo[2])
            self.sch_address_3signal.emit(schoolinfo[3])
            self.sch_teacher_3signal.emit(schoolinfo[4])
            self.sch_teacher_tel_3signal.emit(schoolinfo[5])
            self.sch_teacher_mail_3signal.emit(schoolinfo[6])
            self.logo_signal.emit(schoolinfo[7])
            self.label_38signal.emit('Okul başarılı bir şekilde çekildi!')
        except:
            self.label_38signal.emit('Okul çekilemedi!')
        
    def stop(self):
        self.is_running = False
        self.terminate()
        
class SaveSchoolClass(QtCore.QThread):
    label_19signal = QtCore.pyqtSignal(str)
    sch_comboBox_3signal = QtCore.pyqtSignal(list)
    def __init__(self, parent: None,index=0):
        super(SaveSchoolClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            sm.add_school(self.school_name,self.school_country,self.school_city,self.school_address,self.school_teacher,self.school_teacher_tel,self.school_teacher_mail,self.logo)
            self.sch_comboBox_3signal.emit(sorted(sm.get_combobox_school()))
            self.label_19signal.emit('Okul sisteme kaydedildi!')
        except:
            self.label_19signal.emit('Okul sisteme kaydedilemedi!')
        
    def stop(self):
        self.is_running = False
        self.terminate()

class EditSchoolClass(QtCore.QThread):
    label_38signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(EditSchoolClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            if len(self.new_school_name) < 5 and self.selected_type == True:
                self.label_38signal.emit('Yeni okul adı 5 karakterden kısa olamaz!')
            else:
                if self.selected_type == False:
                    sm.update_school(0,"",self.school_name,self.school_country,self.school_city,self.school_address,self.school_teacher,self.school_teacher_tel,self.school_teacher_mail,self.logo)
                    self.label_38signal.emit('Okul sistemde güncellendi!')
                else:
                    sm.update_school(1,self.new_school_name,self.school_name,self.school_country,self.school_city,self.school_address,self.school_teacher,self.school_teacher_tel,self.school_teacher_mail,self.logo)
                    self.label_38signal.emit('Okul tüm sistemde güncellendi! Sonumuz hayrola!')
        except:
            self.label_38signal.emit('Okul sistemde güncellenemedi!')
        
    def stop(self):
        self.is_running = False
        self.terminate()
        
class UploadLogoClass(QtCore.QThread):
    label_94signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(UploadLogoClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            sm.upload_school_logo(self.upload_file)
            self.label_94signal.emit('Logo yüklendi')
        except:
            self.label_94signal.emit('Yüklenemedi!')
        
    def stop(self):
        self.is_running = False
        self.terminate()
        
class DeleteLogoClass(QtCore.QThread):
    label_96signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(DeleteLogoClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            sm.delete_school_logo(self.filename)
            self.label_96signal.emit('Logo silindi')
        except:
            self.label_96signal.emit('Silinemedi!')
        
    def stop(self):
        self.is_running = False
        self.terminate()
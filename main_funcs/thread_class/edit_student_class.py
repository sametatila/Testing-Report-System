from PyQt5 import QtCore
import main_funcs.mixed.edit_student_info as esi

class GetStudentInfoClass(QtCore.QThread):
    label_14signal = QtCore.pyqtSignal(str)
    edit_student_idsignal = QtCore.pyqtSignal(str)
    edit_student_namesignal = QtCore.pyqtSignal(str)
    edit_student_lastnamesignal = QtCore.pyqtSignal(str)
    edit_student_dobsignal = QtCore.pyqtSignal(str)
    edit_student_gendersignal = QtCore.pyqtSignal(str)
    edit_student_classsignal = QtCore.pyqtSignal(str)
    edit_student_schoolsignal = QtCore.pyqtSignal(str)

    def __init__(self, parent: None,index=0):
        super(GetStudentInfoClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            student_number = self.student_number
            student_info = esi.get_student_info(student_number)
            self.edit_student_idsignal.emit(student_info[0])
            self.edit_student_namesignal.emit(student_info[1])
            self.edit_student_lastnamesignal.emit(student_info[2])
            self.edit_student_dobsignal.emit(student_info[3])
            self.edit_student_gendersignal.emit(student_info[4])
            self.edit_student_classsignal.emit(student_info[5])
            self.edit_student_schoolsignal.emit(student_info[6])
            
            self.label_14signal.emit('Öğrenci başarılı bir şekilde çekildi!')
        except:
            self.label_14signal.emit('Öğrenci çekilemedi!')
        
    def stop(self):
        self.is_running = False
        self.terminate()
        
class EditStudentInfoClass(QtCore.QThread):
    label_39signal = QtCore.pyqtSignal(str)

    def __init__(self, parent: None,index=0):
        super(EditStudentInfoClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            control_list = esi.update_student_info(self.first_student_id,self.student_id,self.student_name,self.student_lastname,self.student_dob,self.student_gender,self.student_class,self.student_school)
            if control_list == []:
                self.label_39signal.emit('Öğrenci başarılı bir şekilde güncellendi!')
            else:
                self.label_39signal.emit('Öğrenci sistemde kayıtlı değil')
        except:
            self.label_39signal.emit('Öğrenci güncellenemedi!')
        
    def stop(self):
        self.is_running = False
        self.terminate()

class CreateStudentInfoClass(QtCore.QThread):
    label_39signal = QtCore.pyqtSignal(str)

    def __init__(self, parent: None,index=0):
        super(CreateStudentInfoClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            esi.create_student_info(self.student_id,self.student_name,self.student_lastname,self.student_dob,self.student_gender,self.student_class,self.student_school)
            self.label_39signal.emit('Öğrenci başarılı bir şekilde sisteme kaydedildi!')
        except:
            self.label_39signal.emit('Öğrenci sisteme kaydedilemedi!')
        
    def stop(self):
        self.is_running = False
        self.terminate()
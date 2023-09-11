from PyQt5 import QtCore
class GetFormCodeClass(QtCore.QThread):
    label_22signal = QtCore.pyqtSignal(str)
    ps1_formsignal = QtCore.pyqtSignal(str)
    ps2_formsignal = QtCore.pyqtSignal(str)
    js_formsignal = QtCore.pyqtSignal(str)
    test_4_formsignal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(GetFormCodeClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.planning.attendance_sheet as ats
            form_code_list = ats.get_form_codes(str(self.plan_date.toString('dd-MM-yyyy')),self.plan_school)
            if len(form_code_list[0]) == 1:
                self.ps1_formsignal.emit(str(form_code_list[0][0]))
            elif form_code_list[0] == []:
                self.ps1_formsignal.emit("PS1 Sinav Yok")
            else:
                self.ps1_formsignal.emit(str(form_code_list[0])+" Sorunlu")
            if len(form_code_list[1]) == 1:
                self.ps2_formsignal.emit(str(form_code_list[1][0]))
            elif form_code_list[1] == []:
                self.ps2_formsignal.emit("PS2 Sinav Yok")
            else:
                self.ps2_formsignal.emit(str(form_code_list[1])+" Sorunlu")
            if len(form_code_list[2]) == 1:
                self.js_formsignal.emit(str(form_code_list[2][0]))
            elif form_code_list[2] == []:
                self.js_formsignal.emit("JS Sinav Yok")
            else:
                self.js_formsignal.emit(str(form_code_list[2])+ "Sorunlu")
            if len(form_code_list[3]) == 1:
                self.test_4_formsignal.emit(str(form_code_list[3][0]))
            elif form_code_list[3] == []:
                self.test_4_formsignal.emit("test_4 Sinav Yok")
            else:
                self.test_4_formsignal.emit(str(form_code_list[3])+" Sorunlu")
            self.label_22signal.emit('Başarılı!')
        except:
            self.label_22signal.emit('Yüklenemedi!')
    def stop(self):
        self.is_running = False
        self.terminate()
        
class test_1OpticClass(QtCore.QThread):
    label_23signal = QtCore.pyqtSignal(str)
    same_form_short_ps1signal = QtCore.pyqtSignal(tuple)
    same_form_short_ps2signal = QtCore.pyqtSignal(tuple)
    def __init__(self, parent: None,index=0):
        super(test_1OpticClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.planning.create_answer_sheet as cas
            if self.hp_printer == True:
                printer = 'hp'
            elif self.riso_printer == True:
                printer = 'riso'
            elif self.xerox_printer == True:
                printer = 'xerox'
            elif self.other_printer == True:
                printer = 'other'
            ps1_list = cas.check_form_code_ps1(self.ps1_new_form,self.plan_date.toString('dd-MM-yyyy'),self.plan_school)
            ps2_list = cas.check_form_code_ps2(self.ps2_new_form,self.plan_date.toString('dd-MM-yyyy'),self.plan_school)
            same_form_code_ps1 = len(ps1_list)
            same_form_code_ps2 = len(ps2_list)
            if same_form_code_ps1 == 0 and same_form_code_ps2 == 0:
                cas.form_code_update(self.ps1_old_form,self.ps1_new_form,self.plan_date.toString('dd-MM-yyyy'),self.plan_school)
                cas.form_code_update(self.ps2_old_form,self.ps2_new_form,self.plan_date.toString('dd-MM-yyyy'),self.plan_school)
                cas.create_test_1optic(self.plan_date.toString('dd-MM-yyyy'),self.plan_school,self.save_directory,printer)
                self.label_23signal.emit('test_1 Optik Oluşturuldu!')
            else:
                same_form_code_ps1_short = ps1_list[0][:-1]
                same_form_code_ps2_short = ps2_list[0][:-1]
                self.same_form_short_ps1signal.emit(same_form_code_ps1_short)
                self.same_form_short_ps2signal.emit(same_form_code_ps2_short)
                self.label_23signal.emit("Aktarılamadı! "+str(same_form_code_ps1)+" öğrenciye Step 1 "+self.ps1_new_form+" verilmiş. "+str(same_form_code_ps2)+" öğrenciye Step 2 "+self.ps2_new_form+" verilmiş. ")
        except:
            self.label_23signal.emit("Oluşturulamadı!")
        
    def stop(self):
        self.is_running = False
        self.terminate()

class test_3OpticClass(QtCore.QThread):
    label_23signal = QtCore.pyqtSignal(str)
    same_form_short_jssignal = QtCore.pyqtSignal(tuple)
    def __init__(self, parent: None,index=0):
        super(test_3OpticClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.planning.create_answer_sheet as cas
            if self.hp_printer == True:
                printer = 'hp'
            elif self.riso_printer == True:
                printer = 'riso'
            elif self.xerox_printer == True:
                printer = 'xerox'
            elif self.other_printer == True:
                printer = 'other'
            js_list = cas.check_form_code_js(self.js_new_form,self.plan_date.toString('dd-MM-yyyy'),self.plan_school)
            same_form_code_js = len(js_list)
            
            if same_form_code_js == 0:
                cas.form_code_update(self.js_old_form,self.js_new_form,self.plan_date.toString('dd-MM-yyyy'),self.plan_school)
                cas.create_test_3_optic(self.plan_date.toString('dd-MM-yyyy'),self.plan_school,self.save_directory,printer)
                self.label_23signal.emit('test_3 Optik Oluşturuldu!')
            else:
                same_form_code_js_short = js_list[0][:-1]
                print(same_form_code_js_short)
                self.same_form_short_jssignal.emit(same_form_code_js_short)
                self.label_23signal.emit("Aktarılamadı! "+str(same_form_code_js)+" öğrenciye test_3 "+self.js_new_form+" verilmiş.")
        except:
            self.label_23signal.emit("Oluşturulamadı!")
        
    def stop(self):
        self.is_running = False
        self.terminate()

class test_4OpticClass(QtCore.QThread):
    label_23signal = QtCore.pyqtSignal(str)
    same_form_short_test_4signal = QtCore.pyqtSignal(tuple)
    def __init__(self, parent: None,index=0):
        super(test_4OpticClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.planning.create_answer_sheet as cas
            if self.hp_printer == True:
                printer = 'hp'
            elif self.riso_printer == True:
                printer = 'riso'
            elif self.xerox_printer == True:
                printer = 'xerox'
            elif self.other_printer == True:
                printer = 'other'
            test_4_list = cas.check_form_code_test_4(self.test_4_new_form,self.plan_date.toString('dd-MM-yyyy'),self.plan_school)
            same_form_code_test_4 = len(test_4_list)
            if same_form_code_test_4 == 0:
                cas.form_code_update(self.test_4_old_form,self.test_4_new_form,self.plan_date.toString('dd-MM-yyyy'),self.plan_school)
                cas.create_test_4_optic(self.plan_date.toString('dd-MM-yyyy'),self.plan_school,self.save_directory,printer)
                self.label_23signal.emit('test_4 Optik Oluşturuldu!')
            else:
                same_form_code_test_4_short = test_4_list[0][:-1]
                self.same_form_short_test_4signal.emit(same_form_code_test_4_short)
                self.label_23signal.emit("Aktarılamadı! "+str(same_form_code_test_4)+" öğrenciye test_4 "+self.test_4_new_form+" verilmiş.")
        except:
            self.label_23signal.emit("Oluşturulamadı!")
            
    def stop(self):
        self.is_running = False
        self.terminate()

class AttendanceSheetIDClass(QtCore.QThread):
    label_23signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(AttendanceSheetIDClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.planning.attendance_sheet as ats
            if self.attendance_tr == True:
                ats.attendance_sheet_pdf("tr",0,self.plan_date.toString('dd-MM-yyyy'),self.plan_school,self.save_directory)
                self.label_23signal.emit("Yoklama Listesi TC'li Oluşturuldu!")
            elif self.attendance_eng == True:
                ats.attendance_sheet_pdf("eng",0,self.plan_date.toString('dd-MM-yyyy'),self.plan_school,self.save_directory)
                self.label_23signal.emit("Attendance Sheet with ID is created!")
        except:
            self.label_23signal.emit("Oluşturulamadı!")
        
    def stop(self):
        self.is_running = False
        self.terminate()

class AttendanceSheetNoIDClass(QtCore.QThread):
    label_23signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(AttendanceSheetNoIDClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.planning.attendance_sheet as ats
            if self.attendance_tr == True:
                ats.attendance_sheet_pdf("tr",1,self.plan_date.toString('dd-MM-yyyy'),self.plan_school,self.save_directory)
                self.label_23signal.emit("Yoklama Listesi TC'siz Oluşturuldu!")
            elif self.attendance_eng == True:
                ats.attendance_sheet_pdf("eng",1,self.plan_date.toString('dd-MM-yyyy'),self.plan_school,self.save_directory)
                self.label_23signal.emit("Attendance Sheet without ID is created!")
        except:
            self.label_23signal.emit("Oluşturulamadı!")

        
    def stop(self):
        self.is_running = False
        self.terminate()
        
class BookletClass(QtCore.QThread):
    label_23signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(BookletClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.planning.attendance_sheet as ats
            ats.attendance_sheet_pdf("tr",2,self.plan_date.toString('dd-MM-yyyy'),self.plan_school,self.save_directory)
            self.label_23signal.emit("Booklet Oluşturuldu!")
        except:
            self.label_23signal.emit("Oluşturulamadı!")

        
    def stop(self):
        self.is_running = False
        self.terminate()

class DeletePlanClass(QtCore.QThread):
    label_23signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(DeletePlanClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.planning.create_answer_sheet as cas
            cas.delete_query(self.plan_date,self.plan_school)
            self.label_23signal.emit("Seçili Plan Silindi!")
        except:
            self.label_23signal.emit("Plan Silinemedi!")
        
    def stop(self):
        self.is_running = False
        self.terminate()

class ExportAttendanceClass(QtCore.QThread):
    label_23signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(ExportAttendanceClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.planning.export_attendance as ea
            ea.attendance_check(self.file_directory,self.save_directory,self.institution,self.test_date.toString('dd-MM-yyyy'),self.test_type)
            self.label_23signal.emit("Gelmeyen öğrenci listesi oluşturuldu")
        except:
            self.label_23signal.emit("Belge oluşturulamadı!")
        
    def stop(self):
        self.is_running = False
        self.terminate()

class PlantoTextClass(QtCore.QThread):
    label_23signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(PlantoTextClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.planning.plan_to_txt as ptt
            ptt.plan_to_txt(self.save_directory,self.plan_date.toString('dd-MM-yyyy'),self.plan_school)
            self.label_23signal.emit("Plan scanner text dosyasına dönüştürüldü")
        except:
            self.label_23signal.emit("Belge oluşturulamadı!")
        
    def stop(self):
        self.is_running = False
        self.terminate()
from PyQt5 import QtCore

class GetSchoolResultClass(QtCore.QThread):
    all_result_signal = QtCore.pyqtSignal(object)
    label_15signal = QtCore.pyqtSignal(str)

    def __init__(self, parent: None,index=0):
        super(GetSchoolResultClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.score_docs.get_school_result as gsr
            if self.report_test_type == 'test_1 Step 1 & 2':
                all_result = gsr.get_school_result_list("test_1step_1","test_1step_2",self.institution,self.main_date,'')
                self.all_result_signal.emit(all_result)
            elif self.report_test_type == 'test_1 Step 1':
                all_result = gsr.get_school_result_list("test_1step_1","",self.institution,self.main_date,'')
                self.all_result_signal.emit(all_result)
            elif self.report_test_type == 'test_1 Step 2':
                all_result = gsr.get_school_result_list("test_1step_2","",self.institution,self.main_date,'')
                self.all_result_signal.emit(all_result)
            elif self.report_test_type == 'test_1 Speaking':
                all_result = gsr.get_school_result_list("test_1speaking","",self.institution,self.main_date,'')
                self.all_result_signal.emit(all_result)
            elif self.report_test_type == 'test_3 Standard':
                all_result = gsr.get_school_result_list("test_3_standard","",self.institution,self.main_date,'')
                self.all_result_signal.emit(all_result)
            elif self.report_test_type == 'test_3 Speaking':
                all_result = gsr.get_school_result_list("test_3_speaking","",self.institution,self.main_date,'')
                self.all_result_signal.emit(all_result)
            elif self.report_test_type == 'test_4':
                all_result = gsr.get_school_result_list("test_4","",self.institution,self.main_date,'')
                self.all_result_signal.emit(all_result)
            elif self.report_test_type == 'test_1 Step 1 & 2 & Speaking':
                all_result = gsr.get_school_result_list("test_1","test_1speaking",self.institution,self.main_date,self.speaking_main_date)
                self.all_result_signal.emit(all_result)
            elif self.report_test_type == 'test_3 Standard & Speaking':
                all_result = gsr.get_school_result_list("test_3","test_3_speaking",self.institution,self.main_date,self.speaking_main_date)
                self.all_result_signal.emit(all_result)
        except:
            self.label_15signal.emit(self.institution+" sonuç getirilemedi.")
        
        
    def stop(self):
        self.is_running = False
        self.terminate()

class CreateTurkishReportClass(QtCore.QThread):
    label_15signal = QtCore.pyqtSignal(str)
    
    def __init__(self, parent: None,index=0):
        super(CreateTurkishReportClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            from datetime import datetime
            print(datetime.now())
            import main_funcs.score_docs.turkish_report as tr
            if self.printable == True:
                selected_option = 0
                doc_type = "Baskı"
            if self.digital == True:
                selected_option = 1
                doc_type = "Dijital"
            if self.all:
                choise = 0
            if self.selected:
                choise = 1
            if self.report_test_type == 'test_1 Step 1':
                tr.ps1_tr_karne(self.save_directory,selected_option,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(doc_type+" amaçlı Türkçe Karne oluşturuldu.")
            elif self.report_test_type == 'test_1 Step 2':
                tr.ps2_tr_karne(self.save_directory,selected_option,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(doc_type+" amaçlı Türkçe Karne oluşturuldu.")
            elif self.report_test_type == 'test_1 Speaking':
                tr.pspk_tr_karne(self.save_directory,selected_option,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(doc_type+" amaçlı Türkçe Karne oluşturuldu.")
            elif self.report_test_type == 'test_3 Standard':
                tr.js_tr_karne(self.save_directory,selected_option,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(doc_type+" amaçlı Türkçe Karne oluşturuldu.")
            elif self.report_test_type == 'test_3 Speaking':
                tr.jspk_tr_karne(self.save_directory,selected_option,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(doc_type+" amaçlı Türkçe Karne oluşturuldu.")
            elif self.test_type_test_4 == True:
                self.label_15signal.emit("test_4 için Türkçe Karne oluşturulamaz!")
            else:
                self.label_15signal.emit("Birleşik Türkçe Karne oluşturulamaz!")
        except:
            self.label_15signal.emit(self.institution+" belge oluşturulamadı.")
            print(datetime.now())
        
    def stop(self):
        self.is_running = False
        self.terminate()
        
class CreateInstitutionalReportClass(QtCore.QThread):
    label_15signal = QtCore.pyqtSignal(str)
    
    def __init__(self, parent: None,index=0):
        super(CreateInstitutionalReportClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.score_docs.institutional_report_and_class_tables as ir
            if self.doc_type == 0:
                signal_text = "Kurumsal Rapor"
                choise = 2
                self.main_list = ""
            elif self.doc_type == 1:
                signal_text = "Sınıf Listesi"
                if self.all:
                    choise = 0
                elif self.selected:
                    choise = 1
            if self.report_test_type == 'test_1 Step 1 & 2':
                ir.test_1institutional_report(self.doc_type,self.save_directory,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_1 Step 1':
                ir.test_1institutional_report(self.doc_type,self.save_directory,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_1 Step 2':
                ir.test_1institutional_report(self.doc_type,self.save_directory,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_1 Speaking':
                ir.pspk_institutional_report(self.doc_type,self.save_directory,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_3 Standard':
                ir.js_institutional_report(self.doc_type,self.save_directory,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_3 Speaking':
                ir.jspk_institutional_report(self.doc_type,self.save_directory,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_4':
                ir.test_4_institutional_report(self.doc_type,self.save_directory,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
        except:
            self.label_15signal.emit(self.institution+" belge oluşturulamadı.")
        
    def stop(self):
        self.is_running = False
        self.terminate()
        
class ExportScoreExcelClass(QtCore.QThread):
    label_15signal = QtCore.pyqtSignal(str)
    
    def __init__(self, parent: None,index=0):
        super(ExportScoreExcelClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.score_docs.export_score_excel as ese
            signal_text = "Score Exceli"
            if self.report_test_type == 'test_1 Step 1':
                ese.export_excel("test_1step_1",self.save_directory,self.institution,self.main_date)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_1 Step 2':
                ese.export_excel("test_1step_2",self.save_directory,self.institution,self.main_date)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_1 Speaking':
                ese.export_excel("test_1speaking",self.save_directory,self.institution,self.main_date)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_3 Standard':
                ese.export_excel("test_3_standard",self.save_directory,self.institution,self.main_date)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_3 Speaking':
                ese.export_excel("test_3_speaking",self.save_directory,self.institution,self.main_date)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_4':
                ese.export_excel("test_4",self.save_directory,self.institution,self.main_date)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
        except:
            self.label_15signal.emit(self.institution+" belge oluşturulamadı.")
        
    def stop(self):
        self.is_running = False
        self.terminate()

class CreateResultLetterClass(QtCore.QThread):
    label_15signal = QtCore.pyqtSignal(str)
    
    def __init__(self, parent: None,index=0):
        super(CreateResultLetterClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.score_docs.institutional_report_and_class_tables as ir
            signal_text = 'Sonuç Zarfı'
            ir.school_letter(self.save_directory,self.institution,self.main_date,self.person)
            self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
        except:
            self.label_15signal.emit(self.institution+" belge oluşturulamadı.")
        
    def stop(self):
        self.is_running = False
        self.terminate()

class CreateAIODigitalClass(QtCore.QThread):
    label_15signal = QtCore.pyqtSignal(str)
    
    def __init__(self, parent: None,index=0):
        super(CreateAIODigitalClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.score_docs.turkish_report as tr
            doc_type = "Dijital"
            if self.all:
                choise = 0
            if self.selected:
                choise = 1
            i = 1
            if self.report_test_type == 'test_1 Step 1':
                tr.ps1_tr_karne(self.save_directory,i,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(doc_type+" amaçlı Türkçe Karne oluşturuldu.")
            elif self.report_test_type == 'test_1 Step 2':
                tr.ps2_tr_karne(self.save_directory,i,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(doc_type+" amaçlı Türkçe Karne oluşturuldu.")
            elif self.report_test_type == 'test_1 Speaking':
                tr.pspk_tr_karne(self.save_directory,i,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(doc_type+" amaçlı Türkçe Karne oluşturuldu.")
            elif self.report_test_type == 'test_3 Standard':
                tr.js_tr_karne(self.save_directory,i,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(doc_type+" amaçlı Türkçe Karne oluşturuldu.")
            elif self.report_test_type == 'test_3 Speaking':
                tr.jspk_tr_karne(self.save_directory,i,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(doc_type+" amaçlı Türkçe Karne oluşturuldu.")
            elif self.test_type_test_4 == True:
                self.label_15signal.emit("test_4 için Türkçe Karne oluşturulamaz!")
            else:
                self.label_15signal.emit("Birleşik Türkçe Karne oluşturulamaz!")
        except:
            self.label_15signal.emit(self.institution+" belge oluşturulamadı.")

        try:
            import main_funcs.score_docs.institutional_report_and_class_tables as ir
            i = 0
            if i == 0:
                signal_text = "Kurumsal Rapor"
                choise = 2
                self.main_list = ""
            elif i == 1:
                signal_text = "Sınıf Listesi"
                if self.all:
                    choise = 0
                elif self.selected:
                    choise = 1
            if self.report_test_type == 'test_1 Step 1 & 2':
                ir.test_1institutional_report(i,self.save_directory+"/"+self.institution,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_1 Step 1':
                ir.test_1institutional_report(i,self.save_directory+"/"+self.institution,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_1 Step 2':
                ir.test_1institutional_report(i,self.save_directory+"/"+self.institution,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_1 Speaking':
                ir.pspk_institutional_report(i,self.save_directory+"/"+self.institution,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_3 Standard':
                ir.js_institutional_report(i,self.save_directory+"/"+self.institution,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_3 Speaking':
                ir.jspk_institutional_report(i,self.save_directory+"/"+self.institution,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_4':
                ir.test_4_institutional_report(i,self.save_directory+"/"+self.institution,self.institution,self.main_date,choise,self.main_list)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            ##### Speaking karma eklenmedi eklenecek
        except:
            self.label_15signal.emit(self.institution+" belge oluşturulamadı.")

        try:
            import main_funcs.score_docs.export_score_excel as ese
            signal_text = "Score Exceli"
            if self.report_test_type == 'test_1 Step 1':
                ese.export_excel("test_1step_1",self.save_directory+"/"+self.institution,self.institution,self.main_date)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_1 Step 2':
                ese.export_excel("test_1step_2",self.save_directory+"/"+self.institution,self.institution,self.main_date)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_1 Speaking':
                ese.export_excel("test_1speaking",self.save_directory+"/"+self.institution,self.institution,self.main_date)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_3 Standard':
                ese.export_excel("test_3_standard",self.save_directory+"/"+self.institution,self.institution,self.main_date)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_3 Speaking':
                ese.export_excel("test_3_speaking",self.save_directory+"/"+self.institution,self.institution,self.main_date)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
            elif self.report_test_type == 'test_4':
                ese.export_excel("test_4",self.save_directory+"/"+self.institution,self.institution,self.main_date)
                self.label_15signal.emit(self.institution+" "+signal_text+" oluşturuldu.")
        except:
            self.label_15signal.emit(self.institution+" belge oluşturulamadı.")

        
        try:
            import main_funcs.tools.iops_file_separation as ifs
            test_type = self.report_test_type.replace(" ", "_").lower()
            if self.upload_file_sr != False:
                ifs.all_sr_sep(self.upload_file_sr,self.save_directory,test_type,self.institution,self.main_date)
                self.label_15signal.emit(self.institution+' IOPS Score Report bölündü.')
            else:
                self.label_15signal.emit(self.institution+' IOPS Score Report bölünemedi.')
            if self.upload_file_c != False:
                if test_type == "test_1step_1" or test_type == "test_1step_2":
                    ifs.pri_c_sep(self.upload_file_c,self.save_directory,test_type,self.institution,self.main_date)
                elif test_type =="test_3_standard" or test_type == "test_4":
                    ifs.js_test_4_c_sep(self.upload_file_c,self.save_directory,test_type,self.institution,self.main_date)
                self.label_15signal.emit(self.institution+' IOPS Certificate bölündü.')
            else:
                self.label_15signal.emit(self.institution+' IOPS Certificate bölünemedi.')
        except:
            self.label_15signal.emit('IOPS belge bölünemedi!')
        
    def stop(self):
        self.is_running = False
        self.terminate()
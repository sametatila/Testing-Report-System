from PyQt5 import QtCore

class UploadPlanClass(QtCore.QThread):
    label_21signal = QtCore.pyqtSignal(str)
    all_upload_list_signal = QtCore.pyqtSignal(list)
    def __init__(self, parent: None,index=0):
        super(UploadPlanClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import main_funcs.planning.sablon_to_db as std
            upload_list = std.sablon_to_db(str(self.upload_date.toString('dd-MM-yyyy')),self.upload_school,self.upload_file)
            self.all_upload_list_signal.emit(upload_list)
            if len(upload_list[1]) > 0: 
                self.label_21signal.emit(str(len(upload_list[1]))+' Öğrenci yüklenemedi!')
            elif upload_list[2] != []:
                self.label_21signal.emit('Yüklenemedi!')
            else:
                self.label_21signal.emit(str(len(upload_list[0]))+' Öğrenci yüklendi!')
        except:
            self.label_21signal.emit('Yüklenemedi!')
            
    def stop(self):
        self.is_running = False
        self.terminate()

class ConvertPlanClass(QtCore.QThread):
    df_signal = QtCore.pyqtSignal(object)
    def __init__(self, parent: None,index=0):
        super(ConvertPlanClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        import main_funcs.mixed.make_plan as mp
        if self.plan_logic == 'Aynı Sınıf A\'dan Z\'ye (PBT)':
            df = mp.same_class_a_to_z(self.file,self.school,self.plan_logic,'')
            self.df_signal.emit(df)
        elif self.plan_logic == 'Tüm Öğrenciler A\'dan Z\'ye (PBT)':
            df = mp.all_student_a_to_z(self.file,self.school,self.plan_logic,self.total_class)
            self.df_signal.emit(df)
        elif self.plan_logic == 'Aynı Sınıf A\'dan Z\'ye (CBT)':
            df = mp.same_class_a_to_z(self.file,self.school,self.plan_logic,self.total_class)
            self.df_signal.emit(df)
        elif self.plan_logic == 'Sınıf Bölme (PBT)':
            df = mp.same_class_a_to_z(self.file,self.school,self.plan_logic,self.total_class)
            self.df_signal.emit(df)
        
            
    def stop(self):
        self.is_running = False
        self.terminate()
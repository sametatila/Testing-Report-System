from PyQt5 import QtCore
class CopyFormCodeFilesClass(QtCore.QThread):
    label_102signal = QtCore.pyqtSignal(str)
    activate_signal = QtCore.pyqtSignal(bool)
    def __init__(self, parent: None,index=0):
        super(CopyFormCodeFilesClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import os
            import random
            import shutil
            
            self.activate_signal.emit(False)
            subfolders = [ f.path for f in os.scandir(self.form_code_directory) if f.is_dir()]
            for info in self.all_info:
                if info[0] and info[1] != 'SD Kart Adı':
                    drive_name, drive_letter, form_code = info[1:]
                    drive_letter = drive_letter+':\\'
                    drive_folders = [ f.path for f in os.scandir(drive_letter) if f.is_dir()]
                    for fol in drive_folders:
                        if 'TEST' in fol:
                            shutil.rmtree(fol)
                    for form_code_folder in subfolders:
                        if form_code in form_code_folder:
                            destination_folder = drive_letter + form_code_folder.split('\\')[-1]
                            if not os.path.exists(destination_folder):
                                os.mkdir(destination_folder)
                                print('yeni yol oluşturuldu')
                            for file_name in os.listdir(form_code_folder):
                                source = form_code_folder + '/' + file_name
                                if os.path.isfile(source):
                                    destination = destination_folder + '/' + file_name
                                    print(source,destination)
                                    shutil.copy2(source, destination)
                            
                            sd_files = os.listdir(destination_folder)
                            for sd_file in sd_files:
                                new_filename = sd_file.replace('Parça','{} {}'.format(form_code,str(random.randint(10000,99999))))
                                os.rename(destination_folder + '/' + sd_file, destination_folder + '/' + new_filename)
                            self.label_102signal.emit(drive_name+" Kopyalama Tamamlandı!")
            self.label_102signal.emit("Tüm Kopyalama Tamamlandı!")
            self.activate_signal.emit(True)
            
        except:
            self.label_69signal.emit("Hata!")
        
        
    def stop(self):
        self.is_running = False
        self.terminate()

from PyQt5 import QtCore
class CopyFormCodeFilesClassT1(QtCore.QThread):
    label_117signal = QtCore.pyqtSignal(str)
    activate_signal_t1 = QtCore.pyqtSignal(bool)
    def __init__(self, parent: None,index=0):
        super(CopyFormCodeFilesClassT1, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import os
            import random
            import shutil
            
            self.activate_signal_t1.emit(False)
            subfolders = [ f.path for f in os.scandir(self.form_code_directory) if f.is_dir()]
            print(subfolders)
            for form_code_folder in subfolders:
                print(self.form_code)
                if self.form_code in form_code_folder:
                    for i in range(1,self.total_num+1):
                        destination_folder = self.save_directory + "/" + form_code_folder.split('\\')[-1] + "(" + str(i) + ")"
                        print(destination_folder)
                        if not os.path.exists(destination_folder):
                            os.mkdir(destination_folder)
                            print('yeni yol oluşturuldu')
                        for file_name in os.listdir(form_code_folder):
                            source = form_code_folder + '/' + file_name
                            if os.path.isfile(source):
                                destination = destination_folder + '/' + file_name
                                print(source,destination)
                                shutil.copy2(source, destination)
                        
                        sd_files = os.listdir(destination_folder)
                        for sd_file in sd_files:
                            new_filename = sd_file.replace('Parça','{} {}'.format(self.form_code,str(random.randint(10000,99999))))
                            os.rename(destination_folder + '/' + sd_file, destination_folder + '/' + new_filename)
            self.label_117signal.emit("Tüm Kopyalama Tamamlandı!")
            self.activate_signal_t1.emit(True)
            
        except:
            self.label_69signal.emit("Hata!")
        
        
    def stop(self):
        self.is_running = False
        self.terminate()
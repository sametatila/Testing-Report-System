from PyQt5 import QtCore

class ExportSchoolsClass(QtCore.QThread):
    label_64signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(ExportSchoolsClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        import main_funcs.mixed.export_schools as es
        try:
            es.get_all_schools_infos(self.save_directory,self.institution)
            self.label_64signal.emit('Dışa aktarma başarılı!')
        except:
            self.label_64signal.emit('Dışa aktarma başarısız!')
        
    def stop(self):
        self.is_running = False
        self.terminate()
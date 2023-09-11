from PyQt5 import QtCore
class PDFRemovePasswordClass(QtCore.QThread):
    label_86signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(PDFRemovePasswordClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import fitz
            import os
            file_paths = [os.path.join(r,file) for r,d,f in os.walk(self.save_directory) for file in f if file.endswith(".PDF") or file.endswith(".pdf")]
            for file in file_paths:
                r,f = os.path.split(file)
                new_r = str(r).split('\\')[1:]
                new_r = '\\'.join(new_r)
                save_path = os.path.expanduser('~/Documents/GTO_Docs/Not_Secured/'+new_r)
                if os.path.exists(save_path) == False:
                    os.makedirs(save_path)
                doc = fitz.open(file)
                doc.save(save_path+'/'+f)

            os.startfile(os.path.expanduser('~/Documents/GTO_Docs/Not_Secured/'))
            self.label_86signal.emit("Seçili klasördeki tüm pdflerin şifreleri kaldırıldı.")
        except:
            self.label_86signal.emit("Hata!")
    
    def stop(self):
        self.is_running = False
        self.terminate()
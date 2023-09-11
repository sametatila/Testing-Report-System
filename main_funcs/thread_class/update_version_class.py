from PyQt5 import QtCore
class UpdateVersionClass(QtCore.QThread):
    progress_signal = QtCore.pyqtSignal(int)
    progress_info_signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(UpdateVersionClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            import ftplib,os
            from threading import Thread

            # Open the FTP connection
            ftp = ftplib.FTP("XXX")
            ftp.cwd('/GTO-Version')
            ftp_files = ftp.nlst()
            files = []
            for file in ftp_files:
                if '.zip' in file:
                    files.append(float(file[:-4]))
            filename = max(files)
            filename = str(filename)+'.zip'
            filesize = ftp.size(filename)
            
            def download_file():
                with open( filename, 'wb' ) as file :
                    ftp.retrbinary('RETR %s' % filename, file.write)
                    file.close()

            def progress():
                count = 0
                while count <= 100:
                    try:
                        if int((os.path.getsize(filename)/filesize)*100) == count:
                            count+=1
                            self.progress_signal.emit(count)
                            if count == 100:
                                os.system("tar -xvf {}".format(filename))
                                os.remove(filename)
                                self.progress_info_signal.emit("Yükleme Tamamlandı")
                                
                    except:
                        pass
                    
            task1 = Thread(target=download_file)
            task2 = Thread(target=progress)
            task1.start()
            task2.start()  
            
        except:
            self.progress_info_signal.emit("Yüklenemedi")
    def stop(self):
        self.is_running = False
        self.terminate()
        
        

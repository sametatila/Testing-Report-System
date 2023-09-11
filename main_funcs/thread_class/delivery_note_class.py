from PyQt5 import QtCore
class PS1DeliveryNoteClass(QtCore.QThread):
    label_23signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(PS1DeliveryNoteClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        import main_funcs.planning.delivery_note as dn
        try:
            dn.create_delivery_note(self.save_directory,self.form_code,8,self.plan_school,self.plan_date.toString('dd-MM-yyyy'))
            self.label_23signal.emit("test_1 Step 1 Delivery Note Oluşturuldu.")
        except:
            self.label_23signal.emit("Oluşturulamadı!")
        
    def stop(self):
        self.is_running = False
        self.terminate()
    
class PS2DeliveryNoteClass(QtCore.QThread):
    label_23signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(PS2DeliveryNoteClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        import main_funcs.planning.delivery_note as dn
        try:
            dn.create_delivery_note(self.save_directory,self.form_code,9,self.plan_school,self.plan_date.toString('dd-MM-yyyy'))
            self.label_23signal.emit("test_1 Step 2 Delivery Note Oluşturuldu.")
        except:
            self.label_23signal.emit("Oluşturulamadı!")
        
    def stop(self):
        self.is_running = False
        self.terminate()
        
class JSDeliveryNoteClass(QtCore.QThread):
    label_23signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(JSDeliveryNoteClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        import main_funcs.planning.delivery_note as dn
        try:
            dn.create_delivery_note(self.save_directory,self.form_code,5,self.plan_school,self.plan_date.toString('dd-MM-yyyy'))
            self.label_23signal.emit("test_3 Standard Delivery Note Oluşturuldu.")
        except:
            self.label_23signal.emit("Oluşturulamadı!")
        
    def stop(self):
        self.is_running = False
        self.terminate()

class test_4DeliveryNoteClass(QtCore.QThread):
    label_23signal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(test_4DeliveryNoteClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        import main_funcs.planning.delivery_note as dn
        try:
            dn.create_delivery_note(self.save_directory,self.form_code,4,self.plan_school,self.plan_date.toString('dd-MM-yyyy'))
            self.label_23signal.emit("test_4 Delivery Note Oluşturuldu.")
        except:
            self.label_23signal.emit("Oluşturulamadı!")
        
    def stop(self):
        self.is_running = False
        self.terminate()
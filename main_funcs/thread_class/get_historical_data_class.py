from PyQt5 import QtCore

class GetHistoricalDataClass(QtCore.QThread):
    count_main_signal = QtCore.pyqtSignal(list)
    edit_test_type_comboBoxsignal = QtCore.pyqtSignal(str)
    def __init__(self, parent: None,index=0):
        super(GetHistoricalDataClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        import main_funcs.mixed.get_historical_data as ghd
        all_data = ghd.get_date_range_history(self.start_date.toString('dd-MM-yyyy'),self.end_date.toString('dd-MM-yyyy'),self.higher_institution,self.city,self.institution)
        main_list = []
        list_1,list_2,list_3,list_4,list_5,list_6,list_7,list_8= [],[],[],[],[],[],[],[]
        for count_number in range(6):
            if self.higher_institution != "Kurum Seç":
                if self.city != "Şehir Seç":
                    if self.institution != "Okul Seç":
                        list_1.append(all_data[count_number][0])
                    elif self.institution == "Okul Seç":
                        list_2.append(all_data[count_number][1])
                elif self.city == "Şehir Seç":
                    if self.institution != "Okul Seç":
                        list_3.append(all_data[count_number][2])
                    elif self.institution == "Okul Seç":
                        list_4.append(all_data[count_number][3])
            elif self.higher_institution == "Kurum Seç":
                if self.city != "Şehir Seç":
                    if self.institution != "Okul Seç":
                        list_5.append(all_data[count_number][4])
                    elif self.institution == "Okul Seç":
                        list_6.append(all_data[count_number][5])
                elif self.city == "Şehir Seç":
                    if self.institution != "Okul Seç":
                        list_7.append(all_data[count_number][6])
                    elif self.institution == "Okul Seç":
                        list_8.append(all_data[count_number][7])
            count_number+=1
        for i in range(1,9):
            if eval("list_"+str(i)) != []:
                main_list.append(eval("list_"+str(i)))
        if main_list != []:
            self.count_main_signal.emit(main_list[0])
        
    def stop(self):
        self.is_running = False
        self.terminate()
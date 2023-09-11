import os
from datetime import datetime, timedelta

import natsort
import numpy as np
import pandas as pd
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import main_funcs.mixed.save_file_location as sfl
from main_funcs.thread_class.make_plan_class import *


class MakePlan(QDialog):
    
    def __init__(self, values = object):
        super(MakePlan, self).__init__()
        uic.loadUi('./data/gui_data/make_plan.ui', self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.pressing = False
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.df,self.school,self.class_list,self.plan_logic,self.total_class = values
        self.time_df = pd.DataFrame([['140','140','80','80','30','40']],columns=['4','5','8','9','20','21'])
        self.plan_logic_label.setText(self.plan_logic)
        self.school_info_label.setText(self.school)
        self.total_student_label.setText(str(len(self.df)))
        self.info_label.setVisible(False)
        self.divide_frame.hide()
        self.divide_frame_2.hide()
        def total_count():
            each_class_count = self.df['class'].value_counts().reset_index()
            each_grade_count = self.df['class'].apply(lambda x:x[0]).value_counts().reset_index()

            each_class_count.columns = ['class','count']
            each_class_count['class-total'] = each_class_count['class'] + ": " + each_class_count['count'].astype(str)
            each_class_count = each_class_count.iloc[natsort.index_humansorted(each_class_count['class-total'],reverse=False)]
            each_grade_count.columns = ['grade','count']
            each_grade_count['grade-total'] = each_grade_count['grade'].apply(lambda x:x.replace('H','Haz')) + ": " + each_grade_count['count'].astype(str)

            new_df = pd.concat([each_class_count, each_grade_count], axis=1).reset_index()
            new_df = new_df[['class-total','grade-total']]
            new_df = new_df.replace(np.nan,'')
            return new_df
        

        self.model_t = PandasModelPlan(total_count())
        self.tableView_t.setModel(self.model_t)

        if self.plan_logic == 'Aynı Sınıf A\'dan Z\'ye (PBT)':
            new_df = pd.DataFrame(self.class_list,columns=['class'])
            new_df['class'] = new_df['class'].apply(lambda x: x.replace('Haz','13'))
            new_df['grade'] = new_df['class'].str.extract('(^\d*)')
            new_df['class'] = new_df['class'].apply(lambda x: x.replace('13','Haz'))
            new_df['session'] = ''
            new_df['time'] = ''
            new_df = new_df[['grade','class','session','time']]
            new_df = new_df.iloc[natsort.index_humansorted(new_df['grade'],reverse=False)]
            self.model = PandasModelPlan(new_df)
            self.tableView_scaz.setModel(self.model)
            self.btn_create_plan.clicked.connect(self.same_class_a_to_z_t)

        elif self.plan_logic == 'Tüm Öğrenciler A\'dan Z\'ye (PBT)':
            grade_list = sorted(self.df['grade'].unique())
            new_df1 = pd.DataFrame()
            for grade in grade_list:
                new_df = pd.DataFrame(list(range(1,int(self.total_class)+1)),columns=['group'])
                new_df = new_df.replace(np.nan,'')
                new_df['grade'] = str(grade)+' - '+new_df['group'].astype(str)+'.Grup'
                new_df['session'] = ''
                new_df['time'] = ''
                new_df['order'] = ''
                new_df['room'] = ''
                new_df = new_df[['grade','session','time','room','order']]
                new_df1 = pd.concat([new_df1,new_df])
            new_df1 = new_df1.iloc[natsort.index_humansorted(new_df1['grade'],reverse=False)]
            self.model = PandasModelPlan(new_df1)
            self.tableView_scaz.setModel(self.model)
            self.btn_create_plan.clicked.connect(self.all_student_a_to_z_t)

        elif self.plan_logic == 'Aynı Sınıf A\'dan Z\'ye (CBT)':
            self.divide_frame_2.show()
            new_df = self.df['class'].value_counts().reset_index()
            new_df.columns = ['class','total']
            new_df = new_df.sort_values(by = ['class'])
            for i in range(int(self.total_class)):
                new_df['room-'+str(i+1)] = '0'
            for i in range(int(self.total_class)):
                new_df['session-'+str(i+1)] = ''
            for i in range(int(self.total_class)):
                new_df['time-'+str(i+1)] = ''
            self.model = PandasModelPlan(new_df)
            self.tableView_scaz.setModel(self.model)
            self.btn_create_plan.clicked.connect(self.same_class_a_to_z_cbt_t)
            selection = self.tableView_scaz.selectionModel()
            selection.selectionChanged.connect(self.selection_change)
            
        elif self.plan_logic == 'Sınıf Bölme (PBT)':
            self.divide_frame.show()
            self.total_class = "2"
            new_df = self.df['class'].value_counts().reset_index()
            new_df.columns = ['class','total']
            new_df = new_df.sort_values(by = ['class'])
            for i in range(int(self.total_class)):
                new_df['room-'+str(i+1)] = '0'
            for i in range(int(self.total_class)):
                new_df['session-'+str(i+1)] = ''
            for i in range(int(self.total_class)):
                new_df['time-'+str(i+1)] = ''
            self.model = PandasModelPlan(new_df)
            self.tableView_scaz.setModel(self.model)
            self.btn_create_plan.clicked.connect(self.divide_class)
            selection = self.tableView_scaz.selectionModel()
            selection.selectionChanged.connect(self.selection_change)

    
    
    def selection_change(self):
        model = self.tableView_scaz.model()
        data = []
        for row in range(model.rowCount()):
            data.append([])
            for column in range(model.columnCount()):
                index = model.index(row, column)
                data[row].append(model.data(index))
        change_df = pd.DataFrame(data,columns=['class','total']+['room-'+str(x) for x in range(1,int(self.total_class)+1)]+['session-'+str(x) for x in range(1,int(self.total_class)+1)]+['time-'+str(x) for x in range(1,int(self.total_class)+1)])
        room_list = [col for col in change_df.columns if 'room' in col]
        for room in room_list:
            change_df[room] = change_df[room].str.split('+')
            change_df[room] = change_df[room].str[0]

        change_df['sum_rooms'] = change_df[room_list].astype(int).sum(axis=1)
        change_df['diff'] = np.where( change_df['total'].astype(int) == change_df['sum_rooms'] , 'Eşit', 'Eşit Değil')
        equal_check = change_df.set_index('class').to_dict()['diff']
        equal_text = str(equal_check).replace('\'','').replace('{','').replace('}','')
        self.info_label.setVisible(True)
        self.info_label.setText(equal_text)
        
    def same_class_a_to_z_t(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            model = self.tableView_scaz.model()
            data = []
            for row in range(model.rowCount()):
                data.append([])
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    data[row].append(model.data(index))
            table_df = pd.DataFrame(data,columns=['grade','class','session','time'])
            table_df = table_df.replace('', np.nan)
            table_df = table_df.ffill().bfill()
            table_dict = table_df.set_index('class').to_dict()
            for key,val in table_dict['session'].items():
                self.df.loc[self.df['class'] == key, 'session'] = val
            for i in self.time_df.columns:
                for key,val in table_dict['time'].items():
                    self.df.loc[(self.df['class'] == key) & (self.df['test type'] == int(i)), 'time'] = val+'-'+(datetime.strptime(val,'%H:%M')+timedelta(minutes=int(self.time_df[i][0]))).strftime('%H:%M')
        
            self.df.to_excel(upload_file+'/'+self.school+' Plan.xlsx', index=False)
            os.startfile(upload_file+'/'+self.school+' Plan.xlsx')
            self.close()
        
    def all_student_a_to_z_t(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            model = self.tableView_scaz.model()
            data = []
            for row in range(model.rowCount()):
                data.append([])
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    data[row].append(model.data(index))
            table_df = pd.DataFrame(data,columns=['grade','session','time','room','order'])
            table_df = table_df.replace('', np.nan)
            table_df['session'] = table_df['session'].ffill().bfill()
            table_df['time'] = table_df['time'].ffill().bfill()
            table_df = table_df[~table_df['room'].isnull()]
            table_df['grade'] = table_df['grade'].str.split().str[0]
            table_df['room'] = table_df['room'].apply(lambda x:"Salon "+str(x) if str(x).isdigit() else x)
            grade_list = sorted(self.df['grade'].unique())
            new_df = pd.DataFrame()
            for grade in grade_list:
                grade_df = self.df.loc[self.df['grade'] == str(grade)].reset_index(drop=True)

                table_grades = table_df.loc[table_df['grade'] == str(grade),'grade'].to_list()
                a = 0
                ng_df = pd.DataFrame()
                for i in range(len(table_grades)):
                    order_range = table_df.loc[table_df['grade'] == str(grade), 'order'].iloc[i]
                    n_df = grade_df.iloc[a:a+int(order_range)].reset_index(drop=True)
                    n_df['order'] = self.df.groupby('school').cumcount()+1
                    n_df['room'] = str(table_df.loc[table_df['grade'] == str(grade), 'room'].iloc[i]).replace('.0','')
                    n_df['session'] = table_df.loc[table_df['grade'] == str(grade), 'session'].iloc[i]
                    n_df['time'] = table_df.loc[table_df['grade'] == str(grade), 'time'].iloc[i]
                    ng_df = pd.concat([ng_df,n_df])
                    a+=int(order_range)
                new_df = pd.concat([new_df,ng_df]).reset_index(drop=True)
            table_dict = table_df.set_index('session').to_dict()
            for i in self.time_df.columns:
                for key,val in table_dict['time'].items():
                    new_df.loc[(new_df['session'] == key) & (new_df['test type'] == int(i)), 'time'] = val+'-'+(datetime.strptime(val,'%H:%M')+timedelta(minutes=int(self.time_df[i][0]))).strftime('%H:%M')
            a_df = new_df.loc[new_df['order'].astype(str) == '1']
            new_df['page'] = a_df.groupby('order').cumcount()+1
            new_df['page'] = new_df['page'].ffill().bfill().astype(int)
            
            new_df.to_excel(upload_file+'/'+self.school+' Plan.xlsx', index=False)
            os.startfile(upload_file+'/'+self.school+' Plan.xlsx')
            self.close()
        
    def same_class_a_to_z_cbt_t(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            model = self.tableView_scaz.model()
            data = []
            for row in range(model.rowCount()):
                data.append([])
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    data[row].append(model.data(index))
            table_df = pd.DataFrame(data,columns=['class','total']+['room-'+str(x) for x in range(1,int(self.total_class)+1)]+['session-'+str(x) for x in range(1,int(self.total_class)+1)]+['time-'+str(x) for x in range(1,int(self.total_class)+1)])
            table_df = table_df.replace('', np.nan)
            table_df[[col for col in table_df.columns if 'session' in col]] = table_df[[col for col in table_df.columns if 'session' in col]].ffill(axis=1).bfill()
            table_df[[col for col in table_df.columns if 'time' in col]] = table_df[[col for col in table_df.columns if 'time' in col]].ffill(axis=1).bfill()
            for i in range(1,int(self.total_class)+1):
                table_df['room-'+str(i)] = table_df['room-'+str(i)].str.split('+')
                table_df['room-'+str(i)+'-1'] = table_df['room-'+str(i)].str[1]
                table_df['room-'+str(i)] = table_df['room-'+str(i)].str[0]
            page = 1
            new_df = pd.DataFrame()
            for y in range(len(self.class_list)):
                spec_df = self.df[self.df['class'] == table_df.loc[y][0]]
                i = 0
                for x in range(int(self.total_class)):
                    spec_df1 = spec_df.iloc[i:i+int(table_df.loc[y][2+x])].reset_index(drop=True)
                    if type(table_df.loc[y][2+int(self.total_class)*3+x]) == str:
                        other_students = table_df.loc[y][2+int(self.total_class)*3+x].split('-')
                        other_df = self.df[self.df['class'] == other_students[0]].iloc[int('-'+other_students[1]):]
                        spec_df1 = pd.concat([other_df,spec_df1]).reset_index(drop=True)
                    spec_df1['room'] = eval("self.edit_room_"+str(1+x)+".text()")
                    spec_df1['session'] = table_df.loc[y][2+int(self.total_class)+x]
                    spec_df1['time'] = table_df.loc[y][2+int(self.total_class)*2+x]
                    spec_df1['order'] = self.df.groupby('school').cumcount()+1
                    spec_df1['time'] = spec_df1['time'][0]+'-'+(datetime.strptime(spec_df1['time'][0],'%H:%M')+timedelta(minutes=int(self.time_df[str(spec_df1['test type'][0])][0]))).strftime('%H:%M')
                    spec_df1['page'] = str(page)
                    new_df = pd.concat([new_df,spec_df1])
                    page+=1
                    i+=int(table_df.loc[y][2+x])


            new_df.to_excel(upload_file+'/'+self.school+' Plan.xlsx', index=False)
            os.startfile(upload_file+'/'+self.school+' Plan.xlsx')
            self.close()
    
    def divide_class(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            model = self.tableView_scaz.model()
            data = []
            for row in range(model.rowCount()):
                data.append([])
                for column in range(model.columnCount()):
                    index = model.index(row, column)
                    data[row].append(model.data(index))
            self.total_class = "2"
            table_df = pd.DataFrame(data,columns=['class','total']+['room-'+str(x) for x in range(1,int(self.total_class)+1)]+['session-'+str(x) for x in range(1,int(self.total_class)+1)]+['time-'+str(x) for x in range(1,int(self.total_class)+1)])
            table_df = table_df.replace('', np.nan)
            table_df[[col for col in table_df.columns if 'session' in col]] = table_df[[col for col in table_df.columns if 'session' in col]].ffill(axis=1).bfill()
            table_df[[col for col in table_df.columns if 'time' in col]] = table_df[[col for col in table_df.columns if 'time' in col]].ffill(axis=1).bfill()
            for i in range(1,int(self.total_class)+1):
                table_df['room-'+str(i)] = table_df['room-'+str(i)].str.split('+')
                table_df['room-'+str(i)+'-1'] = table_df['room-'+str(i)].str[1]
                table_df['room-'+str(i)] = table_df['room-'+str(i)].str[0]
            page = 1
            new_df = pd.DataFrame()
            for y in range(len(self.class_list)):
                spec_df = self.df[self.df['class'] == table_df.loc[y][0]]
                i = 0
                for x in range(int(self.total_class)):
                    spec_df1 = spec_df.iloc[i:i+int(table_df.loc[y][2+x])].reset_index(drop=True)
                    if type(table_df.loc[y][2+int(self.total_class)*3+x]) == str:
                        other_students = table_df.loc[y][2+int(self.total_class)*3+x].split('-')
                        other_df = self.df[self.df['class'] == other_students[0]].iloc[int('-'+other_students[1]):]
                        spec_df1 = pd.concat([other_df,spec_df1]).reset_index(drop=True)
                    spec_df1['room'] = eval("self.edit_room_"+str(1+x)+".text()")
                    spec_df1['session'] = table_df.loc[y][2+int(self.total_class)+x]
                    spec_df1['time'] = table_df.loc[y][2+int(self.total_class)*2+x]
                    spec_df1['order'] = self.df.groupby('school').cumcount()+1
                    spec_df1['time'] = spec_df1['time'][0]+'-'+(datetime.strptime(spec_df1['time'][0],'%H:%M')+timedelta(minutes=int(self.time_df[str(spec_df1['test type'][0])][0]))).strftime('%H:%M')
                    spec_df1['page'] = str(page)
                    new_df = pd.concat([new_df,spec_df1])
                    page+=1
                    i+=int(table_df.loc[y][2+x])


            new_df.to_excel(upload_file+'/'+self.school+' Plan.xlsx', index=False)
            os.startfile(upload_file+'/'+self.school+' Plan.xlsx')
            self.close()

        
        

        






























    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(), 
                                self.mapToGlobal(self.movement).y(), 
                                self.width(), 
                                self.height())
            self.start = self.end
        
    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False
        
    def btn_close_clicked(self):
        self.close()

    def btn_min_clicked(self):
        self.showMinimized()
        

    
        
class PandasModelPlan(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, index=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole or role == Qt.EditRole:
                value = self._data.iloc[index.row(), index.column()]
                return str(value)

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._data.iloc[index.row(), index.column()] = value
            return True
        return False

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(
            colname, ascending=order == Qt.AscendingOrder, inplace=True
        )
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()


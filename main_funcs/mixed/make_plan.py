from unidecode import unidecode  as uc
import pandas as pd
import numpy as np
from datetime import datetime
import os



file_shape = ['school','grade', 'country', 'lang', 'form code','time','test type','session','page','room','order','name','surname','id','class','month','day','year','gender','signature']
test_to_string = {4:'test_4',5:'test_3',8:'STEP 1',9:'STEP 2',20:'PSPK',21:'JSPK'}

def reshape_dataframe(file):
    df = pd.read_excel(file)
    #Shape all dataframe
    df = df.apply(lambda x: x.strip() if type(x) == str else x)
    for col in df.columns:
        df[col] = df[col].apply(lambda x: uc(x) if type(x)== str else x)
        df[col] = df[col].apply(lambda x: x.upper() if type(x)== str else x)

    df['class'] = df['class'].apply(lambda x: x.replace('FEN','Fen').replace('HAZ','Haz') if type(x)== str else x)
    #Correct name
    name_df = df['name'].fillna('') + (' ' + df['surname'].fillna(''))
    name_df = name_df.str.split()
    #Correct id
    df['id'] = df['id'].astype(str).apply(lambda x:x.replace('.0',''))
    #Correct date of birth
    df['day'] = df['day'].apply(lambda x: x if not isinstance(x,datetime) else x.strftime('%d/%m/%Y'))
    dob_df = df['day'].astype(str) + ('/' + df['month'].fillna(12345).astype('Int64').astype(str)) + ('/' + df['year'].fillna(12345).astype('Int64').astype(str))
    dob_df = dob_df.apply(lambda x: x.replace('/12345','') if '/12345' in x else x)
    dob_df = pd.to_datetime(dob_df,dayfirst=True)
    dob_df = dob_df.dt.strftime('%d-%m-%Y')
    dob_df = dob_df.str.split('-')
    #Correct gender
    df['gender'] = df['gender'].apply(lambda x: x.strip() if type(x) == str else x)
    df['gender'] = df['gender'].apply(lambda x: 'M' if x in ['ERKEK','E','MALE'] else x)
    df['gender'] = df['gender'].apply(lambda x: 'F' if x in ['KADIN','KIZ','K','FEMALE'] else x)
    #Correct class
    df['class'] = df['class'].apply(lambda x: x.strip() if type(x) == str else x)
    df['class'] = df['class'].apply(lambda x: x.replace('/','').replace('-','').replace('_','').replace('.','').replace(' ','').replace('\\','') if type(x) == str else x)

    #Replace corrected values
    df['name'] = name_df.str[:-1].apply(' '.join)
    df['surname'] = name_df.str[-1]
    df['day'] = dob_df.str[0]
    df['month'] = dob_df.str[1]
    df['year'] = dob_df.str[2]
    df['test type'] = df['test type'].astype('Int64')

    #Find incorrect id length
    incorrect_id_df = df['id'].str.len() 
    result = incorrect_id_df.index[incorrect_id_df != 11].tolist()
    incorrect_values = []
    for incorrect_index in result:
        incorrect_value = str(df.iloc[incorrect_index]['id'])
        if incorrect_value == 'nan':
            incorrect_value = df.iloc[incorrect_index]['name']
        incorrect_values.append(incorrect_value)

    #Find missing values
    idx, idy = np.where(pd.isnull(df))
    result = np.column_stack([df.index[idx], df.columns[idy]])
    missing_values = []
    for nan_value in result:
        missing_value = str(df.iloc[nan_value[0]]['id'])
        if missing_value == 'nan':
            missing_value = df.iloc[nan_value[0]]['name']
        missing_values.append([missing_value,nan_value[1].title()])
    return df


##################################### Aynı sınıfta Adan Zye Mantığı
def same_class_a_to_z(file,school,plan_logic,total_class):
    df = reshape_dataframe(file)
    df = df.sort_values(by = ['class','name'])

    class_list = sorted(df['class'].unique())
    for i in range(len(class_list)):
        df.loc[df['class'] == class_list[i], 'page'] = str(i+1)
        
    for key,val in test_to_string.items():
        df.loc[df['test type'] == key, 'form code'] = val
        
    df['room'] = df['class']
    df['order'] = df.groupby('class').cumcount()+1
    df['class'] = df['class'].apply(lambda x: x.replace('Haz','13'))
    df['grade']= df['class'].str.extract('(^\d*)')
    df['class'] = df['class'].apply(lambda x:x.replace('13','Haz'))
    df['school'] = school
    df['country'] = '585'
    df['lang'] = '484'
    df['time'] = ''
    df['session'] = ''
    df['signature'] = ''
    
    df = df[file_shape].reset_index(drop=True)
    return df,school,class_list,plan_logic,total_class

##################################### Aynı sınıfta Adan Zye Mantığı
def all_student_a_to_z(file,school,plan_logic,total_class):
    df = reshape_dataframe(file)
    df = df.sort_values(by = ['name','class'])
    class_list = sorted(df['class'].unique())
        
    for key,val in test_to_string.items():
        df.loc[df['test type'] == key, 'form code'] = val

    df['page'] = ''
    df['room'] = ''
    df['order'] = ''
    df['class'] = df['class'].apply(lambda x: x.replace('Haz','13'))
    df['grade']= df['class'].str.extract('(^\d*)')
    df['class'] = df['class'].apply(lambda x:x.replace('13','Haz'))
    df['school'] = school
    df['country'] = '585'
    df['lang'] = '484'
    df['time'] = ''
    df['session'] = ''
    df['signature'] = ''

    
    df = df[file_shape].reset_index(drop=True)
    
    return df,school,class_list,plan_logic,total_class
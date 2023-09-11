import main_funcs.mixed.mysql_connection as mc
import main_funcs.mixed.file_name_checker as fnc
import main_funcs.mixed.school_funcs as sf

import os
import pandas as pd

def attendance_check(file_directory,save_directory,institution,test_date,test_type):
    test_dict = {4:'Test Type 4 Test',5:'Test Type 3 Test',8:'Test Type 1 Test',
                    9:'Test Type 2 Test',20:'Test Type 5 Test',21:'Test Type 6 Test'}

    with open(file_directory,'rb') as f:
        raw_text = f.read()
        raw_text_list = raw_text.splitlines()

    db_pd = mc.engine.connect()
    df = pd.read_sql("SELECT * FROM iopssablon WHERE school = '{}' AND test_date = '{}'".format(institution,test_date),db_pd)
    db_pd.close()

    test_type = test_type.lower()
    print(test_type)

    if test_type == 'test_1':
        raw_text_list = [i[70:81].decode('utf-8') for i in raw_text_list]
        df = df.loc[(df['test_type'] == '8') | (df['test_type'] == '9')]

    elif test_type == 'test_3':
        raw_text_list = [i[43:54].decode('utf-8') for i in raw_text_list]
        df = df.loc[df['test_type'] == '5']

    elif test_type == 'test_4':
        raw_text_list = [i[43:53].decode('utf-8') for i in raw_text_list]
        df = df.loc[df['test_type'] == '4']
        df['student_number'] = df['student_number'].str[:10]

    raw_text_list = [i.replace(' ','') for i in raw_text_list]
    raw_df = pd.DataFrame(raw_text_list, columns=['student_number'])
    dfn = df[~ df["student_number"].isin(raw_df["student_number"])]
    df = dfn[['student_class','student_name','student_lastname','student_number','test_type']]
    df = df.reset_index(drop=True)
    df['test_type'] = df['test_type'].apply(lambda x: test_dict[int(x)])
    file_name = str(save_directory)+"/"+test_date+"_"+str(institution)+"_Gelmeyen Öğrenci Listesi.xlsx"
    file_name = fnc.check_file_name(file_name)
    df.to_excel(file_name, index = False)
    os.startfile(file_name)
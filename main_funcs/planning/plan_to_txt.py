try:
    import main_funcs.mixed.mysql_connection as mc
    import main_funcs.mixed.student_class_function as scf
except:
    import main_funcs.mixed.mysql_connection as mc
    import student_class_function as scf
import os
import pandas as pd

def plan_to_txt(save_directory,test_date,institution):
    db_pd = mc.engine.connect()
    df = pd.read_sql("SELECT * FROM iopssablon WHERE test_date = '{}' AND school = '{}'".format(test_date,institution),db_pd)
    test_type_list = df["test_type"].unique()
    for test_type in test_type_list:
        if test_type != "20" or test_type != "21":
            test_df = df[df['test_type'] == test_type]
            if test_type == "8":
                tmp_df = " "*40 + test_df['student_name'].apply(lambda x:x+(15-len(x))*" ") + test_df['student_lastname'].apply(lambda x:x+(15-len(x))*" ") + test_df['student_number'].apply(lambda x:x+(11-len(x))*" ") + "  " + test_df['bmonth'] + test_df['bday'] + test_df['byear'] + test_df['gender'] + "Y" + test_df['country_code'] + test_df['lang_code'] + "   " + test_df['student_class'].apply(lambda x:str(scf.student_class_val_reverse(x))) + " "*16 + "X" + " "*43 + "X" + " "*45 + "X"
                file_name = str(save_directory)+"/"+test_date+"_"+str(institution)+"Scanner File test_1 Step 1.txt"
                tmp_df.to_csv(file_name,header=None,index=None)
                os.startfile(file_name)
            elif test_type == "9":
                tmp_df = " "*40 + test_df['student_name'].apply(lambda x:x+(15-len(x))*" ") + test_df['student_lastname'].apply(lambda x:x+(15-len(x))*" ") + test_df['student_number'].apply(lambda x:x+(11-len(x))*" ") + "  " + test_df['bmonth'] + test_df['bday'] + test_df['byear'] + test_df['gender'] + "Y" + test_df['country_code'] + test_df['lang_code'] + "   " + test_df['student_class'].apply(lambda x:str(scf.student_class_val_reverse(x))) + " "*16 + "X" + " "*43 + "X" + " "*45 + "X"
                file_name = str(save_directory)+"/"+test_date+"_"+str(institution)+"Scanner File test_1 Step 2.txt"
                tmp_df.to_csv(file_name,header=None,index=None)
                os.startfile(file_name)
            elif test_type == "5":
                tmp_df = " "*43 + test_df['student_number'].apply(lambda x:x+(11-len(x))*" ") + " "*9 + " "*5 + test_df['byear'] + test_df['bmonth'] + test_df['bday'] + (test_df['student_lastname'] + " " +test_df['student_name']).apply(lambda x:x+(21-len(x))*" ") + test_df['country_code'] + test_df['student_class'].apply(lambda x:str(scf.student_class_val_reverse(x))).apply(lambda x:x+(14-len(x))*" ") + test_df['gender'] + " "*127 + "Y" + test_df['lang_code']
                file_name = str(save_directory)+"/"+test_date+"_"+str(institution)+"Scanner File test_3 Standard.txt"
                tmp_df.to_csv(file_name,header=None,index=None)
                os.startfile(file_name)
            elif test_type == "4":
                tmp_df = " "*43 + test_df['student_number'].apply(lambda x:x[:-1]).apply(lambda x:x+(10-len(x))*" ") + " "*10 + test_df['student_lastname'].apply(lambda x:x+(20-len(x))*" ") + " " +test_df['student_name'].apply(lambda x:x+(95-len(x))*" ") + test_df['byear'] + test_df['bmonth'] + test_df['bday'] + test_df['country_code'] + test_df['lang_code'] + test_df['gender'] + " "*63 + "X" + " "*69 + "X" + " "*140 + "X"
                file_name = str(save_directory)+"/"+test_date+"_"+str(institution)+"Scanner File test_4.txt"
                tmp_df.to_csv(file_name,header=None,index=None)
                os.startfile(file_name)
    db_pd.close()



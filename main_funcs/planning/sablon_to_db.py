import pandas as pd
import main_funcs.mixed.mysql_connection as mc

def sablon_to_db(test_date,institution,file):
    db_pd = mc.engine.connect()
    db_pd.execute("CREATE TABLE IF NOT EXISTS iopssablon (test_date VARCHAR(50),school VARCHAR(50),grade VARCHAR(50),country_code VARCHAR(50),lang_code VARCHAR(50),form_code VARCHAR(50),test_time VARCHAR(50),test_type VARCHAR(50), test_session VARCHAR(50),test_page VARCHAR(50),room VARCHAR(50),student_name VARCHAR(50),student_lastname VARCHAR(50),student_number VARCHAR(50),student_class VARCHAR(50),bmonth VARCHAR(50),bday VARCHAR(50),byear VARCHAR(50),gender VARCHAR(50))")
    db_pd.execute("CREATE TABLE IF NOT EXISTS students (student_number VARCHAR(50),student_name VARCHAR(50),student_lastname VARCHAR(50),date_of_birth_d_m_y VARCHAR(50),gender VARCHAR(50),student_class VARCHAR(50),school VARCHAR(50))")
    df = pd.read_excel(file)
    df = df.apply(lambda x:str(x).replace('.0','') if type(x)==float else x)
    df = df.apply(lambda x: x.strip() if type(x) == str else x)
    df['school'] = institution
    df['test_date'] = test_date
    df['grade'] = df['class'].str.extract('(^\d*)')
    df['day'] = df['day'].apply(lambda x:'0'+str(x) if len(str(x)) == 1 else str(x))
    df['month'] = df['month'].apply(lambda x:'0'+str(x) if len(str(x)) == 1 else str(x))
    df['id'] = df['id'].astype(str)
    cols = df.columns.tolist()
    df['date_of_birth_d_m_y'] = df['day'].astype(str)+"-"+df['month'].astype(str)+"-"+df['year'].astype(str)
    student_df = df[['id','name','surname','date_of_birth_d_m_y','gender','class','school']]
    student_df.columns = ['student_number','student_name','student_lastname','date_of_birth_d_m_y','gender','student_class','school']
    df = df[[cols[-1]]+ cols[:10] + cols[11:15] + [cols[15]] + [cols[16]] + cols[17:-2]]
    df.columns = ['test_date','school','grade','country_code','lang_code','form_code','test_time','test_type','test_session','test_page','room','student_name','student_lastname','student_number','student_class','bmonth','bday','byear','gender']
    id_tt_dict = df.set_index('student_number').to_dict()['test_type']
    all_test_types = df['test_type'].unique()
    duplicate_ids_list = []
    for test_typee in all_test_types:
        tmp_df = df.loc[df['test_type'] == test_typee]
        duplicate_id_check = tmp_df['student_number'].duplicated().sum()
        duplicate_ids_list.append(duplicate_id_check)
    duplicate_ids = [i for i in duplicate_ids_list if i != 0]
    true_list, false_list, duplicate_error,student_list, true_list_dif = [],[],[],[],[]
    sablon_df = pd.read_sql('SELECT * FROM iopssablon',db_pd)
    student_id_df = pd.read_sql('SELECT student_number FROM students',db_pd)
    if len(duplicate_ids) == 0:
        for key,val in id_tt_dict.items():
            fetch_one = sablon_df.loc[(sablon_df['test_date'] == test_date) & (sablon_df['school'] == institution) & (sablon_df['student_number'] == key) & (sablon_df['test_type'] == val)].reset_index(drop=True)
            fetch_one = fetch_one.values.tolist()
            false_list.extend(fetch_one)
            fetch_two = student_id_df.loc[(student_id_df['student_number'] == key)].reset_index(drop=True)
            fetch_two = fetch_two.values.tolist()
            student_list.extend(fetch_two)
        if false_list == [] or false_list == None:
            df.to_sql(con=db_pd, name='iopssablon', if_exists='append', index=False)
        if student_list == [] or student_list == None:
            student_df.to_sql(con=db_pd, name='students', if_exists='append', index=False)
        else:
            for student in student_list:
                spec_student_df = student_df.loc[student_df['student_number'] == student[0]].reset_index(drop=True)
                db_pd.execute(
                    "UPDATE students SET date_of_birth_d_m_y = %s ,gender = %s,student_class = %s,school = %s WHERE student_number = %s AND student_lastname = %s",
                    (spec_student_df.iloc[0][3],spec_student_df.iloc[0][4],spec_student_df.iloc[0][5],spec_student_df.iloc[0][6],spec_student_df.iloc[0][0],spec_student_df.iloc[0][2])
                    )
        true_list_dif = [len(id_tt_dict)-len(false_list)]
        true_list = df.to_records(index=False)        
    else:
        duplicate_error = ['Excel\'de TC\'si aynı '+str(int(duplicate_ids[0]))+' öğrenci var!']
        print(duplicate_error)
    db_pd.close()
    return [true_list,false_list,duplicate_error,true_list_dif]





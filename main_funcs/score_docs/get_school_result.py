try:
    import main_funcs.mixed.mysql_connection as mc
except:
    import main_funcs.mixed.mysql_connection as mc
import pandas as pd

def get_school_result_list(test_type_1,test_type_2,institution,main_date,spk_main_date):
    db_pd = mc.engine.connect()
    if test_type_2 == "test_1step_2":
        sql_select_by_date_and_school = """SELECT * FROM {} WHERE school = '{}' AND main_date = '{}' ORDER BY student_class,student_lastname,student_name"""
        df1 = pd.read_sql_query(sql_select_by_date_and_school.format(test_type_1,institution,main_date), con=db_pd)
        sql_select_by_date_and_school = """SELECT * FROM {} WHERE school = '{}' AND main_date = '{}' ORDER BY student_class,student_lastname,student_name"""
        df2 = pd.read_sql_query(sql_select_by_date_and_school.format(test_type_2,institution,main_date), con=db_pd)
        main_df = pd.concat([df1, df2], ignore_index=True, axis=0)
    elif test_type_2 == 'test_1speaking':
        sql_select_by_date_and_school = """SELECT * FROM {} WHERE school = '{}' AND main_date = '{}' ORDER BY student_class,student_lastname,student_name"""
        df1 = pd.read_sql_query(sql_select_by_date_and_school.format('test_1step_1',institution,main_date), con=db_pd)
        sql_select_by_date_and_school = """SELECT * FROM {} WHERE school = '{}' AND main_date = '{}' ORDER BY student_class,student_lastname,student_name"""
        df2 = pd.read_sql_query(sql_select_by_date_and_school.format('test_1step_2',institution,main_date), con=db_pd)
        sql_select_by_date_and_school = """SELECT * FROM {} WHERE school = '{}' AND main_date = '{}' ORDER BY student_class,student_lastname,student_name"""
        df3 = pd.read_sql_query(sql_select_by_date_and_school.format('test_1speaking',institution,spk_main_date), con=db_pd)
        df3['speaking_score'] = df3['total_score']
        df0 = pd.concat([df1, df2], ignore_index=True, axis=0)
        df = pd.merge(df0, df3, on=['country','provience','school','student_lastname','student_name','student_number','student_class'], how='outer', suffixes=('', '_y'))
        df.drop(df.filter(regex='_y$').columns, axis=1, inplace=True)
        df = df.combine_first(df3)
        df = df.fillna('   ')
        main_df = df[['country','provience','school','form_code','main_date','test_date','student_lastname','student_name','student_number','student_class',
            'reading_stars','reading_score','reading_cefr','reading_lexile',
            'listening_stars','listening_score','listening_cefr',
            'speaking_level','speaking_score','speaking_cefr']]

    elif test_type_2 == 'test_3_speaking':
        sql_select_by_date_and_school = """SELECT * FROM {} WHERE school = '{}' AND main_date = '{}' ORDER BY student_class,student_lastname,student_name"""
        df0 = pd.read_sql_query(sql_select_by_date_and_school.format('test_3_standard',institution,main_date), con=db_pd)
        sql_select_by_date_and_school = """SELECT * FROM {} WHERE school = '{}' AND main_date = '{}' ORDER BY student_class,student_lastname,student_name"""
        df3 = pd.read_sql_query(sql_select_by_date_and_school.format('test_3_speaking',institution,spk_main_date), con=db_pd)
        df3['speaking_score'] = df3['total_score']
        df = pd.merge(df0, df3, on=['country','provience','school','student_lastname','student_name','student_number','student_class'], how='outer', suffixes=('', '_y'))
        df.drop(df.filter(regex='_y$').columns, axis=1, inplace=True)
        df = df.combine_first(df3)
        df = df.fillna('   ')
        main_df = df[['country','provience','school','form_code','main_date','test_date','student_lastname','student_name','student_number','student_class',
            'listening_score','listening_cefr',
            'lfm_score','lfm_cefr',
            'reading_score','reading_cefr','reading_lexile',
            'osl','total_score',
            'speaking_level','speaking_score','speaking_cefr']]
    else:
        sql_select_by_date_and_school = """SELECT * FROM {} WHERE school = '{}' AND main_date = '{}' ORDER BY student_class,student_lastname,student_name"""
        main_df = pd.read_sql_query(sql_select_by_date_and_school.format(test_type_1,institution,main_date), con=db_pd)
    db_pd.close()
    return main_df
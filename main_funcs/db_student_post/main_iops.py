import main_funcs.db_student_post.iops_xls as ix
import main_funcs.mixed.student_class_function as scf
import main_funcs.mixed.mysql_connection as mc
    


def ps1_db_aktar(ps1file,ps1formcode,ps1country,ps1city,ps1maindate,institution):
    #Connect Database
    db_pd = mc.engine.connect()
    db_pd.execute("CREATE TABLE IF NOT EXISTS test_1step_1 (country VARCHAR(50), provience VARCHAR(50), school VARCHAR(50), form_code VARCHAR(50), main_date VARCHAR(50), test_date VARCHAR(50), student_lastname VARCHAR(50), student_name VARCHAR(50), student_number VARCHAR(50), student_class VARCHAR(50), reading_stars VARCHAR(50), reading_score VARCHAR(50), reading_cefr VARCHAR(50), reading_lexile VARCHAR(50), listening_stars VARCHAR(50), listening_score VARCHAR(50), listening_cefr VARCHAR(50))")
    
    #Get Dataframe from function
    ps1_df = ix.ps1_iops(ps1file)
    #Get all students and post database
    false_result,true_result = [],[]
    for x in range(len(ps1_df)):
        mycursor = db_pd.execute("SELECT * FROM test_1step_1 WHERE student_number = %s AND form_code = %s",(int(ps1_df.iloc[x][1]),ps1formcode))
        first_fetch = mycursor.fetchall()
        if first_fetch == [] or first_fetch == None:
            mycursor = db_pd.execute(
                "INSERT INTO test_1step_1 (country,provience,school,form_code,main_date,test_date,student_lastname,student_name,student_number,student_class,reading_stars,reading_score,reading_cefr,reading_lexile,listening_stars,listening_score,listening_cefr) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (str(ps1country),str(ps1city),institution,str(ps1formcode),str(ps1maindate),str(ps1_df.iloc[x][10]),str(ps1_df.iloc[x][0]).split()[0].title(),' '.join(str(ps1_df.iloc[x][0]).split()[1:]).title(),int(ps1_df.iloc[x][1]),str(scf.student_class_val(int(ps1_df.iloc[x][2]))),int(ps1_df.iloc[x][3]),str(ps1_df.iloc[x][4]),str(ps1_df.iloc[x][5]),str(ps1_df.iloc[x][6]),str(ps1_df.iloc[x][7]),str(ps1_df.iloc[x][8]),str(ps1_df.iloc[x][9]))
                )
            #Update Database
            
            mycursor = db_pd.execute("SELECT * FROM test_1step_1 WHERE student_number = %s AND form_code = %s",(int(ps1_df.iloc[x][1]),ps1formcode))
            for i in mycursor.fetchall():
                true_result.append(i)
        else:
            mycursor = db_pd.execute("SELECT * FROM test_1step_1 WHERE student_number = %s AND form_code = %s",(int(ps1_df.iloc[x][1]),ps1formcode))
            for i in mycursor.fetchall():
                false_result.append(i)
    db_pd.close()
    return [list(set(true_result)),list(set(false_result))]

def ps2_db_aktar(ps2file,ps2formcode,ps2country,ps2city,ps2maindate,institution):
    #Connect Database
    db_pd = mc.engine.connect()
    db_pd.execute("CREATE TABLE IF NOT EXISTS test_1step_2 (country VARCHAR(50), provience VARCHAR(50), school VARCHAR(50), form_code VARCHAR(50), main_date VARCHAR(50), test_date VARCHAR(50), student_lastname VARCHAR(50), student_name VARCHAR(50), student_number VARCHAR(50), student_class VARCHAR(50), reading_stars VARCHAR(50), reading_score VARCHAR(50), reading_cefr VARCHAR(50), reading_lexile VARCHAR(50), listening_stars VARCHAR(50), listening_score VARCHAR(50), listening_cefr VARCHAR(50))")
    
    #Get Dataframe from function
    ps2_df = ix.ps2_iops(ps2file)
    #Get all students and post database
    false_result,true_result = [],[]
    for x in range(len(ps2_df)):
        mycursor = db_pd.execute("SELECT * FROM test_1step_2 WHERE student_number = %s AND form_code = %s",(int(ps2_df.iloc[x][1]),ps2formcode))
        first_fetch = mycursor.fetchall()
        if first_fetch == [] or first_fetch == None:
            mycursor = db_pd.execute(
                "INSERT INTO test_1step_2 (country,provience,school,form_code,main_date,test_date,student_lastname,student_name,student_number,student_class,reading_stars,reading_score,reading_cefr,reading_lexile,listening_stars,listening_score,listening_cefr) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (str(ps2country),str(ps2city),institution,str(ps2formcode),str(ps2maindate),str(ps2_df.iloc[x][10]),str(ps2_df.iloc[x][0]).split()[0].title(),' '.join(str(ps2_df.iloc[x][0]).split()[1:]).title(),int(ps2_df.iloc[x][1]),str(scf.student_class_val(int(ps2_df.iloc[x][2]))),int(ps2_df.iloc[x][3]),str(ps2_df.iloc[x][4]),str(ps2_df.iloc[x][5]),str(ps2_df.iloc[x][6]),str(ps2_df.iloc[x][7]),str(ps2_df.iloc[x][8]),str(ps2_df.iloc[x][9]))
                )
            #Update Database
            
            mycursor = db_pd.execute("SELECT * FROM test_1step_2 WHERE student_number = %s AND form_code = %s",(int(ps2_df.iloc[x][1]),ps2formcode))
            for i in mycursor.fetchall():
                true_result.append(i)
        else:
            mycursor = db_pd.execute("SELECT * FROM test_1step_2 WHERE student_number = %s AND form_code = %s",(int(ps2_df.iloc[x][1]),ps2formcode))
            for i in mycursor.fetchall():
                false_result.append(i)
    db_pd.close()
    return [list(set(true_result)),list(set(false_result))]

def js_db_aktar(jsfile,jsformcode,jscountry,jscity,jsmaindate,institution):
    #Connect Database
    db_pd = mc.engine.connect()
    db_pd.execute("CREATE TABLE IF NOT EXISTS test_3_standard (country VARCHAR(50), provience VARCHAR(50), school VARCHAR(50), form_code VARCHAR(50), main_date VARCHAR(50), test_date VARCHAR(50), student_lastname VARCHAR(50), student_name VARCHAR(50), student_number VARCHAR(50), student_class VARCHAR(50), listening_score VARCHAR(50), listening_cefr VARCHAR(50), lfm_score VARCHAR(50), lfm_cefr VARCHAR(50), reading_score VARCHAR(50), reading_cefr VARCHAR(50), reading_lexile VARCHAR(50), total_score VARCHAR(50), osl VARCHAR(50))")
    #Get Dataframe from function
    js_df = ix.js_iops(jsfile)
    #Get all students and post database
    false_result,true_result = [],[]
    for x in range(len(js_df)):
        mycursor = db_pd.execute("SELECT * FROM test_3_standard WHERE student_number = %s AND form_code = %s",(int(js_df.iloc[x][1]),jsformcode))
        first_fetch = mycursor.fetchall()
        if first_fetch == [] or first_fetch == None:
            mycursor = db_pd.execute(
                "INSERT INTO test_3_standard (country,provience,school,form_code,main_date,test_date,student_lastname,student_name,student_number,student_class,listening_score,listening_cefr,lfm_score,lfm_cefr,reading_score,reading_cefr,reading_lexile,total_score,osl) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (str(jscountry),str(jscity),institution,str(jsformcode),str(jsmaindate),str(js_df.iloc[x][12]),str(js_df.iloc[x][0]).split()[0].title(),' '.join(str(js_df.iloc[x][0]).split()[1:]).title(),int(js_df.iloc[x][1]),str(scf.student_class_val(int(js_df.iloc[x][2]))),str(js_df.iloc[x][3]),str(js_df.iloc[x][4]),str(js_df.iloc[x][5]),str(js_df.iloc[x][6]),str(js_df.iloc[x][7]),str(js_df.iloc[x][8]),str(js_df.iloc[x][9]),str(js_df.iloc[x][10]),str(js_df.iloc[x][11]))
                )
            #Update Database
            
            mycursor = db_pd.execute("SELECT * FROM test_3_standard WHERE student_number = %s AND form_code = %s",(int(js_df.iloc[x][1]),jsformcode))
            for i in mycursor.fetchall():
                true_result.append(i)
        else:
            mycursor = db_pd.execute("SELECT * FROM test_3_standard WHERE student_number = %s AND form_code = %s",(int(js_df.iloc[x][1]),jsformcode))
            for i in mycursor.fetchall():
                false_result.append(i)
    db_pd.close()
    return [list(set(true_result)),list(set(false_result))]
    
def test_4_db_aktar(test_4file,test_4formcode,test_4country,test_4city,test_4maindate,institution):
    #Connect Database
    db_pd = mc.engine.connect()
    db_pd.execute("CREATE TABLE IF NOT EXISTS test_4 (country VARCHAR(50), provience VARCHAR(50), school VARCHAR(50), form_code VARCHAR(50), main_date VARCHAR(50), test_date VARCHAR(50), student_lastname VARCHAR(50), student_name VARCHAR(50), student_number VARCHAR(50), student_class VARCHAR(50), listening_score VARCHAR(50), listening_cefr VARCHAR(50), swe_score VARCHAR(50), swe_cefr VARCHAR(50), reading_score VARCHAR(50), reading_cefr VARCHAR(50), total_score VARCHAR(50))")
    #Get Dataframe from function
    test_4_df = ix.test_4_iops(test_4file,test_4maindate,institution)
    #Get all students and post database
    false_result,true_result = [],[]
    for x in range(len(test_4_df)):
        mycursor = db_pd.execute("SELECT * FROM test_4 WHERE student_number = %s AND form_code = %s",(int(test_4_df.iloc[x][9]),test_4formcode))
        first_fetch = mycursor.fetchall()
        if first_fetch == [] or first_fetch == None:
            mycursor = db_pd.execute(
                "INSERT INTO test_4 (country,provience,school,form_code,main_date,test_date,student_lastname,student_name,student_number,student_class,listening_score,listening_cefr,swe_score,swe_cefr,reading_score,reading_cefr,total_score) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (str(test_4country),str(test_4city),institution,str(test_4formcode),str(test_4maindate),str(test_4_df.iloc[x][11]),str(test_4_df.iloc[x][0]).split()[0].title(),' '.join(str(test_4_df.iloc[x][0]).split()[1:]).title(),int(test_4_df.iloc[x][9]),str(test_4_df.iloc[x][10]),str(test_4_df.iloc[x][2]),str(test_4_df.iloc[x][3]),str(test_4_df.iloc[x][4]),str(test_4_df.iloc[x][5]),str(test_4_df.iloc[x][6]),str(test_4_df.iloc[x][7]),str(test_4_df.iloc[x][8]))
                )
            #Update Database
            
            mycursor = db_pd.execute("SELECT * FROM test_4 WHERE student_number = %s AND form_code = %s",(int(test_4_df.iloc[x][9]),test_4formcode))
            for i in mycursor.fetchall():
                true_result.append(i)
        else:
            mycursor = db_pd.execute("SELECT * FROM test_4 WHERE student_number = %s AND form_code = %s",(int(test_4_df.iloc[x][9]),test_4formcode))
            for i in mycursor.fetchall():
                false_result.append(i)
    db_pd.close()
    return [list(set(true_result)),list(set(false_result))]

def test_4_db_aktar_no_class(test_4file,test_4formcode,test_4country,test_4city,test_4maindate,institution):
    #Connect Database
    db_pd = mc.engine.connect()
    db_pd.execute("CREATE TABLE IF NOT EXISTS test_4 (country VARCHAR(50), provience VARCHAR(50), school VARCHAR(50), form_code VARCHAR(50), main_date VARCHAR(50), test_date VARCHAR(50), student_lastname VARCHAR(50), student_name VARCHAR(50), student_number VARCHAR(50), student_class VARCHAR(50), listening_score VARCHAR(50), listening_cefr VARCHAR(50), swe_score VARCHAR(50), swe_cefr VARCHAR(50), reading_score VARCHAR(50), reading_cefr VARCHAR(50), total_score VARCHAR(50))")
    #Get Dataframe from function
    test_4_df = ix.test_4_iops_no_class(test_4file,test_4maindate,institution)
    #Get all students and post database
    false_result,true_result = [],[]
    for x in range(len(test_4_df)):
        mycursor = db_pd.execute("SELECT * FROM test_4 WHERE student_number = %s AND form_code = %s",(int(test_4_df.iloc[x][1]),test_4formcode))
        first_fetch = mycursor.fetchall()
        if first_fetch == [] or first_fetch == None:
            mycursor = db_pd.execute(
                "INSERT INTO test_4 (country,provience,school,form_code,main_date,test_date,student_lastname,student_name,student_number,student_class,listening_score,listening_cefr,swe_score,swe_cefr,reading_score,reading_cefr,total_score) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (str(test_4country),str(test_4city),institution,str(test_4formcode),str(test_4maindate),str(test_4_df.iloc[x][9]),str(test_4_df.iloc[x][0]).split()[0].title(),' '.join(str(test_4_df.iloc[x][0]).split()[1:]).title(),int(test_4_df.iloc[x][1]),"Sinif Yok",int(test_4_df.iloc[x][2]),str(test_4_df.iloc[x][3]),int(test_4_df.iloc[x][4]),str(test_4_df.iloc[x][5]),int(test_4_df.iloc[x][6]),str(test_4_df.iloc[x][7]),str(test_4_df.iloc[x][8]))
                )
            #Update Database
            
            mycursor = db_pd.execute("SELECT * FROM test_4 WHERE student_number = %s AND form_code = %s",(int(test_4_df.iloc[x][1]),test_4formcode))
            for i in mycursor.fetchall():
                true_result.append(i)
        else:
            mycursor = db_pd.execute("SELECT * FROM test_4 WHERE student_number = %s AND form_code = %s",(int(test_4_df.iloc[x][1]),test_4formcode))
            for i in mycursor.fetchall():
                false_result.append(i)
    db_pd.close()
    return [list(set(true_result)),list(set(false_result))]

def get_school_info(institution):
    #Connect Database
    db_pd = mc.engine.connect()
    mycursor = db_pd.execute("SELECT school_country,school_city FROM schools WHERE school_name = "+"'"+institution+"'")
    school_info = []
    for i in mycursor.fetchall():
        school_info.append(i)
    db_pd.close()
    return school_info


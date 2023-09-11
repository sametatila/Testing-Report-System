import main_funcs.mixed.mysql_connection as mc

def delete_school_result_by_date(test_type,institution,main_date):
    db_pd = mc.engine.connect()
    db_pd.execute("DELETE FROM "+test_type+" WHERE school = "+"'"+institution+"'"+" AND main_date = "+"'"+main_date+"'")
    db_pd.close()

def delete_selected_result_by_date(test_type,institution,main_date,main_list):
    db_pd = mc.engine.connect()
    main_list = eval(main_list)
    for item in main_list:
        student_number = item[8]
        db_pd.execute("DELETE FROM "+test_type+" WHERE school = "+"'"+institution+"'"+" AND main_date = "+"'"+main_date+"'"+" AND student_number = "+"'"+str(student_number)+"'")
    db_pd.close()
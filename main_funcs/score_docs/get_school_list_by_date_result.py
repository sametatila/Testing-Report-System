import main_funcs.mixed.mysql_connection as mc

def get_school_list_by_date(test_date):
    db_pd = mc.engine.connect()
    test_list = ['test_1step_1','test_1step_2','test_1speaking','test_3_standard','test_3_speaking','test_4']
    main_list = []
    for test_type in test_list:
        date_to_school_list = []
        for i in db_pd.execute("SELECT school FROM "+test_type+" WHERE main_date = %s",(str(test_date),)).fetchall():
            date_to_school_list.append(i[0])
        main_list.append(list(set(date_to_school_list)))
    db_pd.close()
    return main_list

def get_date_list_by_school(institution):
    db_pd = mc.engine.connect()
    test_list = ['test_1step_1','test_1step_2','test_1speaking','test_3_standard','test_3_speaking','test_4']
    main_list = []
    for test_type in test_list:
        date_to_school_list = []
        for i in db_pd.execute("SELECT main_date FROM "+test_type+" WHERE school = %s",(str(institution),)).fetchall():
            date_to_school_list.append(i[0])
        main_list.append(list(set(date_to_school_list)))
    db_pd.close()
    return main_list

def get_school_list_by_test_type():
    db_pd = mc.engine.connect()
    test_list = ['test_1step_1','test_1step_2','test_1speaking','test_3_standard','test_3_speaking','test_4']
    main_list = []
    for test_type in test_list:
        date_to_school_list = []
        for i in db_pd.execute("SELECT school FROM "+test_type).fetchall():
            date_to_school_list.append(i[0])
        main_list.append(list(set(date_to_school_list)))
    db_pd.close()
    return main_list
    
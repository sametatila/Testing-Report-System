import main_funcs.mixed.mysql_connection as mc

def get_historical_data():
    db_pd = mc.engine.connect()
    ps1_data_count,ps2_data_count,pspk_data_count,js_data_count,jspk_data_count,test_4_data_count = [],[],[],[],[],[]
    mycursor = db_pd.execute("SELECT COUNT(*) FROM test_1step_1")
    for i in mycursor.fetchall():
        ps1_data_count.append(i[0])
    mycursor = db_pd.execute("SELECT COUNT(*) FROM test_1step_2")
    for i in mycursor.fetchall():
        ps2_data_count.append(i[0])
    mycursor = db_pd.execute("SELECT COUNT(*) FROM test_1speaking")
    for i in mycursor.fetchall():
        pspk_data_count.append(i[0])
    mycursor = db_pd.execute("SELECT COUNT(*) FROM test_3_standard")
    for i in mycursor.fetchall():
        js_data_count.append(i[0])
    mycursor = db_pd.execute("SELECT COUNT(*) FROM test_3_speaking")
    for i in mycursor.fetchall():
        jspk_data_count.append(i[0])
    mycursor = db_pd.execute("SELECT COUNT(*) FROM test_4")
    for i in mycursor.fetchall():
        test_4_data_count.append(i[0])
    db_pd.close()
    return [ps1_data_count[0],ps2_data_count[0],pspk_data_count[0],js_data_count[0],jspk_data_count[0],test_4_data_count[0]]

def get_date_range_history(start_date,end_date,higher_institution,city,institution):
    import time
    import datetime
    db_pd = mc.engine.connect()
    start_timestamp = time.mktime(datetime.datetime.strptime(start_date,"%d-%m-%Y").timetuple())
    end_timestamp = time.mktime(datetime.datetime.strptime(end_date,"%d-%m-%Y").timetuple())
    table_list = ['test_1step_1','test_1step_2','test_1speaking','test_3_standard','test_3_speaking','test_4']
    main_list= []
    for test_type in table_list:
        sub_list = []
        list_1,list_2,list_3,list_4,list_5,list_6,list_7,list_8= [],[],[],[],[],[],[],[]
        for i in db_pd.execute("SELECT school,provience,main_date,student_class FROM "+test_type).fetchall():
            exam_date = time.mktime(datetime.datetime.strptime(i[2],"%d-%m-%Y").timetuple())
            i = list(i)
            if len(i[3]) == 2:
                i[3] = str(i[3][0])+".Sinif"
            elif len(i[3]) == 3:
                i[3] = str(i[3][:2])+".Sinif"
            elif len(i[3]) == 4:
                i[3] = str(i[3][:3])+".Sinif"
            elif len(i[3]) == 6:
                i[3] = str(i[3][4])+".Sinif"
            elif len(i[3]) == 7:
                i[3] = str(i[3][4:6])+".Sinif"
            if end_timestamp >= int(exam_date) >= start_timestamp:
                if higher_institution.lower() in i[0].lower() and higher_institution != "Kurum Seç":
                    if city.lower() == i[1].lower() and city != "Şehir Seç":
                        if institution.lower() == i[0].lower() and institution != "Okul Seç":
                            list_1.append(i[3])
                        else:
                            list_2.append(i[3])
                    elif city == "Şehir Seç":
                        if institution.lower() == i[0].lower() and institution != "Okul Seç":
                            list_3.append(i[3])
                        else:
                            list_4.append(i[3])
                elif higher_institution == "Kurum Seç":
                    if city.lower() == i[1].lower() and city != "Şehir Seç":
                        if institution.lower() == i[0].lower() and institution != "Okul Seç":
                            list_5.append(i[3])
                        else:
                            list_6.append(i[3])
                    elif city == "Şehir Seç":
                        if institution.lower() == i[0].lower() and institution != "Okul Seç":
                            list_7.append(i[3])
                        else:
                            list_8.append(i[3])
        
        dict_1 = {i:list_1.count(i) for i in list_1}
        dict_2 = {i:list_2.count(i) for i in list_2}
        dict_3 = {i:list_3.count(i) for i in list_3}
        dict_4 = {i:list_4.count(i) for i in list_4}
        dict_5 = {i:list_5.count(i) for i in list_5}
        dict_6 = {i:list_6.count(i) for i in list_6}
        dict_7 = {i:list_7.count(i) for i in list_7}
        dict_8 = {i:list_8.count(i) for i in list_8}
        for i in range(1,9):
            sub_list.append(eval("dict_"+str(i)))
        main_list.append(sub_list)
    db_pd.close()
    return main_list
            
def higher_institution_change_school(higher_institution):
    db_pd = mc.engine.connect()
    selected_school_list = []
    for i in db_pd.execute("SELECT school_name FROM schools").fetchall():
        if higher_institution != "Kurum Seç":
            if higher_institution.lower() in i[0].lower():
                selected_school_list.append(i[0])
    db_pd.close()
    return selected_school_list

def higher_institution_change_city(higher_institution):
    db_pd = mc.engine.connect()
    selected_city_list = []
    for i in db_pd.execute("SELECT school_name,school_city FROM schools").fetchall():
        if higher_institution != "Kurum Seç":
            if higher_institution.lower() in i[0].lower():
                selected_city_list.append(i[1])
    db_pd.close()
    return sorted(list(set(selected_city_list)))

def city_change_higher(higher_institution,city):
    db_pd = mc.engine.connect()
    selected_school_list = []
    for i in db_pd.execute("SELECT school_name,school_city FROM schools").fetchall():
        if higher_institution.lower() in i[0].lower():
            if city != "Şehir Seç":
                if city.lower() == i[1].lower():
                    selected_school_list.append(i[0])
    db_pd.close()
    return selected_school_list

def city_change(city):
    db_pd = mc.engine.connect()
    selected_school_list = []
    for i in db_pd.execute("SELECT school_name,school_city FROM schools").fetchall():
        if city != "Şehir Seç":
            if city.lower() == i[1].lower():
                selected_school_list.append(i[0])
    db_pd.close()
    return selected_school_list

def city_list():
    db_pd = mc.engine.connect()
    city_list = []
    for i in db_pd.execute("SELECT school_city FROM schools").fetchall():
        city_list.append(i[0])
    db_pd.close()
    return sorted(list(set(city_list)))

def institution_list():
    db_pd = mc.engine.connect()
    school_list = []
    for i in db_pd.execute("SELECT school_name FROM schools").fetchall():
        school_list.append(i[0])
    db_pd.close()
    return school_list




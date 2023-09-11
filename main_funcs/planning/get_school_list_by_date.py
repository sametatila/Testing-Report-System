import main_funcs.mixed.mysql_connection as mc

def get_school_list_by_date(test_date):
    db_pd = mc.engine.connect()
    date_to_school_list = []
    for i in db_pd.execute("SELECT school FROM iopssablon WHERE test_date = "+"'"+test_date+"'").fetchall():
        date_to_school_list.append(i[0])
    db_pd.close()
    return list(set(date_to_school_list))


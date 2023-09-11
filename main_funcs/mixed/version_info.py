import main_funcs.mixed.mysql_connection as mc

def get_version_info():
    with open('./main_funcs/mixed/version', 'rb') as f:
        version_info = str(f.read())[2:-1]
    return version_info

def last_version_info():
    db_pd = mc.engine.connect()
    mycursor = db_pd.execute("SELECT version_info FROM version_info")
    fetch = mycursor.fetchall()
    last_version = fetch[-1][0]
    db_pd.close()
    return last_version
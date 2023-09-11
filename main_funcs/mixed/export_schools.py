import main_funcs.mixed.mysql_connection as mc
import csv

def get_all_schools_infos(save_directory,institution):
    db_pd = mc.engine.connect()
    mycursor = db_pd.execute("SELECT * FROM schools")
    headers = [col for col in mycursor.keys()]
    rows = []
    for i in mycursor:
        school_name_raw = i[0]
        if institution == "?":
            rows.append((x.upper() for x in i))
        elif institution.lower() in school_name_raw.lower():
            rows.append((x.upper() for x in i))
    rows.insert(0, tuple(headers))
    fp = open(str(save_directory)+"/"+institution+".csv", 'w', newline = '') 
    myFile = csv.writer(fp)
    myFile.writerows(rows)
    fp.close()
    import os
    os.startfile(str(save_directory)+"/"+institution+".csv")
    db_pd.close()





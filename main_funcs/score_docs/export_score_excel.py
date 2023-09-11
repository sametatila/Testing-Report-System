import main_funcs.mixed.mysql_connection as mc
from openpyxl import Workbook
from datetime import datetime
import math
import main_funcs.mixed.file_name_checker as fnc

def export_excel(test_type,save_directory,institution,main_date):
    db_pd = mc.engine.connect()
    mycursor = db_pd.execute("SELECT * FROM {} WHERE school = '{}' AND main_date = '{}' ORDER BY student_class,student_lastname,student_name".format(test_type,institution,main_date))
    headers = [col for col in mycursor.keys()]
    headers = tuple(headers)
    if test_type == "test_1step_1" or test_type == "test_1step_2":
        headers = (headers[9].replace("student_class","Class"),headers[7].replace("student_name","Given Name"),headers[6].replace("student_lastname","Family Name")
                ,headers[8].replace("student_number","Student ID"))+tuple([x.replace("_"," ").title() for x in list(headers[10:])])+tuple(["Total Score"])
    else:
        headers = (headers[9].replace("student_class","Class"),headers[7].replace("student_name","Given Name"),headers[6].replace("student_lastname","Family Name")
                ,headers[8].replace("student_number","Student ID"))+tuple([x.replace("_"," ").title() for x in list(headers[10:])])
    wb = Workbook()
    ws = wb['Sheet']
    ws.append(headers)
    for i in mycursor:
        if test_type == "test_1step_1" or test_type == "test_1step_2":
            try:
                total_score = math.ceil((int(i[11])+int(i[15]))/2)
            except:
                total_score = "NS"
            i = (i[9],i[7].upper(),i[6].upper(),i[8])+i[10:]+tuple([str(total_score)])
        else:
            i = (i[9],i[7].upper(),i[6].upper(),i[8])+i[10:]
        ws.append(i)
    main_date = datetime.strptime(main_date, '%d-%m-%Y').strftime('%B, %Y')
    test_type_file = test_type.replace('_',' ').title()
    file_name = save_directory+"/"+str(main_date)+"_"+institution+"_"+test_type_file+"_Score Roster.xlsx"
    file_name = fnc.check_file_name(file_name)
    wb.save(file_name)
    import os
    os.startfile(file_name)
    db_pd.close()

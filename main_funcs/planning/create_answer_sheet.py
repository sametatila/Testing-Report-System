from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import json
import main_funcs.mixed.student_class_function as scf
import main_funcs.mixed.mysql_connection as mc
import pandas as pd
import os
import main_funcs.mixed.file_name_checker as fnc


pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
pdfmetrics.registerFont(TTFont('VerdanaB', './data/gui_data/fonts/verdanab.ttf'))



def create_test_1optic(test_date,institution,save_directory,printer):
    def read_json_file():
        with open('./data/exam_data/answer_sheet_data.json','r') as f:
            data = json.load(f)
        return data

    json_data_raw = read_json_file()

    def write_name(name,x,y):
        x = x + json_data['first_name_x']
        y = y + json_data['first_name_y']
        for b in range(15):
            if b in range(len(name)):
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,name[b])
                for c in range(len(letterlist)):
                    if name[b] != " ":
                        if name[b] == letterlist[c]:
                            pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)

    def write_lastname(lastname,x,y):
        x = x + json_data['last_name_x']
        y = y + json_data['last_name_y']
        for b in range(15):
            if b in range(len(lastname)):
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,lastname[b])
                for c in range(len(letterlist)):
                    if lastname[b] != " ":
                        if lastname[b] == letterlist[c]:
                            pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)

    def write_student_id(student_id,x,y):
        x = x + json_data['student_id_x']
        y = y + json_data['student_id_y']
        for b in range(13):
            if b in range(len(student_id)):
                if student_id != "" or student_id != " " or student_id != "  ":
                    pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,student_id[b])
                    for c in range(len(numlist)):
                        if student_id[b] != " ":
                            if student_id[b] == numlist[c]:
                                pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)

    def write_student_date_of_birth(bmonth,bday,byear,x,y):
        x = x + json_data['dob_month_x']
        y = y + json_data['dob_month_y']
        b = 0
        for c in range(len(datelist)):
            if bmonth != "" or bmonth != " " or bmonth != "  ":
                if bmonth == datelist[c]:
                    pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
        x = x + json_data['dob_day_x']
        y = y + json_data['dob_day_y']
        for b in range(2):
            if bday != "" or bday != " " or bday != "  ":
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,bday[b])
                for c in range(len(numlist)):
                    if bday[b] == numlist[c]:
                        pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
        x = x + json_data['dob_year_x']
        y = y + json_data['dob_year_y']
        for b in range(4):
            if byear != "" or byear != " " or byear != "  ":
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,byear[b])
                for c in range(len(numlist)):
                    if byear[b] == numlist[c]:
                        pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)

    def write_gender(gender,x,y):
        x = x + json_data['gender_x']
        y = y + json_data['gender_y']
        b = 0
        for c in range(len(genderlist)):
            if gender != "" or gender != " " or gender != "  ":
                if gender == genderlist[c]:
                    pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*json_data['gender_vertical_spacing'], main_circle_width, fill=1)

    def write_country_code(country_code,x,y):
        x = x + json_data['country_code_x']
        y = y + json_data['country_code_y']
        for b in range(3):
            pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,country_code[b])
            for c in range(len(numlist)):
                if country_code[b] == numlist[c]:
                    pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)

    def write_lang_code(lang_code,x,y):
        x = x + json_data['language_code_x']
        y = y + json_data['language_code_y']
        for b in range(3):
            pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,lang_code[b])
            for c in range(len(numlist)):
                if lang_code[b] == numlist[c]:
                    pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)

    def write_grade(grade,x,y):
        x = x + json_data['grade_x']
        y = y + json_data['grade_y']
        b = 0
        for c in range(len(gradelist)):
            if grade != "" or grade != " " or grade != "  ":
                if grade == gradelist[c]:
                    pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)

    def write_group_code(group_code,x,y):
        x = x + json_data['group_code_x']
        y = y + json_data['group_code_y']
        for b in range(len(group_code)):
            pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,group_code[b])
            for c in range(len(numlist)):
                if group_code[b] == numlist[c]:
                    pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
    file_name = str(save_directory)+"/"+test_date[6:]+"-"+test_date[3:5]+"-"+test_date[:2]+"_"+str(institution)+"_test_1Optic.pdf"
    file_name = fnc.check_file_name(file_name)
    pdf = canvas.Canvas(file_name, pagesize=letter)
    width,height = letter
    
    #Select iopssablon table and turn into dataframe
    db_pd = mc.engine.connect()
    sql_select_by_date_and_school = "SELECT * FROM iopssablon WHERE test_date = "+"'"+test_date+"'"+" AND school = "+"'"+institution+"'"
    df = pd.read_sql(sql_select_by_date_and_school, con=db_pd)
    #Format page col into int
    df["test_page"] = df["test_page"].astype('int64')
    #Loop pages
    for i in range(df["test_page"].max()):
        page_info = df[df.test_page == i+1]
        #Get records
        for x in range(len(page_info)):
            name = str(page_info['student_name'].iloc[x])
            lastname = str(page_info['student_lastname'].iloc[x])
            student_id = str(page_info['student_number'].iloc[x])
            student_class = str(page_info['student_class'].iloc[x])
            gender = str(page_info['gender'].iloc[x])
            bmonth = str(page_info['bmonth'].iloc[x])
            if len(str(page_info['bmonth'].iloc[x])) == 1:
                bmonth = "0"+str(page_info['bmonth'].iloc[x])
            bday = str(page_info['bday'].iloc[x])
            if len(str(page_info['bday'].iloc[x])) == 1:
                bday = "0"+str(page_info['bday'].iloc[x])
            byear = str(page_info['byear'].iloc[x])
            group_code = scf.student_class_val_reverse(student_class)
            form_code = str(page_info['form_code'].iloc[x])
            country_code = str(page_info['country_code'].iloc[x])
            lang_code = str(page_info['lang_code'].iloc[x])
            grade = str(page_info['grade'].iloc[x])
            test_type = int(page_info['test_type'].iloc[x])
            
            if test_type == 8 or test_type == 9:
                if printer == 'riso':
                    json_data = json_data_raw['test_1optic']['riso']
                    x, y = json_data['riso_x'], json_data['riso_y']
                elif printer == "xerox":
                    json_data = json_data_raw['test_1optic']['xerox']
                    x, y = json_data['xerox_x'], json_data['xerox_y']
                elif printer == "hp":
                    json_data = json_data_raw['test_1optic']['hp']
                    x, y = json_data['hp_x'], json_data['hp_y']
                else:
                    json_data = json_data_raw['test_1optic']['other']
                    x, y = json_data['other_printer_x'], json_data['other_printer_y']
                
                main_plus_string_x = json_data['main_plus_string_x']
                main_plus_string_y = json_data['main_plus_string_y']
                main_plus_circle_x = json_data['main_plus_circle_x']
                main_plus_circle_y = json_data['main_plus_circle_y']
                h_spacing = json_data['horizontal_spacing']
                v_spacing = json_data['vertical_spacing']
                main_circle_width = json_data['main_circle_width']

                pdf.setFont('VerdanaB',11)
                pdf.drawString(x+json_data['header_first_name_x'],y+json_data['header_first_name_y'],name)
                pdf.drawString(x+json_data['header_last_name_x'],y+json_data['header_last_name_y'],lastname)
                pdf.drawString(x+json_data['header_form_code_x'],y+json_data['header_form_code_y'],form_code)
                pdf.drawString(x+json_data['header_test_date_x'],y+json_data['header_test_date_y'],test_date)
                pdf.circle(x+json_data['header_consent_circle_x'],y+json_data['header_consent_circle_y'],main_circle_width,fill=1)
                if len(institution) < 22:
                    pdf.drawString(x+json_data['header_institution_x_1'],y+json_data['header_institution_y_1'],institution)
                else:
                    if len(institution.split()) == 3:
                        pdf.drawString(x+json_data['header_institution_x_1'],y+json_data['header_institution_y_1'],institution.split()[0]+" "+institution.split()[1])
                        pdf.drawString(x+json_data['header_institution_x_2'],y+json_data['header_institution_y_2'],institution.split()[2])
                    elif len(institution.split()) == 4:
                        pdf.drawString(x+json_data['header_institution_x_1'],y+json_data['header_institution_y_1'],institution.split()[0]+" "+institution.split()[1])
                        pdf.drawString(x+json_data['header_institution_x_2'],json_data['header_institution_y_2'],institution.split()[2]+" "+institution.split()[3])
                    elif len(institution.split()) == 5:
                        pdf.drawString(x+json_data['header_institution_x_1'],y+json_data['header_institution_y_1'],institution.split()[0]+" "+institution.split()[1]+" "+institution.split()[2])
                        pdf.drawString(x+json_data['header_institution_x_2'],json_data['header_institution_y_2'],institution.split()[3]+" "+institution.split()[4])
                letterlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                numlist = ['0','1','2','3','4','5','6','7','8','9']
                datelist = ['01','02','03','04','05','06','07','08','09','10','11','12']
                genderlist = ['M','F']
                gradelist = ['1','2','3','4','5','6','7','8','9','Other']
                
                write_name(name,x,y)
                write_lastname(lastname,x,y)
                write_student_id(student_id,x,y)
                write_student_date_of_birth(bmonth,bday,byear,x,y)
                write_gender(gender,x,y)
                write_country_code(country_code,x,y)
                write_lang_code(lang_code,x,y)
                write_grade(grade,x,y)
                write_group_code(group_code,x,y)

                pdf.showPage()
    
    pdf.save()
    os.startfile(file_name)
    db_pd.close()
    
def create_test_3_optic(test_date,institution,save_directory,printer):
    def read_json_file():
        with open('./data/exam_data/answer_sheet_data.json','r') as f:
            data = json.load(f)
        return data

    json_data_raw = read_json_file()
    
    def write_name(name,lastname,x,y):
        x = x + json_data['full_name_x']
        y = y + json_data['full_name_y']
        full_name = lastname+" "+name
        for b in range(21):
            if b in range(len(full_name)):
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,full_name[b])
                for c in range(len(letterlist)):
                    if full_name[b] != " ":
                        if full_name[b] == letterlist[c]:
                            pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
                            
    def write_student_id(student_id,x,y):
        x = x + json_data['student_id_x']
        y = y + json_data['student_id_y']
        for b in range(12):
            if b in range(len(student_id)):
                if student_id != "" or student_id != " " or student_id != "  ":
                    pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,student_id[b])
                    for c in range(len(numlist)):
                        if student_id[b] != " ":
                            if student_id[b] == numlist[c]:
                                pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
    
    def write_group_code(student_class,x,y):
        x = x + json_data['group_code_x']
        y = y + json_data['group_code_y']
        for b in range(5):
            if b in range(len(student_class)):
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,student_class[b])
                for c in range(len(numlist)):
                    if student_class[b] != " ":
                        if student_class[b] == numlist[c]:
                            pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
    
    def write_student_date_of_birth(bmonth,bday,byear,x,y):
        x = x + json_data['dob_year_x']
        y = y + json_data['dob_year_y']
        b = 0
        for b in range(4):
            if byear != "" or byear != " " or byear != "  ":
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,byear[b])
                for c in range(len(numlist)):
                    if byear[b] == numlist[c]:
                        pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
        x = x + json_data['dob_month_x']
        y = y + json_data['dob_month_y']
        for b in range(2):
            if bmonth != "" or bmonth != " " or bmonth != "  ":
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,bmonth[b])
                for c in range(len(numlist)):
                    if bmonth[b] == numlist[c]:
                        pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
        x = x + json_data['dob_day_x']
        y = y + json_data['dob_day_y']
        for b in range(2):
            pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,bday[b])
            if bday != "" or bday != " " or bday != "  ":
                for c in range(len(numlist)):
                    if bday[b] == numlist[c]:
                        pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)

    def write_country_code(country_code,x,y):
        x = x + json_data['country_code_x']
        y = y + json_data['country_code_y']
        for b in range(5):
            if b in range(len(country_code)):
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,country_code[b])
                for c in range(len(numlist)):
                    if country_code[b] != " ":
                        if country_code[b] == numlist[c]:
                            pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
    
    def write_lang_code(lang_code,x,y):
        x = x + json_data['language_code_x']
        y = y + json_data['language_code_y']
        for b in range(5):
            if b in range(len(lang_code)):
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,lang_code[b])
                for c in range(len(numlist)):
                    if lang_code[b] != " ":
                        if lang_code[b] == numlist[c]:
                            pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
    
    def write_gender(gender,x,y):
        x = x + json_data['gender_x']
        y = y + json_data['gender_y']
        b = 0
        for c in range(len(genderlist)):
            if gender != "" or gender != " " or gender != "  ":
                if gender == genderlist[c]:
                    pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y+c*json_data['gender_vertical_spacing'], main_circle_width, fill=1)
    file_name = str(save_directory)+"/"+test_date[6:]+"-"+test_date[3:5]+"-"+test_date[:2]+"_"+str(institution)+"_test_3Optic.pdf"
    file_name = fnc.check_file_name(file_name)
    pdf = canvas.Canvas(file_name, pagesize=letter)
        
    #Select iopssablon table and turn into dataframe
    db_pd = mc.engine.connect()
    sql_select_by_date_and_school = "SELECT * FROM iopssablon WHERE test_date = "+"'"+test_date+"'"+" AND school = "+"'"+institution+"'"
    df = pd.read_sql(sql_select_by_date_and_school, con=db_pd)
    #Format page col into int
    df["test_page"] = df["test_page"].astype('int64')
    #Loop pages
    for i in range(df["test_page"].max()):
        page_info = df[df.test_page == i+1]
        #Get records
        for x in range(len(page_info)):
            name = str(page_info['student_name'].iloc[x])
            lastname = str(page_info['student_lastname'].iloc[x])
            student_id = str(page_info['student_number'].iloc[x])
            student_class = str(page_info['student_class'].iloc[x])
            gender = str(page_info['gender'].iloc[x])
            bmonth = str(page_info['bmonth'].iloc[x])
            if len(str(page_info['bmonth'].iloc[x])) == 1:
                bmonth = "0"+str(page_info['bmonth'].iloc[x])
            bday = str(page_info['bday'].iloc[x])
            if len(str(page_info['bday'].iloc[x])) == 1:
                bday = "0"+str(page_info['bday'].iloc[x])
            byear = str(page_info['byear'].iloc[x])
            group_code = scf.student_class_val_reverse(student_class)
            form_code = str(page_info['form_code'].iloc[x])
            country_code = str(page_info['country_code'].iloc[x])
            lang_code = str(page_info['lang_code'].iloc[x])
            test_type = int(page_info['test_type'].iloc[x])
            
            if test_type == 5:
                if printer == 'riso':
                    json_data = json_data_raw['test_3_optic']['riso']
                    x, y = json_data['riso_x'], json_data['riso_y']
                elif printer == 'xerox':
                    json_data = json_data_raw['test_3_optic']['xerox']
                    x, y = json_data['xerox_x'], json_data['xerox_y']
                elif printer == "hp":
                    json_data = json_data_raw['test_3_optic']['hp']
                    x, y = json_data['hp_x'], json_data['hp_y']
                else:
                    json_data = json_data_raw['test_3_optic']['other_printer']
                    x, y = json_data['other_printer_x'], json_data['other_printer_y']
                
                main_plus_string_x = json_data['main_plus_string_x']
                main_plus_string_y = json_data['main_plus_string_y']
                main_plus_circle_x = json_data['main_plus_circle_x']
                main_plus_circle_y = json_data['main_plus_circle_y']
                h_spacing = json_data['horizontal_spacing']
                v_spacing = json_data['vertical_spacing']
                main_circle_width = json_data['main_circle_width']

                pdf.setFont('VerdanaB',11)
                pdf.drawString(x+json_data['header_last_name_x'],y+json_data['header_last_name_y'],lastname)
                pdf.drawString(x+json_data['header_first_name_x'],y+json_data['header_first_name_y'],name)
                pdf.drawString(x+json_data['header_form_code_x'],y+json_data['header_form_code_y'],form_code)
                pdf.drawString(x+json_data['header_test_date_x'],y+json_data['header_test_date_y'],test_date)
                pdf.circle(x+json_data['header_consent_circle_x'],y+json_data['header_consent_circle_y'], main_circle_width, fill=1)
                if len(institution) < 22:
                    pdf.drawString(x+json_data['header_institution_x_1'],y+json_data['header_institution_y_1'],institution)
                else:
                    if len(institution.split()) == 3:
                        pdf.drawString(x+json_data['header_institution_x_1'],y+json_data['header_institution_y_1'],institution.split()[0]+" "+institution.split()[1])
                        pdf.drawString(x+json_data['header_institution_x_2'],y+json_data['header_institution_y_2'],institution.split()[2])
                    elif len(institution.split()) == 4:
                        pdf.drawString(x+json_data['header_institution_x_1'],y+json_data['header_institution_y_1'],institution.split()[0]+" "+institution.split()[1])
                        pdf.drawString(x+json_data['header_institution_x_2'],y+json_data['header_institution_y_2'],institution.split()[2]+" "+institution.split()[3])
                    elif len(institution.split()) == 5:
                        pdf.drawString(x+json_data['header_institution_x_1'],y+json_data['header_institution_y_1'],institution.split()[0]+" "+institution.split()[1]+" "+institution.split()[2])
                        pdf.drawString(x+json_data['header_institution_x_2'],y+json_data['header_institution_y_2'],institution.split()[3]+" "+institution.split()[4])

                letterlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                numlist = ['0','1','2','3','4','5','6','7','8','9']
                genderlist = ['M','F']

                write_name(name,lastname,x,y)
                write_student_id(student_id,x,y)
                write_student_date_of_birth(bmonth,bday,byear,x,y)
                write_gender(gender,x,y)
                write_country_code(country_code,x,y)
                write_lang_code(lang_code,x,y)
                write_group_code(group_code,x,y)

                pdf.showPage()
    
    pdf.save()
    os.startfile(file_name)
    db_pd.close()

def create_test_4_optic(test_date,institution,save_directory,printer):
    def read_json_file():
        with open('./data/exam_data/answer_sheet_data.json','r') as f:
            data = json.load(f)
        return data

    json_data_raw = read_json_file()
    
    def write_name(name,x,y):
        x = x + json_data['first_name_x']
        y = y + json_data['first_name_y']
        for b in range(15):
            if b in range(len(name)):
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,name[b])
                for c in range(len(letterlist)):
                    if name[b] != " ":
                        if name[b] == letterlist[c]:
                            pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)

    def write_lastname(lastname,x,y):
        x = x + json_data['last_name_x']
        y = y + json_data['last_name_y']
        for b in range(15):
            if b in range(len(lastname)):
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,lastname[b])
                for c in range(len(letterlist)):
                    if lastname[b] != " ":
                        if lastname[b] == letterlist[c]:
                            pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
                            
    def write_student_id(student_id,x,y):
        x = x + json_data['student_id_x']
        y = y + json_data['student_id_y']
        for b in range(10):
            if b in range(len(student_id)):
                if student_id != "" or student_id != " " or student_id != "  ":
                    pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,student_id[b])
                    for c in range(len(numlist)):
                        if student_id[b] != " ":
                            if student_id[b] == numlist[c]:
                                pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
    
    def write_student_date_of_birth(bmonth,bday,byear,x,y):
        x = x + json_data['dob_month_x']
        y = y + json_data['dob_month_y']
        b = 0
        for c in range(len(datelist)):
            if bmonth != "" or bmonth != " " or bmonth != "  ":
                if bmonth == datelist[c]:
                    pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
        x = x + json_data['dob_day_x']
        y = y + json_data['dob_day_y']
        for b in range(2):
            if bday != "" or bday != " " or bday != "  ":
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,bday[b])
                for c in range(len(numlist)):
                    if bday[b] == numlist[c]:
                        pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
        x = x + json_data['dob_year_x']
        y = y + json_data['dob_year_y']
        for b in range(4):
            if byear != "" or byear != " " or byear != "  ":
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,byear[b])
                for c in range(len(numlist)):
                    if byear[b] == numlist[c]:
                        pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)

    def write_country_code(country_code,x,y):
        x = x + json_data['country_code_x']
        y = y + json_data['country_code_y']
        for b in range(5):
            if b in range(len(country_code)):
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,country_code[b])
                for c in range(len(numlist)):
                    if country_code[b] != " ":
                        if country_code[b] == numlist[c]:
                            pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
    
    def write_lang_code(lang_code,x,y):
        x = x + json_data['language_code_x']
        y = y + json_data['language_code_y']
        for b in range(5):
            if b in range(len(lang_code)):
                pdf.drawString(x+main_plus_string_x+b*h_spacing,y+main_plus_string_y,lang_code[b])
                for c in range(len(numlist)):
                    if lang_code[b] != " ":
                        if lang_code[b] == numlist[c]:
                            pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*v_spacing, main_circle_width, fill=1)
    
    def write_gender(gender,x,y):
        x = x + json_data['gender_x']
        y = y + json_data['gender_y']
        b = 0
        for c in range(len(genderlist)):
            if gender != "" or gender != " " or gender != "  ":
                if gender == genderlist[c]:
                    pdf.circle(x+main_plus_circle_x+b*h_spacing,y+main_plus_circle_y-c*json_data['gender_vertical_spacing'], main_circle_width, fill=1)
    file_name = str(save_directory)+"/"+test_date[6:]+"-"+test_date[3:5]+"-"+test_date[:2]+"_"+str(institution)+"_test_4Optic.pdf"
    file_name = fnc.check_file_name(file_name)
    pdf = canvas.Canvas(file_name, pagesize=letter)
    width,height = letter
    
    #Select iopssablon table and turn into dataframe
    db_pd = mc.engine.connect()
    sql_select_by_date_and_school = "SELECT * FROM iopssablon WHERE test_date = "+"'"+test_date+"'"+" AND school = "+"'"+institution+"'"
    df = pd.read_sql(sql_select_by_date_and_school, con=db_pd)
    #Format page col into int
    df["test_page"] = df["test_page"].astype('int64')
    #Loop pages
    for i in range(df["test_page"].max()):
        page_info = df[df.test_page == i+1]
        #Get records
        for x in range(len(page_info)):
            name = str(page_info['student_name'].iloc[x])
            lastname = str(page_info['student_lastname'].iloc[x])
            student_id = str(page_info['student_number'].iloc[x])
            student_class = str(page_info['student_class'].iloc[x])
            gender = str(page_info['gender'].iloc[x])
            bmonth = str(page_info['bmonth'].iloc[x])
            if len(str(page_info['bmonth'].iloc[x])) == 1:
                bmonth = "0"+str(page_info['bmonth'].iloc[x])
            bday = str(page_info['bday'].iloc[x])
            if len(str(page_info['bday'].iloc[x])) == 1:
                bday = "0"+str(page_info['bday'].iloc[x])
            byear = str(page_info['byear'].iloc[x])
            form_code = str(page_info['form_code'].iloc[x])
            country_code = str(page_info['country_code'].iloc[x])
            lang_code = str(page_info['lang_code'].iloc[x])
            test_type = int(page_info['test_type'].iloc[x])
            
            if test_type == 4:
                if printer == 'riso':
                    json_data = json_data_raw['test_4_optic']['riso']
                    x, y = json_data['riso_x'], json_data['riso_y']
                elif printer == 'xerox':
                    json_data = json_data_raw['test_4_optic']['xerox']
                    x, y = json_data['xerox_x'], json_data['xerox_y']
                elif printer == "hp":
                    json_data = json_data_raw['test_4_optic']['hp']
                    x, y = json_data['hp_x'], json_data['hp_y']
                else:
                    json_data = json_data_raw['test_4_optic']['other_printer']
                    x, y = json_data['other_printer_x'], json_data['other_printer_y']

                main_plus_string_x = json_data['main_plus_string_x']
                main_plus_string_y = json_data['main_plus_string_y']
                main_plus_circle_x = json_data['main_plus_circle_x']
                main_plus_circle_y = json_data['main_plus_circle_y']
                h_spacing = json_data['horizontal_spacing']
                v_spacing = json_data['vertical_spacing']
                main_circle_width = json_data['main_circle_width']

                #pdf.drawImage('test_4 optik form_Page_1.jpg', 0, 0, width = width, height = height, mask = None)
                pdf.setFont('VerdanaB',11)
                pdf.drawString(x+json_data['header_institution_x'],y+json_data['header_institution_y'],institution)
                pdf.drawString(x+json_data['header_form_code_x'],y+json_data['header_form_code_y'],form_code)
                pdf.drawString(x+json_data['header_test_date_x_1'],y+json_data['header_test_date_y_1'],test_date[3:5])
                pdf.drawString(x+json_data['header_test_date_x_2'],y+json_data['header_test_date_y_2'],test_date[:2])
                pdf.drawString(x+json_data['header_test_date_x_3'],y+json_data['header_test_date_y_3'],test_date[6:])
                pdf.circle(x+json_data['header_consent_circle_x'],y+json_data['header_consent_circle_y'], main_circle_width, fill=1)
                letterlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                numlist = ['0','1','2','3','4','5','6','7','8','9']
                datelist = ['01','02','03','04','05','06','07','08','09','10','11','12']
                genderlist = ['M','F']
                
                write_name(name,x,y)
                write_lastname(lastname,x,y)
                write_student_id(student_id,x,y)
                write_student_date_of_birth(bmonth,bday,byear,x,y)
                write_gender(gender,x,y)
                write_country_code(country_code,x,y)
                write_lang_code(lang_code,x,y)

                pdf.showPage()
    
    pdf.save()
    os.startfile(file_name)
    db_pd.close()
    
#You can update form_code whenever you want
def form_code_update(old_form_code,new_form_code,test_date,institution):
    db_pd = mc.engine.connect()
    sql_form_code_update_query ="UPDATE iopssablon SET form_code = %s WHERE form_code = %s AND test_date =%s AND school = %s"
    vals = (new_form_code,old_form_code,test_date,institution)
    db_pd.execute(sql_form_code_update_query,vals)
    db_pd.close()

#You can delete wrong uploads
def delete_query(test_date,institution):
    db_pd = mc.engine.connect()
    db_pd.execute("DELETE FROM iopssablon WHERE test_date = '{}' AND school = '{}'".format(test_date,institution))
    db_pd.close()

def check_form_code_ps1(new_form_code,test_date,institution):
    db_pd = mc.engine.connect()
    mycursor = db_pd.execute("SELECT student_number FROM iopssablon WHERE test_date = %s AND school = %s",(test_date,institution))
    false_list = []
    for i in mycursor.fetchall():
        student_id = i[0]
        mycursor_1 = db_pd.execute("SELECT * FROM test_1step_1 WHERE student_number = %s AND form_code = %s",(int(student_id),new_form_code))
        for i in mycursor_1.fetchall():
            false_list.append(i[3])
    db_pd.close()
    return list(set(false_list))

def check_form_code_ps2(new_form_code,test_date,institution):
    db_pd = mc.engine.connect()
    mycursor = db_pd.execute("SELECT student_number FROM iopssablon WHERE test_date = %s AND school = %s",(test_date,institution))
    false_list = []
    for i in mycursor.fetchall():
        student_id = i[0]
        mycursor_1 = db_pd.execute("SELECT * FROM test_1step_2 WHERE student_number = %s AND form_code = %s",(int(student_id),new_form_code))
        for i in mycursor_1.fetchall():
            false_list.append(i)
    db_pd.close()
    return list(set(false_list))

def check_form_code_js(new_form_code,test_date,institution):
    db_pd = mc.engine.connect()
    mycursor = db_pd.execute("SELECT student_number FROM iopssablon WHERE test_date = %s AND school = %s",(test_date,institution))
    false_list = []
    for i in mycursor.fetchall():
        student_id = i[0]
        mycursor_1 = db_pd.execute("SELECT * FROM test_3_standard WHERE student_number = %s AND form_code = %s",(int(student_id),new_form_code))
        for i in mycursor_1.fetchall():
            false_list.append(i)
    db_pd.close()
    return list(set(false_list))

def check_form_code_test_4(new_form_code,test_date,institution):
    db_pd = mc.engine.connect()
    mycursor = db_pd.execute("SELECT student_number FROM iopssablon WHERE test_date = %s AND school = %s",(test_date,institution))
    false_list = []
    for i in mycursor.fetchall():
        student_id = i[0]
        mycursor_1 = db_pd.execute("SELECT * FROM test_4 WHERE student_number = %s AND form_code = %s",(int(student_id),new_form_code))
        for i in mycursor_1.fetchall():
            false_list.append(i)
    db_pd.close()
    return list(set(false_list))
        

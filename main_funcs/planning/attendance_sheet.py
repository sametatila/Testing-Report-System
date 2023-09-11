import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import data.exam_data.checklisttext as clt
import main_funcs.mixed.mysql_connection as mc
import os
import main_funcs.mixed.file_name_checker as fnc

pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
pdfmetrics.registerFont(TTFont('VerdanaB', './data/gui_data/fonts/verdanab.ttf'))




#id_or_not takes only two args which are 0 or 1
def attendance_sheet_pdf(tr_eng,id_or_not,test_date,institution,save_directory):
    def front_header():
        logo_1 = r"./data/exam_data/ysslogo.png"
        logo_2 = r"./data/exam_data/test_4logo.png"
        #Write and draw shapes and infos
        if test_type_int != 4:
            pdf.drawImage(logo_1, int(A4[0])-160,int(A4[1])-120, width=120,height=80,mask=None)
        else:
            pdf.drawImage(logo_2, int(A4[0])-170,int(A4[1])-95, width=130,height=30,mask=None)
        pdf.rect(30, int(A4[1])-130, width = int(A4[0])-60, height = 100, stroke=1, fill=0)
        pdf.rect(28, int(A4[1])-132, width = int(A4[0])-56, height = 104, stroke=1, fill=0)
        textobjectkey = pdf.beginText(45, int(A4[1])-50)
        textobjectkey.setFont("VerdanaB", 11)
        textobjectval = pdf.beginText(125, int(A4[1])-50)
        textobjectval.setFont("VerdanaB", 11)
        headdic = {
            "Test Date": str(test_date),
            "Test Center": str(institution),
            "Test Type": str(test_type),
            "Test Room": str(test_room),
            "Test Session": str(test_session)+".Seans",
            "Test Time": str(test_time)
            }
        for key, value in headdic.items():
            textobjectkey.textLine(key)
            textobjectval.textLine(':  '+value)
        pdf.setFillColor("red")
        pdf.drawText(textobjectkey)
        pdf.setFillColor("black")
        pdf.drawText(textobjectval)

    def front_footer_tr():
        #Write pbt footer
        if test_type_int != 20 and test_type_int != 21:
            textobjectkey1 = pdf.beginText(30, 170)
            textobjectkey1.setFont("Verdana", 10)
            footdic1 = {
                "Test Form Code": "Test Form Code :",
                "Boşluk": "",
                "Test Date": "Test Date :"
                }
            for key, value in footdic1.items():
                textobjectkey1.textLine(value)
            textobjectkey2 = pdf.beginText(250, 170)
            textobjectkey2.setFont("Verdana", 10)
            footdic2 = {
                "Total Booklets": "Total Booklets :",
                "Boşluk1": "",
                "Used Booklets": "Used Booklets :",
                "Boşluk2": "",
                "Total CD Number": "Total CD Number :"
                }
            for key, value in footdic2.items():
                textobjectkey2.textLine(value)
            textobjectkey3 = pdf.beginText(400, 170)
            textobjectkey3.setFont("Verdana", 10)
            footdic3 = {
                "Total Answer Sheets": "Total Answer Sheets :",
                "Boşluk1": "",
                "Used Answer Sheets": "Used Answer Sheets :",
                "Boşluk2": "",
                "Boşluk3": "",
                "Boşluk5": "",
                "Proctor": "Proctor :",
                "Boşluk4": "",
                "Signature": "Signature :",
                }
            for key, value in footdic3.items():
                textobjectkey3.textLine(value)

            pdf.drawText(textobjectkey1)
            pdf.drawText(textobjectkey2)
            pdf.drawText(textobjectkey3)

            pdf.setFont("Verdana", 8)
            pdf.drawString(30,100, "XXX".encode("utf-8"))
            pdf.drawString(30,65, "XXX".encode("utf-8"))
        #Write speaking footer
        else:
            textobjectkey4 = pdf.beginText(400, 100)
            textobjectkey4.setFont("Verdana", 10)
            footdic4 = {
                "Proctor": "Proctor :",
                "Boşluk4": "",
                "Signature": "Signature :",
                }
            for key, value in footdic4.items():
                textobjectkey4.textLine(value)
            pdf.drawText(textobjectkey4)
    
    def front_footer_eng():
        #Write pbt footer
        if test_type_int != 20 and test_type_int != 21:
            textobjectkey1 = pdf.beginText(30, 170)
            textobjectkey1.setFont("Verdana", 10)
            footdic1 = {
                "Test Form Code": "Test Form Code :",
                "Boşluk": "",
                "Test Date": "Test Date :"
                }
            for key, value in footdic1.items():
                textobjectkey1.textLine(value)
            textobjectkey2 = pdf.beginText(250, 170)
            textobjectkey2.setFont("Verdana", 10)
            footdic2 = {
                "Total Booklets": "Total Booklets :",
                "Boşluk1": "",
                "Used Booklets": "Used Booklets :",
                "Boşluk2": "",
                "Total CD Number": "Total CD Number :"
                }
            for key, value in footdic2.items():
                textobjectkey2.textLine(value)
            textobjectkey3 = pdf.beginText(400, 170)
            textobjectkey3.setFont("Verdana", 10)
            footdic3 = {
                "Total Answer Sheets": "Total Answer Sheets :",
                "Boşluk1": "",
                "Used Answer Sheets": "Used Answer Sheets :",
                "Boşluk2": "",
                "Boşluk3": "",
                "Boşluk5": "",
                "Proctor": "Proctor :",
                "Boşluk4": "",
                "Signature": "Signature :",
                }
            for key, value in footdic3.items():
                textobjectkey3.textLine(value)

            pdf.drawText(textobjectkey1)
            pdf.drawText(textobjectkey2)
            pdf.drawText(textobjectkey3)

            pdf.setFont("Verdana", 8)
            pdf.drawString(30,100, "XXX".encode("utf-8"))
            pdf.drawString(30,65, "XXX".encode("utf-8"))
        #Write speaking footer
        else:
            textobjectkey4 = pdf.beginText(400, 100)
            textobjectkey4.setFont("Verdana", 10)
            footdic4 = {
                "Proctor": "Proctor :",
                "Boşluk4": "",
                "Signature": "Signature :",
                }
            for key, value in footdic4.items():
                textobjectkey4.textLine(value)
            pdf.drawText(textobjectkey4)

    def student_table():
        #Set student table style
        data_table=Table(rawdata)
        data_table.setStyle([
            ('FONTNAME', (0,0), (-1,0), 'VerdanaB'),
            ('FONTSIZE', (0,0), (-1,0), 9),
            ('FONTNAME', (0,1), (-1,-1), 'Verdana'),
            ('FONTSIZE', (0,1), (-1,-1), 9),
            ("VALIGN", (0,0), (-1,0), "MIDDLE"),
            ("ALIGN", (0,0), (-1,0), "CENTER"),
            ("VALIGN", (0,0), (0,-1), "MIDDLE"),
            ("ALIGN", (0,0), (0,-1), "CENTER"),
            ("VALIGN", (3,0), (4,-1), "MIDDLE"),
            ("ALIGN", (3,0), (4,-1), "CENTER"),
            ('RIGHTPADDING',(0,0),(0,0),3),
            ('LEFTPADDING',(0,0),(0,0),3),
            ('RIGHTPADDING',(1,0),(3,0),35),
            ('LEFTPADDING',(1,0),(3,0),35),
            ('RIGHTPADDING',(5,0),(5,0),20),
            ('LEFTPADDING',(5,0),(5,0),20),
            ('GRID',(0,0),(-1,-1),1,colors.black),
            ])
        #Wrap and draw specific x,y(Don't change!!!)
        data_table.wrapOn(pdf, int(A4[0]), int(A4[1]))
        data_table.drawOn(pdf, 30,int(A4[1])-210-len(page_info)*18+34)
        pdf.rect(28, int(A4[1])-210-len(page_info)*18+34-2, width = int(A4[0])-56, height = len(page_info)*18+34, stroke=1, fill=0)

    def checklist_tr(testtypetext):
        # Create textobject
        textobject = pdf.beginText()
        # Set text location (x, y)
        textobject.setTextOrigin(20, int(A4[1])-80)
        # Set font face and size
        textobject.setFont('VerdanaB', 9)
        textobject.setLeading(25)
        textobject.setCharSpace(-0.5)
        # Write lines by test type from checklisttext.py
        if testtypetext == 8 or testtypetext == 9:
            pdf.setFont('VerdanaB', 14)
            pdf.drawCentredString(int(A4[0])/2,800,"Test Type 1-2 Checklist")
            textobject.textLines(clt.checklisttest_1)
            for i in range(21):
                pdf.roundRect(int(A4[0])-60, int(A4[1])-83-25*i, width = 25, height = 15, stroke=1, fill=0, radius=3)
            pdf.drawText(textobject)
        elif testtypetext == 5:
            pdf.setFont('VerdanaB', 14)
            pdf.drawCentredString(int(A4[0])/2,800,"Test Type 3 Checklist")
            textobject.textLines(clt.checklisttest_3)
            for i in range(24):
                pdf.roundRect(int(A4[0])-60, int(A4[1])-83-25*i, width = 25, height = 15, stroke=1, fill=0, radius=3)
            pdf.drawText(textobject)
        elif testtypetext == 4:
            pdf.setFont('VerdanaB', 14)
            pdf.drawCentredString(int(A4[0])/2,800,"Test Type 4 Checklist")
            textobject.textLines(clt.checklisttest_4)
            for i in range(24):
                pdf.roundRect(int(A4[0])-60, int(A4[1])-83-25*i, width = 25, height = 15, stroke=1, fill=0, radius=3)
            pdf.drawText(textobject)
        # Write specific infos to pdf
        pdf.setFont('Verdana', 9)
        pdf.drawString(20,100,"XXX")
        pdf.drawString(20,80,"XXX")
        pdf.setFont('VerdanaB', 9)
        pdf.drawString(470,120,"XXX")
        pdf.roundRect(447,80, width = 120, height = 30, stroke=1, fill=0, radius=3)
        pdf.showPage()
    
    def checklist_eng(testtypetext):
        # Create textobject
        textobject = pdf.beginText()
        # Set text location (x, y)
        textobject.setTextOrigin(20, int(A4[1])-80)
        # Set font face and size
        textobject.setFont('VerdanaB', 9)
        textobject.setLeading(25)
        textobject.setCharSpace(-0.5)
        # Write lines by test type from checklisttext.py
        if testtypetext == 8 or testtypetext == 9:
            pdf.setFont('VerdanaB', 14)
            pdf.drawCentredString(int(A4[0])/2,800,"Test Type 1-2 Checklist")
            textobject.textLines(clt.checklisttest_1eng)
            for i in range(21):
                pdf.roundRect(int(A4[0])-60, int(A4[1])-83-25*i, width = 25, height = 15, stroke=1, fill=0, radius=3)
            pdf.drawText(textobject)
        elif testtypetext == 5:
            pdf.setFont('VerdanaB', 14)
            pdf.drawCentredString(int(A4[0])/2,800,"Test Type 3 Checklist")
            textobject.textLines(clt.checklisttest_3_eng)
            for i in range(24):
                pdf.roundRect(int(A4[0])-60, int(A4[1])-83-25*i, width = 25, height = 15, stroke=1, fill=0, radius=3)
            pdf.drawText(textobject)
        elif testtypetext == 4:
            pdf.setFont('VerdanaB', 14)
            pdf.drawCentredString(int(A4[0])/2,800,"Test Type 4 Checklist")
            textobject.textLines(clt.checklisttest_4_eng)
            for i in range(24):
                pdf.roundRect(int(A4[0])-60, int(A4[1])-83-25*i, width = 25, height = 15, stroke=1, fill=0, radius=3)
            pdf.drawText(textobject)
        # Write specific infos to pdf
        pdf.setFont('Verdana', 9)
        pdf.drawString(20,100,"XXX")
        pdf.drawString(20,80,"XXX")
        pdf.setFont('VerdanaB', 9)
        pdf.drawString(470,120,"XXX")
        pdf.roundRect(447,80, width = 120, height = 30, stroke=1, fill=0, radius=3)
        pdf.showPage()
        
    #Create pdf options
    #Attendance sheet with student id
    if id_or_not == 0:
        addfilename = "ID"
    #Attendance sheet without student id
    elif id_or_not == 1:
        addfilename = "No ID"
    #Booklet
    elif id_or_not == 2:
        addfilename = "Booklet"
    file_name =str(save_directory)+"/"+test_date[6:]+"-"+test_date[3:5]+"-"+test_date[:2]+"_"+str(institution)+"_Yoklama Listesi "+addfilename+".pdf"
    file_name = fnc.check_file_name(file_name)
    pdf = canvas.Canvas(file_name, pagesize=A4)
    #Select iopssablon table and turn into dataframe
    db_pd = mc.engine.connect()
    sql_select_by_date_and_school = "SELECT * FROM iopssablon WHERE test_date = "+"'"+test_date+"'"+" AND school = "+"'"+institution+"'"
    df = pd.read_sql(sql_select_by_date_and_school, con=db_pd)
    #Get records according to date and school
    institution = df.iloc[0][1]
    #Format page col into int
    df["test_page"] = df["test_page"].astype('int64')
    #Loop pages
    for i in range(df["test_page"].max()):
        page_info = df[df.test_page == i+1]
        #Create data table list for pdf tables
        rawdata = [["Order\nNo","First Name","Last Name","ID\nNumber","Student\nClass","Student\nSignature"]]
        #Get records
        for x in range(len(page_info)):
            name = page_info['student_name'].iloc[x]
            lastname = page_info['student_lastname'].iloc[x]
            student_id = page_info['student_number'].iloc[x]
            student_class = page_info['student_class'].iloc[x]
            test_room = page_info['room'].iloc[x]
            test_time = page_info['test_time'].iloc[x]
            test_session = page_info['test_session'].iloc[x]
            if int(page_info['test_type'].iloc[x]) == 4:
                test_type = "Test Type 4"
                test_type_int = 4
            elif int(page_info['test_type'].iloc[x]) == 8:
                test_type = "Test Type 1"
                test_type_int = 8
            elif int(page_info['test_type'].iloc[x]) == 9:
                test_type = "Test Type 2"
                test_type_int = 9
            elif int(page_info['test_type'].iloc[x]) == 5:
                test_type = "Test Type 3"
                test_type_int = 5
            elif int(page_info['test_type'].iloc[x]) == 20:
                test_type = "Test Type 5"
                test_type_int = 20
            elif int(page_info['test_type'].iloc[x]) == 21:
                test_type = "Test Type 6"
                test_type_int = 21
            #Attendance sheet with student id
            if id_or_not == 0:
                data = [str(x+1),str(name),str(lastname),str(student_id),str(student_class),""]
            #Attendance sheet without student id
            elif id_or_not == 1:
                data = [str(x+1),str(name),str(lastname),"",str(student_class),""]
            #Booklet
            elif id_or_not == 2:
                data = [str(x+1),str(name),str(lastname),str(student_id),str(student_class),""]
            #Append  all page to rawdata list
            rawdata.append(data)
        #Create layouts
        if tr_eng == "tr":
            front_header()
            if id_or_not != 1 and id_or_not != 2: 
                front_footer_tr()
            student_table()
            #Finish and create pages
            pdf.showPage()
            #If not booklet
            if id_or_not == 0:
                #If tests are speaking, there will be no checklist
                if test_type_int != 20 and test_type_int != 21:
                    checklist_tr(test_type_int)
                else:
                    pdf.showPage()

        elif tr_eng =="eng":
            front_header()
            if id_or_not != 1 and id_or_not != 2:
                front_footer_eng()
            student_table()
            #Finish and create pages
            pdf.showPage()
            #If not booklet
            if id_or_not == 0:
                #If tests are speaking, there will be no checklist
                if test_type_int != 20 and test_type_int != 21:
                    checklist_eng(test_type_int)
                else:
                    pdf.showPage()
    pdf.save()
    os.startfile(file_name)
    db_pd.close()
    

def get_form_codes(test_date,institution):
    db_pd = mc.engine.connect()
    sql_get_form_code_query ="SELECT * FROM iopssablon WHERE test_date = %s AND school = %s"
    vals = (test_date,institution)
    ps1_list, ps2_list, js_list, test_4_list = [], [], [], []
    for i in db_pd.execute(sql_get_form_code_query,vals).fetchall():
        if i[7] == "4":
            test_type_test_4 = i[5]
            test_4_list.append(test_type_test_4)
        if i[7] == "5":
            test_type_js = i[5]
            js_list.append(test_type_js)
        if i[7] == "8":
            test_type_ps1 = i[5]
            ps1_list.append(test_type_ps1)
        if i[7] == "9":
            test_type_ps2 = i[5]
            ps2_list.append(test_type_ps2)
    db_pd.close()
    return [list(set(ps1_list)),list(set(ps2_list)),list(set(js_list)),list(set(test_4_list))]
            

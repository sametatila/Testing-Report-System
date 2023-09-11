from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import main_funcs.mixed.mysql_connection as mc
import main_funcs.mixed.file_name_checker as fnc
import os
 
#A4 size
width, height = A4
#Import Fonts
pdfmetrics.registerFont(TTFont('Calibri', './data/gui_data/fonts/CalibriRegular.ttf'))
pdfmetrics.registerFont(TTFont('CalibriB', './data/gui_data/fonts/CalibriBold.ttf'))
pdfmetrics.registerFont(TTFont('CalibriI', './data/gui_data/fonts/CalibriItalic.ttf'))
pdfmetrics.registerFont(TTFont('CalibriBI', './data/gui_data/fonts/CalibriBoldItalic.ttf'))
save_directory = "./"
def create_delivery_note(save_directory,form_code,test_type,institution,test_date):
    db_pd = mc.engine.connect()
    mycursor = db_pd.execute("SELECT * FROM iopssablon WHERE school = %s AND test_date = %s AND test_type = %s",(institution,test_date,test_type))
    page_list = []
    for i in mycursor.fetchall():
        page_list.append(i[9])
    total_cd = str(len(list(set(page_list))))
    total_student = str(len(page_list))
    if test_type == 8:
        test_type_str = "Test Type 1"
    elif test_type == 9:
        test_type_str = "Test Type 2"
    elif test_type == 20:
        test_type_str = "Test Type 5"
    elif test_type == 5:
        test_type_str = "Test Type 3"
    elif test_type == 21:
        test_type_str = "Test Type 6"
    elif test_type == 4:
        test_type_str = "Test Type 4"
    file_name = str(save_directory)+"/"+test_date[6:]+"-"+test_date[3:5]+"-"+test_date[:2]+"_"+str(institution)+"Sınav Hazırlama Formu_"+test_type_str+".pdf"
    file_name = fnc.check_file_name(file_name)
    pdf = canvas.Canvas(file_name, pagesize=A4)
    pdf.drawImage("./data/docs/XXX.jpg", 0,0, width= width,height=height,mask=None)

    pdf.setFont('CalibriB',14)
    pdf.drawString(112,715.5,"XXX")
    if len(institution) < 18:
        pdf.drawString(125,680,institution)
    else:
        pdf.drawString(35,655,institution)
    pdf.setFont('CalibriB',14)
    pdf.drawString(390,722,test_date)
    pdf.drawString(390,695,"________")
    pdf.drawString(390,659,form_code)
    pdf.drawString(390,627,test_type_str)

    pdf.drawCentredString(58,548.5,str(int(total_cd)+1))
    pdf.drawCentredString(58,529,str(int(total_student)+10))
    pdf.drawCentredString(58,510,str(int(total_student)+10))
    pdf.showPage()
    pdf.save()
    os.startfile(file_name)
    db_pd.close()


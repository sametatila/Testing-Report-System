from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table
import math
import main_funcs.mixed.student_class_function as scf
import data.exam_data.turkish_report_text as trt
import main_funcs.mixed.file_name_checker as fnc
import main_funcs.mixed.db_tables as dbt
import os
import pandas as pd
from datetime import datetime



# A4 size
width, height = A4
# Import Fonts
pdfmetrics.registerFont(TTFont('Calibri', './data/gui_data/fonts/CalibriRegular.ttf'))
pdfmetrics.registerFont(TTFont('CalibriB', './data/gui_data/fonts/CalibriBold.ttf'))
pdfmetrics.registerFont(TTFont('CalibriI', './data/gui_data/fonts/CalibriItalic.ttf'))
pdfmetrics.registerFont(TTFont('CalibriBI', './data/gui_data/fonts/CalibriBoldItalic.ttf'))

# Image Data
gt_logo = "./data/gui_data/logos/gt.jpg"
pri_logo = "./data/gui_data/logos/ps1.png"
jun_logo = "./data/gui_data/logos/js.png"
ps1_ns_star = "./data/exam_data/step1_ns.jpg"
ps1_1star = "./data/exam_data/step1_1star.jpg"
ps1_2star = "./data/exam_data/step1_2star.jpg"
ps1_3star = "./data/exam_data/step1_3star.jpg"
ps1_4star = "./data/exam_data/step1_4star.jpg"
ps2_ns_badge = "./data/exam_data/step2_ns.jpg"
ps2_1badge = "./data/exam_data/step2_1badge.jpg"
ps2_2badge = "./data/exam_data/step2_2badge.jpg"
ps2_3badge = "./data/exam_data/step2_3badge.jpg"
ps2_4badge = "./data/exam_data/step2_4badge.jpg"
ps2_5badge = "./data/exam_data/step2_5badge.jpg"
pspk_ns_ribbon = "./data/exam_data/pspk_ns.jpg"
pspk_1_ribbon = "./data/exam_data/pspk_1ribbons.jpg"
pspk_2_ribbon = "./data/exam_data/pspk_2ribbons.jpg"
pspk_3_ribbon = "./data/exam_data/pspk_3ribbons.jpg"
pspk_4_ribbon = "./data/exam_data/pspk_4ribbons.jpg"
pspk_5_ribbon = "./data/exam_data/pspk_5ribbons.jpg"
js_fix = "./data/exam_data/js_fix.jpg"
jspk_fix = "./data/exam_data/jspk_fix.jpg"

ps1_df = dbt.ps1_df()
ps2_df = dbt.ps2_df()
pspk_df = dbt.pspk_df()
js_df = dbt.js_df()
jspk_df = dbt.jspk_df()

# Sub Functions
def header_pri(pdf, test_type, student_name, student_number, student_class, school_name, test_date):
    if test_type == 8:
        test_type_str = "Test Type 1"
    elif test_type == 9:
        test_type_str = "Test Type 2"
    elif test_type == 20:
        test_type_str = "Test Type 5"
    pdf.setFillColor(colors.navy)
    pdf.setStrokeColor(colors.navy)
    pdf.rect(20, 725, width = width-40, height = 55)
    pdf.rect(20, 775, width = width-40, height = 5, fill = 1)
    pdf.setFillColor(colors.black)
    pdf.setStrokeColor(colors.black)
    pdf.drawImage(gt_logo, 20, 790, width = 100, height = 44, mask = None)
    pdf.drawImage(pri_logo, 385, 795, width = 187, height = 30, mask = None)
    student_info_1 = [str(student_name), str(test_date), str(student_class)]
    student_info_2 = [str(student_number), str(school_name), str(test_type_str)]
    textobject1 = pdf.beginText()
    textobject1.setTextOrigin(35, 760)
    textobject1.setFont('CalibriB', 10)
    textobject1.setLeading(13)
    for key, value in trt.header_1.items():
        textobject1.textLine(key)
    pdf.drawText(textobject1)
    textobject2 = pdf.beginText()
    textobject2.setTextOrigin(310, 760)
    textobject2.setFont('CalibriB', 10)
    textobject2.setLeading(13)
    for key, value in trt.header_2.items():
        textobject2.textLine(key)
    pdf.drawText(textobject2)
    textobject3 = pdf.beginText()
    textobject3.setTextOrigin(125, 760)
    textobject3.setFont('Calibri', 10)
    textobject3.setLeading(13)
    for item in student_info_1:
        textobject3.textLine(item)
    pdf.drawText(textobject3)
    textobject4 = pdf.beginText()
    textobject4.setTextOrigin(410, 760)
    textobject4.setFont('Calibri', 10)
    textobject4.setLeading(13)
    for item in student_info_2:
        textobject4.textLine(item)
    pdf.drawText(textobject4)
    
def reading_pri(pdf, test_type, reading_score, reading_cefr, lexile, total_score, star_logo_reading, test_type_text_reading):
    if test_type == 8:
        range_eng = "100 to 109"
        range_tr = "100 ile 109"
    elif test_type == 9:
        range_eng = "104 to 115"
        range_tr = "104 ile 115"
    pdf.setFillColor(colors.navy)
    pdf.setStrokeColor(colors.navy)
    pdf.rect(20, 20, width = (width-40)/2-5, height = 680)
    pdf.rect(20+(width-40)/2+5, 20, width = (width-40)/2-5, height = 680)
    pdf.rect(20, 30+640, width = (width-40)/2-5, height = 30, fill = 1)
    pdf.rect(20+(width-40)/2+5, 30+640, width = (width-40)/2-5, height = 30, fill = 1)
    pdf.setFillColor(colors.black)
    pdf.setStrokeColor(colors.black)
    pdf.drawImage(star_logo_reading, 70, 595, width = 180, height = 70, mask = None)
    pdf.setFillColor(colors.white)
    pdf.setFont('CalibriB', 15)
    pdf.drawCentredString(160, 680, "READING - OKUMA")
    pdf.setFillColor(colors.black)
    pdf.setFont('CalibriB', 11)
    pdf.drawCentredString(160, 577, "Score : "+str(reading_score)+"     CEFR : "+str(reading_cefr)+"     Lexile : "+str(lexile))
    if reading_score != "NS":
        pdf.setFont('Calibri', 9)
        pdf.drawString(30, 560, "The Student received "+str(reading_score)+" on a scale of "+str(range_eng)+".")
        pdf.drawString(30, 545, "Öğrenci "+str(range_tr)+" arasındaki ölçekte "+str(reading_score)+" puan almıştır.")
    textStyle = ParagraphStyle(name = 'Normal', 
                                fontSize = 9, 
                                leading = 11)
    message = test_type_text_reading.replace('\n', '<br/>')
    message = Paragraph(message, style = textStyle)
    w, h = message.wrap(width/2-40, height+100)
    message.drawOn(pdf, 30, 550-h)
    pdf.setFont('CalibriB', 12)
    pdf.drawCentredString(width/2, 710, "Total Score : "+str(total_score))
    
def listening_pri(pdf, test_type, listening_score, listening_cefr, star_logo_listening, test_type_text_listening):
    if test_type == 8:
        range_eng = "100 to 109"
        range_tr = "100 ile 109"
    elif test_type == 9:
        range_eng = "104 to 115"
        range_tr = "104 ile 115"
    pdf.drawImage(star_logo_listening, 350, 595, width = 180, height = 70, mask = None)
    pdf.setFillColor(colors.white)
    pdf.setFont('CalibriB', 15)
    pdf.drawCentredString(445, 680, "LISTENING - DİNLEME")
    pdf.setFillColor(colors.black)
    pdf.setFont('CalibriB', 11)
    pdf.drawCentredString(445, 577, "Score : "+str(listening_score)+"     CEFR : "+str(listening_cefr))
    if listening_score != "NS":
        pdf.setFont('Calibri', 9)
        pdf.drawString(312, 560, "The Student received "+str(listening_score)+" on a scale of "+str(range_eng)+".")
        pdf.drawString(312, 545, "Öğrenci "+str(range_tr)+" arasındaki ölçekte "+str(listening_score)+" puan almıştır.")
    textStyle = ParagraphStyle(name = 'Normal', 
                               leading = 11, 
                               fontSize = 9)
    message = test_type_text_listening.replace('\n', '<br/>')
    message = Paragraph(message, style = textStyle)
    w, h = message.wrap(width/2-40, height+100)
    message.drawOn(pdf, 312, 550-h)
    
def speaking_pri(pdf, speaking_score, speaking_cefr, speaking_level, star_logo_speaking, test_type_text_speaking):
    range_eng = "1 to 27"
    range_tr = "1 ile 27"
    pdf.setFillColor(colors.navy)
    pdf.setStrokeColor(colors.navy)
    pdf.rect(width/2-190, 20, width = (width-40)/2+100, height = 680)
    pdf.rect(width/2-190, 30+640, width = (width-40)/2+100, height = 30, fill = 1)
    pdf.setFillColor(colors.black)
    pdf.setStrokeColor(colors.black)
    pdf.setFillColor(colors.white)
    pdf.setFont('CalibriB', 15)
    pdf.drawCentredString(width/2, 680, "SPEAKING - KONUŞMA")
    pdf.setFillColor(colors.black)
    pdf.setFont('CalibriB', 11)
    pdf.drawCentredString(width/2, 577, "Score : "+str(speaking_score)+"     CEFR : "+str(speaking_cefr)+"     Ribbons : "+str(speaking_level))
    if speaking_score != "NS" and speaking_score != "0":
        pdf.setFont('CalibriB', 13)
        pdf.drawCentredString(width/2, 654, "The Student' Level is:")
        pdf.drawCentredString(width/2, 595, str(speaking_level)+" Out of 5 Ribbons")
        pdf.drawImage(star_logo_speaking, width/2-90, 610, width = 180, height = 38, mask = None)
        pdf.setFont('Calibri', 11)
        pdf.drawString(120, 560, "The Student received "+str(speaking_score)+" on a scale of "+str(range_eng)+".")
        pdf.drawString(120, 545, "Öğrenci "+str(range_tr)+" arasındaki ölçekte "+str(speaking_score)+" puan almıştır.")
    else:
        pdf.drawImage(star_logo_speaking, width/2-90, 610, width = 180, height = 38, mask = None)
    textStyle = ParagraphStyle(name = 'Normal', 
                                fontSize = 10, 
                                leading = 13)
    message = test_type_text_speaking.replace('\n', '<br/>')
    message = Paragraph(message, style = textStyle)
    w, h = message.wrap(width/2+60, height+100)
    message.drawOn(pdf, 120, 540-h)

def header_jun(pdf, test_type, student_name, student_number, student_class, school_name, test_date):
    if test_type == 5:
        test_type_str = "Test Type 3"
    elif test_type == 21:
        test_type_str = "Test Type 6"
    pdf.setFillColorRGB(0.2, 0.7, 0.76)
    pdf.setStrokeColorRGB(0.2, 0.7, 0.76)
    pdf.roundRect(20, 725, width = width-40, height = 55, radius = 5)
    pdf.setFillColor(colors.white)
    pdf.setStrokeColor(colors.white)
    pdf.rect(20, 776, width = width-40, height = 5, fill = 1)
    pdf.setFillColorRGB(0.2, 0.7, 0.76)
    pdf.setStrokeColorRGB(0.2, 0.7, 0.76)
    pdf.roundRect(20, 771, width = width-40, height = 10, fill = 1, radius = 5)
    pdf.setFillColor(colors.white)
    pdf.setStrokeColor(colors.white)
    pdf.rect(21, 770, width = width-42, height = 5, fill = 1)
    pdf.setFillColor(colors.black)
    pdf.setStrokeColor(colors.black)
    pdf.drawImage(gt_logo, 20, 790, width = 100, height = 44, mask = None)
    pdf.drawImage(jun_logo, 400, 795, width = 175, height = 29, mask = None)
    student_info_1 = [str(student_name), str(test_date), str(student_class)]
    student_info_2 = [str(student_number), str(school_name), str(test_type_str)]
    textobject1 = pdf.beginText()
    textobject1.setTextOrigin(35, 760)
    textobject1.setFont('CalibriB', 10)
    textobject1.setLeading(13)
    for key, value in trt.header_1.items():
        textobject1.textLine(key)
    pdf.drawText(textobject1)
    textobject2 = pdf.beginText()
    textobject2.setTextOrigin(310, 760)
    textobject2.setFont('CalibriB', 10)
    textobject2.setLeading(13)
    for key, value in trt.header_2.items():
        textobject2.textLine(key)
    pdf.drawText(textobject2)
    textobject3 = pdf.beginText()
    textobject3.setTextOrigin(125, 760)
    textobject3.setFont('Calibri', 10)
    textobject3.setLeading(13)
    for item in student_info_1:
        textobject3.textLine(item)
    pdf.drawText(textobject3)
    textobject4 = pdf.beginText()
    textobject4.setTextOrigin(410, 760)
    textobject4.setFont('Calibri', 10)
    textobject4.setLeading(13)
    for item in student_info_2:
        textobject4.textLine(item)
    pdf.drawText(textobject4)

def listening_jun(pdf, listening_score, listening_cefr, total_score, osl, test_type_text_listening):
    pdf.setFillColorRGB(0.2, 0.7, 0.76)
    pdf.setStrokeColorRGB(0.2, 0.7, 0.76)
    pdf.roundRect(20, 480, width = width-40, height = 220, radius = 10)
    pdf.setFillColor(colors.white)
    pdf.setStrokeColor(colors.white)
    pdf.rect(20, 671, width = width-39, height = 30, fill = 1)
    pdf.setFillColorRGB(0.2, 0.7, 0.76)
    pdf.setStrokeColorRGB(0.2, 0.7, 0.76)
    pdf.roundRect(20, 640, width = width/2-40, height = 60, fill = 1, radius = 10)
    pdf.setFillColor(colors.white)
    pdf.setStrokeColor(colors.white)
    pdf.rect(21, 639, width = width/2-40, height = 30, fill = 1)
    pdf.setFillColor(colors.black)
    pdf.setStrokeColor(colors.black)
    range_eng = "200 to 300"
    range_tr = "200 ile 300"
    pdf.setFillColor(colors.white)
    pdf.setFont('CalibriB', 15)
    pdf.drawCentredString(width/4, 680, "LISTENING - DİNLEME")
    pdf.setFillColor(colors.black)
    pdf.setFont('CalibriB', 11)
    pdf.drawCentredString(width/4, 655, "Score : "+str(listening_score)+"     CEFR : "+str(listening_cefr))
    pdf.drawImage(js_fix, width/2+40, 645, width = 160, height = 40, mask = None)
    if listening_score != "NS":
        pdf.setFont('Calibri', 9)
        pdf.drawCentredString(width/2+54+(int(listening_score)-200)*1.33, 687, str(listening_score))
        pdf.line(width/2+54+(int(listening_score)-200)*1.33, 674, width/2+54+(int(listening_score)-200)*1.33, 684)
        pdf.roundRect(width/2+40+(int(listening_score)-200)*1.33, 684, width = 28, height = 13, radius = 5)
        pdf.setFont('Calibri', 9)
        pdf.drawString(30, 640, "The Student received "+str(listening_score)+" on a scale of "+str(range_eng)+". (Öğrenci "+str(range_tr)+" arasındaki ölçekte "+str(listening_score)+" puan almıştır.)")
    textStyle = ParagraphStyle(name = 'Normal', 
                                fontSize = 9, 
                                leading = 10.3)
    message = test_type_text_listening.replace('\n', '<br/>')
    message = Paragraph(message, style = textStyle)
    w, h = message.wrap(width-55, height+100)
    message.drawOn(pdf, 30, 645-h)
    if str(osl) == "nan":
        pdf.setFont('CalibriB', 12)
        pdf.drawCentredString(width/2, 710, "Overall Score Level : NA               Total Score : "+str(total_score))
    else:
        try:
            pdf.setFont('CalibriB', 12)
            pdf.drawCentredString(width/2, 710, "Overall Score Level : "+str(int(float(osl)))+"               Total Score : "+str(total_score))
        except:
            pdf.setFont('CalibriB', 12)
            pdf.drawCentredString(width/2, 710, "Overall Score Level : "+str(osl)+"               Total Score : "+str(total_score))

def lfm_jun(pdf, lfm_score, lfm_cefr, test_type_text_lfm):
    pdf.setFillColorRGB(0.2, 0.7, 0.76)
    pdf.setStrokeColorRGB(0.2, 0.7, 0.76)
    pdf.roundRect(20, 250, width = width-40, height = 220, radius = 10)
    pdf.setFillColor(colors.white)
    pdf.setStrokeColor(colors.white)
    pdf.rect(20, 441, width = width-39, height = 30, fill = 1)
    pdf.setFillColorRGB(0.2, 0.7, 0.76)
    pdf.setStrokeColorRGB(0.2, 0.7, 0.76)
    pdf.roundRect(20, 410, width = width/2-40, height = 60, fill = 1, radius = 10)
    pdf.setFillColor(colors.white)
    pdf.setStrokeColor(colors.white)
    pdf.rect(21, 409, width = width/2-40, height = 30, fill = 1)
    pdf.setFillColor(colors.black)
    pdf.setStrokeColor(colors.black)
    range_eng = "200 to 300"
    range_tr = "200 ile 300"
    pdf.setFillColor(colors.white)
    pdf.setFont('CalibriB', 15)
    pdf.drawCentredString(width/4, 450, "LFM - DİL YAPISI VE ANLAM")
    pdf.setFillColor(colors.black)
    pdf.setFont('CalibriB', 11)
    pdf.drawCentredString(width/4, 425, "Score : "+str(lfm_score)+"     CEFR : "+str(lfm_cefr))
    pdf.drawImage(js_fix, width/2+40, 415, width = 160, height = 40, mask = None)
    if lfm_score != "NS":
        pdf.setFont('Calibri', 9)
        pdf.drawCentredString(width/2+54+(int(lfm_score)-200)*1.33, 457, str(lfm_score))
        pdf.line(width/2+54+(int(lfm_score)-200)*1.33, 444, width/2+54+(int(lfm_score)-200)*1.33, 454)
        pdf.roundRect(width/2+40+(int(lfm_score)-200)*1.33, 454, width = 28, height = 13, radius = 5)
        pdf.setFont('Calibri', 9)
        pdf.drawString(30, 410, "The Student received "+str(lfm_score)+" on a scale of "+str(range_eng)+". (Öğrenci "+str(range_tr)+" arasındaki ölçekte "+str(lfm_score)+" puan almıştır.)")
    textStyle = ParagraphStyle(name = 'Normal', 
                                fontSize = 9, 
                                leading = 10.3)
    message = test_type_text_lfm.replace('\n', '<br/>')
    message = Paragraph(message, style = textStyle)
    w, h = message.wrap(width-55, height+100)
    message.drawOn(pdf, 30, 415-h)

def reading_jun(pdf, reading_score, reading_cefr, lexile, test_type_text_reading):
    pdf.setFillColorRGB(0.2, 0.7, 0.76)
    pdf.setStrokeColorRGB(0.2, 0.7, 0.76)
    pdf.roundRect(20, 20, width = width-40, height = 220, radius = 10)
    pdf.setFillColor(colors.white)
    pdf.setStrokeColor(colors.white)
    pdf.rect(20, 211, width = width-39, height = 30, fill = 1)
    pdf.setFillColorRGB(0.2, 0.7, 0.76)
    pdf.setStrokeColorRGB(0.2, 0.7, 0.76)
    pdf.roundRect(20, 180, width = width/2-40, height = 60, fill = 1, radius = 10)
    pdf.setFillColor(colors.white)
    pdf.setStrokeColor(colors.white)
    pdf.rect(21, 179, width = width/2-40, height = 30, fill = 1)
    pdf.setFillColor(colors.black)
    pdf.setStrokeColor(colors.black)
    range_eng = "200 to 300"
    range_tr = "200 ile 300"
    pdf.setFillColor(colors.white)
    pdf.setFont('CalibriB', 15)
    pdf.drawCentredString(width/4, 220, "READING - OKUMA")
    pdf.setFillColor(colors.black)
    pdf.setFont('CalibriB', 11)
    pdf.drawCentredString(width/4, 195, "Score : "+str(reading_score)+"     CEFR : "+str(reading_cefr)+"     Lexile : "+str(lexile))
    pdf.drawImage(js_fix, width/2+40, 185, width = 160, height = 40, mask = None)
    if reading_score != "NS":
        pdf.setFont('Calibri', 9)
        pdf.drawCentredString(width/2+54+(int(reading_score)-200)*1.33, 227, str(reading_score))
        pdf.line(width/2+54+(int(reading_score)-200)*1.33, 214, width/2+54+(int(reading_score)-200)*1.33, 224)
        pdf.roundRect(width/2+40+(int(reading_score)-200)*1.33, 224, width = 28, height = 13, radius = 5)
        pdf.setFont('Calibri', 9)
        pdf.drawString(30, 180, "The Student received "+str(reading_score)+" on a scale of "+str(range_eng)+". (Öğrenci "+str(range_tr)+" arasındaki ölçekte "+str(reading_score)+" puan almıştır.)")
    textStyle = ParagraphStyle(name = 'Normal', 
                                fontSize = 9, 
                                leading = 10.3)
    message = test_type_text_reading.replace('\n', '<br/>')
    message = Paragraph(message, style = textStyle)
    w, h = message.wrap(width-55, height+100)
    message.drawOn(pdf, 30, 185-h)

def speaking_jun(pdf, speaking_score, speaking_cefr, speaking_level, test_type_text_speaking):
    pdf.setFillColorRGB(0.2, 0.7, 0.76)
    pdf.setStrokeColorRGB(0.2, 0.7, 0.76)
    pdf.roundRect(20, 320, width = width-40, height = 380, radius = 10)
    pdf.setFillColor(colors.white)
    pdf.setStrokeColor(colors.white)
    pdf.rect(20, 671, width = width-39, height = 30, fill = 1)
    pdf.setFillColorRGB(0.2, 0.7, 0.76)
    pdf.setStrokeColorRGB(0.2, 0.7, 0.76)
    pdf.roundRect(20, 640, width = width-40, height = 60, fill = 1, radius = 10)
    pdf.setFillColor(colors.white)
    pdf.setStrokeColor(colors.white)
    pdf.rect(21, 639, width = width-42, height = 30, fill = 1)
    pdf.setFillColor(colors.black)
    pdf.setStrokeColor(colors.black)
    range_eng = "1 to 16"
    range_tr = "1 ile 16"
    pdf.drawImage(jspk_fix, width/2-90-0.4, 600, width = 180.2, height = 25, mask = None)
    pdf.setFillColor(colors.white)
    pdf.setFont('CalibriB', 15)
    pdf.drawCentredString(width/2, 680, "SPEAKING - KONUŞMA")
    pdf.setFillColor(colors.black)
    pdf.setFont('CalibriB', 11)
    pdf.drawCentredString(width/2, 577, "Score : "+str(speaking_score)+"     CEFR : "+str(speaking_cefr)+"     Level : "+str(speaking_level))
    if speaking_score != "NS":
        pdf.setFont('Calibri', 10)
        pdf.drawCentredString(210.3+int(speaking_score)*10.687, 638, str(speaking_score))
        pdf.line(211+int(speaking_score)*10.687, 625, 211+int(speaking_score)*10.687, 635)
        pdf.rect(203+int(speaking_score)*10.687, 635, width = 15, height = 13)
        if speaking_score != "0":
            pdf.setFont('Calibri', 10)
            pdf.drawString(30, 560, "The Student received "+str(speaking_score)+" on a scale of "+str(range_eng)+". (Öğrenci "+str(range_tr)+" arasındaki ölçekte "+str(speaking_score)+" puan almıştır.)")
    textStyle = ParagraphStyle(name = 'Normal', 
                                fontSize = 10, 
                                leading = 12)
    message = test_type_text_speaking.replace('\n', '<br/>')
    message = Paragraph(message, style = textStyle)
    w, h = message.wrap(width-55, height+100)
    message.drawOn(pdf, 30, 560-h)

def test_history(pdf,last_test_date,id_n,color_1):
    color_1 = colors.gray
    color_2 = colors.white
    color_3 = colors.white
    pri_header_list = [["Date", "School", "Test Type", "Class", "Reading Section", "", "", "", "Listening Section", "", ""],
                ["", "", "", "", "Stars/\nBadges", "Score", "CEFR", "LXL", "Stars/\nBadges", "Score", "CEFR"]]
    pri_table_style = [('FONTNAME', (0, 0), (-1, 1), 'CalibriB'),
                    ('FONTNAME', (0, 2), (-1, -1), 'Calibri'),
                    ('FONTSIZE', (0, 0), (-1, -1), 8),
                    ('BACKGROUND', (0, 0), (-1, 1), color_1),
                    ('TEXTCOLOR', (0, 0), (-1, 1), color_2),
                    ('GRID', (0, 0), (-1, 1), 0.5, color_3),
                    ('GRID', (0, 2), (-1, -1), 0.5, color_1),
                    ('BOX', (0, 0), (-1, -1), 0.5, color_1),
                    ('BOTTOMPADDING', (0, 0), (-1, 1), 3),
                    ('TOPPADDING', (0, 0), (-1, 1), 4),
                    ('BOTTOMPADDING', (0, 2), (-1, -1), 1),
                    ('TOPPADDING', (0, 2), (-1, -1), 0),
                    ('RIGHTPADDING', (0, 0), (0, 1), 16),
                    ('LEFTPADDING', (0, 0), (0, 1), 16),
                    ('RIGHTPADDING', (1, 0), (1, 1), 45),
                    ('LEFTPADDING', (1, 0), (1, 1), 45),
                    ('RIGHTPADDING', (2, 0), (2, 1), 20),
                    ('LEFTPADDING', (2, 0), (2, 1), 20),
                    ('RIGHTPADDING', (3, 0), (3, 0), 6),
                    ('LEFTPADDING', (3, 0), (3, 0), 6),
                    ('RIGHTPADDING', (4, 1), (4, 1), 5),
                    ('LEFTPADDING', (4, 1), (4, 1), 5),
                    ('RIGHTPADDING', (5, 1), (5, 1), 9),
                    ('LEFTPADDING', (5, 1), (5, 1), 9),
                    ('RIGHTPADDING', (6, 1), (7, 1), 15),
                    ('LEFTPADDING', (6, 1), (7, 1), 15),
                    ('RIGHTPADDING', (8, 1), (8, 1), 5),
                    ('LEFTPADDING', (8, 1), (8, 1), 5),
                    ('RIGHTPADDING', (9, 1), (9, 1), 9),
                    ('LEFTPADDING', (9, 1), (9, 1), 9),
                    ('RIGHTPADDING', (10, 1), (10, 1), 15),
                    ('LEFTPADDING', (10, 1), (10, 1), 15),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ('SPAN', (0, 0), (0, 1)),
                    ('SPAN', (1, 0), (1, 1)),
                    ('SPAN', (2, 0), (2, 1)),
                    ('SPAN', (3, 0), (3, 1)),
                    ('SPAN', (4, 0), (7, 0)),
                    ('SPAN', (8, 0), (10, 0)),
                    ]

    spk_header_list = [["Date", "School", "Test Type", "Class", "Level", "CEFR", "Total"]]

    spk_table_style = [('FONTNAME', (0, 0), (-1, 0), 'Calibri'),
                    ('FONTNAME', (0, 1), (-1, -1), 'Calibri'),
                    ('FONTSIZE', (0, 0), (-1, -1), 8),
                    ('BACKGROUND', (0, 0), (-1, 0), color_1),
                    ('TEXTCOLOR', (0, 0), (-1, 0), color_2),
                    ('GRID', (0, 0), (-1, 0), 0.5, color_3),
                    ('GRID', (0, 1), (-1, -1), 0.5, color_1),
                    ('BOX', (0, 0), (-1, -1), 0.5, color_1),
                    ('BOTTOMPADDING', (0, 0), (-1, 1), 3),
                    ('TOPPADDING', (0, 0), (-1, 1), 4),
                    ('BOTTOMPADDING', (0, 1), (-1, -1), 1),
                    ('TOPPADDING', (0, 1), (-1, -1), 0),
                    ('RIGHTPADDING', (0, 0), (0, 0), 16),
                    ('LEFTPADDING', (0, 0), (0, 0), 16),
                    ('RIGHTPADDING', (1, 0), (1, 0), 45),
                    ('LEFTPADDING', (1, 0), (1, 0), 45),
                    ('RIGHTPADDING', (2, 0), (2, 0), 20),
                    ('LEFTPADDING', (2, 0), (2, 0), 20),
                    ('RIGHTPADDING', (3, 0), (3, 0), 6),
                    ('LEFTPADDING', (3, 0), (3, 0), 6),
                    ('RIGHTPADDING', (4, 0), (6, 0), 37.6),
                    ('LEFTPADDING', (4, 0), (6, 0), 37.6),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ]

    js_header_list = [["Date", "School", "Test Type", "Class", "Listening Section", "", "LFM Section", "", "Reading Section", "", "", "Total"],
                ["", "", "", "", "Score", "CEFR", "Score", "CEFR", "Score", "CEFR", "LXL", ""]]

    js_table_style = [('FONTNAME', (0, 0), (-1, 1), 'Calibri'),
                    ('FONTNAME', (0, 2), (-1, -1), 'Calibri'),
                    ('FONTSIZE', (0, 0), (-1, -1), 8),
                    ('BACKGROUND', (0, 0), (-1, 1), color_1),
                    ('TEXTCOLOR', (0, 0), (-1, 1), color_2),
                    ('GRID', (0, 0), (-1, 1), 0.5, color_3),
                    ('GRID', (0, 2), (-1, -1), 0.5, color_1),
                    ('BOX', (0, 0), (-1, -1), 0.5, color_1),
                    ('BOTTOMPADDING', (0, 0), (-1, 1), 3),
                    ('BOTTOMPADDING', (0, 2), (-1, -1), 2),
                    ('TOPPADDING', (0, 2), (-1, -1), 0),
                    ('RIGHTPADDING', (0, 0), (0, 1), 16),
                    ('LEFTPADDING', (0, 0), (0, 1), 16),
                    ('RIGHTPADDING', (1, 0), (1, 1), 45),
                    ('LEFTPADDING', (1, 0), (1, 1), 45),
                    ('RIGHTPADDING', (2, 0), (2, 1), 20),
                    ('LEFTPADDING', (2, 0), (2, 1), 20),
                    ('RIGHTPADDING', (3, 0), (3, 1), 6),
                    ('LEFTPADDING', (3, 0), (3, 1), 6),
                    ('RIGHTPADDING', (4, 1), (4, 1), 3.5),
                    ('LEFTPADDING', (4, 1), (4, 1), 3.5),
                    ('RIGHTPADDING', (5, 1), (5, 1), 14),
                    ('LEFTPADDING', (5, 1), (5, 1), 14),
                    ('RIGHTPADDING', (6, 1), (6, 1), 3.5),
                    ('LEFTPADDING', (6, 1), (6, 1), 3.5),
                    ('RIGHTPADDING', (7, 1), (7, 1), 14),
                    ('LEFTPADDING', (7, 1), (7, 1), 14),
                    ('RIGHTPADDING', (8, 1), (8, 1), 3.5),
                    ('LEFTPADDING', (8, 1), (8, 1), 3.5),
                    ('RIGHTPADDING', (9, 1), (9, 1), 14),
                    ('LEFTPADDING', (9, 1), (9, 1), 14),
                    ('RIGHTPADDING', (10, 1), (10, 1), 14),
                    ('LEFTPADDING', (10, 1), (10, 1), 14),
                    ('RIGHTPADDING', (11, 1), (11, 1), 3),
                    ('LEFTPADDING', (11, 1), (11, 1), 3),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ('SPAN', (0, 0), (0, 1)),
                    ('SPAN', (1, 0), (1, 1)),
                    ('SPAN', (2, 0), (2, 1)),
                    ('SPAN', (3, 0), (3, 1)),
                    ('SPAN', (4, 0), (5, 0)),
                    ('SPAN', (6, 0), (7, 0)),
                    ('SPAN', (8, 0), (10, 0)),
                    ('SPAN', (11, 0), (11, 1)),
                    ]

    scale_table_style = [('FONTNAME', (0, 0), (-1, 1), 'Calibri'),
                    ('FONTNAME', (0, 2), (-1, -1), 'Calibri'),
                    ('FONTSIZE', (0, 0), (-1, 1), 10),
                    ('FONTSIZE', (0, 2), (-1, -1), 9),
                    ('BACKGROUND', (0, 0), (-1, 1), color_1),
                    ('TEXTCOLOR', (0, 0), (-1, 1), colors.white),
                    ('GRID', (0, 0), (-1, 1), 0.5, colors.white),
                    ('GRID', (0, 2), (-1, -1), 0.5, color_1),
                    ('BOX', (0, 0), (-1, -1), 0.5, color_1),
                    ('RIGHTPADDING', (0, 0), (1, 0), 32),
                    ('LEFTPADDING', (0, 0), (1, 0), 32),
                    ('RIGHTPADDING', (2, 1), (-1, 1), 16),
                    ('LEFTPADDING', (2, 1), (-1, 1), 16),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ('SPAN', (0, 0), (0, 1)),
                    ('SPAN', (1, 0), (1, 1)),
                    ('SPAN', (2, 0), (-1, 0)),
                    ('SPAN', (0, 2), (0, 3)),
                    ('SPAN', (0, 4), (0, 5)),
                    ('SPAN', (0, 6), (0, 8)),
                    ('SPAN', (0, 9), (1, 9)),
                    ('SPAN', (0, 10), (1, 10)),
                    ('SPAN', (2, 6), (3, 6)),
                    ('SPAN', (2, 7), (3, 7)),
                    ('SPAN', (2, 8), (3, 8)),
                    ('SPAN', (2, 10), (3, 10)),
                    ]

    pdf.drawImage(gt_logo, width/2-50, 790, width = 100, height = 44, mask = None)
    pdf.setFillColor(color_1)
    pdf.setStrokeColor(color_1)
    pdf.rect(30, 750, width = width-59, height = 30, fill = 1)
    pdf.setFillColor(colors.white)
    pdf.setFont('CalibriB', 15)
    pdf.drawCentredString(width/2, 760, "TEST HISTORY - TEST GEÇMİŞİ")
    pdf.setFillColor(colors.black)
    pdf.setFont("CalibriI", 8)
    pdf.drawCentredString(width/2, 20, "*NS: No Score       *NA: No Answer       *CEFR: Common European Framework Reference       *LXL: The Lexile Framework for Reading       *LFM: Language Form and Meaning")

    scale_list = [['Test Type','Section','CEFR','','','',''],
        ['','','Below A1','Level A1','Level A2','Level B1','Level B2'],
        ['test_1 Step 1','Reading','100-101','102-106','107-109','-','-'],
        ['','Listening','100-101','102-104','105-109','-','-'],
        ['test_1 Step 2','Reading','100-101','102-106','107-113','114-115','-'],
        ['','Listening','100-101','102-104','105-112','113-115','-'],
        ['test_3 Standard','Listening','200-220','','225-245','250-285','290-300'],
        ['','LFM','200-205','','210-245','250-275','280-300'],
        ['','Reading','200-205','','210-240','245-275','280-300'],
        ['test_1 Speaking','','1-9','10-15','16-21','22-25','26-27'],
        ['Juinor Speaking','','1-7','','8-10','11-13','14-16'],
        ]
    scale_table = Table(scale_list)
    scale_table.setStyle(scale_table_style)
    scale_table.wrapOn(pdf, width, height)
    scale_table.drawOn(pdf, 30, 50)

    ps1_raw_df = ps1_df.loc[ps1_df['student_number']==id_n]
    ps2_raw_df = ps2_df.loc[ps2_df['student_number']==id_n]
    pspk_raw_df = pspk_df.loc[pspk_df['student_number']==id_n]
    js_raw_df = js_df.loc[js_df['student_number']==id_n]
    jspk_raw_df = jspk_df.loc[jspk_df['student_number']==id_n]

    pri_list = []

    ps1_raw_df = ps1_raw_df[pd.to_datetime(ps1_raw_df['main_date'], format='%d-%m-%Y') <= datetime.strptime(last_test_date, '%d-%m-%Y')]
    ps1_raw_df['test_type'] = 'test_1 Step 1'
    ps1_raw_df['school'] = ps1_raw_df['school'].apply(lambda x: x[:23]+'...' if len(x) > 26 else x)
    cols = ps1_raw_df.columns
    ps1_raw_df = ps1_raw_df[[cols[5]]+[cols[2]]+[cols[-1]]+cols[9:-1].tolist()]
    ps1_raw_list = ps1_raw_df.values.tolist()

    pri_list.extend(ps1_raw_list)

    ps2_raw_df = ps2_raw_df[pd.to_datetime(ps2_raw_df['main_date'], format='%d-%m-%Y') <= datetime.strptime(last_test_date, '%d-%m-%Y')]
    ps2_raw_df['test_type'] = 'test_1 Step 2'
    ps2_raw_df['school'] = ps2_raw_df['school'].apply(lambda x: x[:23]+'...' if len(x) > 26 else x)
    cols = ps2_raw_df.columns
    ps2_raw_df = ps2_raw_df[[cols[5]]+[cols[2]]+[cols[-1]]+cols[9:-1].tolist()]
    ps2_raw_list = ps2_raw_df.values.tolist()

    pri_list.extend(ps2_raw_list)

    if len(pri_list) > 0:
        pri_list = sorted(pri_list, key=lambda x: datetime.strptime(x[0], '%d-%m-%Y'))
        main_list = pri_header_list+pri_list
        table_len = height-135-len(main_list)*13
        history_table_1 = Table(main_list)
        history_table_1.setStyle(pri_table_style)
        history_table_1.wrapOn(pdf, width, height)
        history_table_1.drawOn(pdf, 30, table_len)
    else:
        table_len = height-90


    js_raw_df = js_raw_df[pd.to_datetime(js_raw_df['main_date'], format='%d-%m-%Y') <= datetime.strptime(last_test_date, "%d-%m-%Y")]
    js_raw_df['test_type'] = 'test_3 Standard'
    js_raw_df['school'] = js_raw_df['school'].apply(lambda x: x[:23]+'...' if len(x) > 26 else x)
    cols = js_raw_df.columns
    js_raw_df = js_raw_df[[cols[5]]+[cols[2]]+[cols[-1]]+cols[9:-2].tolist()]
    js_list = js_raw_df.values.tolist()

    if len(js_list) > 0:
        js_list = sorted(js_list, key=lambda x: datetime.strptime(x[0], '%d-%m-%Y'))
        main_list = js_header_list+js_list
        table_len = table_len-30-len(main_list)*13
        history_table_2 = Table(main_list)
        history_table_2.setStyle(js_table_style)
        history_table_2.wrapOn(pdf, width, height)
        history_table_2.drawOn(pdf, 30, table_len)
    elif len(pri_list) > 0 and len(js_list) == 0:
        table_len = table_len

    spk_list = []

    pspk_raw_df = pspk_raw_df[pd.to_datetime(pspk_raw_df['main_date'], format='%d-%m-%Y') <= datetime.strptime(last_test_date, "%d-%m-%Y")]
    pspk_raw_df['test_type'] = 'test_1 Speaking'
    pspk_raw_df['school'] = pspk_raw_df['school'].apply(lambda x: x[:23]+'...' if len(x) > 26 else x)
    cols = pspk_raw_df.columns
    pspk_raw_df = pspk_raw_df[[cols[5]]+[cols[2]]+[cols[-1]]+[cols[9]]+[cols[12]]+[cols[11]]+[cols[10]]]
    pspk_raw_list = pspk_raw_df.values.tolist()
        
    spk_list.extend(pspk_raw_list)

    jspk_raw_df = jspk_raw_df[pd.to_datetime(jspk_raw_df['main_date'], format='%d-%m-%Y') <= datetime.strptime(last_test_date, "%d-%m-%Y")]
    jspk_raw_df['test_type'] = 'test_3 Speaking'
    jspk_raw_df['school'] = jspk_raw_df['school'].apply(lambda x: x[:23]+'...' if len(x) > 26 else x)
    cols = jspk_raw_df.columns
    jspk_raw_df = jspk_raw_df[[cols[5]]+[cols[2]]+[cols[-1]]+[cols[9]]+[cols[12]]+[cols[11]]+[cols[10]]]
    jspk_raw_list = jspk_raw_df.values.tolist()
        
    spk_list.extend(jspk_raw_list)

    if len(spk_list) > 0:
        spk_list = sorted(spk_list, key=lambda x: datetime.strptime(x[0], '%d-%m-%Y'))
        main_list = spk_header_list+spk_list
        table_len = table_len-26-len(main_list)*13
        history_table_3 = Table(main_list)
        history_table_3.setStyle(spk_table_style)
        history_table_3.wrapOn(pdf, width, height)
        history_table_3.drawOn(pdf, 30, table_len)

    pdf.showPage()

        


# Main Functions
def ps1_tr_karne(save_directory, selected_option, institution, main_date, choise, main_list):
    if selected_option == 0:
        file_name = str(save_directory)+"/"+main_date[6:]+"-"+main_date[3:5]+"-"+main_date[:2]+"_"+str(institution)+"_PS1_TK.pdf"
        file_name = fnc.check_file_name(file_name)
        pdf = canvas.Canvas(file_name, pagesize = A4)
    if choise == 0:
        df = ps1_df.loc[(ps1_df['school'] == institution) & \
                (ps1_df['main_date'] == main_date)].reset_index(drop=True)
    elif choise == 1:
        for student in eval(main_list):
            student_id = student[8]
            df = ps1_df.loc[(ps1_df['school'] == institution) & \
                    (ps1_df['main_date'] == main_date) & \
                        (ps1_df['student_number'] == student_id)].reset_index(drop=True)
    df['student_class'] = df['student_class'].apply(lambda x: int(scf.student_class_val_reverse(x)))
    df = df.sort_values(by = ['student_class', 'student_lastname','student_name']).reset_index(drop=True)
    new_list = df.values.tolist()
    for i in new_list:
        test_type = 8
        test_date = i[5]
        student_name = i[6]+" "+i[7]
        student_number = i[8]
        student_class = scf.student_class_val(i[9])
        school_name = i[2]
        reading_level = i[10]
        reading_score = i[11]
        reading_cefr = i[12]
        lexile = i[13]
        listening_level = i[14]
        listening_score = i[15]
        listening_cefr = i[16]
        if reading_score != "NS" and listening_score != "NS":
            total_score = math.ceil((int(reading_score)+int(listening_score))/2)
        else:
            total_score = "--"
        level_list = ["NA","1", "2", "3", "4"]
        for lvl in level_list:
            if reading_level == lvl:
                if reading_score == "NS":
                    star_logo_reading = ps1_ns_star
                    test_type_text_reading = trt.ps1_reading_ns_tr
                    reading_cefr = "**"
                    lexile = "**"
                else:
                    star_logo_reading = eval("ps1_"+str(lvl)+"star")
                    test_type_text_reading = eval("trt.ps1_reading_"+str(lvl)+"_tr")
            if listening_level == lvl:
                if listening_score == "NS":
                    star_logo_listening = ps1_ns_star
                    test_type_text_listening = trt.ps1_listening_ns_tr
                    listening_cefr = "**"
                else:
                    star_logo_listening = eval("ps1_"+str(lvl)+"star")
                    test_type_text_listening = eval("trt.ps1_listening_"+str(lvl)+"_tr")
        if selected_option == 1:
            path = save_directory+"/"+institution+"/"+student_class
            os.makedirs(path, exist_ok = True)
            filedir = path+"/"+i[6].upper()+i[7][0].upper()+"_"+str(student_number)+"_test_1 Step 1_TK.pdf"
            pdf = canvas.Canvas(filedir, pagesize = A4)
        header_pri(pdf, test_type, student_name, student_number, student_class, school_name, test_date)
        reading_pri(pdf, test_type, reading_score, reading_cefr, lexile, total_score, star_logo_reading, test_type_text_reading)
        listening_pri(pdf, test_type, listening_score, listening_cefr, star_logo_listening, test_type_text_listening)
        pdf.showPage()
        test_history(pdf,main_date,str(student_number), colors.navy)
        if selected_option == 1:
            pdf.save()
    if selected_option == 0:
        pdf.save()
        os.startfile(file_name)

def ps2_tr_karne(save_directory, selected_option, institution, main_date, choise, main_list):
    if selected_option == 0:
        file_name = str(save_directory)+"/"+main_date[6:]+"-"+main_date[3:5]+"-"+main_date[:2]+"_"+str(institution)+"_PS2_TK.pdf"
        file_name = fnc.check_file_name(file_name)
        pdf = canvas.Canvas(file_name, pagesize = A4)
    if choise == 0:
        df = ps2_df.loc[(ps2_df['school'] == institution) & \
                (ps2_df['main_date'] == main_date)].reset_index(drop=True)
    elif choise == 1:
        for student in eval(main_list):
            student_id = student[8]
            df = ps2_df.loc[(ps2_df['school'] == institution) & \
                    (ps2_df['main_date'] == main_date) & \
                        (ps2_df['student_number'] == student_id)].reset_index(drop=True)
    df['student_class'] = df['student_class'].apply(lambda x: int(scf.student_class_val_reverse(x)))
    df = df.sort_values(by = ['student_class', 'student_lastname','student_name']).reset_index(drop=True)
    new_list = df.values.tolist()
    for i in new_list:
        test_type = 9
        test_date = i[5]
        student_name = i[6]+" "+i[7]
        student_number = i[8]
        student_class = scf.student_class_val(i[9])
        school_name = i[2]
        reading_level = i[10]
        reading_score = i[11]
        reading_cefr = i[12]
        lexile = i[13]
        listening_level = i[14]
        listening_score = i[15]
        listening_cefr = i[16]
        if reading_score != "NS" and listening_score != "NS":
            total_score = math.ceil((int(reading_score)+int(listening_score))/2)
        else:
            total_score = "--"
        level_list = ["NA","1", "2", "3", "4", "5"]
        for lvl in level_list:
            if reading_level == lvl:
                if reading_score == "NS":
                    star_logo_reading = ps2_ns_badge
                    test_type_text_reading = trt.ps2_reading_ns_tr
                    reading_cefr = "**"
                    lexile = "**"
                else:
                    star_logo_reading = eval("ps2_"+str(lvl)+"badge")
                    test_type_text_reading = eval("trt.ps2_reading_"+str(lvl)+"_tr")
            if listening_level == lvl:
                if listening_score == "NS":
                    star_logo_listening = ps2_ns_badge
                    test_type_text_listening = trt.ps2_listening_ns_tr
                    listening_cefr = "**"
                else:
                    star_logo_listening = eval("ps2_"+str(lvl)+"badge")
                    test_type_text_listening = eval("trt.ps2_listening_"+str(lvl)+"_tr")
        if selected_option == 1:
            path = save_directory+"/"+institution+"/"+student_class
            os.makedirs(path, exist_ok = True)
            filedir = path+"/"+i[6].upper()+i[7][0].upper()+"_"+str(student_number)+"_test_1 Step 2_TK.pdf"
            pdf = canvas.Canvas(filedir, pagesize = A4)
        header_pri(pdf, test_type, student_name, student_number, student_class, school_name, test_date)
        reading_pri(pdf, test_type, reading_score, reading_cefr, lexile, total_score, star_logo_reading, test_type_text_reading)
        listening_pri(pdf, test_type, listening_score, listening_cefr, star_logo_listening, test_type_text_listening)
        pdf.showPage()
        test_history(pdf,main_date,str(student_number), colors.navy)
        if selected_option == 1:
            pdf.save()
    if selected_option == 0:
        pdf.save()
        os.startfile(file_name)
        
def pspk_tr_karne(save_directory, selected_option, institution, main_date, choise, main_list):
    if selected_option == 0:
        file_name = str(save_directory)+"/"+main_date[6:]+"-"+main_date[3:5]+"-"+main_date[:2]+"_"+str(institution)+"_PSPK_TK.pdf"
        file_name = fnc.check_file_name(file_name)
        pdf = canvas.Canvas(file_name, pagesize = A4)
    if choise == 0:
        df = pspk_df.loc[(pspk_df['school'] == institution) & \
                (pspk_df['main_date'] == main_date)].reset_index(drop=True)
    elif choise == 1:
        for student in eval(main_list):
            student_id = student[8]
            df = pspk_df.loc[(pspk_df['school'] == institution) & \
                    (pspk_df['main_date'] == main_date) & \
                        (pspk_df['student_number'] == student_id)].reset_index(drop=True)
    df['student_class'] = df['student_class'].apply(lambda x: int(scf.student_class_val_reverse(x)))
    df = df.sort_values(by = ['student_class', 'student_lastname','student_name']).reset_index(drop=True)
    new_list = df.values.tolist()
    for i in new_list:
        test_type = 20
        test_date = i[5]
        student_name = i[6]+" "+i[7]
        student_number = i[8]
        student_class = scf.student_class_val(i[9])
        school_name = i[2]
        speaking_score = i[10]
        speaking_cefr = i[11]
        speaking_level = i[12]
        level_list = ["-","1", "2", "3", "4", "5"]
        for lvl in level_list:
            if speaking_level == lvl:
                if speaking_score == "0":
                    test_type_text_speaking = trt.pspk_0_tr
                    star_logo_speaking = pspk_ns_ribbon
                elif speaking_score == "NS":
                    test_type_text_speaking = trt.pspk_ns_tr
                    star_logo_speaking = pspk_ns_ribbon
                else:
                    test_type_text_speaking = eval("trt.pspk_"+str(lvl)+"_tr")
                    star_logo_speaking = eval("pspk_"+str(lvl)+"_ribbon")
        if selected_option == 1:
            path = save_directory+"/"+institution+"/"+student_class
            os.makedirs(path, exist_ok = True)
            filedir = path+"/"+i[6].upper()+i[7][0].upper()+"_"+str(student_number)+"_test_1 Speaking_TK.pdf"
            pdf = canvas.Canvas(filedir, pagesize = A4)
        header_pri(pdf, test_type, student_name, student_number, student_class, school_name, test_date)
        speaking_pri(pdf, speaking_score, speaking_cefr, speaking_level, star_logo_speaking, test_type_text_speaking)
        pdf.showPage()
        test_history(pdf,main_date,str(student_number), colors.navy)
        if selected_option == 1:
            pdf.save()
    if selected_option == 0:
        pdf.save()
        os.startfile(file_name)

def js_tr_karne(save_directory, selected_option, institution, main_date, choise, main_list):
    if selected_option == 0:
        file_name = str(save_directory)+"/"+main_date[6:]+"-"+main_date[3:5]+"-"+main_date[:2]+"_"+str(institution)+"_JS_TK.pdf"
        file_name = fnc.check_file_name(file_name)
        pdf = canvas.Canvas(file_name, pagesize = A4)
    if choise == 0:
        df = js_df.loc[(js_df['school'] == institution) & \
                (js_df['main_date'] == main_date)].reset_index(drop=True)
    elif choise == 1:
        for student in eval(main_list):
            student_id = student[8]
            df = js_df.loc[(js_df['school'] == institution) & \
                    (js_df['main_date'] == main_date) & \
                        (js_df['student_number'] == student_id)].reset_index(drop=True)
    df['student_class'] = df['student_class'].apply(lambda x: int(scf.student_class_val_reverse(x)))
    df = df.sort_values(by = ['student_class', 'student_lastname','student_name']).reset_index(drop=True)
    new_list = df.values.tolist()
    for i in new_list:
        test_type = 5
        test_date = i[5]
        student_name = i[6]+" "+i[7]
        student_number = i[8]
        student_class = scf.student_class_val(i[9])
        school_name = i[2]
        listening_score = i[10]
        listening_cefr = i[11]
        lfm_score = i[12]
        lfm_cefr = i[13]
        reading_score = i[14]
        reading_cefr = i[15]
        lexile = i[16]
        total_score = i[17]
        osl = i[18]
        if  listening_score != "NS":
            if 200 <= int(listening_score) <= 220: 
                listening_level = "1"
            elif 225 <= int(listening_score) <= 245: 
                listening_level = "2"
            elif 250 <= int(listening_score) <= 285: 
                listening_level = "3"
            elif 290 <= int(listening_score) <= 300: 
                listening_level = "4"
        else:
            listening_level = "NS"
        if  lfm_score != "NS":
            if 200 <= int(lfm_score) <= 205: 
                lfm_level = "1"
            elif 210 <= int(lfm_score) <= 245: 
                lfm_level = "2"
            elif 250 <= int(lfm_score) <= 275: 
                lfm_level = "3"
            elif 280 <= int(lfm_score) <= 300: 
                lfm_level = "4"
        else:
            lfm_level = "NS"
        if reading_score != "NS":
            if 200 <= int(reading_score) <= 205: 
                reading_level = "1"
            elif 210 <= int(reading_score) <= 240: 
                reading_level = "2"
            elif 245 <= int(reading_score) <= 275: 
                reading_level = "3"
            elif 280 <= int(reading_score) <= 300: 
                reading_level = "4"
        else:
            reading_level = "NS"
        level_list = ["NS","1", "2", "3", "4"]
        for lvl in level_list:
            if listening_level == lvl:
                if listening_level == "NS":
                    test_type_text_listening = trt.js_listening_ns_tr
                    listening_cefr = "**"
                else:
                    test_type_text_listening = eval("trt.js_listening_"+str(lvl)+"_tr")
            if lfm_level == lvl:
                if lfm_level == "NS":
                    test_type_text_lfm = trt.js_lfm_ns_tr
                    lfm_cefr = "**"
                else:
                    test_type_text_lfm = eval("trt.js_lfm_"+str(lvl)+"_tr")
            if reading_level == lvl:
                if reading_level == "NS":
                    test_type_text_reading = trt.js_reading_ns_tr
                    reading_cefr = "**"
                    lexile = "**"
                else:
                    test_type_text_reading = eval("trt.js_reading_"+str(lvl)+"_tr")
        if selected_option == 1:
            path = save_directory+"/"+institution+"/"+student_class
            os.makedirs(path, exist_ok = True)
            filedir = path+"/"+i[6].upper()+i[7][0].upper()+"_"+str(student_number)+"_test_3 Standard_TK.pdf"
            pdf = canvas.Canvas(filedir, pagesize = A4)
        header_jun(pdf, test_type, student_name, student_number, student_class, school_name, test_date)
        listening_jun(pdf, listening_score, listening_cefr, total_score, osl, test_type_text_listening)
        lfm_jun(pdf, lfm_score, lfm_cefr, test_type_text_lfm)
        reading_jun(pdf, reading_score, reading_cefr, lexile, test_type_text_reading)
        pdf.showPage()
        test_history(pdf,main_date,str(student_number), colors.Color(red=(0.2),green=(0.7),blue=(0.76)))
        if selected_option == 1:
            pdf.save()
    if selected_option == 0:
        pdf.save()
        os.startfile(file_name)

def jspk_tr_karne(save_directory, selected_option, institution, main_date, choise, main_list):
    if selected_option == 0:
        file_name = str(save_directory)+"/"+main_date[6:]+"-"+main_date[3:5]+"-"+main_date[:2]+"_"+str(institution)+"_JSPK_TK.pdf"
        file_name = fnc.check_file_name(file_name)
        pdf = canvas.Canvas(file_name, pagesize = A4)
    if choise == 0:
        df = jspk_df.loc[(jspk_df['school'] == institution) & \
                (jspk_df['main_date'] == main_date)].reset_index(drop=True)
    elif choise == 1:
        for student in eval(main_list):
            student_id = student[8]
            df = jspk_df.loc[(jspk_df['school'] == institution) & \
                    (jspk_df['main_date'] == main_date) & \
                        (jspk_df['student_number'] == student_id)].reset_index(drop=True)
    df['student_class'] = df['student_class'].apply(lambda x: int(scf.student_class_val_reverse(x)))
    df = df.sort_values(by = ['student_class', 'student_lastname','student_name']).reset_index(drop=True)
    new_list = df.values.tolist()
    for i in new_list:
        test_type = 21
        test_date = i[5]
        student_name = i[6]+" "+i[7]
        student_number = i[8]
        student_class = scf.student_class_val(i[9])
        school_name = i[2]
        speaking_score = i[10]
        speaking_cefr = i[11]
        speaking_level = i[12]
        level_list = ["-","1", "2", "3", "4"]
        for lvl in level_list:
            if speaking_level == lvl:
                if speaking_score == "0":
                    test_type_text_speaking = trt.jspk_0_tr
                elif speaking_score == "NS":
                    test_type_text_speaking = trt.jspk_ns_tr
                else:
                    test_type_text_speaking = eval("trt.jspk_"+str(lvl)+"_tr")
        if selected_option == 1:
            path = save_directory+"/"+institution+"/"+student_class
            os.makedirs(path, exist_ok = True)
            filedir = path+"/"+i[6].upper()+i[7][0].upper()+"_"+str(student_number)+"_test_3 Speaking_TK.pdf"
            pdf = canvas.Canvas(filedir, pagesize = A4)
        header_jun(pdf, test_type, student_name, student_number, student_class, school_name, test_date)
        speaking_jun(pdf, speaking_score, speaking_cefr, speaking_level, test_type_text_speaking)
        pdf.showPage()
        test_history(pdf,main_date,str(student_number), colors.Color(red=(0.2),green=(0.7),blue=(0.76)))
        if selected_option == 1:
            pdf.save()
    if selected_option == 0:
        pdf.save()
        os.startfile(file_name)
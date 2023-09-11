from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

#Import Fonts
pdfmetrics.registerFont(TTFont('Calibri', './data/gui_data/fonts/CalibriRegular.ttf'))
pdfmetrics.registerFont(TTFont('CalibriB', './data/gui_data/fonts/CalibriBold.ttf'))
pdfmetrics.registerFont(TTFont('CalibriI', './data/gui_data/fonts/CalibriItalic.ttf'))
pdfmetrics.registerFont(TTFont('CalibriBI', './data/gui_data/fonts/CalibriBoldItalic.ttf'))

img1 = "./data/sales_card_data/test_4.jpg"
img2 = "./data/sales_card_data/2.sinif.jpg"
img3 = "./data/sales_card_data/3.sinif.jpg"
img4 = "./data/sales_card_data/4.sinif.jpg"
img5 = "./data/sales_card_data/5.sinif.jpg"
img6 = "./data/sales_card_data/6.sinif.jpg"
img7 = "./data/sales_card_data/7.sinif.jpg"
img8 = "./data/sales_card_data/8.sinif.jpg"
img9 = "./data/sales_card_data/9.sinif.jpg"
img10 = "./data/sales_card_data/hazsinif.jpg"
img11 = "./data/sales_card_data/10.sinif.jpg"
img12 = "./data/sales_card_data/11.sinif.jpg"
img13 = "./data/sales_card_data/12.sinif.jpg"
img2s = "./data/sales_card_data/2.sinifspk.jpg"
img3s = "./data/sales_card_data/3.sinifspk.jpg"
img4s = "./data/sales_card_data/4.sinifspk.jpg"
img5s = "./data/sales_card_data/5.sinifspk.jpg"
img6s = "./data/sales_card_data/6.sinifspk.jpg"
img7s = "./data/sales_card_data/7.sinifspk.jpg"
img8s = "./data/sales_card_data/8.sinifspk.jpg"
img9s = "./data/sales_card_data/9.sinifspk.jpg"
img10s = "./data/sales_card_data/hazsinifspk.jpg"
img11s = "./data/sales_card_data/10.sinifspk.jpg"
img12s = "./data/sales_card_data/11.sinifspk.jpg"
img13s = "./data/sales_card_data/12.sinifspk.jpg"

def create_sales_card(save_directory,institution,student_class,period,start_num,end_num,choice):
    translationTable = str.maketrans("ğĞıİöÖüÜşŞçÇ", "gGiIoOuUsScC")
    pdf = canvas.Canvas(save_directory+"/"+str(institution).translate(translationTable)+"_"+str(student_class)+"_Satis_Karti.pdf",pagesize=(420.6385, 595))
    while start_num <= end_num:
        #pdf.drawImage(img1, 0,0, width=420.6385,height=595,mask=None)
        if "SPEAKING" in str(student_class).split():
            student_class_header = student_class[:-9]
        else:
            student_class_header = student_class
        header = str(student_class_header)+" / "+str(institution)+" Test Type 1-2 SINAV GİRİŞ KARTI"
        pdf.setFont('Calibri', 17)
        pdf.drawCentredString(90,515, "No: "+str(start_num))
        pdf.drawCentredString(90,212, "No: "+str(start_num))
        if len(str(header))<=50:
            pdf.setFont('CalibriB', 11)
            pdf.drawString(163,525, header)
            pdf.drawString(163,225, header)
        else:
            pdf.setFont('CalibriB', 9.5)
            pdf.drawString(163,525, header)
            pdf.drawString(163,225, header)
        pdf.setFont('Calibri', 9)
        pdf.drawString(165,132, "Bu kart sadece öğrencinin "+period+" eğitim döneminde")
        pdf.drawString(165,122, "okulunda düzenlenecek olan Test Type 1-2 kurumsal testleri için")
        pdf.drawString(165,112, "kullanılabilir.")
        if choice == 0:
            if student_class =="2. SINIF":
                pdf.drawImage(img2, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img2, 315,249, width=90,height=35,mask=None)
            if student_class =="3. SINIF":
                pdf.drawImage(img3, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img3, 315,249, width=90,height=35,mask=None)
            if student_class =="4. SINIF":
                pdf.drawImage(img4, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img4, 315,249, width=90,height=35,mask=None)
            if student_class =="5. SINIF":
                pdf.drawImage(img5, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img5, 315,249, width=90,height=35,mask=None)
            if student_class =="6. SINIF":
                pdf.drawImage(img6, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img6, 315,249, width=90,height=35,mask=None)
            if student_class =="7. SINIF":
                pdf.drawImage(img7, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img7, 315,249, width=90,height=35,mask=None)
            if student_class =="8. SINIF":
                pdf.drawImage(img8, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img8, 315,249, width=90,height=35,mask=None)
            if student_class =="9. SINIF":
                pdf.drawImage(img9, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img9, 315,249, width=90,height=35,mask=None)
            if student_class =="HAZIRLIK SINIFI" or student_class == "HAZIRLIK" or student_class == "HAZ. SINIFI":
                pdf.drawImage(img10, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img10, 315,249, width=90,height=35,mask=None)
            if student_class =="10. SINIF":
                pdf.drawImage(img11, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img11, 315,249, width=90,height=35,mask=None)
            if student_class =="11. SINIF":
                pdf.drawImage(img12, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img12, 315,249, width=90,height=35,mask=None)
            if student_class =="12. SINIF":
                pdf.drawImage(img13, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img13, 315,249, width=90,height=35,mask=None)
            if student_class =="2. SINIF SPEAKING":
                pdf.drawImage(img2s, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img2s, 315,249, width=90,height=35,mask=None)
            if student_class =="3. SINIF SPEAKING":
                pdf.drawImage(img3s, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img3s, 315,249, width=90,height=35,mask=None)
            if student_class =="4. SINIF SPEAKING":
                pdf.drawImage(img4s, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img4s, 315,249, width=90,height=35,mask=None)
            if student_class =="5. SINIF SPEAKING":
                pdf.drawImage(img5s, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img5s, 315,249, width=90,height=35,mask=None)
            if student_class =="6. SINIF SPEAKING":
                pdf.drawImage(img6s, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img6s, 315,249, width=90,height=35,mask=None)
            if student_class =="7. SINIF SPEAKING":
                pdf.drawImage(img7s, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img7s, 315,249, width=90,height=35,mask=None)
            if student_class =="8. SINIF SPEAKING":
                pdf.drawImage(img8s, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img8s, 315,249, width=90,height=35,mask=None)
            if student_class =="9. SINIF SPEAKING":
                pdf.drawImage(img9s, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img9s, 315,249, width=90,height=35,mask=None)
            if student_class =="HAZIRLIK SINIFI SPEAKING" or student_class == "HAZIRLIK SPEAKING" or student_class == "HAZ. SINIFI SPEAKING":
                pdf.drawImage(img10s, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img10s, 315,249, width=90,height=35,mask=None)
            if student_class =="10. SINIF SPEAKING":
                pdf.drawImage(img11s, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img11s, 315,249, width=90,height=35,mask=None)
            if student_class =="11. SINIF SPEAKING":
                pdf.drawImage(img12s, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img12s, 315,249, width=90,height=35,mask=None)
            if student_class =="12. SINIF SPEAKING":
                pdf.drawImage(img13s, 315,552, width=90,height=35,mask=None)
                pdf.drawImage(img13s, 315,249, width=90,height=35,mask=None)
        elif choice == 1:
            pass
            #Barkodsuz
            
        
        pdf.showPage()
        start_num+=1
    pdf.save()
    import os,time
    time.sleep(1)
    os.startfile(save_directory+"/"+str(institution).translate(translationTable)+"_"+str(student_class)+"_Satis_Karti.pdf")
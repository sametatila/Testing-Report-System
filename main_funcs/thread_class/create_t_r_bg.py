from PyQt5 import QtCore
class CreateTurkishReportBGClass(QtCore.QThread):
    def __init__(self, parent: None,index=0):
        super(CreateTurkishReportBGClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors
        from reportlab.pdfgen import canvas
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.platypus import Table

        import os

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

        def header_pri():
            pdf.drawImage(gt_logo, 20, 790, width = 100, height = 44, mask = None)
            pdf.drawImage(pri_logo, 385, 795, width = 187, height = 30, mask = None)
            pdf.setFillColor(colors.navy)
            pdf.setStrokeColor(colors.navy)
            pdf.rect(20, 725, width = width-40, height = 55)
            pdf.rect(20, 775, width = width-40, height = 5, fill = 1)

        def pbt_pri():
            pdf.setFillColor(colors.black)
            pdf.setStrokeColor(colors.black)
            pdf.setFillColor(colors.navy)
            pdf.setStrokeColor(colors.navy)
            pdf.rect(20, 20, width = (width-40)/2-5, height = 680)
            pdf.rect(20+(width-40)/2+5, 20, width = (width-40)/2-5, height = 680)
            pdf.rect(20, 30+640, width = (width-40)/2-5, height = 30, fill = 1)
            pdf.rect(20+(width-40)/2+5, 30+640, width = (width-40)/2-5, height = 30, fill = 1)
            pdf.setFillColor(colors.white)
            pdf.setFont('CalibriB', 15)
            pdf.drawCentredString(160, 680, "READING - OKUMA")
            pdf.drawCentredString(445, 680, "LISTENING - DİNLEME")

        def speaking_pri():
            pdf.setFillColor(colors.navy)
            pdf.setStrokeColor(colors.navy)
            pdf.rect(width/2-190, 20, width = (width-40)/2+100, height = 680)
            pdf.rect(width/2-190, 30+640, width = (width-40)/2+100, height = 30, fill = 1)
            pdf.setFillColor(colors.white)
            pdf.setFont('CalibriB', 15)
            pdf.drawCentredString(width/2, 680, "SPEAKING - KONUŞMA")

        def header_jun():
            pdf.drawImage(gt_logo, 20, 790, width = 100, height = 44, mask = None)
            pdf.drawImage(jun_logo, 400, 795, width = 175, height = 29, mask = None)
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

        def pbt_jun():
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
            pdf.setFillColor(colors.white)
            pdf.setFont('CalibriB', 15)
            pdf.drawCentredString(width/4, 680, "LISTENING - DİNLEME")
            pdf.drawCentredString(width/4, 450, "LFM - DİL YAPISI VE ANLAM")
            pdf.drawCentredString(width/4, 220, "READING - OKUMA")

        def speaking_jun():
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
            pdf.setFillColor(colors.white)
            pdf.setFont('CalibriB', 15)
            pdf.drawCentredString(width/2, 680, "SPEAKING - KONUŞMA")

        def test_history(pdf, selected_color):
            pdf.showPage()
            scale_table_style = [('FONTNAME', (0, 0), (-1, 1), 'Calibri'),
                            ('FONTNAME', (0, 2), (-1, -1), 'Calibri'),
                            ('FONTSIZE', (0, 0), (-1, 1), 10),
                            ('FONTSIZE', (0, 2), (-1, -1), 9),
                            ('BACKGROUND', (0, 0), (-1, 1), selected_color),
                            ('TEXTCOLOR', (0, 0), (-1, 1), colors.white),
                            ('GRID', (0, 0), (-1, 1), 0.5, colors.white),
                            ('GRID', (0, 2), (-1, -1), 0.5, selected_color),
                            ('BOX', (0, 0), (-1, -1), 0.5, selected_color),
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
            pdf.setFillColor(selected_color)
            pdf.setStrokeColor(selected_color)
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

        if self.pri_pbt:
            file_path = '{}/test_1 PBT Türkçe Karne Arkaplan Baskı.pdf'.format(self.save_directory)
            pdf = canvas.Canvas(file_path, pagesize = A4)
            header_pri()
            pbt_pri()
            test_history(pdf, colors.navy)
        elif self.pri_cbt:
            file_path = '{}/test_1 CBT Türkçe Karne Arkaplan Baskı.pdf'.format(self.save_directory)
            pdf = canvas.Canvas(file_path, pagesize = A4)
            header_pri()
            speaking_pri()
            test_history(pdf, colors.navy)
        elif self.jun_pbt:
            file_path = '{}/test_3 PBT Türkçe Karne Arkaplan Baskı.pdf'.format(self.save_directory)
            pdf = canvas.Canvas(file_path, pagesize = A4)
            header_jun()
            pbt_jun()
            test_history(pdf, colors.navy)
        elif self.jun_cbt:
            file_path = '{}/test_3 CBT Türkçe Karne Arkaplan Baskı.pdf'.format(self.save_directory)
            pdf = canvas.Canvas(file_path, pagesize = A4)
            header_jun()
            speaking_jun()
            test_history(pdf, colors.navy)

        pdf.save()
        os.startfile(file_path)

    def stop(self):
        self.is_running = False
        self.terminate()

import main_funcs.mixed.mysql_connection as mc
import main_funcs.mixed.student_class_function as scf
import main_funcs.mixed.file_name_checker as fnc
import main_funcs.mixed.school_funcs as sf

import os
from datetime import datetime
from decimal import ROUND_HALF_UP, Decimal

import natsort
import pandas as pd
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Table

# Import Fonts
pdfmetrics.registerFont(TTFont('Calibri', './data/gui_data/fonts/CalibriRegular.ttf'))
pdfmetrics.registerFont(TTFont('CalibriB', './data/gui_data/fonts/CalibriBold.ttf'))
pdfmetrics.registerFont(TTFont('CalibriI', './data/gui_data/fonts/CalibriItalic.ttf'))
pdfmetrics.registerFont(TTFont('CalibriBI', './data/gui_data/fonts/CalibriBoldItalic.ttf'))

diff_list = [1,2,1.5,3,5,8,1.5,2,2.5,5]
between_diff_list = [1,3,10,20,7,10]
ps_main_diff, ps_class_diff, pspk_main_diff, pspk_class_diff, js_main_diff, js_class_diff, jspk_main_diff, jspk_class_diff, test_4_main_diff, test_4_class_diff = diff_list
ps_b_main_diff,ps_b_class_diff,js_b_main_diff,js_b_class_diff,test_4_b_main_diff,test_4_b_class_diff = between_diff_list

filigram = "./data/exam_data/filigram.jpeg"
pri_info = "./data/exam_data/test_1info.png"
pspk_info = "./data/exam_data/pspk_info.png"
js_info = "./data/exam_data/js_info.png"
jspk_info = "./data/exam_data/jspk_info.png"
test_4_info = "./data/exam_data/test_4_info.png"
width, height = A4

def school_letter(save_directory, institution, main_date, person):
    db_pd = mc.engine.connect()
    file_date = datetime.strptime(main_date, '%d-%m-%Y').strftime('%B, %Y')
    file_name = str(save_directory)+"/"+file_date+"_"+str(institution)+"_Zarf.pdf"
    file_name = fnc.check_file_name(file_name)
    pdf = canvas.Canvas(file_name, pagesize = A4)
    pdf.drawImage(filigram, 0, 0, width = width, height = height, mask = None)
    db_pd = mc.engine.connect()
    mycursor = db_pd.execute("SELECT logo FROM schools WHERE school_name = %s",(institution,))
    logo_file = mycursor.fetchone()[0]
    try:
        if logo_file != "Logo seç" or logo_file != None:
            logo_file = './data/tmp/'+sf.download_school_logo(logo_file)
            pdf.drawImage(logo_file, width/2-125, height/2+20, width = 250, height = 250, mask = None)
    except:
        pass
    pdf.setFont("CalibriB", 23)
    pdf.setFillColor(colors.maroon)
    pdf.drawCentredString(width/2, height/2+40, 'T Test')
    pdf.setFillColor(colors.navy)
    pdf.drawCentredString(width/2, height/2, institution)
    file_date = datetime.strptime(main_date, '%d-%m-%Y').strftime('%B, %Y')
    pdf.drawCentredString(width/2, height/2-40, str(file_date))
    pdf.drawCentredString(width/2, height/2-300, 'Sn. '+person.title())
    pdf.showPage()
    pdf.save()
    os.startfile(file_name)
    db_pd.close()

def first_info(pdf,second_page,test_type_str,institution,main_date):
    pdf.drawImage(filigram, 0, 0, width = width, height = height, mask = None)
    db_pd = mc.engine.connect()
    mycursor = db_pd.execute("SELECT logo FROM schools WHERE school_name = %s",(institution,))
    logo_file = mycursor.fetchone()[0]
    try:
        if logo_file != "Logo seç" or logo_file != None:
            logo_file = './data/tmp/'+sf.download_school_logo(logo_file)
            pdf.drawImage(logo_file, width/2-125, height/2+20, width = 250, height = 250, mask = None)
    except:
        pass
    pdf.setFont("CalibriB", 23)
    pdf.setFillColor(colors.maroon)
    pdf.drawCentredString(width/2, height/2+40, test_type_str)
    pdf.setFillColor(colors.navy)
    pdf.drawCentredString(width/2, height/2, institution)
    pdf.setFillColor(colors.black)
    pdf.drawCentredString(width/2, height/2-40, "INSTITUTIONAL REPORT")
    file_date = datetime.strptime(main_date, '%d-%m-%Y').strftime('%B, %Y')
    pdf.drawCentredString(width/2, height/2-80, str(file_date))
    pdf.showPage()

    pdf.drawImage(second_page, 0, 0, width = width, height = height, mask = None)
    pdf.showPage()

def color_style_for_table_class(test_type_styling,styles,data,column_list,min_value,max_value):
    for count in range(len(column_list)):
        for row, r in enumerate(data):
            for col, val in enumerate(r):
                if val != 'NS':
                    if test_type_styling == 'PS':
                        score = [i for i, x in enumerate(data[1]) if x == 'Score'][count]
                        bool_val = row != 0 and row != 1
                    elif test_type_styling in ['PSPK','JSPK']:
                        score = [i for i, x in enumerate(data[0]) if x == 'Total'][count]
                        bool_val = row != 0
                    elif test_type_styling in ['JS','test_4']:
                        score = [i for i, x in enumerate(data[1]) if x == 'Score'][count]
                        bool_val = row != 0 and row != 1

                    if bool_val and col == score:
                        min_val = min_value
                        max_val = max_value
                        val = int(val)
                        percentage = ((val-min_val)*(100/(max_val-min_val)))/100
                        if val <= column_list[list(column_list.keys())[count]][0]:
                            style = [
                                ('BACKGROUND',(col,row),(col,row),('LINEARGRADIENT',(percentage-0.01,0),
                                (percentage,0),True,(colors.HexColor('#FF4136'),colors.white),None))
                            ]
                            styles.extend(style)
                        elif val >= column_list[list(column_list.keys())[count]][1]:
                            style = [
                                ('BACKGROUND',(col,row),(col,row),('LINEARGRADIENT',(percentage-0.01,0),
                                (percentage,0),True,(colors.HexColor('#3D9970'),colors.white),None))
                            ]
                            styles.extend(style)
                        else:
                            style = [
                                ('BACKGROUND',(col,row),(col,row),('LINEARGRADIENT',(percentage-0.01,0),
                                (percentage,0),True,(colors.HexColor('#e8b425'),colors.white),None))
                            ]
                            styles.extend(style)

                    if (row != 0 and row != 1) and test_type_styling != 'PSPK' and test_type_styling != 'JSPK':
                        if test_type_styling == 'PS':
                            cb_diff = ps_b_class_diff
                            if r[[i for i, x in enumerate(data[1]) if x == 'Score'][0]] != 'NS' and \
                                    r[[i for i, x in enumerate(data[1]) if x == 'Score'][1]] != 'NS':
                                if abs(int(r[[i for i, x in enumerate(data[1]) if x == 'Score'][0]]) - \
                                        int(r[[i for i, x in enumerate(data[1]) if x == 'Score'][1]])) >= cb_diff:
                                    style = [
                                        ('BACKGROUND',(data[0].index('Student Name'),row),
                                        (data[0].index('Student Name'),row),colors.HexColor('#8AC7DB'))
                                    ]
                                    styles.extend(style)
                        else:
                            if test_type_styling == 'JS':
                                cb_diff = js_b_class_diff
                            elif test_type_styling == 'test_4':
                                cb_diff = test_4_b_class_diff
                            if r[[i for i, x in enumerate(data[1]) if x == 'Score'][0]] != 'NS' and \
                                    r[[i for i, x in enumerate(data[1]) if x == 'Score'][1]] != 'NS' and \
                                        r[[i for i, x in enumerate(data[1]) if x == 'Score'][2]] != 'NS':
                                if abs(int(r[[i for i, x in enumerate(data[1]) if x == 'Score'][0]]) - \
                                        int(r[[i for i, x in enumerate(data[1]) if x == 'Score'][1]])) >= cb_diff or \
                                        abs(int(r[[i for i, x in enumerate(data[1]) if x == 'Score'][1]]) - \
                                            int(r[[i for i, x in enumerate(data[1]) if x == 'Score'][2]])) >= cb_diff or \
                                            abs(int(r[[i for i, x in enumerate(data[1]) if x == 'Score'][0]]) - \
                                                int(r[[i for i, x in enumerate(data[1]) if x == 'Score'][2]])) >= cb_diff:
                                    style = [
                                        ('BACKGROUND',(data[0].index('Student Name'),row),
                                        (data[0].index('Student Name'),row),colors.HexColor('#8AC7DB'))
                                    ]
                                    styles.extend(style)
    return styles

def color_style_for_table_main(test_type_styling,styles,data,column_list,min_value,max_value):
    for count in range(len(column_list)):
        for row, r in enumerate(data):
            for col, val in enumerate(r):
                if val != 'NS':
                    if row != 0 and col == data[0].index(list(column_list.keys())[count]):
                        min_val = min_value
                        max_val = max_value
                        val = float(val)
                        percentage = ((val-min_val)*(100/(max_val-min_val)))/100
                        if val <= column_list[list(column_list.keys())[count]][0]:
                            style = [
                                ('BACKGROUND',(col,row),(col,row),('LINEARGRADIENT',(percentage-0.01,0),
                                (percentage,0),True,(colors.HexColor('#FF4136'),colors.white),None))
                            ]
                            styles.extend(style)
                        elif val >= column_list[list(column_list.keys())[count]][1]:
                            style = [
                                ('BACKGROUND',(col,row),(col,row),('LINEARGRADIENT',(percentage-0.01,0),
                                (percentage,0),True,(colors.HexColor('#3D9970'),colors.white),None))
                            ]
                            styles.extend(style)
                        else:
                            style = [
                                ('BACKGROUND',(col,row),(col,row),('LINEARGRADIENT',(percentage-0.01,0),
                                (percentage,0),True,(colors.HexColor('#E8B425'),colors.white),None))
                            ]
                            styles.extend(style)
                    if row != 0 and test_type_styling != 'PSPK' and test_type_styling != 'JSPK':
                        if test_type_styling == 'PS':
                            mb_diff = ps_b_main_diff
                            if r[data[0].index(list(column_list.keys())[0])] != 'NS' and \
                                    r[data[0].index(list(column_list.keys())[1])] != 'NS':
                                if abs(float(r[data[0].index(list(column_list.keys())[0])]) - \
                                        float(r[data[0].index(list(column_list.keys())[1])])) >= mb_diff:
                                    style = [
                                        ('BACKGROUND',(data[0].index('Class'),row),
                                        (data[0].index('Class'),row),colors.HexColor('#8AC7DB'))
                                    ]
                                    styles.extend(style)
                        else:
                            if test_type_styling == 'JS':
                                mb_diff = js_b_main_diff
                            elif test_type_styling == 'test_4':
                                mb_diff = test_4_b_main_diff
                            if r[data[0].index(list(column_list.keys())[0])] != 'NS' and \
                                    r[data[0].index(list(column_list.keys())[1])] != 'NS' and \
                                        r[data[0].index(list(column_list.keys())[2])] != 'NS':
                                if abs(float(r[data[0].index(list(column_list.keys())[0])]) - \
                                        float(r[data[0].index(list(column_list.keys())[1])])) >= mb_diff or \
                                        abs(float(r[data[0].index(list(column_list.keys())[0])]) - \
                                            float(r[data[0].index(list(column_list.keys())[2])])) >= mb_diff or \
                                            abs(float(r[data[0].index(list(column_list.keys())[1])]) - \
                                                float(r[data[0].index(list(column_list.keys())[2])])) >= mb_diff:
                                    style = [
                                        ('BACKGROUND',(data[0].index('Class'),row),
                                        (data[0].index('Class'),row),colors.HexColor('#8AC7DB'))
                                    ]
                                    styles.extend(style)
    return styles

def test_1institutional_report(doc_type,save_directory, institution, main_date, choise, main_list):
    db_pd = mc.engine.connect()
    file_date = datetime.strptime(main_date, '%d-%m-%Y').strftime('%B, %Y')
    file_name = str(save_directory)+"/"+file_date+"_"+str(institution)+"_test_1_Institutional_Report.pdf"
    ### file_name = fnc.check_file_name(file_name)
    pdf = canvas.Canvas(file_name, pagesize = A4)

    sql_select_by_date_and_school = "SELECT * FROM test_1step_1 WHERE main_date = '{}' AND school = '{}' ORDER BY student_class, student_lastname, student_name".format(main_date,institution)
    df_1 = pd.read_sql(sql_select_by_date_and_school, con = db_pd)
    df_1.insert(0, 'test_type', 'ps1')

    sql_select_by_date_and_school = "SELECT * FROM test_1step_2 WHERE main_date = '{}' AND school = '{}' ORDER BY student_class, student_lastname, student_name".format(main_date,institution)
    df_2 = pd.read_sql(sql_select_by_date_and_school, con = db_pd)
    df_2.insert(0, 'test_type', 'ps2')

    selected_df = pd.concat([df_1, df_2])
    if (choise == 2 and doc_type == 0) or (choise == 0 and doc_type == 1):
        main_df = selected_df
    elif choise == 1 and doc_type == 1:
        class_df = pd.DataFrame()
        for student_id in eval(main_list):
            student_id = student_id[8]
            sql_select_by_date_and_school = """SELECT student_class FROM test_1step_1 WHERE school = '{}' AND main_date = '{}' AND student_number = '{}'"""
            df1 = pd.read_sql(sql_select_by_date_and_school.format(institution,main_date,student_id), con = db_pd)
            class_df = pd.concat([df1, class_df], ignore_index=True, axis=0)
        for student_id in eval(main_list):
            student_id = student_id[8]
            sql_select_by_date_and_school = """SELECT student_class FROM test_1step_2 WHERE school = '{}' AND main_date = '{}' AND student_number = '{}'"""
            df2 = pd.read_sql(sql_select_by_date_and_school.format(institution,main_date,student_id), con = db_pd)
            class_df = pd.concat([df2, class_df], ignore_index=True, axis=0)
        selected_class_list = [i[0] for i in class_df.values.tolist()]
        main_df = pd.DataFrame()
        for single_class in selected_class_list:
            df_1 = selected_df.loc[selected_df['student_class'] == single_class]
            main_df = pd.concat([df_1, main_df], ignore_index=True, axis=0)

    name_df = main_df['student_lastname'].str.cat(main_df['student_name'], sep = ' ').str.upper()
    main_df.insert(1, 'full_name', name_df)
    main_df = main_df.reset_index()
    main_df = main_df.drop(columns = ['index','country', 'provience', 'school', 'form_code', 'main_date', 'test_date', 'student_lastname', 'student_name'])
    total_df = (main_df['reading_score'].loc[(main_df['reading_score'] != "NS") & (main_df['listening_score'] != "NS")].astype('int64')+main_df['listening_score'].loc[(main_df['reading_score'] != "NS") & (main_df['listening_score'] != "NS")].astype('int64'))/2
    total_df = total_df.map(lambda x: Decimal(x).quantize(0,rounding=ROUND_HALF_UP)).astype('int64').astype('str')
    main_df.insert(11, 'total_score', total_df)
    if doc_type == 0:
        main_df = main_df.sort_values(by = ['student_class', 'test_type', 'total_score'], ascending = [True, True, False])
    elif doc_type == 1:
        main_df = main_df.sort_values(by = ['student_class', 'test_type', 'full_name'], ascending = [True, True, True])
    class_list = sorted(list(set(main_df['student_class'].values.tolist())))
    for i in range(len(class_list)):
        class_list[i] = int(scf.student_class_val_reverse(class_list[i]))
    class_list = sorted(class_list)
    main_df = main_df.drop(columns = ['test_type', 'student_number'])
    main_average_df = main_df.loc[(main_df['reading_score'] != "NS") & (main_df['listening_score'] != "NS")]

    def main_table(first_class):
        #Create average table
        raw_average_table = []
        total_number = 0
        total_include_number = 0
        for single_class in first_class:
            spec_list = main_df.loc[main_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_list = [[x[0]]+x[2:] for x in spec_list]
            for i in spec_list:
                if str(i[-1]) == "nan":
                    i[-1] = ""
            spec_average_list = main_average_df.loc[main_average_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_average_list = [[x[0]]+x[2:] for x in spec_average_list]
            total_number = total_number + len(spec_list)
            total_include_number = total_include_number + len(spec_average_list)
            if spec_average_list != []:
                average_item = spec_average_list
                reading_average = round(sum([int(float(x[2])) for x in average_item if x[2] != "NS"])/len([int(float(x[2])) for x in average_item if x[2] != "NS"]), 2)
                listening_average = round(sum([int(float(x[6])) for x in average_item if x[6] != "NS"])/len([int(float(x[6])) for x in average_item if x[6] != "NS"]), 2)
                total_average = round((reading_average+listening_average)/2, 2)
                second_data_list = [scf.student_class_val(single_class), str("{:.2f}".format(reading_average)), str("{:.2f}".format(listening_average)), str("{:.2f}".format(total_average)), str(len(spec_average_list)),str(len(spec_list))]
                raw_average_table.append(second_data_list)
        school_reading_average = round(sum([float(x[1])*int(x[4]) for x in raw_average_table])/sum([int(x[4]) for x in raw_average_table]), 2)
        school_listening_average = round(sum([float(x[2])*int(x[4]) for x in raw_average_table])/sum([int(x[4]) for x in raw_average_table]), 2)
        school_total_average = round(sum([float(x[3])*int(x[4]) for x in raw_average_table])/sum([int(x[4]) for x in raw_average_table]), 2)
        school_average = ["School",  str("{:.2f}".format(school_reading_average)), str("{:.2f}".format(school_listening_average)),str("{:.2f}".format(school_total_average)),str(total_include_number), str(total_number)]
        average_data = [["Class", "Reading\nAverage", "Listening\nAverage", "Total\nAverage", "Number of Students\nIncluded in Average","Total\nNumber of Students"]]
        average_data.extend(raw_average_table)
        average_data.append(school_average)
        average_table = Table(average_data)
        average_table_style = [
            ('FONTNAME', (0, 0), (-1, 0), 'CalibriB'),
            ('FONTNAME', (0, 1), (-1, -1), 'Calibri'),
            ('FONTSIZE', (0, 0), (-1, 1), 10),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('TOPPADDING', (0, 1), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 2),
            ('RIGHTPADDING', (0, 0), (0, 0), 12),
            ('LEFTPADDING', (0, 0), (0, 0), 12),
            ('RIGHTPADDING', (1, 0), (3, 0), 29),
            ('LEFTPADDING', (1, 0), (3, 0), 29),
            ('RIGHTPADDING', (4, 0), (4, 0), 2),
            ('LEFTPADDING', (4, 0), (4, 0), 2),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ]
        average_table.setStyle(color_style_for_table_main("PS",average_table_style,average_data[:-1],{'Reading\nAverage':[school_reading_average-ps_main_diff,school_reading_average+ps_main_diff],'Listening\nAverage':[school_listening_average-ps_main_diff,school_listening_average+ps_main_diff]},99,115))
        pdf.drawImage(filigram, 0, 0, width = width, height = height, mask = None)
        pdf.setFillColor(colors.maroon)
        pdf.setFont("CalibriB", 16)
        pdf.drawCentredString(width/2, 740, "Test Type 1-2 Test Results")
        pdf.setFillColor(colors.navy)
        pdf.setFont("CalibriB", 16)
        pdf.drawCentredString(width/2, 715, institution)
        styling_info_dict = {
                '#8AC7DB':'{} scale score difference between reading and listening.'.format(str(ps_b_main_diff)),
                '#3D9970':'{} scale score or higher than the school average.'.format(str(ps_main_diff)),
                '#E8B425':'Within {} scale score range of the school average.'.format(str(ps_main_diff)),
                '#FF4136':'{} scale scores below school average.'.format(str(ps_main_diff))
                }
        counter_1 = 0
        pdf.setLineWidth(0.1)
        for key, val in styling_info_dict.items():
            pdf.setFillColor(colors.HexColor(key))
            pdf.rect(30, 125-counter_1, 17, 8, stroke=1, fill=1)
            pdf.setFillColor(colors.black)
            pdf.setFont("CalibriBI", 8)
            pdf.drawString(52, 125-counter_1+1, val)
            counter_1+=15
        pdf.setFillColor(colors.black)

        class_len = height-175-len(average_data)*15
        average_table.wrapOn(pdf, width, height)
        average_table.drawOn(pdf, 40, class_len)
        #Average table END

        legend_data = [x[0] for x in average_data[1:]]
        legend_data = [legend_data[-1]]+legend_data[:-1]
        chart_data = [x[1:-2] for x in average_data[1:]]
        for i in chart_data:
            for y in range(len(i)):
                i[y] = float(i[y])
        chart_data = [tuple(i) for i in [chart_data[-1]]+chart_data[:-1]]
        max_graph_value = round(max(max(chart_data)))+2

        drawing = Drawing(400, 200)
        if len(chart_data) < 17:
            bc = VerticalBarChart()
            bc.x = 50
            bc.y = 50
            bc.height = 170
            bc.width = 485
            color_list = [colors.mediumaquamarine, colors.darkmagenta, colors.chartreuse, colors.cornflowerblue, colors.plum, colors.rosybrown, colors.salmon, colors.seagreen, colors.tan, colors.steelblue, colors.violet, colors.yellowgreen, colors.lemonchiffon, colors.aqua, colors.blueviolet, colors.coral, colors.skyblue, colors.blanchedalmond, colors.darkgoldenrod]
            for x in range(len(color_list)):
                for i in range(3):
                    bc.bars[(x, i)].fillColor = color_list[x]
            bc.data = chart_data
            bc.strokeColor = colors.black
            bc.strokeWidth = 0.3
            bc.groupSpacing = 30
            bc.barSpacing = 0.5
            bc.valueAxis.valueMin = 100
            bc.valueAxis.valueMax = max_graph_value
            bc.valueAxis.valueStep = 2
            bc.valueAxis.strokeWidth = 0.3
            bc.valueAxis.strokeColor = colors.black
            bc.valueAxis.gridStart = bc.x
            bc.valueAxis.gridEnd = bc.x+bc.width
            bc.valueAxis.gridStrokeWidth = 0.1
            bc.valueAxis.gridStrokeColor = colors.black
            bc.valueAxis.visibleGrid = True
            bc.valueAxis.visibleTicks = False
            bc.valueAxis.labels.fontSize = 10
            bc.valueAxis.labels.fontName = 'Calibri'
            bc.barLabelFormat = '%.2f'
            bc.barLabels.fontSize = 7
            bc.barLabels.fontName = 'Calibri'
            bc.barLabels.dy = -20
            bc.barLabels.dx = -1
            bc.barLabels.angle = 90
            bc.bars.strokeWidth = 0.2
            bc.categoryAxis.labels.boxAnchor = 'ne'
            bc.categoryAxis.labels.dx = 35
            bc.categoryAxis.labels.dy = -10
            bc.categoryAxis.labels.angle = 0
            bc.categoryAxis.labels.fontSize = 12
            bc.categoryAxis.labels.fontName = 'Calibri'
            bc.categoryAxis.categoryNames = ['Reading Average', 'Listening Average', 'Total Average']
            low_bar_labels = []
            for i in chart_data:
                if sum(i)/len(i) < 101.5:
                    low_bar_labels.append(i)
            if len(low_bar_labels) > 0:
                bc.barLabels.visible = False
            else:
                bc.barLabels.visible = True
            drawing.add(bc)

            legend = Legend()
            legend.alignment = 'right'
            legend.boxAnchor = 'sw'
            legend.columnMaximum = 1
            legend.colEndCallout = 0
            legend.dx = 15
            legend.dxTextSpace = 4
            legend.dy = 8
            legend.fontName = 'Calibri'
            legend.fontSize = 11
            legend.subCols.minWidth = 25
            legend.strokeWidth = 0.1
            legend.variColumn = 1
            legend.x = 51
            legend.y = -10
            legend.deltay = 10
            legend.colorNamePairs = [(color_list[i], (legend_data[i])) for i in range (len(bc.data[:1]))]
            legend.autoXPadding = 20

            legend1 = Legend()
            legend1.alignment = 'right'
            legend1.boxAnchor = 'sw'
            legend1.columnMaximum = 1
            legend1.colEndCallout = 0
            legend1.dx = 15
            legend1.dxTextSpace = 4
            legend1.dy = 8
            legend1.fontName = 'Calibri'
            legend1.fontSize = 11
            legend1.subCols.minWidth = 25
            legend1.strokeWidth = 0.1
            legend1.variColumn = 1
            legend1.x = 115
            legend1.y = -10
            legend1.deltay = 10
            legend1.colorNamePairs = [(color_list[i+1], (legend_data[i+1])) for i in range (len(bc.data[1:8]))]
            legend1.autoXPadding = 20
            if len(bc.data) > 8:
                legend2 = Legend()
                legend2.alignment = 'right'
                legend2.boxAnchor = 'sw'
                legend2.columnMaximum = 1
                legend2.colEndCallout = 0
                legend2.dx = 15
                legend2.dxTextSpace = 4
                legend2.dy = 8
                legend2.fontName = 'Calibri'
                legend2.fontSize = 11
                legend2.subCols.minWidth = 25
                legend2.strokeWidth = 0.1
                legend2.variColumn = 1
                legend2.x = 51
                legend2.y = -30
                legend2.deltay = 10
                legend2.colorNamePairs = [(color_list[i+8], (legend_data[i+8])) for i in range (len(bc.data[8:]))]
                legend2.autoXPadding = 20
                drawing.add(legend2)
            drawing.add(legend)
            drawing.add(legend1)
        x, y = 10, class_len-250
        renderPDF.draw(drawing, pdf, x, y, showBoundary = False)

        pdf.showPage()
        return school_reading_average,school_listening_average

    def class_tables(first_class,school_reading_average,school_listening_average):
        for single_class in first_class:
            pdf.drawImage(filigram, 0, 0, width = width, height = height, mask = None)
            spec_list = main_df.loc[main_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_list = [[x[0]]+x[2:] for x in spec_list]
            for i in spec_list:
                if str(i[-1]) == "nan":
                    i[-1] = "NS"
            spec_average_list = main_average_df.loc[main_average_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_average_list = [[x[0]]+x[2:] for x in spec_average_list]
            ps1data = [["Student Name", "Reading Section", "", "", "", "Listening Section", "", "", "Total"],
                    ["", "Stars/\nBadges", "Score", "CEFR", "LXL", "Stars/\nBadges", "Score", "CEFR", ""]]

            ps1data.extend(spec_list)
            ps1data_table = Table(ps1data)
            ps1_style = [('FONTNAME', (0, 0), (-1, 1), 'CalibriB'),
                ('FONTNAME', (0, 2), (-1, -1), 'Calibri'),
                ('FONTSIZE', (0, 0), (-1, 1), 10),
                ('FONTSIZE', (0, 2), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 1), 3),
                ('BOTTOMPADDING', (0, 2), (-1, -1), 2),
                ('TOPPADDING', (0, 2), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (0, 1), 58),
                ('LEFTPADDING', (0, 0), (0, 1), 58),
                ('RIGHTPADDING', (1, 1), (1, 1), 7),
                ('LEFTPADDING', (1, 1), (1, 1), 7),
                ('RIGHTPADDING', (2, 1), (2, 1), 12),
                ('LEFTPADDING', (2, 1), (2, 1), 12),
                ('RIGHTPADDING', (5, 1), (5, 1), 7),
                ('LEFTPADDING', (5, 1), (5, 1), 7),
                ('RIGHTPADDING', (6, 1), (6, 1), 12),
                ('LEFTPADDING', (6, 1), (6, 1), 12),
                ('RIGHTPADDING', (3, 1), (4, 1), 15),
                ('LEFTPADDING', (3, 1), (4, 1), 15),
                ('RIGHTPADDING', (7, 1), (7, 1), 15),
                ('LEFTPADDING', (7, 1), (7, 1), 15),
                ("VALIGN", (0, 0), (0, 1), "MIDDLE"),
                ("ALIGN", (0, 0), (0, 1), "CENTER"),
                ("VALIGN", (1, 1), (-1, 1), "MIDDLE"),
                ("ALIGN", (1, 1), (-1, 1), "CENTER"),
                ("VALIGN", (1, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (1, 0), (-1, -1), "CENTER"),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                ('SPAN', (0, 0), (0, 1)),
                ('SPAN', (1, 0), (4, 0)),
                ('SPAN', (5, 0), (7, 0)),
                ('SPAN', (8, 0), (8, 1)),
                ]

            ############################################################################### BURAYA Bİ ÇÖZÜM BUL
            reading_average = round(sum([int(float(x[2])) for x in spec_average_list if x[2] != "NS"])/len([int(float(x[2])) for x in spec_average_list if x[2] != "NS"]), 2)
            listening_average = round(sum([int(float(x[6])) for x in spec_average_list if x[6] != "NS"])/len([int(float(x[6])) for x in spec_average_list if x[6] != "NS"]), 2)
            total_average = round((reading_average+listening_average)/2, 2)
            ########################################################################### AYNISI MAIN TABLE'DA DA VAR

            ps1data_table.setStyle(color_style_for_table_class('PS',ps1_style,ps1data,{'Reading Section':[school_reading_average-ps_class_diff,school_reading_average+ps_class_diff],'Listening Section':[school_listening_average-ps_class_diff,school_listening_average+ps_class_diff]},99,115))
            class_len = height-185-len(ps1data)*14
            ps1data_table.wrapOn(pdf, width, height)
            ps1data_table.drawOn(pdf, 30, class_len)
            pdf.setFillColor(colors.maroon)
            pdf.setFont("CalibriB", 16)
            pdf.drawCentredString(width/2, 740, "Test Type 1-2 Test Results")
            pdf.setFillColor(colors.navy)
            pdf.setFont("CalibriB", 16)
            pdf.drawCentredString(width/2, 715, institution)
            pdf.setFillColor(colors.maroon)
            pdf.setFont("CalibriB", 20)
            pdf.drawCentredString(width/2, 690, scf.student_class_val(single_class))
            pdf.setFillColor(colors.black)
            pdf.setFont("CalibriB", 10)
            pdf.drawString(129, class_len-20, "Reading Average : ")
            pdf.drawString(125, class_len-35, "Listening Average : ")
            pdf.drawString(141, class_len-50, "Total Average : ")
            pdf.drawString(30, class_len-65, "Number of Students Included in Average : ")
            pdf.drawString(91, class_len-80, "Total Number of Students : ")
            pdf.setFont("Calibri", 10)
            pdf.drawString(207, class_len-20, str("{:.2f}".format(reading_average)))
            pdf.drawString(207, class_len-35, str("{:.2f}".format(listening_average)))
            pdf.drawString(207, class_len-50, str("{:.2f}".format(total_average)))
            pdf.drawString(207, class_len-65, str(len(spec_average_list)))
            pdf.drawString(207, class_len-80, str(len(spec_list)))
            pdf.setFont("CalibriI", 8)
            pdf.drawCentredString(width/2, 70, "*NS: No Score               *NA: No Answer               *CEFR: Common European Framework Reference               *LXL: The Lexile Framework for Reading")
            styling_info_dict = {
                '#8AC7DB':'{} scale score difference between reading and listening.'.format(str(ps_b_class_diff)),
                '#3D9970':'{} scale score or higher than the school average.'.format(str(ps_class_diff)),
                '#E8B425':'Within {} scale score range of the school average.'.format(str(ps_class_diff)),
                '#FF4136':'{} scale scores below school average.'.format(str(ps_class_diff))
                }
            counter_1 = 0
            pdf.setLineWidth(0.1)
            for key, val in styling_info_dict.items():
                pdf.setFillColor(colors.HexColor(key))
                pdf.rect(30, 135-counter_1, 17, 8, stroke=1, fill=1)
                pdf.setFillColor(colors.black)
                pdf.setFont("CalibriBI", 8)
                pdf.drawString(52, 135-counter_1+1, val)
                counter_1+=15

            pdf.showPage()

            if doc_type == 1:
                pdf.drawImage(pri_info, 0, 0, width = width, height = height, mask = None)
                pdf.showPage()
    test_type_str = "Test Type 1-2 Tests"
    if doc_type == 0:
        first_info(pdf,pri_info,test_type_str,institution,main_date)
        class_int_list = []
        for c in range(0, 1900, 100):class_int_list.append(c)
        for c in range(10900, 11200, 100):class_int_list.append(c)
        for c in class_int_list:
            try:
                aa = []
                for i in class_list:
                    if 200+c > int(i) > 100+c:
                        aa.append(i)
                school_reading_average,school_listening_average = main_table(aa)
                class_tables(aa,school_reading_average,school_listening_average)
            except ZeroDivisionError:
                pass

    elif doc_type == 1:
        class_int_list = []
        for c in range(0, 1900, 100):class_int_list.append(c)
        for c in range(10900, 11200, 100):class_int_list.append(c)
        for c in class_int_list:
            try:
                aa = []
                for i in class_list:
                    if 200+c > int(i) > 100+c:
                        aa.append(i)
                class_tables(aa)
            except ZeroDivisionError:
                pass

    pdf.save()
    os.startfile(file_name)
    db_pd.close()


def pspk_institutional_report(doc_type,save_directory, institution, main_date, choise, main_list):
    db_pd = mc.engine.connect()
    file_date = datetime.strptime(main_date, '%d-%m-%Y').strftime('%B, %Y')
    file_name = str(save_directory)+"/"+file_date+"_"+str(institution)+"_test_1_Speaking_Institutional_Report.pdf"
    file_name = fnc.check_file_name(file_name)
    pdf = canvas.Canvas(file_name, pagesize = A4)

    sql_select_by_date_and_school = "SELECT * FROM test_1speaking WHERE main_date = '{}' AND school = '{}' ORDER BY student_class, student_lastname, student_name".format(main_date,institution)
    selected_df = pd.read_sql(sql_select_by_date_and_school, con = db_pd)
    if (choise == 2 and doc_type == 0) or (choise == 0 and doc_type == 1):
        main_df = selected_df
    elif choise == 1 and doc_type == 1:
        class_df = pd.DataFrame()
        for student_id in eval(main_list):
            student_id = student_id[8]
            sql_select_by_date_and_school = """SELECT student_class FROM test_1speaking WHERE school = '{}' AND main_date = '{}' AND student_number = '{}'"""
            df = pd.read_sql(sql_select_by_date_and_school.format(institution,main_date,student_id), con = db_pd)
            class_df = pd.concat([df, class_df], ignore_index=True, axis=0)
        selected_class_list = [i[0] for i in class_df.values.tolist()]
        main_df = pd.DataFrame()
        for single_class in selected_class_list:
            df_1 = selected_df.loc[selected_df['student_class'] == single_class]
            main_df = pd.concat([df_1, main_df], ignore_index=True, axis=0)

    name_df = main_df['student_lastname'].str.cat(main_df['student_name'], sep = ' ').str.upper()
    main_df.insert(0, 'full_name', name_df)
    main_df = main_df.drop(columns = ['country', 'provience', 'school', 'form_code', 'main_date', 'test_date', 'student_lastname', 'student_name'])
    main_df['total_score'] = main_df['total_score'].loc[(main_df['total_score'] != "NS")].astype('int64').astype('str')

    if doc_type == 0:
        main_df = main_df.iloc[natsort.index_humansorted(main_df['total_score'],reverse=True)]
    elif doc_type == 1:
        main_df = main_df.sort_values(by = ['student_class', 'full_name'], ascending = [True, True])
    class_list = sorted(list(set(main_df['student_class'].values.tolist())))
    for i in range(len(class_list)):
        class_list[i] = int(scf.student_class_val_reverse(class_list[i]))
    class_list = sorted(class_list)
    main_df = main_df.drop(columns = ['student_number'])
    main_average_df = main_df.loc[(main_df['total_score'].notna())]

    def main_table(first_class):
        #Create average table
        raw_average_table = []
        total_number = 0
        total_include_number = 0
        for single_class in first_class:
            spec_list = main_df.loc[main_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_list = [[x[0]]+x[2:] for x in spec_list]
            for i in spec_list:
                if str(i[-3]) == "nan":
                    i[-3] = ""
            spec_average_list = main_average_df.loc[main_average_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_average_list = [[x[0]]+x[2:] for x in spec_average_list]
            total_number = total_number + len(spec_list)
            total_include_number = total_include_number + len(spec_average_list)
            if spec_average_list != []:
                average_item = spec_average_list
                total_average = round(sum([int(x[1]) for x in average_item])/len(average_item), 2)
                second_data_list = [scf.student_class_val(single_class), str("{:.2f}".format(total_average)),str(len(spec_average_list)), str(len(spec_list))]
                raw_average_table.append(second_data_list)

        school_total_average = round(sum([float(x[1])*int(x[2]) for x in raw_average_table])/sum([int(x[2]) for x in raw_average_table]), 2)
        school_average = ["School", str("{:.2f}".format(school_total_average)),str(total_include_number), str(total_number)]
        average_data = [["Class", "Speaking\nAverage", "Number of Students\nIncluded in Average","Total\nNumber of Students"]]
        average_data.extend(raw_average_table)
        average_data.append(school_average)
        average_table = Table(average_data)
        average_table_style = [
            ('FONTNAME', (0, 0), (-1, 0), 'CalibriB'),
            ('FONTNAME', (0, 1), (-1, -1), 'Calibri'),
            ('FONTSIZE', (0, 0), (-1, 1), 10),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('TOPPADDING', (0, 1), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 2),
            ('RIGHTPADDING', (0, 0), (0, 0), 12),
            ('LEFTPADDING', (0, 0), (0, 0), 12),
            ('RIGHTPADDING', (1, 0), (1, 0), 30),
            ('LEFTPADDING', (1, 0), (1, 0), 30),
            ('RIGHTPADDING', (2, 0), (-1, 0), 5),
            ('LEFTPADDING', (2, 0), (-1, 0), 5),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ]
        average_table.setStyle(color_style_for_table_main('PSPK',average_table_style,average_data[:-1],{'Speaking\nAverage':[school_total_average-pspk_main_diff,school_total_average+pspk_main_diff]},-1,27))
        pdf.drawImage(filigram, 0, 0, width = width, height = height, mask = None)
        pdf.setFillColor(colors.maroon)
        pdf.setFont("CalibriB", 16)
        pdf.drawCentredString(width/2, 740, "Test Type 5 Test Results")
        pdf.setFillColor(colors.navy)
        pdf.setFont("CalibriB", 16)
        pdf.drawCentredString(width/2, 715, institution)
        styling_info_dict = {
                '#3D9970':'{} scale score or higher than the school average.'.format(str(pspk_main_diff)),
                '#E8B425':'Within {} scale score range of the school average.'.format(str(pspk_main_diff)),
                '#FF4136':'{} scale scores below school average.'.format(str(pspk_main_diff))
                }
        counter_1 = 0
        pdf.setLineWidth(0.1)
        for key, val in styling_info_dict.items():
            pdf.setFillColor(colors.HexColor(key))
            pdf.rect(30, 110-counter_1, 17, 8, stroke=1, fill=1)
            pdf.setFillColor(colors.black)
            pdf.setFont("CalibriBI", 8)
            pdf.drawString(52, 110-counter_1+1, val)
            counter_1+=15
        pdf.setFillColor(colors.black)

        class_len = height-160-len(average_data)*15
        average_table.wrapOn(pdf, width, height)
        average_table.drawOn(pdf, 130, class_len)
        #Average table END

        legend_data = [x[0] for x in average_data[1:]]
        legend_data = [legend_data[-1]]+legend_data[:-1]
        chart_data = [x[1:-2] for x in average_data[1:]]
        for i in chart_data:
            for y in range(len(i)):
                i[y] = float(i[y])
        chart_data = [tuple(i) for i in [chart_data[-1]]+chart_data[:-1]]
        max_graph_value = round(max(max(chart_data)))+2

        drawing = Drawing(400, 200)
        if len(chart_data) < 17:
            bc = VerticalBarChart()
            bc.x = 50
            bc.y = 50
            bc.height = 170
            bc.width = 400
            color_list = [colors.mediumaquamarine, colors.darkmagenta, colors.chartreuse, colors.cornflowerblue, colors.plum, colors.rosybrown, colors.salmon, colors.seagreen, colors.tan, colors.steelblue, colors.violet, colors.yellowgreen, colors.lemonchiffon, colors.aqua, colors.blueviolet, colors.coral, colors.skyblue, colors.blanchedalmond, colors.darkgoldenrod]
            for x in range(len(color_list)):
                for i in range(3):
                    bc.bars[(x, i)].fillColor = color_list[x]
            bc.data = chart_data
            bc.strokeColor = colors.black
            bc.strokeWidth = 0.3
            bc.groupSpacing = 30
            bc.barSpacing = 0.5
            bc.valueAxis.valueMin = 0
            bc.valueAxis.valueMax = max_graph_value
            bc.valueAxis.valueStep = 2
            bc.valueAxis.strokeWidth = 0.3
            bc.valueAxis.strokeColor = colors.black
            bc.valueAxis.gridStart = bc.x
            bc.valueAxis.gridEnd = bc.x+bc.width
            bc.valueAxis.gridStrokeWidth = 0.1
            bc.valueAxis.gridStrokeColor = colors.black
            bc.valueAxis.visibleGrid = True
            bc.valueAxis.visibleTicks = False
            bc.valueAxis.labels.fontSize = 10
            bc.valueAxis.labels.fontName = 'Calibri'
            bc.barLabelFormat = '%.2f'
            bc.barLabels.fontSize = 7
            bc.barLabels.fontName = 'Calibri'
            bc.barLabels.dy = -20
            bc.barLabels.dx = -1
            bc.barLabels.angle = 90
            bc.bars.strokeWidth = 0.2
            bc.categoryAxis.labels.boxAnchor = 'ne'
            bc.categoryAxis.labels.dx = 35
            bc.categoryAxis.labels.dy = -10
            bc.categoryAxis.labels.angle = 0
            bc.categoryAxis.labels.fontSize = 12
            bc.categoryAxis.labels.fontName = 'Calibri'
            bc.categoryAxis.categoryNames = ['Speaking Average']
            low_bar_labels = []
            for i in chart_data:
                if sum(i)/len(i) < 2:
                    low_bar_labels.append(i)
            if len(low_bar_labels) > 0:
                bc.barLabels.visible = False
            else:
                bc.barLabels.visible = True
            drawing.add(bc)

            legend = Legend()
            legend.alignment = 'right'
            legend.boxAnchor = 'sw'
            legend.columnMaximum = 1
            legend.colEndCallout = 0
            legend.dx = 15
            legend.dxTextSpace = 4
            legend.dy = 8
            legend.fontName = 'Calibri'
            legend.fontSize = 11
            legend.subCols.minWidth = 25
            legend.strokeWidth = 0.1
            legend.variColumn = 1
            legend.x = 51
            legend.y = -10
            legend.deltay = 10
            legend.colorNamePairs = [(color_list[i], (legend_data[i])) for i in range (len(bc.data[:1]))]
            legend.autoXPadding = 20

            legend1 = Legend()
            legend1.alignment = 'right'
            legend1.boxAnchor = 'sw'
            legend1.columnMaximum = 1
            legend1.colEndCallout = 0
            legend1.dx = 15
            legend1.dxTextSpace = 4
            legend1.dy = 8
            legend1.fontName = 'Calibri'
            legend1.fontSize = 11
            legend1.subCols.minWidth = 25
            legend1.strokeWidth = 0.1
            legend1.variColumn = 1
            legend1.x = 115
            legend1.y = -10
            legend1.deltay = 10
            legend1.colorNamePairs = [(color_list[i+1], (legend_data[i+1])) for i in range (len(bc.data[1:8]))]
            legend1.autoXPadding = 20
            if len(bc.data) > 8:
                legend2 = Legend()
                legend2.alignment = 'right'
                legend2.boxAnchor = 'sw'
                legend2.columnMaximum = 1
                legend2.colEndCallout = 0
                legend2.dx = 15
                legend2.dxTextSpace = 4
                legend2.dy = 8
                legend2.fontName = 'Calibri'
                legend2.fontSize = 11
                legend2.subCols.minWidth = 25
                legend2.strokeWidth = 0.1
                legend2.variColumn = 1
                legend2.x = 51
                legend2.y = -30
                legend2.deltay = 10
                legend2.colorNamePairs = [(color_list[i+8], (legend_data[i+8])) for i in range (len(bc.data[8:]))]
                legend2.autoXPadding = 20
                drawing.add(legend2)
            drawing.add(legend)
            drawing.add(legend1)

        x, y = 47, class_len-250
        renderPDF.draw(drawing, pdf, x, y, showBoundary = False)

        pdf.showPage()
        return school_total_average

    def class_tables(first_class,school_total_average):
        for single_class in first_class:
            pdf.drawImage(filigram, 0, 0, width = width, height = height, mask = None)
            spec_list = main_df.loc[main_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_list = [[x[0]]+[str(x[4])+" Ribbons"]+[x[3]]+[x[2]] for x in spec_list]
            for i in spec_list:
                if str(i[3]) == "nan":
                    i[3] = "NS"
            spec_average_list = main_average_df.loc[main_average_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_average_list = [[x[0]]+[str(x[4])+" Ribbons"]+[x[3]]+[x[2]] for x in spec_average_list]
            ps1data = [["Student Name", "Level", "CEFR", "Total"]]
            ps1data.extend(spec_list)
            ps1data_table = Table(ps1data)
            ps1_style = [
                ('FONTNAME', (0, 0), (-1, 0), 'CalibriB'),
                ('FONTNAME', (0, 1), (-1, -1), 'Calibri'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                ('TOPPADDING', (0, 0), (-1, 0), 6),
                ('BOTTOMPADDING', (0, 1), (-1, -1), 2),
                ('TOPPADDING', (0, 1), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (0, 0), 115),
                ('LEFTPADDING', (0, 0), (0, 0), 115),
                ('RIGHTPADDING', (1, 0), (3, 0), 30),
                ('LEFTPADDING', (1, 0), (3, 0), 30),
                ("VALIGN", (0, 0), (0, 0), "MIDDLE"),
                ("ALIGN", (0, 0), (0, 0), "CENTER"),
                ("VALIGN", (1, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (1, 0), (-1, -1), "CENTER"),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                ]
            
            total_average = round(sum([int(x[3]) for x in spec_average_list])/len(spec_average_list), 2)
            
            ps1data_table.setStyle(color_style_for_table_class('PSPK',ps1_style,ps1data,{'Total':[school_total_average-pspk_class_diff,school_total_average+pspk_class_diff]},-1,27))
            class_len = height-185-len(ps1data)*14
            ps1data_table.wrapOn(pdf, width, height)
            ps1data_table.drawOn(pdf, 30, class_len)
            pdf.setFillColor(colors.maroon)
            pdf.setFont("CalibriB", 16)
            pdf.drawCentredString(width/2, 740, "Test Type 5 Test Results")
            pdf.setFillColor(colors.navy)
            pdf.setFont("CalibriB", 16)
            pdf.drawCentredString(width/2, 715, institution)
            pdf.setFillColor(colors.maroon)
            pdf.setFont("CalibriB", 20)
            pdf.drawCentredString(width/2, 690, scf.student_class_val(single_class))
            pdf.setFillColor(colors.black)
            pdf.setFont("CalibriB", 10)
            pdf.drawString(141, class_len-20, "Total Average : ")
            pdf.drawString(30, class_len-35, "Number of Students Included in Average : ")
            pdf.drawString(91, class_len-50, "Total Number of Students : ")
            pdf.setFont("Calibri", 10)
            pdf.drawString(207, class_len-20, str("{:.2f}".format(total_average)))
            pdf.drawString(207, class_len-35, str(len(spec_average_list)))
            pdf.drawString(207, class_len-50, str(len(spec_list)))
            pdf.setFont("CalibriI", 8)
            pdf.drawCentredString(width/2, 70, "*NS: No Score               *NA: No Answer               *CEFR: Common European Framework Reference")
            styling_info_dict = {
                '#3D9970':'{} scale score or higher than the school average.'.format(str(pspk_class_diff)),
                '#E8B425':'Within {} scale score range of the school average.'.format(str(pspk_class_diff)),
                '#FF4136':'{} scale scores below school average.'.format(str(pspk_class_diff))
                }
            counter_1 = 0
            pdf.setLineWidth(0.1)
            for key, val in styling_info_dict.items():
                pdf.setFillColor(colors.HexColor(key))
                pdf.rect(30, 120-counter_1, 17, 8, stroke=1, fill=1)
                pdf.setFillColor(colors.black)
                pdf.setFont("CalibriBI", 8)
                pdf.drawString(52, 120-counter_1+1, val)
                counter_1+=15

            pdf.showPage()

            if doc_type == 1:
                pdf.drawImage(pspk_info, 0, 0, width = width, height = height, mask = None)
                pdf.showPage()
    test_type_str = "Test Type 5 Test"
    if doc_type == 0:
        first_info(pdf,pspk_info,test_type_str,institution,main_date)
        class_int_list = []
        for c in range(0, 1900, 100):class_int_list.append(c)
        for c in range(10900, 11200, 100):class_int_list.append(c)
        for c in class_int_list:
            try:
                aa = []
                for i in class_list:
                    if 200+c > int(i) > 100+c:
                        aa.append(i)
                school_total_average = main_table(aa)
                class_tables(aa,school_total_average)
            except ZeroDivisionError:
                pass
    elif doc_type == 1:
        class_int_list = []
        for c in range(0, 1900, 100):class_int_list.append(c)
        for c in range(10900, 11200, 100):class_int_list.append(c)
        for c in class_int_list:
            try:
                aa = []
                for i in class_list:
                    if 200+c > int(i) > 100+c:
                        aa.append(i)
                class_tables(aa)
            except ZeroDivisionError:
                pass

    pdf.save()
    os.startfile(file_name)
    db_pd.close()

def js_institutional_report(doc_type,save_directory, institution, main_date, choise, main_list):
    db_pd = mc.engine.connect()
    file_date = datetime.strptime(main_date, '%d-%m-%Y').strftime('%B, %Y')
    file_name = str(save_directory)+"/"+file_date+"_"+str(institution)+"_test_3_Standard_Institutional_Report.pdf"
    file_name = fnc.check_file_name(file_name)
    pdf = canvas.Canvas(file_name, pagesize = A4)

    sql_select_by_date_and_school = "SELECT * FROM test_3_standard WHERE main_date = '{}' AND school = '{}' ORDER BY student_class, student_lastname, student_name".format(main_date,institution)
    selected_df = pd.read_sql(sql_select_by_date_and_school, con = db_pd)
    if (choise == 2 and doc_type == 0) or (choise == 0 and doc_type == 1):
        main_df = selected_df
    elif choise == 1 and doc_type == 1:
        class_df = pd.DataFrame()
        for student_id in eval(main_list):
            student_id = student_id[8]
            sql_select_by_date_and_school = """SELECT student_class FROM test_3_standard WHERE school = '{}' AND main_date = '{}' AND student_number = '{}'"""
            df = pd.read_sql(sql_select_by_date_and_school.format(institution,main_date,student_id), con = db_pd)
            class_df = pd.concat([df, class_df], ignore_index=True, axis=0)
        selected_class_list = [i[0] for i in class_df.values.tolist()]
        main_df = pd.DataFrame()
        for single_class in selected_class_list:
            df_1 = selected_df.loc[selected_df['student_class'] == single_class]
            main_df = pd.concat([df_1, main_df], ignore_index=True, axis=0)

    name_df = main_df['student_lastname'].str.cat(main_df['student_name'], sep = ' ').str.upper()
    main_df = main_df.drop(columns = ['country', 'provience', 'school', 'form_code', 'main_date', 'test_date', 'student_lastname', 'student_name'])
    main_df.insert(0, 'full_name', name_df)
    if doc_type == 0:
        main_df = main_df.sort_values(by = ['student_class', 'total_score'], ascending = [True, False])
    elif doc_type == 1:
        main_df = main_df.sort_values(by = ['student_class', 'full_name'], ascending = [True, True])
    class_list = sorted(list(set(main_df['student_class'].values.tolist())))
    for i in range(len(class_list)):
        class_list[i] = int(scf.student_class_val_reverse(class_list[i]))
    class_list = sorted(class_list)
    main_df = main_df.drop(columns = ['student_number'])
    main_average_df = main_df.loc[(main_df['listening_score'] != "NS") & (main_df['lfm_score'] != "NS") & (main_df['reading_score'] != "NS")]

    def main_table(first_class):
        #Create average table
        raw_average_table = []
        total_number = 0
        total_include_number = 0
        for single_class in first_class:
            spec_list = main_df.loc[main_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_list = [[x[0]]+x[2:] for x in spec_list]
            spec_average_list = main_average_df.loc[main_average_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_average_list = [[x[0]]+x[2:] for x in spec_average_list]
            total_number = total_number + len(spec_list)
            total_include_number = total_include_number + len(spec_average_list)
            if spec_average_list != []:
                average_item = spec_average_list
                listening_average = round(sum([int(x[1]) for x in average_item])/len(average_item), 2)
                lfm_average = round(sum([int(x[3]) for x in average_item])/len(average_item), 2)
                reading_average = round(sum([int(x[5]) for x in average_item])/len(average_item), 2)
                total_average = round(sum([int(x[8]) for x in average_item])/len(average_item), 2)
                second_data_list = [scf.student_class_val(single_class), str("{:.2f}".format(listening_average)), str("{:.2f}".format(lfm_average)), str("{:.2f}".format(reading_average)), str("{:.2f}".format(total_average)), str(len(spec_average_list)), str(len(spec_list))]
                raw_average_table.append(second_data_list)
        school_listening_average = round(sum([float(x[1])*int(x[5]) for x in raw_average_table])/sum([int(x[5]) for x in raw_average_table]), 2)
        school_lfm_average = round(sum([float(x[2])*int(x[5]) for x in raw_average_table])/sum([int(x[5]) for x in raw_average_table]), 2)
        school_reading_average = round(sum([float(x[3])*int(x[5]) for x in raw_average_table])/sum([int(x[5]) for x in raw_average_table]), 2)
        school_total_average = round(sum([float(x[4])*int(x[5]) for x in raw_average_table])/sum([int(x[5]) for x in raw_average_table]), 2)
        school_average = ["School", str("{:.2f}".format(school_listening_average)), str("{:.2f}".format(school_lfm_average)), str("{:.2f}".format(school_reading_average)), str("{:.2f}".format(school_total_average)), str(total_include_number), str(total_number)]
        average_data = [["Class", "Listening\nAverage", "LFM\nAverage", "Reading\nAverage", "Total\nAverage", "Number of Students\nIncluded in Average","Total\nNumber of Students"]]
        average_data.extend(raw_average_table)
        average_data.append(school_average)

        average_table = Table(average_data)
        average_table_style = [
            ('FONTNAME', (0, 0), (-1, 0), 'CalibriB'),
            ('FONTNAME', (0, 1), (-1, -1), 'Calibri'),
            ('FONTSIZE', (0, 0), (-1, 1), 10),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('TOPPADDING', (0, 1), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 2),
            ('RIGHTPADDING', (0, 0), (0, 0), 12),
            ('LEFTPADDING', (0, 0), (0, 0), 12),
            ('RIGHTPADDING', (1, 0), (4, 0), 18),
            ('LEFTPADDING', (1, 0), (4, 0), 18),
            ('RIGHTPADDING', (5, 0), (6, 0), 3),
            ('LEFTPADDING', (5, 0), (6, 0), 3),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ]
        average_table.setStyle(color_style_for_table_main("JS",average_table_style,average_data[:-1],{'Reading\nAverage':[school_reading_average-js_main_diff,school_reading_average+js_main_diff],'LFM\nAverage':[school_lfm_average-js_main_diff,school_lfm_average+js_main_diff],'Listening\nAverage':[school_listening_average-js_main_diff,school_listening_average+js_main_diff]},195,300))
        pdf.drawImage(filigram, 0, 0, width = width, height = height, mask = None)
        pdf.setFillColor(colors.maroon)
        pdf.setFont("CalibriB", 16)
        pdf.drawCentredString(width/2, 740, "Test Type 3 Test Results")
        pdf.setFillColor(colors.navy)
        pdf.setFont("CalibriB", 16)
        pdf.drawCentredString(width/2, 715, institution)
        styling_info_dict = {
                '#8AC7DB':'{} scale score difference between listening, language form and meaning or reading.'.format(str(js_b_main_diff)),
                '#3D9970':'{} scale score or higher than the school average.'.format(str(js_main_diff)),
                '#E8B425':'Within {} scale score range of the school average.'.format(str(js_main_diff)),
                '#FF4136':'{} scale scores below school average.'.format(str(js_main_diff))
                }
        counter_1 = 0
        pdf.setLineWidth(0.1)
        for key, val in styling_info_dict.items():
            pdf.setFillColor(colors.HexColor(key))
            pdf.rect(30, 125-counter_1, 17, 8, stroke=1, fill=1)
            pdf.setFillColor(colors.black)
            pdf.setFont("CalibriBI", 8)
            pdf.drawString(52, 125-counter_1+1, val)
            counter_1+=15
        pdf.setFillColor(colors.black)

        class_len = height-165-len(average_data)*15
        average_table.wrapOn(pdf, width, height)
        average_table.drawOn(pdf, 40, class_len)
        #Average table END

        legend_data = [x[0] for x in average_data[1:]]
        legend_data = [legend_data[-1]]+legend_data[:-1]
        chart_data = [x[1:-3] for x in average_data[1:]]
        for i in chart_data:
            for y in range(len(i)):
                i[y] = float(i[y])
        chart_data = [tuple(i) for i in [chart_data[-1]]+chart_data[:-1]]
        max_graph_value = round(max(max(chart_data)))+7

        drawing = Drawing(400, 200)
        if len(chart_data) < 17:
            bc = VerticalBarChart()
            bc.x = 50
            bc.y = 50
            bc.height = 170
            bc.width = 485
            color_list = [colors.mediumaquamarine, colors.darkmagenta, colors.chartreuse, colors.cornflowerblue, colors.plum, colors.rosybrown, colors.salmon, colors.seagreen, colors.tan, colors.steelblue, colors.violet, colors.yellowgreen, colors.lemonchiffon, colors.aqua, colors.blueviolet, colors.coral, colors.skyblue, colors.blanchedalmond, colors.darkgoldenrod]
            for x in range(len(color_list)):
                for i in range(3):
                    bc.bars[(x, i)].fillColor = color_list[x]
            bc.data = chart_data
            bc.strokeColor = colors.black
            bc.strokeWidth = 0.3
            bc.groupSpacing = 30
            bc.barSpacing = 0.5
            bc.valueAxis.valueMin = 200
            bc.valueAxis.valueMax = max_graph_value
            bc.valueAxis.valueStep = 10
            bc.valueAxis.strokeWidth = 0.3
            bc.valueAxis.strokeColor = colors.black
            bc.valueAxis.gridStart = bc.x
            bc.valueAxis.gridEnd = bc.x+bc.width
            bc.valueAxis.gridStrokeWidth = 0.1
            bc.valueAxis.gridStrokeColor = colors.black
            bc.valueAxis.visibleGrid = True
            bc.valueAxis.visibleTicks = False
            bc.valueAxis.labels.fontSize = 10
            bc.valueAxis.labels.fontName = 'Calibri'
            bc.barLabelFormat = '%.2f'
            bc.barLabels.fontSize = 7
            bc.barLabels.fontName = 'Calibri'
            bc.barLabels.dy = -20
            bc.barLabels.dx = -1
            bc.barLabels.angle = 90
            bc.bars.strokeWidth = 0.2
            bc.categoryAxis.labels.boxAnchor = 'ne'
            bc.categoryAxis.labels.dx = 35
            bc.categoryAxis.labels.dy = -10
            bc.categoryAxis.labels.angle = 0
            bc.categoryAxis.labels.fontSize = 12
            bc.categoryAxis.labels.fontName = 'Calibri'
            bc.categoryAxis.categoryNames = ['Listening Average', 'LFM Average', 'Reading Average']
            low_bar_labels = []
            for i in chart_data:
                if sum(i)/len(i) < 206:
                    low_bar_labels.append(i)
            if len(low_bar_labels) > 0:
                bc.barLabels.visible = False
            else:
                bc.barLabels.visible = True
            drawing.add(bc)

            legend = Legend()
            legend.alignment = 'right'
            legend.boxAnchor = 'sw'
            legend.columnMaximum = 1
            legend.colEndCallout = 0
            legend.dx = 15
            legend.dxTextSpace = 4
            legend.dy = 8
            legend.fontName = 'Calibri'
            legend.fontSize = 11
            legend.subCols.minWidth = 25
            legend.strokeWidth = 0.1
            legend.variColumn = 1
            legend.x = 51
            legend.y = -10
            legend.deltay = 10
            legend.colorNamePairs = [(color_list[i], (legend_data[i])) for i in range (len(bc.data[:1]))]
            legend.autoXPadding = 20

            legend1 = Legend()
            legend1.alignment = 'right'
            legend1.boxAnchor = 'sw'
            legend1.columnMaximum = 1
            legend1.colEndCallout = 0
            legend1.dx = 15
            legend1.dxTextSpace = 4
            legend1.dy = 8
            legend1.fontName = 'Calibri'
            legend1.fontSize = 11
            legend1.subCols.minWidth = 25
            legend1.strokeWidth = 0.1
            legend1.variColumn = 1
            legend1.x = 115
            legend1.y = -10
            legend1.deltay = 10
            legend1.colorNamePairs = [(color_list[i+1], (legend_data[i+1])) for i in range (len(bc.data[1:8]))]
            legend1.autoXPadding = 20
            if len(bc.data) > 8:
                legend2 = Legend()
                legend2.alignment = 'right'
                legend2.boxAnchor = 'sw'
                legend2.columnMaximum = 1
                legend2.colEndCallout = 0
                legend2.dx = 15
                legend2.dxTextSpace = 4
                legend2.dy = 8
                legend2.fontName = 'Calibri'
                legend2.fontSize = 11
                legend2.subCols.minWidth = 25
                legend2.strokeWidth = 0.1
                legend2.variColumn = 1
                legend2.x = 51
                legend2.y = -30
                legend2.deltay = 10
                legend2.colorNamePairs = [(color_list[i+8], (legend_data[i+8])) for i in range (len(bc.data[8:]))]
                legend2.autoXPadding = 20
                drawing.add(legend2)
            drawing.add(legend)
            drawing.add(legend1)
        x, y = 10, class_len-250
        renderPDF.draw(drawing, pdf, x, y, showBoundary = False)

        pdf.showPage()
        return school_listening_average,school_lfm_average,school_reading_average

    def class_tables(first_class,school_listening_average,school_lfm_average,school_reading_average):
        for single_class in first_class:
            pdf.drawImage(filigram, 0, 0, width = width, height = height, mask = None)
            spec_list = main_df.loc[main_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_list = [[x[0]]+x[2:9]+[x[-1]]+[x[9]] for x in spec_list]
            spec_average_list = main_average_df.loc[main_average_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_average_list = [[x[0]]+x[2:9]+[x[-1]]+[x[9]] for x in spec_average_list]
            ps1data = [["Student Name", "Listening Section", "", "LFM Section", "", "Reading Section", "", "", "OSL", "Total"],
                    ["", "Score", "CEFR", "Score", "CEFR", "Score", "CEFR", "LXL", "", ""]]

            ps1data.extend(spec_list)
            ps1data_table = Table(ps1data)
            ps1_style = [
                ('FONTNAME', (0, 0), (-1, 1), 'CalibriB'),
                ('FONTNAME', (0, 2), (-1, -1), 'Calibri'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 1), 3),
                ('BOTTOMPADDING', (0, 2), (-1, -1), 2),
                ('TOPPADDING', (0, 2), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (0, 1), 50),
                ('LEFTPADDING', (0, 0), (0, 1), 50),
                ('RIGHTPADDING', (1, 1), (1, 1), 3),
                ('LEFTPADDING', (1, 1), (1, 1), 3),
                ('RIGHTPADDING', (3, 1), (3, 1), 3),
                ('LEFTPADDING', (3, 1), (3, 1), 3),
                ('RIGHTPADDING', (5, 1), (5, 1), 3),
                ('LEFTPADDING', (5, 1), (5, 1), 3),
                ('RIGHTPADDING', (8, 1), (-1, 1), 3),
                ('LEFTPADDING', (8, 1), (-1, 1), 3),
                ('RIGHTPADDING', (2, 1), (2, 1), 19),
                ('LEFTPADDING', (2, 1), (2, 1), 19),
                ('RIGHTPADDING', (4, 1), (4, 1), 19),
                ('LEFTPADDING', (4, 1), (4, 1), 19),
                ('RIGHTPADDING', (6, 1), (6, 1), 19),
                ('LEFTPADDING', (6, 1), (6, 1), 19),
                ('RIGHTPADDING', (7, 1), (7, 1), 19),
                ('LEFTPADDING', (7, 1), (7, 1), 19),
                ("VALIGN", (0, 0), (0, 1), "MIDDLE"),
                ("ALIGN", (0, 0), (0, 1), "CENTER"),
                ("VALIGN", (1, 1), (-1, 1), "MIDDLE"),
                ("ALIGN", (1, 1), (-1, 1), "CENTER"),
                ("VALIGN", (1, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (1, 0), (-1, -1), "CENTER"),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                ('SPAN', (0, 0), (0, 1)),
                ('SPAN', (1, 0), (2, 0)),
                ('SPAN', (3, 0), (4, 0)),
                ('SPAN', (5, 0), (7, 0)),
                ('SPAN', (8, 0), (8, 1)),
                ('SPAN', (9, 0), (9, 1)),
                ]
            listening_average = round(sum([int(x[1]) for x in spec_average_list])/len(spec_average_list), 2)
            lfm_average = round(sum([int(x[3]) for x in spec_average_list])/len(spec_average_list), 2)
            reading_average = round(sum([int(x[5]) for x in spec_average_list])/len(spec_average_list), 2)
            total_average = round(sum([int(x[9]) for x in spec_average_list])/len(spec_average_list), 2)
            
            ps1data_table.setStyle(color_style_for_table_class('JS',ps1_style,ps1data,{'Listening Section':[school_listening_average-js_class_diff,school_listening_average+js_class_diff],'LFM Section':[school_lfm_average-js_class_diff,school_lfm_average+js_class_diff],'Reading Section':[school_reading_average-js_class_diff,school_reading_average+js_class_diff]},195,300))
            class_len = height-185-len(ps1data)*14
            ps1data_table.wrapOn(pdf, width, height)
            ps1data_table.drawOn(pdf, 30, class_len)
            pdf.setFillColor(colors.maroon)
            pdf.setFont("CalibriB", 16)
            pdf.drawCentredString(width/2, 740, "Test Type 3 Test Results")
            pdf.setFillColor(colors.navy)
            pdf.setFont("CalibriB", 16)
            pdf.drawCentredString(width/2, 715, institution)
            pdf.setFillColor(colors.maroon)
            pdf.setFont("CalibriB", 20)
            pdf.drawCentredString(width/2, 690, scf.student_class_val(single_class))
            pdf.setFillColor(colors.black)
            pdf.setFont("CalibriB", 10)
            pdf.drawString(125, class_len-20, "Listening Average : ")
            pdf.drawString(144.5, class_len-35, "LFM Average : ")
            pdf.drawString(129, class_len-50, "Reading Average : ")
            pdf.drawString(141, class_len-65, "Total Average : ")
            pdf.drawString(30, class_len-80, "Number of Students Included in Average : ")
            pdf.drawString(91, class_len-95, "Total Number of Students : ")
            pdf.setFont("Calibri", 10)
            pdf.drawString(207, class_len-20, str("{:.2f}".format(listening_average)))
            pdf.drawString(207, class_len-35, str("{:.2f}".format(lfm_average)))
            pdf.drawString(207, class_len-50, str("{:.2f}".format(reading_average)))
            pdf.drawString(207, class_len-65, str("{:.2f}".format(total_average)))
            pdf.drawString(207, class_len-80, str(len(spec_average_list)))
            pdf.drawString(207, class_len-95, str(len(spec_list)))
            pdf.setFont("CalibriI", 8)
            pdf.drawCentredString(width/2, 70, "*NS: No Score       *NA: No Answer       *CEFR: Common European Framework Reference       *LXL: The Lexile Framework for Reading       *LFM: Language Form and Meaning")
            styling_info_dict = {
                '#8AC7DB':'{} scale score difference between listening, language form and meaning or reading.'.format(str(js_b_class_diff)),
                '#3D9970':'{} scale score or higher than the school average.'.format(str(js_class_diff)),
                '#E8B425':'Within {} scale score range of the school average.'.format(str(js_class_diff)),
                '#FF4136':'{} scale scores below school average.'.format(str(js_class_diff))
                }
            counter_1 = 0
            pdf.setLineWidth(0.1)
            for key, val in styling_info_dict.items():
                pdf.setFillColor(colors.HexColor(key))
                pdf.rect(30, 135-counter_1, 17, 8, stroke=1, fill=1)
                pdf.setFillColor(colors.black)
                pdf.setFont("CalibriBI", 8)
                pdf.drawString(52, 135-counter_1+1, val)
                counter_1+=15

            pdf.showPage()
            if doc_type == 1:
                pdf.drawImage(js_info, 0, 0, width = width, height = height, mask = None)
                pdf.showPage()
    test_type_str = "Test Type 3 Test"
    if doc_type == 0:
        first_info(pdf,js_info,test_type_str,institution,main_date)
        class_int_list = []
        for c in range(0, 1900, 100):class_int_list.append(c)
        for c in range(10900, 11200, 100):class_int_list.append(c)
        for c in class_int_list:
            try:
                aa = []
                for i in class_list:
                    if 200+c > int(i) > 100+c:
                        aa.append(i)
                school_listening_average,school_lfm_average,school_reading_average = main_table(aa)
                class_tables(aa,school_listening_average,school_lfm_average,school_reading_average)
            except ZeroDivisionError:
                pass

    elif doc_type == 1:
        class_int_list = []
        for c in range(0, 1900, 100):class_int_list.append(c)
        for c in range(10900, 11200, 100):class_int_list.append(c)
        for c in class_int_list:
            try:
                aa = []
                for i in class_list:
                    if 200+c > int(i) > 100+c:
                        aa.append(i)
                class_tables(aa)
            except ZeroDivisionError:
                pass

    pdf.save()
    os.startfile(file_name)
    db_pd.close()

def jspk_institutional_report(doc_type,save_directory, institution, main_date, choise, main_list):
    db_pd = mc.engine.connect()
    file_date = datetime.strptime(main_date, '%d-%m-%Y').strftime('%B, %Y')
    file_name = str(save_directory)+"/"+file_date+"_"+str(institution)+"_test_3_Speaking_Institutional_Report.pdf"
    file_name = fnc.check_file_name(file_name)
    pdf = canvas.Canvas(file_name, pagesize = A4)

    sql_select_by_date_and_school = "SELECT * FROM test_3_speaking WHERE main_date = '{}' AND school = '{}' ORDER BY student_class, student_lastname, student_name".format(main_date,institution)
    selected_df = pd.read_sql(sql_select_by_date_and_school, con = db_pd)
    if (choise == 2 and doc_type == 0) or (choise == 0 and doc_type == 1):
        main_df = selected_df
    elif choise == 1 and doc_type == 1:
        class_df = pd.DataFrame()
        for student_id in eval(main_list):
            student_id = student_id[8]
            sql_select_by_date_and_school = """SELECT student_class FROM test_3_speaking WHERE school = '{}' AND main_date = '{}' AND student_number = '{}'"""
            df = pd.read_sql(sql_select_by_date_and_school.format(institution,main_date,student_id), con = db_pd)
            class_df = pd.concat([df, class_df], ignore_index=True, axis=0)
        selected_class_list = [i[0] for i in class_df.values.tolist()]
        main_df = pd.DataFrame()
        for single_class in selected_class_list:
            df_1 = selected_df.loc[selected_df['student_class'] == single_class]
            main_df = pd.concat([df_1, main_df], ignore_index=True, axis=0)
    name_df = main_df['student_lastname'].str.cat(main_df['student_name'], sep = ' ').str.upper()
    main_df.insert(0, 'full_name', name_df)
    main_df = main_df.drop(columns = ['country', 'provience', 'school', 'form_code', 'main_date', 'test_date', 'student_lastname', 'student_name'])
    main_df['total_score'] = main_df['total_score'].loc[(main_df['total_score'] != "NS")].astype('int64').astype('str')
    if doc_type == 0:
        main_df = main_df.iloc[natsort.index_humansorted(main_df['total_score'],reverse=True)]
    elif doc_type == 1:
        main_df = main_df.sort_values(by = ['student_class', 'full_name'], ascending = [True, True])
    class_list = sorted(list(set(main_df['student_class'].values.tolist())))
    for i in range(len(class_list)):
        class_list[i] = int(scf.student_class_val_reverse(class_list[i]))
    class_list = sorted(class_list)
    main_df = main_df.drop(columns = ['student_number'])
    main_average_df = main_df.loc[(main_df['total_score'].notna())]

    def main_table(first_class):
        #Create average table
        raw_average_table = []
        total_number = 0
        total_include_number = 0
        for single_class in first_class:
            spec_list = main_df.loc[main_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_list = [[x[0]]+x[2:] for x in spec_list]
            spec_average_list = main_average_df.loc[main_average_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_average_list = [[x[0]]+x[2:] for x in spec_average_list]
            total_number = total_number + len(spec_list)
            total_include_number = total_include_number + len(spec_average_list)
            if spec_average_list != []:
                average_item = spec_average_list
                total_average = round(sum([int(x[1]) for x in average_item])/len(average_item), 2)
                second_data_list = [scf.student_class_val(single_class), str("{:.2f}".format(total_average)),str(len(spec_average_list)), str(len(spec_list))]
                raw_average_table.append(second_data_list)
        school_total_average = round(sum([float(x[1])*int(x[2]) for x in raw_average_table])/sum([int(x[2]) for x in raw_average_table]), 2)
        school_average = ["School", str("{:.2f}".format(school_total_average)),str(total_include_number), str(total_number)]
        average_data = [["Class", "Speaking\nAverage", "Number of Students\nIncluded in Average","Total\nNumber of Students"]]
        average_data.extend(raw_average_table)
        average_data.append(school_average)
        average_table = Table(average_data)
        average_table_style = [
            ('FONTNAME', (0, 0), (-1, 0), 'CalibriB'),
            ('FONTNAME', (0, 1), (-1, -1), 'Calibri'),
            ('FONTSIZE', (0, 0), (-1, 1), 10),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('TOPPADDING', (0, 1), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 2),
            ('RIGHTPADDING', (0, 0), (0, 0), 12),
            ('LEFTPADDING', (0, 0), (0, 0), 12),
            ('RIGHTPADDING', (1, 0), (1, 0), 30),
            ('LEFTPADDING', (1, 0), (1, 0), 30),
            ('RIGHTPADDING', (2, 0), (-1, 0), 5),
            ('LEFTPADDING', (2, 0), (-1, 0), 5),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
            ]
        average_table.setStyle(color_style_for_table_main('JSPK',average_table_style,average_data[:-1],{'Speaking\nAverage':[school_total_average-jspk_main_diff,school_total_average+jspk_main_diff]},-1,16))
        pdf.drawImage(filigram, 0, 0, width = width, height = height, mask = None)
        pdf.setFillColor(colors.maroon)
        pdf.setFont("CalibriB", 16)
        pdf.drawCentredString(width/2, 740, "Test Type 6 Test Results")
        pdf.setFillColor(colors.navy)
        pdf.setFont("CalibriB", 16)
        pdf.drawCentredString(width/2, 715, institution)
        styling_info_dict = {
                '#3D9970':'{} scale score or higher than the school average.'.format(str(jspk_main_diff)),
                '#E8B425':'Within {} scale score range of the school average.'.format(str(jspk_main_diff)),
                '#FF4136':'{} scale scores below school average.'.format(str(jspk_main_diff))
                }
        counter_1 = 0
        pdf.setLineWidth(0.1)
        for key, val in styling_info_dict.items():
            pdf.setFillColor(colors.HexColor(key))
            pdf.rect(30, 110-counter_1, 17, 8, stroke=1, fill=1)
            pdf.setFillColor(colors.black)
            pdf.setFont("CalibriBI", 8)
            pdf.drawString(52, 110-counter_1+1, val)
            counter_1+=15
        pdf.setFillColor(colors.black)

        class_len = height-160-len(average_data)*15
        average_table.wrapOn(pdf, width, height)
        average_table.drawOn(pdf, 130, class_len)
        #Average table END

        legend_data = [x[0] for x in average_data[1:]]
        legend_data = [legend_data[-1]]+legend_data[:-1]
        chart_data = [x[1:-2] for x in average_data[1:]]
        for i in chart_data:
            for y in range(len(i)):
                i[y] = float(i[y])
        chart_data = [tuple(i) for i in [chart_data[-1]]+chart_data[:-1]]
        max_graph_value = round(max(max(chart_data)))+2

        drawing = Drawing(400, 200)
        if len(chart_data) < 17:
            bc = VerticalBarChart()
            bc.x = 50
            bc.y = 50
            bc.height = 170
            bc.width = 400
            color_list = [colors.mediumaquamarine, colors.darkmagenta, colors.chartreuse, colors.cornflowerblue, colors.plum, colors.rosybrown, colors.salmon, colors.seagreen, colors.tan, colors.steelblue, colors.violet, colors.yellowgreen, colors.lemonchiffon, colors.aqua, colors.blueviolet, colors.coral, colors.skyblue, colors.blanchedalmond, colors.darkgoldenrod]
            for x in range(len(color_list)):
                for i in range(3):
                    bc.bars[(x, i)].fillColor = color_list[x]
            bc.data = chart_data
            bc.strokeColor = colors.black
            bc.strokeWidth = 0.3
            bc.groupSpacing = 30
            bc.barSpacing = 0.5
            bc.valueAxis.valueMin = 0
            bc.valueAxis.valueMax = max_graph_value
            bc.valueAxis.valueStep = 2
            bc.valueAxis.strokeWidth = 0.3
            bc.valueAxis.strokeColor = colors.black
            bc.valueAxis.gridStart = bc.x
            bc.valueAxis.gridEnd = bc.x+bc.width
            bc.valueAxis.gridStrokeWidth = 0.1
            bc.valueAxis.gridStrokeColor = colors.black
            bc.valueAxis.visibleGrid = True
            bc.valueAxis.visibleTicks = False
            bc.valueAxis.labels.fontSize = 10
            bc.valueAxis.labels.fontName = 'Calibri'
            bc.barLabelFormat = '%.2f'
            bc.barLabels.fontSize = 7
            bc.barLabels.fontName = 'Calibri'
            bc.barLabels.dy = -20
            bc.barLabels.dx = -1
            bc.barLabels.angle = 90
            bc.bars.strokeWidth = 0.2
            bc.categoryAxis.labels.boxAnchor = 'ne'
            bc.categoryAxis.labels.dx = 35
            bc.categoryAxis.labels.dy = -10
            bc.categoryAxis.labels.angle = 0
            bc.categoryAxis.labels.fontSize = 12
            bc.categoryAxis.labels.fontName = 'Calibri'
            bc.categoryAxis.categoryNames = ['Speaking Average']
            low_bar_labels = []
            for i in chart_data:
                if sum(i)/len(i) < 2:
                    low_bar_labels.append(i)
            if len(low_bar_labels) > 0:
                bc.barLabels.visible = False
            else:
                bc.barLabels.visible = True
            drawing.add(bc)

            legend = Legend()
            legend.alignment = 'right'
            legend.boxAnchor = 'sw'
            legend.columnMaximum = 1
            legend.colEndCallout = 0
            legend.dx = 15
            legend.dxTextSpace = 4
            legend.dy = 8
            legend.fontName = 'Calibri'
            legend.fontSize = 11
            legend.subCols.minWidth = 25
            legend.strokeWidth = 0.1
            legend.variColumn = 1
            legend.x = 51
            legend.y = -10
            legend.deltay = 10
            legend.colorNamePairs = [(color_list[i], (legend_data[i])) for i in range (len(bc.data[:1]))]
            legend.autoXPadding = 20

            legend1 = Legend()
            legend1.alignment = 'right'
            legend1.boxAnchor = 'sw'
            legend1.columnMaximum = 1
            legend1.colEndCallout = 0
            legend1.dx = 15
            legend1.dxTextSpace = 4
            legend1.dy = 8
            legend1.fontName = 'Calibri'
            legend1.fontSize = 11
            legend1.subCols.minWidth = 25
            legend1.strokeWidth = 0.1
            legend1.variColumn = 1
            legend1.x = 115
            legend1.y = -10
            legend1.deltay = 10
            legend1.colorNamePairs = [(color_list[i+1], (legend_data[i+1])) for i in range (len(bc.data[1:8]))]
            legend1.autoXPadding = 20
            if len(bc.data) > 8:
                legend2 = Legend()
                legend2.alignment = 'right'
                legend2.boxAnchor = 'sw'
                legend2.columnMaximum = 1
                legend2.colEndCallout = 0
                legend2.dx = 15
                legend2.dxTextSpace = 4
                legend2.dy = 8
                legend2.fontName = 'Calibri'
                legend2.fontSize = 11
                legend2.subCols.minWidth = 25
                legend2.strokeWidth = 0.1
                legend2.variColumn = 1
                legend2.x = 51
                legend2.y = -30
                legend2.deltay = 10
                legend2.colorNamePairs = [(color_list[i+8], (legend_data[i+8])) for i in range (len(bc.data[8:]))]
                legend2.autoXPadding = 20
                drawing.add(legend2)
            drawing.add(legend)
            drawing.add(legend1)

        x, y = 47, class_len-250
        renderPDF.draw(drawing, pdf, x, y, showBoundary = False)

        pdf.showPage()
        return school_total_average

    def class_tables(first_class,school_total_average):
        for single_class in first_class:
            pdf.drawImage(filigram, 0, 0, width = width, height = height, mask = None)
            spec_list = main_df.loc[main_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_list = [[x[0]]+[str(x[4])]+[x[3]]+[x[2]] for x in spec_list]
            for i in spec_list:
                if str(i[-1]) == "nan":
                    i[-1] = "NS"
            spec_average_list = main_average_df.loc[main_average_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_average_list = [[x[0]]+[str(x[4])]+[x[3]]+[x[2]] for x in spec_average_list]
            ps1data = [["Student Name", "Level", "CEFR", "Total"]]
            ps1data.extend(spec_list)
            ps1data_table = Table(ps1data)
            ps1_style = [
                ('FONTNAME', (0, 0), (-1, 0), 'CalibriB'),
                ('FONTNAME', (0, 1), (-1, -1), 'Calibri'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                ('TOPPADDING', (0, 0), (-1, 0), 6),
                ('BOTTOMPADDING', (0, 1), (-1, -1), 2),
                ('TOPPADDING', (0, 1), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (0, 0), 115),
                ('LEFTPADDING', (0, 0), (0, 0), 115),
                ('RIGHTPADDING', (1, 0), (3, 0), 30),
                ('LEFTPADDING', (1, 0), (3, 0), 30),
                ("VALIGN", (0, 0), (0, 0), "MIDDLE"),
                ("ALIGN", (0, 0), (0, 0), "CENTER"),
                ("VALIGN", (1, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (1, 0), (-1, -1), "CENTER"),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                ]
            total_average = round(sum([int(x[3]) for x in spec_average_list])/len(spec_average_list), 2)
            
            ps1data_table.setStyle(color_style_for_table_class('JSPK',ps1_style,ps1data,{'Total':[school_total_average-jspk_class_diff,school_total_average+jspk_class_diff]},-1,16))
            class_len = height-185-len(ps1data)*14
            ps1data_table.wrapOn(pdf, width, height)
            ps1data_table.drawOn(pdf, 30, class_len)
            pdf.setFillColor(colors.maroon)
            pdf.setFont("CalibriB", 16)
            pdf.drawCentredString(width/2, 740, "Test Type 6 Test Results")
            pdf.setFillColor(colors.navy)
            pdf.setFont("CalibriB", 16)
            pdf.drawCentredString(width/2, 715, institution)
            pdf.setFillColor(colors.maroon)
            pdf.setFont("CalibriB", 20)
            pdf.drawCentredString(width/2, 690, scf.student_class_val(single_class))
            pdf.setFillColor(colors.black)
            pdf.setFont("CalibriB", 10)
            pdf.drawString(141, class_len-20, "Total Average : ")
            pdf.drawString(30, class_len-35, "Number of Students Included in Average : ")
            pdf.drawString(91, class_len-50, "Total Number of Students : ")
            pdf.setFont("Calibri", 10)
            pdf.drawString(207, class_len-20, str("{:.2f}".format(total_average)))
            pdf.drawString(207, class_len-35, str(len(spec_average_list)))
            pdf.drawString(207, class_len-50, str(len(spec_list)))
            pdf.setFont("CalibriI", 8)
            pdf.drawCentredString(width/2, 70, "*NS: No Score               *NA: No Answer               *CEFR: Common European Framework Reference")
            styling_info_dict = {
                '#3D9970':'{} scale score or higher than the school average.'.format(str(jspk_class_diff)),
                '#E8B425':'Within {} scale score range of the school average.'.format(str(jspk_class_diff)),
                '#FF4136':'{} scale scores below school average.'.format(str(jspk_class_diff))
                }
            counter_1 = 0
            pdf.setLineWidth(0.1)
            for key, val in styling_info_dict.items():
                pdf.setFillColor(colors.HexColor(key))
                pdf.rect(30, 120-counter_1, 17, 8, stroke=1, fill=1)
                pdf.setFillColor(colors.black)
                pdf.setFont("CalibriBI", 8)
                pdf.drawString(52, 120-counter_1+1, val)
                counter_1+=15

            pdf.showPage()

            if doc_type == 1:
                pdf.drawImage(jspk_info, 0, 0, width = width, height = height, mask = None)
                pdf.showPage()

    test_type_str = "Test Type 6 Test"
    if doc_type == 0:
        first_info(pdf,jspk_info,test_type_str,institution,main_date)
        class_int_list = []
        for c in range(0, 1900, 100):class_int_list.append(c)
        for c in range(10900, 11200, 100):class_int_list.append(c)
        for c in class_int_list:
            try:
                aa = []
                for i in class_list:
                    if 200+c > int(i) > 100+c:
                        aa.append(i)
                school_total_average = main_table(aa)
                class_tables(aa,school_total_average)
            except ZeroDivisionError:
                pass
    elif doc_type == 1:
        class_int_list = []
        for c in range(0, 1900, 100):class_int_list.append(c)
        for c in range(10900, 11200, 100):class_int_list.append(c)
        for c in class_int_list:
            try:
                aa = []
                for i in class_list:
                    if 200+c > int(i) > 100+c:
                        aa.append(i)
                class_tables(aa)
            except ZeroDivisionError:
                pass

    pdf.save()
    os.startfile(file_name)
    db_pd.close()


def test_4_institutional_report(doc_type,save_directory, institution, main_date, choise, main_list):
    db_pd = mc.engine.connect()
    file_date = datetime.strptime(main_date, '%d-%m-%Y').strftime('%B, %Y')
    file_name = str(save_directory)+"/"+file_date+"_"+str(institution)+"_test_4_Institutional_Report.pdf"
    file_name = fnc.check_file_name(file_name)
    pdf = canvas.Canvas(file_name, pagesize = A4)

    sql_select_by_date_and_school = "SELECT * FROM test_4 WHERE main_date = '{}' AND school = '{}' ORDER BY student_class, student_lastname, student_name".format(main_date,institution)
    selected_df = pd.read_sql(sql_select_by_date_and_school, con = db_pd)
    if (choise == 2 and doc_type == 0) or (choise == 0 and doc_type == 1):
        main_df = selected_df
    elif choise == 1 and doc_type == 1:
        class_df = pd.DataFrame()
        for student_id in eval(main_list):
            student_id = student_id[8]
            sql_select_by_date_and_school = """SELECT student_class FROM test_4 WHERE school = '{}' AND main_date = '{}' AND student_number = '{}'"""
            df = pd.read_sql(sql_select_by_date_and_school.format(institution,main_date,student_id), con = db_pd)
            class_df = pd.concat([df, class_df], ignore_index=True, axis=0)
        selected_class_list = [i[0] for i in class_df.values.tolist()]
        main_df = pd.DataFrame()
        for single_class in selected_class_list:
            df_1 = selected_df.loc[selected_df['student_class'] == single_class]
            main_df = pd.concat([df_1, main_df], ignore_index=True, axis=0)

    name_df = main_df['student_lastname'].str.cat(main_df['student_name'], sep = ' ').str.upper()
    main_df = main_df.drop(columns = ['country', 'provience', 'school', 'form_code', 'main_date', 'test_date', 'student_lastname', 'student_name'])
    main_df.insert(0, 'full_name', name_df)
    if doc_type == 0:
        main_df = main_df.sort_values(by = ['student_class', 'total_score'], ascending = [True, False])
    elif doc_type == 1:
        main_df = main_df.sort_values(by = ['student_class', 'full_name'], ascending = [True, True])
    class_list = sorted(list(set(main_df['student_class'].values.tolist())))
    for i in range(len(class_list)):
        class_list[i] = int(scf.student_class_val_reverse(class_list[i]))
    class_list = sorted(class_list)
    main_df = main_df.drop(columns = ['student_number'])
    main_average_df = main_df.loc[(main_df['listening_score'] != "NS") & (main_df['swe_score'] != "NS") & (main_df['reading_score'] != "NS")]

    def main_table(first_class):
        #Create average table
        raw_average_table = []
        total_number = 0
        total_include_number = 0
        for single_class in first_class:
            spec_list = main_df.loc[main_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_list = [[x[0]]+x[2:] for x in spec_list]
            spec_average_list = main_average_df.loc[main_average_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_average_list = [[x[0]]+x[2:] for x in spec_average_list]
            total_number = total_number + len(spec_list)
            total_include_number = total_include_number + len(spec_average_list)
            if spec_average_list != []:
                average_item = spec_list
                listening_average = round(sum([int(x[1]) for x in average_item])/len(average_item), 2)
                swe_average = round(sum([int(x[3]) for x in average_item])/len(average_item), 2)
                reading_average = round(sum([int(x[5]) for x in average_item])/len(average_item), 2)
                total_average = round(sum([int(x[7]) for x in average_item])/len(average_item), 2)
                second_data_list = [scf.student_class_val(single_class), str("{:.2f}".format(listening_average)), str("{:.2f}".format(swe_average)), str("{:.2f}".format(reading_average)), str("{:.2f}".format(total_average)), str(len(spec_average_list)), str(len(spec_list))]
                raw_average_table.append(second_data_list)

        school_listening_average = round(sum([float(x[1])*int(x[5]) for x in raw_average_table])/sum([int(x[5]) for x in raw_average_table]), 2)
        school_swe_average = round(sum([float(x[2])*int(x[5]) for x in raw_average_table])/sum([int(x[5]) for x in raw_average_table]), 2)
        school_reading_average = round(sum([float(x[3])*int(x[5]) for x in raw_average_table])/sum([int(x[5]) for x in raw_average_table]), 2)
        school_total_average = round(sum([float(x[4])*int(x[5]) for x in raw_average_table])/sum([int(x[5]) for x in raw_average_table]), 2)
        school_average = ["School", str("{:.2f}".format(school_listening_average)), str("{:.2f}".format(school_swe_average)), str("{:.2f}".format(school_reading_average)), str("{:.2f}".format(school_total_average)), str(total_include_number), str(total_number)]
        average_data = [["Class", "Listening\nAverage", "SWE\nAverage", "Reading\nAverage", "Total\nAverage", "Number of Students\nIncluded in Average","Total\nNumber of Students"]]
        average_data.extend(raw_average_table)
        average_data.append(school_average)

        average_table = Table(average_data)
        average_table_style = [
            ('FONTNAME', (0, 0), (-1, 0), 'CalibriB'),
            ('FONTNAME', (0, 1), (-1, -1), 'Calibri'),
            ('FONTSIZE', (0, 0), (-1, 1), 10),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('TOPPADDING', (0, 1), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 2),
            ('RIGHTPADDING', (0, 0), (0, 0), 12),
            ('LEFTPADDING', (0, 0), (0, 0), 12),
            ('RIGHTPADDING', (1, 0), (4, 0), 18),
            ('LEFTPADDING', (1, 0), (4, 0), 18),
            ('RIGHTPADDING', (5, 0), (6, 0), 3),
            ('LEFTPADDING', (5, 0), (6, 0), 3),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),

            ]
        average_table.setStyle(color_style_for_table_main("test_4",average_table_style,average_data[:-1],{'Reading\nAverage':[school_reading_average-test_4_main_diff,school_reading_average+test_4_main_diff],'SWE\nAverage':[school_swe_average-test_4_main_diff,school_swe_average+test_4_main_diff],'Listening\nAverage':[school_listening_average-test_4_main_diff,school_listening_average+test_4_main_diff]},30,68))
        pdf.drawImage(filigram, 0, 0, width = width, height = height, mask = None)
        pdf.setFillColor(colors.maroon)
        pdf.setFont("CalibriB", 16)
        pdf.drawCentredString(width/2, 740, "Test Type 4 Test Results")
        pdf.setFillColor(colors.navy)
        pdf.setFont("CalibriB", 16)
        pdf.drawCentredString(width/2, 715, institution)
        styling_info_dict = {
                '#8AC7DB':'{} scale score difference between listening, structure and written expression or reading'.format(str(test_4_b_main_diff)),
                '#3D9970':'{} scale score or higher than the school average.'.format(str(test_4_main_diff)),
                '#E8B425':'Within {} scale score range of the school average.'.format(str(test_4_main_diff)),
                '#FF4136':'{} scale scores below school average.'.format(str(test_4_main_diff))
                }
        counter_1 = 0
        pdf.setLineWidth(0.1)
        for key, val in styling_info_dict.items():
            pdf.setFillColor(colors.HexColor(key))
            pdf.rect(30, 125-counter_1, 17, 8, stroke=1, fill=1)
            pdf.setFillColor(colors.black)
            pdf.setFont("CalibriBI", 8)
            pdf.drawString(52, 125-counter_1+1, val)
            counter_1+=15
        pdf.setFillColor(colors.black)

        class_len = height-165-len(average_data)*15
        average_table.wrapOn(pdf, width, height)
        average_table.drawOn(pdf, 40, class_len)
        #Average table END

        legend_data = [x[0] for x in average_data[1:]]
        legend_data = [legend_data[-1]]+legend_data[:-1]
        chart_data = [x[1:-3] for x in average_data[1:]]
        for i in chart_data:
            for y in range(len(i)):
                i[y] = float(i[y])
        chart_data = [tuple(i) for i in [chart_data[-1]]+chart_data[:-1]]

        max_graph_value = round(max(max(chart_data)))+3

        drawing = Drawing(400, 200)
        if len(chart_data) < 17:
            bc = VerticalBarChart()
            bc.x = 50
            bc.y = 50
            bc.height = 170
            bc.width = 485
            color_list = [colors.mediumaquamarine, colors.darkmagenta, colors.chartreuse, colors.cornflowerblue, colors.plum, colors.rosybrown, colors.salmon, colors.seagreen, colors.tan, colors.steelblue, colors.violet, colors.yellowgreen, colors.lemonchiffon, colors.aqua, colors.blueviolet, colors.coral, colors.skyblue, colors.blanchedalmond, colors.darkgoldenrod]
            for x in range(len(color_list)):
                for i in range(3):
                    bc.bars[(x, i)].fillColor = color_list[x]
            bc.data = chart_data
            bc.strokeColor = colors.black
            bc.strokeWidth = 0.3
            bc.groupSpacing = 30
            bc.barSpacing = 0.5
            bc.valueAxis.valueMin = 31
            bc.valueAxis.valueMax = max_graph_value
            bc.valueAxis.valueStep = 4
            bc.valueAxis.strokeWidth = 0.3
            bc.valueAxis.strokeColor = colors.black
            bc.valueAxis.gridStart = bc.x
            bc.valueAxis.gridEnd = bc.x+bc.width
            bc.valueAxis.gridStrokeWidth = 0.1
            bc.valueAxis.gridStrokeColor = colors.black
            bc.valueAxis.visibleGrid = True
            bc.valueAxis.visibleTicks = False
            bc.valueAxis.labels.fontSize = 10
            bc.valueAxis.labels.fontName = 'Calibri'
            bc.barLabelFormat = '%.2f'
            bc.barLabels.fontSize = 7
            bc.barLabels.fontName = 'Calibri'
            bc.barLabels.dy = -20
            bc.barLabels.dx = -1
            bc.barLabels.angle = 90
            bc.bars.strokeWidth = 0.2
            bc.categoryAxis.labels.boxAnchor = 'ne'
            bc.categoryAxis.labels.dx = 35
            bc.categoryAxis.labels.dy = -10
            bc.categoryAxis.labels.angle = 0
            bc.categoryAxis.labels.fontSize = 12
            bc.categoryAxis.labels.fontName = 'Calibri'
            bc.categoryAxis.categoryNames = ['Listening Average', 'SWE Average', 'Reading Average']
            low_bar_labels = []
            for i in chart_data:
                if sum(i)/len(i) < 32:
                    low_bar_labels.append(i)
            if len(low_bar_labels) > 0:
                bc.barLabels.visible = False
            else:
                bc.barLabels.visible = True
            drawing.add(bc)

            legend = Legend()
            legend.alignment = 'right'
            legend.boxAnchor = 'sw'
            legend.columnMaximum = 1
            legend.colEndCallout = 0
            legend.dx = 15
            legend.dxTextSpace = 4
            legend.dy = 8
            legend.fontName = 'Calibri'
            legend.fontSize = 11
            legend.subCols.minWidth = 25
            legend.strokeWidth = 0.1
            legend.variColumn = 1
            legend.x = 51
            legend.y = -10
            legend.deltay = 10
            legend.colorNamePairs = [(color_list[i], (legend_data[i])) for i in range (len(bc.data[:1]))]
            legend.autoXPadding = 20

            legend1 = Legend()
            legend1.alignment = 'right'
            legend1.boxAnchor = 'sw'
            legend1.columnMaximum = 1
            legend1.colEndCallout = 0
            legend1.dx = 15
            legend1.dxTextSpace = 4
            legend1.dy = 8
            legend1.fontName = 'Calibri'
            legend1.fontSize = 11
            legend1.subCols.minWidth = 25
            legend1.strokeWidth = 0.1
            legend1.variColumn = 1
            legend1.x = 115
            legend1.y = -10
            legend1.deltay = 10
            legend1.colorNamePairs = [(color_list[i+1], (legend_data[i+1])) for i in range (len(bc.data[1:8]))]
            legend1.autoXPadding = 20
            if len(bc.data) > 8:
                legend2 = Legend()
                legend2.alignment = 'right'
                legend2.boxAnchor = 'sw'
                legend2.columnMaximum = 1
                legend2.colEndCallout = 0
                legend2.dx = 15
                legend2.dxTextSpace = 4
                legend2.dy = 8
                legend2.fontName = 'Calibri'
                legend2.fontSize = 11
                legend2.subCols.minWidth = 25
                legend2.strokeWidth = 0.1
                legend2.variColumn = 1
                legend2.x = 51
                legend2.y = -30
                legend2.deltay = 10
                legend2.colorNamePairs = [(color_list[i+8], (legend_data[i+8])) for i in range (len(bc.data[8:]))]
                legend2.autoXPadding = 20
                drawing.add(legend2)
            drawing.add(legend)
            drawing.add(legend1)
        x, y = 10, class_len-250
        renderPDF.draw(drawing, pdf, x, y, showBoundary = False)

        pdf.showPage()
        return school_listening_average,school_swe_average,school_reading_average

    def class_tables(first_class,school_listening_average,school_swe_average,school_reading_average):
        for single_class in first_class:
            pdf.drawImage(filigram, 0, 0, width = width, height = height, mask = None)
            spec_list = main_df.loc[main_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_list = [[x[0]]+x[2:8]+[x[-1]] for x in spec_list]
            spec_average_list = main_average_df.loc[main_average_df['student_class'] == scf.student_class_val(single_class)].values.tolist()
            spec_average_list = [[x[0]]+x[2:7]+[x[-1]]+[x[7]] for x in spec_average_list]
            ps1data = [["Student Name", "Listening Section", "", "SWE Section", "", "Reading Section", "", "Total"],
                    ["", "Score", "CEFR", "Score", "CEFR", "Score", "CEFR", ""]]

            ps1data.extend(spec_list)
            ps1data_table = Table(ps1data)
            ps1_style = [
                ('FONTNAME', (0, 0), (-1, 1), 'CalibriB'),
                ('FONTNAME', (0, 2), (-1, -1), 'Calibri'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 1), 3),
                ('BOTTOMPADDING', (0, 2), (-1, -1), 2),
                ('TOPPADDING', (0, 2), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (0, 1), 52),
                ('LEFTPADDING', (0, 0), (0, 1), 52),
                ('RIGHTPADDING', (1, 1), (1, 1), 13),
                ('LEFTPADDING', (1, 1), (1, 1), 13),
                ('RIGHTPADDING', (3, 1), (3, 1), 13),
                ('LEFTPADDING', (3, 1), (3, 1), 13),
                ('RIGHTPADDING', (5, 1), (5, 1), 13),
                ('LEFTPADDING', (5, 1), (5, 1), 13),
                ('RIGHTPADDING', (2, 1), (2, 1), 19),
                ('LEFTPADDING', (2, 1), (2, 1), 19),
                ('RIGHTPADDING', (4, 1), (4, 1), 19),
                ('LEFTPADDING', (4, 1), (4, 1), 19),
                ('RIGHTPADDING', (6, 1), (6, 1), 19),
                ('LEFTPADDING', (6, 1), (6, 1), 19),
                ('RIGHTPADDING', (7, 0), (7, 0), 13),
                ('LEFTPADDING', (7, 0), (7, 0), 13),
                ("VALIGN", (0, 0), (0, 1), "MIDDLE"),
                ("ALIGN", (0, 0), (0, 1), "CENTER"),
                ("VALIGN", (1, 1), (-1, 1), "MIDDLE"),
                ("ALIGN", (1, 1), (-1, 1), "CENTER"),
                ("VALIGN", (1, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (1, 0), (-1, -1), "CENTER"),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                ('SPAN', (0, 0), (0, 1)),
                ('SPAN', (1, 0), (2, 0)),
                ('SPAN', (3, 0), (4, 0)),
                ('SPAN', (5, 0), (6, 0)),
                ('SPAN', (7, 0), (7, 1)),
                ]
            listening_average = round(sum([int(x[1]) for x in ps1data[2:]])/len(ps1data[2:]), 2)
            swe_average = round(sum([int(x[3]) for x in ps1data[2:]])/len(ps1data[2:]), 2)
            reading_average = round(sum([int(x[5]) for x in ps1data[2:]])/len(ps1data[2:]), 2)
            total_average = round(sum([int(x[7]) for x in ps1data[2:]])/len(ps1data[2:]), 2)
            
            ps1data_table.setStyle(color_style_for_table_class('test_4',ps1_style,ps1data,{'Listening Section':[school_listening_average-test_4_class_diff,school_listening_average+test_4_class_diff],'LFM Section':[school_swe_average-test_4_class_diff,school_swe_average+test_4_class_diff],'Reading Section':[school_reading_average-test_4_class_diff,school_reading_average+test_4_class_diff]},30,68))
            class_len = height-185-len(ps1data)*14
            ps1data_table.wrapOn(pdf, width, height)
            ps1data_table.drawOn(pdf, 30, class_len)
            pdf.setFillColor(colors.maroon)
            pdf.setFont("CalibriB", 16)
            pdf.drawCentredString(width/2, 740, "Test Type 4 Test Results")
            pdf.setFillColor(colors.navy)
            pdf.setFont("CalibriB", 16)
            pdf.drawCentredString(width/2, 715, institution)
            pdf.setFillColor(colors.maroon)
            pdf.setFont("CalibriB", 20)
            pdf.drawCentredString(width/2, 690, scf.student_class_val(single_class))
            pdf.setFillColor(colors.black)
            pdf.setFont("CalibriB", 10)
            pdf.drawString(125, class_len-20, "Listening Average : ")
            pdf.drawString(144.5, class_len-35, "SWE Average : ")
            pdf.drawString(129, class_len-50, "Reading Average : ")
            pdf.drawString(141, class_len-65, "Total Average : ")
            pdf.drawString(30, class_len-80, "Number of Students Included in Average : ")
            pdf.drawString(91, class_len-95, "Total Number of Students : ")
            pdf.setFont("Calibri", 10)
            pdf.drawString(207, class_len-20, str("{:.2f}".format(listening_average)))
            pdf.drawString(207, class_len-35, str("{:.2f}".format(swe_average)))
            pdf.drawString(207, class_len-50, str("{:.2f}".format(reading_average)))
            pdf.drawString(207, class_len-65, str("{:.2f}".format(total_average)))
            pdf.drawString(207, class_len-80, str(len(spec_average_list)))
            pdf.drawString(207, class_len-95, str(len(spec_list)))
            pdf.setFont("CalibriI", 8)
            pdf.drawCentredString(width/2, 70, "*NS: No Score       *NA: No Answer       *CEFR: Common European Framework Reference       *SWE: Structure and Written Expression")
            styling_info_dict = {
                '#8AC7DB':'{} scale score difference between listening, structure and written expression or reading.'.format(str(test_4_b_class_diff)),
                '#3D9970':'{} scale score or higher than the school average.'.format(str(test_4_class_diff)),
                '#E8B425':'Within {} scale score range of the school average.'.format(str(test_4_class_diff)),
                '#FF4136':'{} scale scores below school average.'.format(str(test_4_class_diff))
                }
            counter_1 = 0
            pdf.setLineWidth(0.1)
            for key, val in styling_info_dict.items():
                pdf.setFillColor(colors.HexColor(key))
                pdf.rect(30, 135-counter_1, 17, 8, stroke=1, fill=1)
                pdf.setFillColor(colors.black)
                pdf.setFont("CalibriBI", 8)
                pdf.drawString(52, 135-counter_1+1, val)
                counter_1+=15
            
            pdf.showPage()

            if doc_type == 1:
                pdf.drawImage(test_4_info, 0, 0, width = width, height = height, mask = None)
                pdf.showPage()
    test_type_str = "Test Type 4 Test"
    if doc_type == 0:
        first_info(pdf,test_4_info,test_type_str,institution,main_date)
        class_int_list = []
        for c in range(0, 1900, 100):class_int_list.append(c)
        for c in range(10900, 11200, 100):class_int_list.append(c)
        for c in class_int_list:
            try:
                aa = []
                for i in class_list:
                    if 200+c > int(i) > 100+c:
                        aa.append(i)
                school_listening_average,school_swe_average,school_reading_average = main_table(aa)
                class_tables(aa,school_listening_average,school_swe_average,school_reading_average)
            except ZeroDivisionError:
                pass
    elif doc_type == 1:
        class_int_list = []
        for c in range(0, 1900, 100):class_int_list.append(c)
        for c in range(10900, 11200, 100):class_int_list.append(c)
        for c in class_int_list:
            try:
                aa = []
                for i in class_list:
                    if 200+c > int(i) > 100+c:
                        aa.append(i)
                class_tables(aa)
            except ZeroDivisionError:
                pass

    pdf.save()
    os.startfile(file_name)
    db_pd.close()
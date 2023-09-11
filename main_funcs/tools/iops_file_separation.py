import pdfplumber, re, os
from PyPDF2 import PdfFileReader, PdfFileWriter
import main_funcs.mixed.mysql_connection as mc


pri_sr_wm_file = "./data/exam_data/watermarks/pri_sr_watermark.pdf"
js_sr_wm_file = "./data/exam_data/watermarks/js_sr_watermark.pdf"
test_4_sr_wm_file = "./data/exam_data/watermarks/test_4_sr_watermark.pdf"

pri_c_wm_file = "./data/exam_data/watermarks/pri_c_watermark.pdf"
js_c_list = {"GOLD":"./data/exam_data/watermarks/js_gold_c_watermark.pdf","SILVER":"./data/exam_data/watermarks/js_silver_c_watermark.pdf","BRONZE":"./data/exam_data/watermarks/js_bronze_c_watermark.pdf","GREEN":"./data/exam_data/watermarks/js_green_c_watermark.pdf","BLUE":"./data/exam_data/watermarks/js_blue_c_watermark.pdf"}
test_4_c_list = {"GOLD":"./data/exam_data/watermarks/test_4_gold_c_watermark.pdf","SILVER":"./data/exam_data/watermarks/test_4_silver_c_watermark.pdf","BRONZE":"./data/exam_data/watermarks/test_4_bronze_c_watermark.pdf"}

def get_db_info(test_type,institution,main_date):
    db_pd = mc.engine.connect()
    mycursor = db_pd.execute("SELECT student_lastname,student_name,student_number,student_class FROM "+test_type+" WHERE school = %s AND main_date = %s",(institution,main_date))
    first_fetch = mycursor.fetchall()
    db_pd.close()
    return first_fetch

def all_sr_sep(main_pdf,save_directory,test_type,institution,main_date):
    first_fetch = get_db_info(test_type,institution,main_date)
    find_name = re.compile(r'Student Name:  .*')
    find_id = re.compile(r'Student Number:  .*')

    if test_type == "test_1step_1":
        a, b = 2, -4
        c = 11
        watermark_file = pri_sr_wm_file
        test_type_str = "test_1 Step 1"
    elif test_type == "test_1step_2":
        a, b = 2, -4
        c = 11
        watermark_file = pri_sr_wm_file
        test_type_str = "test_1 Step 2"
    elif test_type == "test_3_standard":
        a, b = 2, -3
        c = 11
        watermark_file = js_sr_wm_file
        test_type_str = "test_3 Standard"
    elif test_type == "test_4":
        a, b = 2, None
        c = 10
        watermark_file = test_4_sr_wm_file
        test_type_str = "test_4"
    with pdfplumber.open(main_pdf) as pdf:
        total_page = len(pdf.pages)
        pdf_list = []
        for i in range(total_page):
            pdf_list_raw = []
            text = pdf.pages[i].extract_text()
            pdf_list_raw.append(i)
            for line in text.split('\n'):
                if find_name.match(line):
                    name = line.split()[a:b]
                    name = name[0].upper()+name[1][0].upper()
                    pdf_list_raw.append(name)
                if find_id.match(line):
                    student_id = line.split()[2]
                    pdf_list_raw.append(student_id)
            pdf_list.append(pdf_list_raw)
            
    for info in first_fetch:
        for iops_info in pdf_list:
            if info[2][:c] == iops_info[2]:
                student_class = info[3]
                page_num = iops_info[0]
                name = iops_info[1]
                student_id = iops_info[2]
                pdfReader = PdfFileReader(main_pdf)
                pdfWriter = PdfFileWriter()
                with open(watermark_file, "rb") as w_f:
                    w_f = PdfFileReader(w_f)
                    watermark_first_page = w_f.getPage(0)
                    score_page = pdfReader.getPage(page_num)
                    watermark_first_page.mergePage(score_page)
                    pdfWriter.addPage(watermark_first_page)
                    path = save_directory+"/"+institution+"/"+student_class
                    os.makedirs(path, exist_ok = True)
                    with open(save_directory+"/"+institution+"/"+student_class+"/"+name+"_"+student_id+"_"+test_type_str+"_SR.pdf", 'wb') as f:
                        pdfWriter.write(f)

def pri_c_sep(main_pdf,save_directory,test_type,institution,main_date):
    first_fetch = get_db_info(test_type,institution,main_date)
    test_type_str = "test_1"
    with pdfplumber.open(main_pdf) as pdf:
        total_page = len(pdf.pages)
        pdf_list = []
        for i in range(total_page):
            text = pdf.pages[i].extract_text()
            name = text.split('\n')[5].upper()
            pdf_list.append([i,name])

    for info in first_fetch:
        for iops_info in pdf_list:
            if (" ".join(info[:-2])).upper() == iops_info[1]:
                student_class = info[3]
                page_num = iops_info[0]
                student_id = info[2]
                name = (info[0]+info[1][0]).upper()
                pdfReader = PdfFileReader(main_pdf)
                pdfWriter = PdfFileWriter()
                with open(pri_c_wm_file, "rb") as w_f:
                    w_f = PdfFileReader(w_f)
                    watermark_first_page = w_f.getPage(0)
                    score_page = pdfReader.getPage(page_num)
                    watermark_first_page.mergePage(score_page)
                    pdfWriter.addPage(watermark_first_page)
                    path = save_directory+"/"+institution+"/"+student_class
                    os.makedirs(path, exist_ok = True)
                    with open(save_directory+"/"+institution+"/"+student_class+"/"+name+"_"+str(student_id)+"_"+test_type_str+"_C.pdf", 'wb') as f:
                        pdfWriter.write(f)

def js_test_4_c_sep(main_pdf,save_directory,test_type,institution,main_date):
    first_fetch = get_db_info(test_type,institution,main_date)
    if test_type == "test_3_standard":
        test_type_str = "test_3 Standard"
        cer_list = js_c_list
    elif test_type == "test_4":
        test_type_str = "test_4"
        cer_list = test_4_c_list
    with pdfplumber.open(main_pdf) as pdf:
        total_page = len(pdf.pages)
        pdf_list = []
        for i in range(total_page):
            text = pdf.pages[i].extract_text()
            name = text.split('\n')[0].upper()
            if test_type == 'test_3_standard':
                c_type = text.split('\n')[8].upper()
            elif test_type == "test_4":
                c_type = (text.split('\n')[9]).split(":")[0].upper()
            pdf_list.append([i,name,c_type])
            
    for key, value in cer_list.items():
        for info in first_fetch:
            for iops_info in pdf_list:
                if (" ".join(info[:-2])).upper() == iops_info[1] and key == iops_info[2]:
                    student_class = info[3]
                    page_num = iops_info[0]
                    student_id = info[2]
                    name = (info[0]+info[1][0]).upper()
                    pdfReader = PdfFileReader(main_pdf)
                    pdfWriter = PdfFileWriter()
                    with open(value, "rb") as w_f:
                        w_f = PdfFileReader(w_f)
                        watermark_first_page = w_f.getPage(0)
                        score_page = pdfReader.getPage(page_num)
                        watermark_first_page.mergePage(score_page)
                        pdfWriter.addPage(watermark_first_page)
                        path = save_directory+"/"+institution+"/"+student_class
                        os.makedirs(path, exist_ok = True)
                        with open(save_directory+"/"+institution+"/"+student_class+"/"+name+"_"+str(student_id)+"_"+test_type_str+"_C.pdf", 'wb') as f:
                            pdfWriter.write(f)
                
            
            

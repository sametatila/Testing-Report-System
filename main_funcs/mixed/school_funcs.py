import main_funcs.mixed.mysql_connection as mc
import ftplib,os


def add_school(school_name,school_country,school_city,school_address,teacher_name,teacher_tel,teacher_mail,logo):
    db_pd = mc.engine.connect()
    db_pd.execute("CREATE TABLE IF NOT EXISTS schools (school_name VARCHAR(50),test_1 KEY (school_name),school_country VARCHAR(50),school_city VARCHAR(50),school_address VARCHAR(100),teacher_name VARCHAR(50),teacher_tel VARCHAR(50),teacher_mail VARCHAR(50),logo VARCHAR(100))")
    db_pd.execute("INSERT IGNORE INTO schools (school_name,school_country,school_city,school_address,teacher_name,teacher_tel,teacher_mail,logo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",(school_name,school_country,school_city,school_address,teacher_name,teacher_tel,teacher_mail,logo))
    db_pd.close()

def get_school(school_name):
    db_pd = mc.engine.connect()
    for schools in db_pd.execute("SELECT * FROM schools WHERE school_name = "+"'"+school_name+"'").fetchall():
        schoolinfo = schools
    db_pd.close()
    return schoolinfo

def get_combobox_school():
    db_pd = mc.engine.connect()
    school_list = []
    for i in db_pd.execute("SELECT school_name FROM schools").fetchall():
        school_list.append(i[0])
    db_pd.close()
    return school_list

def update_school(selected_type,new_school_name,school_name,school_country,school_city,school_address,school_teacher,school_teacher_tel,school_teacher_mail,logo):
    db_pd = mc.engine.connect()
    if selected_type == 0:
        db_pd.execute("DELETE FROM schools WHERE school_name = "+"'"+school_name+"'")
        db_pd.execute("INSERT IGNORE INTO schools (school_name,school_country,school_city,school_address,teacher_name,teacher_tel,teacher_mail,logo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",(school_name,school_country,school_city,school_address,school_teacher,school_teacher_tel,school_teacher_mail,logo))
    else:
        table_list = ['test_1step_1','test_1step_2','test_1speaking','test_3_standard','test_3_speaking','test_4','students','iopssablon']
        for item in table_list:
            db_pd.execute("UPDATE "+item+" SET school = %s WHERE school = %s",(new_school_name,school_name))
        db_pd.execute("DELETE FROM schools WHERE school_name = "+"'"+school_name+"'")
        db_pd.execute("INSERT IGNORE INTO schools (school_name,school_country,school_city,school_address,teacher_name,teacher_tel,teacher_mail,logo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",(new_school_name,school_country,school_city,school_address,school_teacher,school_teacher_tel,school_teacher_mail,logo))
        
    
    db_pd.close()
        
def get_school_logo_list():
    ftp = ftplib.FTP("XXX")
    ftp.cwd('/GTO-Version/school_logos')
    logo_list = ftp.nlst()
    try:logo_list.remove('.')
    except:pass
    try:logo_list.remove('..')
    except:pass
    return logo_list

def upload_school_logo(logo_path):
    ftp = ftplib.FTP("XXX")
    ftp.cwd('/GTO-Version/school_logos')
    file_name = os.path.basename(logo_path)
    filename, extension = os.path.splitext(file_name)
    logo_list = get_school_logo_list()
    i = 1
    con = True
    while con:
        if file_name in logo_list:
            file_name = '%s(%i)%s' % (filename, i, extension)
            i += 1
        else:
            con = False
    with open(logo_path, "rb") as img_file:
        ftp.storbinary(f"STOR {file_name}", img_file)
        
def download_school_logo(filename):
    ftp = ftplib.FTP("XXX")
    ftp.cwd('/GTO-Version/school_logos')
    isExist = os.path.exists('./data/tmp/')
    if not isExist:
        os.makedirs('./data/tmp/')
    with open( './data/tmp/'+str(filename), 'wb' ) as f :
        ftp.retrbinary('RETR %s' % str(filename), f.write)
    ftp.close()
    return filename

def delete_school_logo(filename):
    ftp = ftplib.FTP("XXX")
    ftp.cwd('/GTO-Version/school_logos')
    ftp.delete(f"{filename}")
    ftp.close()

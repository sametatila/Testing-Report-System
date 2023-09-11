import main_funcs.mixed.mysql_connection as mc

def create_form_code(form_code,test_type):
    db_pd = mc.engine.connect()
    db_pd.execute("CREATE TABLE IF NOT EXISTS form_codes (form_code VARCHAR(50), test_type VARCHAR(50))")
    mycursor = db_pd.execute("SELECT * FROM form_codes WHERE form_code = %s",(form_code,))
    true_list,false_list = [],[]
    if mycursor.fetchall() == [] or mycursor.fetchall() == None:
        db_pd.execute("INSERT INTO form_codes (form_code,test_type) VALUES (%s,%s)",(form_code,test_type))
        for i in db_pd.execute("SELECT * FROM form_codes WHERE form_code = %s",(form_code,)).fetchall():
            true_list.append(i)
    else:
        for i in db_pd.execute("SELECT * FROM form_codes WHERE form_code = %s",(form_code,)).fetchall():
            false_list.append(i)
    db_pd.close()
    return [list(set(true_list)),list(set(false_list))]

def delete_form_code(form_code):
    db_pd = mc.engine.connect()
    db_pd.execute("DELETE FROM form_codes WHERE form_code =%s",(form_code,))
    true_list = []
    for i in db_pd.execute("SELECT * FROM form_codes WHERE form_code = %s",(form_code,)).fetchall():
        true_list.append(i)
    if true_list == []:
        true_list.append(form_code)
    db_pd.close()
    return list(set(true_list))

def get_form_code(form_code):
    db_pd = mc.engine.connect()
    for i in db_pd.execute("SELECT * FROM form_codes WHERE form_code = %s",(form_code,)).fetchall():
        form_code_info = i
    db_pd.close()
    return form_code_info

def edit_form_code(form_code,test_type):
    db_pd = mc.engine.connect()
    db_pd.execute("DELETE FROM form_codes WHERE form_code =%s",(form_code,))
    db_pd.execute("INSERT INTO form_codes (form_code,test_type) VALUES (%s,%s)",(form_code,test_type))
    for i in db_pd.execute("SELECT * FROM form_codes WHERE form_code =%s",(form_code,)).fetchall():
        form_code_info = i
    db_pd.close()
    return form_code_info
    
    
def get_all_form_codes():
    db_pd = mc.engine.connect()
    ps1_form_codes,ps2_form_codes,js_form_codes,test_4_form_codes,pspk_form_codes,jspk_form_codes = [],[],[],[],[],[]
    all_form_codes = []
    for i in db_pd.execute("SELECT * FROM form_codes").fetchall():
        if i[1] == "Test Type 1":
            fc = i[0].replace('\t','')
            ps1_form_codes.append(fc)
        if i[1] == "Test Type 2":
            fc = i[0].replace('\t','')
            ps2_form_codes.append(fc)
        if i[1] == "Test Type 3":
            fc = i[0].replace('\t','')
            js_form_codes.append(fc)
        if i[1] == "Test Type 4":
            fc = i[0].replace('\t','')
            test_4_form_codes.append(fc)
        if i[1] == "Test Type 5":
            fc = i[0].replace('\t','')
            pspk_form_codes.append(fc)
        if i[1] == "Test Type 6":
            fc = i[0].replace('\t','')
            jspk_form_codes.append(fc)
    for i in db_pd.execute("SELECT * FROM form_codes").fetchall():
        fc = i[0].replace('\t','')
        all_form_codes.append(fc)
    db_pd.close()
    return [list(set(all_form_codes)),list(set(ps1_form_codes)),list(set(ps2_form_codes)),list(set(js_form_codes)),list(set(test_4_form_codes)),list(set(pspk_form_codes)),list(set(jspk_form_codes))]

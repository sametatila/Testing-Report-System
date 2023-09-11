import main_funcs.mixed.mysql_connection as mc

def get_student_info(student_id):
    db_pd = mc.engine.connect()
    for student_info in db_pd.execute("SELECT * FROM students WHERE student_number = %s",(str(student_id),)).fetchall():
        return student_info
    db_pd.close()
    
def update_student_info(first_student_id,student_id,student_name,student_lastname,student_dob,student_gender,student_class,student_school):
    db_pd = mc.engine.connect()
    mycursor = db_pd.execute("SELECT * FROM students WHERE student_number = %s",(str(first_student_id),))
    some_list = []
    if mycursor.fetchall() != []:
        db_pd.execute("UPDATE students SET student_number = %s,student_name = %s,student_lastname = %s,date_of_birth_d_m_y = %s ,gender = %s,student_class = %s,school = %s WHERE student_number = %s AND student_lastname = %s",(str(student_id),str(student_name).title(),str(student_lastname).title(),str(student_dob),str(student_gender),str(student_class),str(student_school),str(first_student_id),str(student_lastname).title()))
    else:
        some_list = ["1"]
    test_list = ["test_1step_1","test_1step_2","test_1speaking","test_3_standard","test_3_speaking","test_4"]
    for test_type in test_list:
        mycursor = db_pd.execute("SELECT * FROM "+test_type+" WHERE student_number = %s",(str(first_student_id),))
        if mycursor.fetchall() != []:
            db_pd.execute("UPDATE "+test_type+" SET student_number = %s,student_name = %s,student_lastname = %s,student_class = %s WHERE student_number = %s",(str(student_id),str(student_name).title(),str(student_lastname).title(),str(student_class),str(first_student_id)))
    db_pd.close()
    return some_list
    
def create_student_info(student_id,student_name,student_lastname,student_dob,student_gender,student_class,student_school):
    db_pd = mc.engine.connect()
    mycursor = db_pd.execute("SELECT * FROM students WHERE student_number = %s",(str(student_id),))
    if mycursor.fetchall() == [] or mycursor.fetchall() == None:
        mycursor.execute("INSERT INTO students (student_number,student_name,student_lastname,date_of_birth_d_m_y,gender,student_class,school) VALUES(%s,%s,%s,%s,%s,%s,%s)",(str(student_id),str(student_name).title(),str(student_lastname).title(),str(student_dob),str(student_gender),str(student_class),str(student_school)))
    db_pd.close()

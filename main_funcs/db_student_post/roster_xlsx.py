import pandas as pd
import main_funcs.mixed.mysql_connection as mc

def pspk_roster(file):
    df = pd.read_excel(file, 'Sheet2')
    df['CEFR'] = df['CEFR'].astype('str')
    df.loc[df['CEFR'] == '**', 'CEFR'] = 'NA'
    df['Date Completed'] = df['Date Completed'].dt.strftime('%d-%m-%Y')
    return df

def jspk_roster(file):
    df = pd.read_excel(file, 'Sheet2')
    df['CEFR'] = df['CEFR'].astype('str')
    df.loc[df['CEFR'] == '**', 'CEFR'] = 'NA'
    df['Date Completed'] = df['Date Completed'].dt.strftime('%d-%m-%Y')
    return df

def ps1_roster(file):
    try:
        df = pd.read_excel(file, 'Sheet2',skiprows=[1])
        df.loc[df['Unnamed: 9'].isna(), 'Unnamed: 9'] = 'NA'
        df.loc[df['Unnamed: 10'].isna(), 'Unnamed: 10'] = 'NA'
        df.loc[df['Unnamed: 11'].isna(), 'Unnamed: 11'] = 'NA'
        df.loc[df['Unnamed: 13'].isna(), 'Unnamed: 13'] = 'NA'
        df.loc[df['Unnamed: 14'].isna(), 'Unnamed: 14'] = 'NA'
        df['Date Completed'] = df['Date Completed'].dt.strftime('%d-%m-%Y')
    except:
        df = pd.read_excel(file, 'Sheet2')
        df.loc[df['Unnamed: 9'].isna(), 'Unnamed: 9'] = 'NA'
        df.loc[df['Unnamed: 10'].isna(), 'Unnamed: 10'] = 'NA'
        df.loc[df['Unnamed: 11'].isna(), 'Unnamed: 11'] = 'NA'
        df.loc[df['Unnamed: 13'].isna(), 'Unnamed: 13'] = 'NA'
        df.loc[df['Unnamed: 14'].isna(), 'Unnamed: 14'] = 'NA'
        df['Date Completed'] = df['Date Completed'].dt.strftime('%d-%m-%Y')
    return df

def ps2_roster(file):
    try:
        df = pd.read_excel(file, 'Sheet2',skiprows=[1])
        df.loc[df['Unnamed: 9'].isna(), 'Unnamed: 9'] = 'NA'
        df.loc[df['Unnamed: 10'].isna(), 'Unnamed: 10'] = 'NA'
        df.loc[df['Unnamed: 11'].isna(), 'Unnamed: 11'] = 'NA'
        df.loc[df['Unnamed: 13'].isna(), 'Unnamed: 13'] = 'NA'
        df.loc[df['Unnamed: 14'].isna(), 'Unnamed: 14'] = 'NA'
        df['Date Completed'] = df['Date Completed'].dt.strftime('%d-%m-%Y')
    except:
        df = pd.read_excel(file, 'Sheet2')
        df.loc[df['Unnamed: 9'].isna(), 'Unnamed: 9'] = 'NA'
        df.loc[df['Unnamed: 10'].isna(), 'Unnamed: 10'] = 'NA'
        df.loc[df['Unnamed: 11'].isna(), 'Unnamed: 11'] = 'NA'
        df.loc[df['Unnamed: 13'].isna(), 'Unnamed: 13'] = 'NA'
        df.loc[df['Unnamed: 14'].isna(), 'Unnamed: 14'] = 'NA'
        df['Date Completed'] = df['Date Completed'].dt.strftime('%d-%m-%Y')
        
    return df

def js_roster(file):
    try:
        df = pd.read_excel(file, 'Sheet2',skiprows=[1])
        df['OSL'] = df['OSL'].astype('str')
        df.loc[df['Unnamed: 11'].isna(), 'Unnamed: 11'] = 'NA'
        df.loc[df['Unnamed: 13'].isna(), 'Unnamed: 13'] = 'NA'
        df.loc[df['Unnamed: 15'].isna(), 'Unnamed: 15'] = 'NA'
        df.loc[df['Unnamed: 16'].isna(), 'Unnamed: 16'] = 'NA'
        df.loc[df['OSL'] == "nan", 'OSL'] = 'NA'
        df['OSL'] = df["OSL"].replace({'.0':''}, regex=True)
        df['Date Completed'] = df['Date Completed'].dt.strftime('%d-%m-%Y')
    except:
        df = pd.read_excel(file, 'Sheet2')
        df['OSL'] = df['OSL'].astype('str')
        df.loc[df['Listening Comprehension_CEFR'].isna(), 'Listening Comprehension_CEFR'] = 'NA'
        df.loc[df['Language Form and Meaning_CEFR'].isna(), 'Language Form and Meaning_CEFR'] = 'NA'
        df.loc[df['Reading Comprehension_CEFR'].isna(), 'Reading Comprehension_CEFR'] = 'NA'
        df.loc[df['Reading Comprehension_Lexile'].isna(), 'Reading Comprehension_Lexile'] = 'NA'
        df.loc[df['OSL'] == "nan", 'OSL'] = 'NA'
        df['OSL'] = df["OSL"].replace({'.0':''}, regex=True)
        df['Date Completed'] = df['Date Completed'].dt.strftime('%d-%m-%Y')
    return df


def test_4_roster(file,test_date,institution):
    df = pd.read_excel(file, 'Sheet2')
    if "Student(s)" in df.iloc[-1][0]:
        df = df.iloc[:-1,:]
    db_pd = mc.engine.connect()
    sql_select_by_date_and_school = "SELECT * FROM iopssablon WHERE test_date = "+"'"+test_date+"'"+" AND school = "+"'"+institution+"'"
    sdf = pd.read_sql(sql_select_by_date_and_school, con=db_pd)
    sdf['student_number'] = sdf['student_number'].astype('str')
    df['Student ID'] = df['Student ID'].astype('str')
    df['Date Completed'] = df['Date Completed'].dt.strftime('%d-%m-%Y')
    studentnumbers = list(set(df['Student ID'].tolist()))
    studentnumbers = [str(int(float(i))) for i in studentnumbers if i != '--' and i != 'nan']
    #Create empty dataframe
    mdf = pd.DataFrame()
    for studentnumber in studentnumbers:
        #Find studentnumber from planning xls
        asdf = sdf[sdf['student_number'].str.contains(str(studentnumber))]
        #Find studentnumber from iops xls
        bsdf = df[df['Student ID'].str.contains(str(studentnumber))]
        #Add studentclass info from planning xls to iops dataframe Col 12
        bsdf.insert(loc=12, column="class", value=[str(asdf.iloc[0][14])])
        #Add institution Col 13
        bsdf.insert(loc=13, column="institution", value=[str(institution)])
        mdf = pd.concat([mdf,bsdf])
    db_pd.close()
    mdf.loc[mdf['Unnamed: 7'] == '**', 'Unnamed: 7'] = 'NA'
    mdf.loc[mdf['Unnamed: 9'] == '**', 'Unnamed: 9'] = 'NA'
    mdf.loc[mdf['Unnamed: 11'] == '**', 'Unnamed: 11'] = 'NA'
    mdf['Total Score'] = mdf['Total Score'].astype('str')
    mdf= mdf.replace({'\.0':''}, regex=True)
    return mdf

def test_4_roster_no_class(file,test_date,institution):
    df = pd.read_excel(file, 'Sheet2')
    if "Student(s)" in df.iloc[-1][0]:
        df = df.iloc[:-1,:]
    df['Student ID'] = df['Student ID'].astype('str')
    df['Date Completed'] = df['Date Completed'].dt.strftime('%d-%m-%Y')
    studentnumbers = list(set(df['Student ID'].tolist()))
    studentnumbers = [str(int(float(i))) for i in studentnumbers if i != '--' and i != 'nan']
    #Create empty dataframe
    mdf = pd.DataFrame()
    for studentnumber in studentnumbers:
        #Find studentnumber from iops xls
        bsdf = df[df['Student ID'].str.contains(str(studentnumber))]
        #Add institution Col 12
        bsdf.insert(loc=12, column="institution", value=[str(institution)])
        mdf = pd.concat([mdf,bsdf])
    mdf.loc[mdf['Unnamed: 7'] == '**', 'Unnamed: 7'] = 'NA'
    mdf.loc[mdf['Unnamed: 9'] == '**', 'Unnamed: 9'] = 'NA'
    mdf.loc[mdf['Unnamed: 11'] == '**', 'Unnamed: 11'] = 'NA'
    mdf['Total Score'] = mdf['Total Score'].astype('str')
    mdf= mdf.replace({'\.0':''}, regex=True)
    return mdf
    
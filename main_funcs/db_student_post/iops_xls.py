import pandas as pd
import main_funcs.mixed.mysql_connection as mc

def ps1_iops(file):
    try:
        #################################################
        #If xls file change you can edit heads from below
        colstudentname = 'Unnamed: 7'
        colstudentid = 'Unnamed: 13'
        collisteningcefr = 'Unnamed: 43'
        colreadingcefr = 'Unnamed: 26'
        #################################################
        #Read excel with pandas for first usable info
        df = pd.read_excel(file)
        #Row 4, Col 4 date info
        day,month,year = str(df.iat[4,3])[8:-9],str(df.iat[4,3])[5:-12],str(df.iat[4,3])[:-15]
        #Don't need to use now Row 1, Col 41
        testtype = df.iat[1,41]
        #Schollname Row 3, Col 0
        institution = df.iat[3,0]
        #Read excel to rearrange student records/ skiprow 0-15 starts Row 17 in xls
        df = pd.read_excel(file,skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13])
        df.dropna(subset=[colstudentname],inplace=True)
        df = df.dropna(axis=1,how='all')
        #Select only student records
        df = df.loc[:,colstudentname:collisteningcefr]
        df = df.fillna('NS')
        df = df.astype('str')
        #Retype student number col int
        df[colstudentid] = df[colstudentid].astype('float').astype('int64')
        #Add testdate to Col 10
        df.insert(loc=10, column="testdate", value=[day+"-"+month+"-"+year]*len(df))
        #Add institution info to Col 11
        df.insert(loc=11, column="institution", value=[institution]*len(df))
        #Replace * values to Below A1
        df.loc[df[collisteningcefr] == '**', collisteningcefr] = 'Below A1'
        df.loc[df[colreadingcefr] == '**', colreadingcefr] = 'Below A1'
        df.loc[df[collisteningcefr] == '*', collisteningcefr] = 'Below A1'
        df.loc[df[colreadingcefr] == '*', colreadingcefr] = 'Below A1'
        df= df.replace({'\.0':''}, regex=True)
    except:
        #################################################
        #If xls file change you can edit heads from below
        colstudentname = 'Unnamed: 8'
        colstudentid = 'Unnamed: 16'
        collisteningcefr = 'CEFR.1'
        colreadingcefr = 'CEFR'
        #################################################
        #Read excel with pandas for first usable info
        df = pd.read_excel(file)
        #Row 4, Col 4 date info
        day,month,year = str(df.iat[4,4])[8:-9],str(df.iat[4,4])[5:-12],str(df.iat[4,4])[:-15]
        #Don't need to use now Row 1, Col 41
        testtype = df.iat[1,41]
        #Schollname Row 3, Col 0
        institution = df.iat[3,0]
        #Read excel to rearrange student records/ skiprow 0-15 starts Row 17 in xls
        df = pd.read_excel(file,skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
        df.dropna(subset=[colstudentname],inplace=True)
        df = df.dropna(axis=1,how='all')
        #Select only student records
        df = df.loc[:,colstudentname:collisteningcefr]
        df = df.fillna('NS')
        df = df.astype('str')
        #Retype student number col int
        df[colstudentid] = df[colstudentid].astype('float').astype('int64')
        #Add testdate to Col 10
        df.insert(loc=10, column="testdate", value=[day+"-"+month+"-"+year]*len(df))
        #Add institution info to Col 11
        df.insert(loc=11, column="institution", value=[institution]*len(df))
        #Replace * values to Below A1
        df.loc[df[collisteningcefr] == '**', collisteningcefr] = 'Below A1'
        df.loc[df[colreadingcefr] == '**', colreadingcefr] = 'Below A1'
        df.loc[df[collisteningcefr] == '*', collisteningcefr] = 'Below A1'
        df.loc[df[colreadingcefr] == '*', colreadingcefr] = 'Below A1'
        df= df.replace({'\.0':''}, regex=True)
    return df

def ps2_iops(file):
    try:
        #################################################
        #If xls file change you can edit heads from below
        colstudentname = 'Unnamed: 7'
        colstudentid = 'Unnamed: 13'
        collisteningcefr = 'Unnamed: 43'
        colreadingcefr = 'Unnamed: 26'
        #################################################
        #Read excel with pandas for first usable info
        df = pd.read_excel(file)
        #Row 4, Col 4 date info
        day,month,year = str(df.iat[4,3])[8:-9],str(df.iat[4,3])[5:-12],str(df.iat[4,3])[:-15]
        #Don't need to use now Row 1, Col 41
        testtype = df.iat[1,41]
        #Schollname Row 3, Col 0
        institution = df.iat[3,0]
        #Read excel to rearrange student records/ skiprow 0-15 starts Row 17 in xls
        df = pd.read_excel(file,skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13])
        df.dropna(subset=[colstudentname],inplace=True)
        df = df.dropna(axis=1,how='all')
        #Select only student records
        df = df.loc[:,colstudentname:collisteningcefr]
        df = df.fillna('NS')
        df = df.astype('str')
        #Retype student number col int
        df[colstudentid] = df[colstudentid].astype('float').astype('int64')
        #Add testdate to Col 10
        df.insert(loc=10, column="testdate", value=[day+"-"+month+"-"+year]*len(df))
        #Add institution info to Col 11
        df.insert(loc=11, column="institution", value=[institution]*len(df))
        #Replace * values to Below A1
        df.loc[df[collisteningcefr] == '**', collisteningcefr] = 'Below A1'
        df.loc[df[colreadingcefr] == '**', colreadingcefr] = 'Below A1'
        df.loc[df[collisteningcefr] == '*', collisteningcefr] = 'Below A1'
        df.loc[df[colreadingcefr] == '*', colreadingcefr] = 'Below A1'
        df = df.replace({'\.0':''}, regex=True)
    except:
        #################################################
        #If xls file change you can edit heads from below
        colstudentname = 'Unnamed: 8'
        colstudentid = 'Unnamed: 16'
        collisteningcefr = 'CEFR.1'
        colreadingcefr = 'CEFR'
        #################################################
        #Read excel with pandas for first usable info
        df = pd.read_excel(file)
        #Row 4, Col 4 date info
        day,month,year = str(df.iat[4,4])[8:-9],str(df.iat[4,4])[5:-12],str(df.iat[4,4])[:-15]
        #Don't need to use now Row 1, Col 41
        testtype = df.iat[1,41]
        #Schollname Row 3, Col 0
        institution = df.iat[3,0]
        #Read excel to rearrange student records/ skiprow 0-15 starts Row 17 in xls
        df = pd.read_excel(file,skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
        df.dropna(subset=[colstudentname],inplace=True)
        df = df.dropna(axis=1,how='all')
        #Select only student records
        df = df.loc[:,colstudentname:collisteningcefr]
        df = df.fillna('NS')
        df = df.astype('str')
        #Retype student number col int
        df[colstudentid] = df[colstudentid].astype('float').astype('int64')
        #Add testdate to Col 10
        df.insert(loc=10, column="testdate", value=[day+"-"+month+"-"+year]*len(df))
        #Add institution info to Col 11
        df.insert(loc=11, column="institution", value=[institution]*len(df))
        #Replace * values to Below A1
        df.loc[df[collisteningcefr] == '**', collisteningcefr] = 'Below A1'
        df.loc[df[colreadingcefr] == '**', colreadingcefr] = 'Below A1'
        df.loc[df[collisteningcefr] == '*', collisteningcefr] = 'Below A1'
        df.loc[df[colreadingcefr] == '*', colreadingcefr] = 'Below A1'
        df= df.replace({'\.0':''}, regex=True)
    return df

def js_iops(file):
    try:
        #################################################
        #If xls file change you can edit heads from below
        colstudentname = 'Student Name'
        colstudentid = 'Student Number'
        collisteningcefr = 'CEFR'
        collfmcefr = 'CEFR.1'
        colreadingcefr = 'CEFR.2'
        colosl = 'Unnamed: 34'
        #################################################
        #Read excel with pandas for first usable info
        df = pd.read_excel(file)
        #Row 2, Col 5 date info
        day,month,year = str(df.iat[2,5])[8:-9],str(df.iat[2,5])[5:-12],str(df.iat[2,5])[:-15]
        #Schollname Row 0, Col 0
        institution = df.iat[0,0]
        #Read excel to rearrange student records/ skiprow 0-15 starts Row 17 in xls
        df = pd.read_excel(file,skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        
        df.dropna(subset=[colstudentname],inplace=True)
        df = df.dropna(axis=1,how='all')
        #Select only student records
        df = df.loc[:,colstudentname:colosl]
        df = df.astype('str')
        #Retype student number col int
        df[colstudentid] = df[colstudentid].astype('float').astype('int64')
        #Add testdate to Col 12
        df.insert(loc=12, column="testdate", value=[day+"-"+month+"-"+year]*len(df))
        #Add institution info to Col 13
        df.insert(loc=13, column="institution", value=[institution]*len(df))
        #Replace * values to Below A1
        df.loc[df[collisteningcefr] == '*', collisteningcefr] = 'Below A2'
        df.loc[df[collfmcefr] == '*', collfmcefr] = 'Below A2'
        df.loc[df[colreadingcefr] == '*', colreadingcefr] = 'Below A2'
        df= df.replace({'\.0':''}, regex=True)
        df.loc[df[collisteningcefr] == 'nan', collisteningcefr] = 'NA'
        df.loc[df[collfmcefr] == 'nan', collfmcefr] = 'NA'
        df.loc[df[colreadingcefr] == 'nan', colreadingcefr] = 'NA'
        df.loc[df[colosl] == 'nan', colosl] = 'NA'
        df.loc[df['Unnamed: 30'] == 'nan', 'Unnamed: 30'] = 'NA'
        df.loc[df['Total'] == 'nan', 'Total'] = 'NS'
        df.loc[df['SS'] == 'nan', 'SS'] = 'NS'
        df.loc[df['SS.1'] == 'nan', 'SS.1'] = 'NS'
        df.loc[df['SS.2'] == 'nan', 'SS.2'] = 'NS'
    except:
        #################################################
        #If xls file change you can edit heads from below
        colstudentname = 'Student Name'
        colstudentid = 'Student Number'
        collisteningcefr = 'CEFR'
        collfmcefr = 'CEFR.1'
        colreadingcefr = 'CEFR.2'
        colosl = 'Unnamed: 34'
        #################################################
        #Read excel with pandas for first usable info
        df = pd.read_excel(file)
        #Row 2, Col 5 date info
        day,month,year = str(df.iat[3,5])[8:-9],str(df.iat[3,5])[5:-12],str(df.iat[3,5])[:-15]
        #Schollname Row 0, Col 0
        institution = df.iat[1,0]
        #Read excel to rearrange student records/ skiprow 0-15 starts Row 17 in xls
        df = pd.read_excel(file,skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
        df.dropna(subset=[colstudentname],inplace=True)
        
        #Select only student records
        #df = df.loc[:,colstudentname:colosl]
        df = df[[colstudentname,colstudentid,'Group','SS',collisteningcefr,'SS.1',collfmcefr,'SS.2',colreadingcefr,'Unnamed: 30','Total',colosl]]
        df = df.astype('str')
        #Retype student number col int
        df[colstudentid] = df[colstudentid].astype('float').astype('int64')
        collenght = len(df.columns)
        #Add testdate to Col 12
        df.insert(loc=collenght, column="testdate", value=[day+"-"+month+"-"+year]*len(df))
        #Add institution info to Col 13
        df.insert(loc=collenght+1, column="institution", value=[institution]*len(df))

        #Replace * values to Below A1
        df.loc[df[collisteningcefr] == '*', collisteningcefr] = 'Below A2'
        df.loc[df[collfmcefr] == '*', collfmcefr] = 'Below A2'
        df.loc[df[colreadingcefr] == '*', colreadingcefr] = 'Below A2'
        df= df.replace({'\.0':''}, regex=True)
        df.loc[df[collisteningcefr] == 'nan', collisteningcefr] = 'NA'
        df.loc[df[collfmcefr] == 'nan', collfmcefr] = 'NA'
        df.loc[df[colreadingcefr] == 'nan', colreadingcefr] = 'NA'
        df.loc[df[colosl] == 'nan', colosl] = 'NA'
        df.loc[df['Unnamed: 30'] == 'nan', 'Unnamed: 30'] = 'NA'
        df.loc[df['Total'] == 'nan', 'Total'] = 'NS'
        df.loc[df['SS'] == 'nan', 'SS'] = 'NS'
        df.loc[df['SS.1'] == 'nan', 'SS.1'] = 'NS'
        df.loc[df['SS.2'] == 'nan', 'SS.2'] = 'NS'
    return df

def test_4_iops(test_4file,test_date,institution):
    try:
        #################################################
        #If xls file change you can edit heads from below
        colstudentname = 'Unnamed: 8'
        colstudentid = 'Unnamed: 13'
        collisteningcefr = 'CEFR'
        collfmcefr = 'CEFR.1'
        colreadingcefr = 'Unnamed: 27'
        coltotalscore = 'Unnamed: 31'
        #################################################
        #Read excel with pandas for first usable info
        df = pd.read_excel(test_4file)
        #Schollname Row 5, Col 1
        #Read excel to rearrange student records/ skiprow 0-15 starts Row 17 in xls
        df = pd.read_excel(test_4file,skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        df.dropna(subset=[colstudentname],inplace=True)
        #Row 0, Col 34 date info from first student
        day,month,year = str(df.iat[0,33])[8:-9],str(df.iat[0,33])[5:-12],str(df.iat[0,33])[:-15]
        df = df.dropna(axis=1,how='all')
        #Select only student records
        df = df.loc[:,colstudentname:coltotalscore]
        #Delete shitttty rows from dataframe
        df = df.astype('str')
        df = df[~df[colstudentname].str.contains(str('\nStudent Name'), na=False)]
        #Get student numbers from test_4 oips xls to list
        studentnumbers = list(set(df[colstudentid].tolist()))
        #Read planning excel
        db_pd = mc.engine.connect()
        sql_select_by_date_and_school = "SELECT * FROM iopssablon WHERE test_date = "+"'"+test_date+"'"+" AND school = "+"'"+institution+"'"
        sdf = pd.read_sql(sql_select_by_date_and_school, con=db_pd)
        #Retype student number col str
        sdf = sdf.astype('str')
        #Create empty dataframe
        mdf = pd.DataFrame()
        for studentnumber in studentnumbers:
            studentnumber = str(studentnumber).replace(".0","")
            asdf = sdf[sdf['student_number'].str.contains(str(studentnumber))]
            #Find studentnumber from iops xls
            bsdf = df[df[colstudentid].str.contains(str(studentnumber))]
            #Add new true studentnumber from planning xls to iops dataframe Col 9
            bsdf.insert(loc=9, column="id", value=[str(asdf.iloc[0][13])])
            #Add studentclass info from planning xls to iops dataframe Col 10
            bsdf.insert(loc=10, column="class", value=[str(asdf.iloc[0][14])])
            #Add testdate to Col 11
            bsdf.insert(loc=11, column="testdate", value=[day+"-"+month+"-"+year])
            #Add institution info to Col 12
            bsdf.insert(loc=12, column="instution", value=[institution])
            #Add all specific student dataframe to empty dataframe to make rearranged dataframe
            mdf = pd.concat([mdf,bsdf])
        #Replace * values to Below A1
        print(mdf)
        mdf.loc[mdf[collisteningcefr] == '**', collisteningcefr] = 'Below A2'
        mdf.loc[mdf[collfmcefr] == '**', collfmcefr] = 'Below A2'
        mdf.loc[mdf[colreadingcefr] == '**', colreadingcefr] = 'Below A2'
        mdf.loc[mdf[collisteningcefr] == '*', collisteningcefr] = 'Below A2'
        mdf.loc[mdf[collfmcefr] == '*', collfmcefr] = 'Below A2'
        mdf.loc[mdf[colreadingcefr] == '*', colreadingcefr] = 'Below A2'
        mdf.loc[mdf[collisteningcefr] == 'nan', collisteningcefr] = 'NA'
        mdf.loc[mdf[collfmcefr] == 'nan', collfmcefr] = 'NA'
        mdf.loc[mdf[colreadingcefr] == 'nan', colreadingcefr] = 'NA'
        mdf.loc[mdf[coltotalscore] == 'nan', coltotalscore] = 'NS'
        mdf.loc[mdf['SS'] == 'nan', 'SS'] = 'NS'
        mdf.loc[mdf['SS.1'] == 'nan', 'SS.1'] = 'NS'
        mdf.loc[mdf['SS.2'] == 'nan', 'SS.2'] = 'NS'
        mdf= mdf.replace({'\.0':''}, regex=True)
        db_pd.close()
    except:
        #################################################
        #If xls file change you can edit heads from below
        colstudentname = 'Unnamed: 8'
        colstudentid = 'Unnamed: 14'
        collisteningcefr = 'Unnamed: 20'
        collfmcefr = 'Unnamed: 25'
        colreadingcefr = 'Unnamed: 28'
        coltotalscore = 'Unnamed: 32'
        #################################################
        #Read excel with pandas for first usable info
        df = pd.read_excel(test_4file)
        
        #Schollname Row 5, Col 1
        #Read excel to rearrange student records/ skiprow 0-15 starts Row 17 in xls
        df = pd.read_excel(test_4file,skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        df.dropna(subset=[colstudentname],inplace=True)
        #Row 0, Col 34 date info from first student
        day,month,year = str(df.iat[0,34])[8:-9],str(df.iat[0,34])[5:-12],str(df.iat[0,34])[:-15]
        df = df.dropna(axis=1,how='all')
        #Select only student records
        df = df.loc[:,colstudentname:coltotalscore]
        print(df)
        #Delete shitttty rows from dataframe
        df = df.astype('str')
        df = df[~df[colstudentname].str.contains(str('\nStudent Name'), na=False)]
        #Get student numbers from test_4 oips xls to list
        studentnumbers = list(set(df[colstudentid].tolist()))
        #Read planning excel
        db_pd = mc.engine.connect()
        sql_select_by_date_and_school = "SELECT * FROM iopssablon WHERE test_date = "+"'"+test_date+"'"+" AND school = "+"'"+institution+"'"
        sdf = pd.read_sql(sql_select_by_date_and_school, con=db_pd)
        #Retype student number col str
        sdf = sdf.astype('str')
        #Create empty dataframe
        mdf = pd.DataFrame()
        for studentnumber in studentnumbers:
            #Find studentnumber from planning xls
            studentnumber = str(studentnumber).replace(".0","")
            asdf = sdf[sdf['student_number'].str.contains(str(studentnumber))]
            #Find studentnumber from iops xls
            bsdf = df[df[colstudentid].str.contains(str(studentnumber))]
            #Add new true studentnumber from planning xls to iops dataframe Col 9
            bsdf.insert(loc=9, column="id", value=[str(asdf.iloc[0][13])])
            #Add studentclass info from planning xls to iops dataframe Col 10
            bsdf.insert(loc=10, column="class", value=[str(asdf.iloc[0][14])])
            #Add testdate to Col 11
            bsdf.insert(loc=11, column="testdate", value=[day+"-"+month+"-"+year])
            #Add institution info to Col 12
            bsdf.insert(loc=12, column="instution", value=[institution])
            #Add all specific student dataframe to empty dataframe to make rearranged dataframe
            mdf = pd.concat([mdf,bsdf])
        #Replace * values to Below A1
        mdf.loc[mdf[collisteningcefr] == '**', collisteningcefr] = 'Below A2'
        mdf.loc[mdf[collfmcefr] == '**', collfmcefr] = 'Below A2'
        mdf.loc[mdf[colreadingcefr] == '**', colreadingcefr] = 'Below A2'
        mdf.loc[mdf[collisteningcefr] == '*', collisteningcefr] = 'Below A2'
        mdf.loc[mdf[collfmcefr] == '*', collfmcefr] = 'Below A2'
        mdf.loc[mdf[colreadingcefr] == '*', colreadingcefr] = 'Below A2'
        mdf.loc[mdf[collisteningcefr] == 'nan', collisteningcefr] = 'NA'
        mdf.loc[mdf[collfmcefr] == 'nan', collfmcefr] = 'NA'
        mdf.loc[mdf[colreadingcefr] == 'nan', colreadingcefr] = 'NA'
        mdf.loc[mdf[coltotalscore] == 'nan', coltotalscore] = 'NS'
        mdf.loc[mdf['SS'] == 'nan', 'SS'] = 'NS'
        mdf.loc[mdf['SS.1'] == 'nan', 'SS.1'] = 'NS'
        mdf.loc[mdf['SS.2'] == 'nan', 'SS.2'] = 'NS'
        mdf= mdf.replace({'\.0':''}, regex=True)
        db_pd.close()
    return mdf

def test_4_iops_no_class(test_4file,test_date,institution):
    try:
        #################################################
        #If xls file change you can edit heads from below
        colstudentname = 'Unnamed: 8'
        colstudentid = 'Unnamed: 13'
        collisteningcefr = 'CEFR'
        collfmcefr = 'CEFR.1'
        colreadingcefr = 'Unnamed: 27'
        coltotalscore = 'Unnamed: 31'
        #################################################
        #Read excel with pandas for first usable info
        df = pd.read_excel(test_4file)
        #Schollname Row 5, Col 1
        #Read excel to rearrange student records/ skiprow 0-15 starts Row 17 in xls
        df = pd.read_excel(test_4file,skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        df.dropna(subset=[colstudentname],inplace=True)
        #Row 0, Col 34 date info from first student
        day,month,year = str(df.iat[0,34])[8:-9],str(df.iat[0,34])[5:-12],str(df.iat[0,34])[:-15]
        df = df.dropna(axis=1,how='all')
        #Select only student records
        df = df.loc[:,colstudentname:coltotalscore]
        df = df.astype('str')
        #Delete shitttty rows from dataframe
        df = df[~df[colstudentname].str.contains(str('\nStudent Name'), na=False)]
        #Get student numbers from test_4 oips xls to list
        studentnumbers = list(set(df[colstudentid].tolist()))
        #Retype student number col str
        #Create empty dataframe
        mdf = pd.DataFrame()
        for studentnumber in studentnumbers:
            #Find studentnumber from iops xls
            bsdf = df[df[colstudentid].str.contains(str(studentnumber))]            
            #Add testdate to Col 9
            bsdf.insert(loc=9, column="testdate", value=[day+"-"+month+"-"+year])
            #Add institution info to Col 10
            bsdf.insert(loc=10, column="instution", value=[institution])
            #Add all specific student dataframe to empty dataframe to make rearranged dataframe
            mdf = pd.concat([mdf,bsdf])
        #Replace * values to Below A1
        mdf.loc[mdf[collisteningcefr] == '**', collisteningcefr] = 'Below A2'
        mdf.loc[mdf[collfmcefr] == '**', collfmcefr] = 'Below A2'
        mdf.loc[mdf[colreadingcefr] == '**', colreadingcefr] = 'Below A2'
        mdf.loc[mdf[collisteningcefr] == '*', collisteningcefr] = 'Below A2'
        mdf.loc[mdf[collfmcefr] == '*', collfmcefr] = 'Below A2'
        mdf.loc[mdf[colreadingcefr] == '*', colreadingcefr] = 'Below A2'
        mdf= mdf.replace({'\.0':''}, regex=True)
    except:
        #################################################
        #If xls file change you can edit heads from below
        colstudentname = 'Unnamed: 8'
        colstudentid = 'Unnamed: 14'
        collisteningcefr = 'Unnamed: 20'
        collfmcefr = 'Unnamed: 25'
        colreadingcefr = 'Unnamed: 28'
        coltotalscore = 'Unnamed: 32'
        #################################################
        #Read excel with pandas for first usable info
        df = pd.read_excel(test_4file)
        #Schollname Row 5, Col 1
        #Read excel to rearrange student records/ skiprow 0-15 starts Row 17 in xls
        df = pd.read_excel(test_4file,skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        df.dropna(subset=[colstudentname],inplace=True)
        #Row 0, Col 34 date info from first student
        day,month,year = str(df.iat[0,34])[8:-9],str(df.iat[0,34])[5:-12],str(df.iat[0,34])[:-15]
        df = df.dropna(axis=1,how='all')
        #Select only student records
        df = df.loc[:,colstudentname:coltotalscore]
        df = df.astype('str')
        #Delete shitttty rows from dataframe
        df = df[~df[colstudentname].str.contains(str('\nStudent Name'), na=False)]
        #Get student numbers from test_4 oips xls to list
        studentnumbers = list(set(df[colstudentid].tolist()))
        #Retype student number col str
        #Create empty dataframe
        mdf = pd.DataFrame()
        for studentnumber in studentnumbers:
            #Find studentnumber from iops xls
            bsdf = df[df[colstudentid].str.contains(str(studentnumber))]            
            #Add testdate to Col 9
            bsdf.insert(loc=9, column="testdate", value=[day+"-"+month+"-"+year])
            #Add institution info to Col 10
            bsdf.insert(loc=10, column="instution", value=[institution])
            #Add all specific student dataframe to empty dataframe to make rearranged dataframe
            mdf = pd.concat([mdf,bsdf])
        #Replace * values to Below A1
        mdf.loc[mdf[collisteningcefr] == '**', collisteningcefr] = 'Below A2'
        mdf.loc[mdf[collfmcefr] == '**', collfmcefr] = 'Below A2'
        mdf.loc[mdf[colreadingcefr] == '**', colreadingcefr] = 'Below A2'
        mdf.loc[mdf[collisteningcefr] == '*', collisteningcefr] = 'Below A2'
        mdf.loc[mdf[collfmcefr] == '*', collfmcefr] = 'Below A2'
        mdf.loc[mdf[colreadingcefr] == '*', colreadingcefr] = 'Below A2'
        mdf= mdf.replace({'\.0':''}, regex=True)
    return mdf

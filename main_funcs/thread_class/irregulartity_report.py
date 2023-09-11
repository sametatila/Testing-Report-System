from PyQt5 import QtCore

class IrregularityReportClass(QtCore.QThread):
    irr_label_signal = QtCore.pyqtSignal(str)

    def __init__(self, parent: None,index=0):
        super(IrregularityReportClass, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.service import Service
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.common.by import By
            from selenium.webdriver.common.alert import Alert
            import os
            import time
            import pandas as pd
            from bs4 import BeautifulSoup
            from datetime import datetime
            from webdriver_manager.chrome import ChromeDriverManager

            i_date = self.i_date.toPyDate()
            i_date = i_date.strftime("%b-%Y")

            headless = False
            u_pass = "XXX"
            url = "XXX"
            driver_exe = ChromeDriverManager().install()
            options = webdriver.ChromeOptions()
            options.headless = headless
            options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
            options.add_experimental_option('excludeSwitches', ['enable-logging'])


            def get_irr_report(user_name,type_1,type_2):
                s = Service(executable_path=driver_exe)
                driver = webdriver.Chrome(service=s,options=options)
                driver.delete_all_cookies()
                wait = WebDriverWait(driver, 10)
                driver.get(url)
                cookies = [
                    {'name': 'LANG2', 'value': 'en-US', 'domain': 'XXX'},
                    {'name': 'longurl', 'value': 'XXXX', 'domain': 'XXX'},
                ]
                for cookie in cookies:
                    driver.add_cookie(cookie)
                driver.refresh()
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#btnlogin")))
                driver.find_element(By.CSS_SELECTOR,"#uname").send_keys(user_name)
                driver.find_element(By.CSS_SELECTOR,"#pass").send_keys(u_pass)
                driver.find_element(By.CSS_SELECTOR,"#btnlogin").click()
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#navribbon > li:nth-child("+type_1+") > a")))
                driver.find_element(By.CSS_SELECTOR,"#navribbon > li:nth-child("+type_1+") > a").click()
                frame = driver.find_element(By.CSS_SELECTOR, "#middle")
                driver.switch_to.frame(frame)
                wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div/table/tbody/tr[2]/td[1]/a')))
                driver.find_element(By.XPATH, '//*[@id="content"]/div/table/tbody/tr[2]/td[1]/a').click()
                try:
                    time.sleep(1)
                    driver.execute_script("window.scrollTo(0, 300)")
                    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="WidgetSection"]/div/div[2]/table/tbody/tr['+type_2+']/td[7]')))
                    driver.find_element(By.XPATH, '//*[@id="WidgetSection"]/div/div[2]/table/tbody/tr['+type_2+']/td[7]').click()
                    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="aDownload"]')))
                    driver.find_element(By.XPATH, '//*[@id="aDownload"]').click()
                    break_num = False
                    time.sleep(2)
                except:
                    break_num = True
                return break_num
                
            def check_ns(user_name,type_1,test_type,test_date):
                s = Service(executable_path=driver_exe)
                driver = webdriver.Chrome(service=s,options=options)
                wait = WebDriverWait(driver, 10)
                driver.get(url)
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#btnlogin")))
                driver.find_element(By.CSS_SELECTOR,"#uname").send_keys(user_name)
                driver.find_element(By.CSS_SELECTOR,"#pass").send_keys(u_pass)
                driver.find_element(By.CSS_SELECTOR,"#btnlogin").click()
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#navribbon > li:nth-child("+type_1+") > a")))
                driver.find_element(By.CSS_SELECTOR,"#navribbon > li:nth-child("+type_1+") > a").click()
                frame = driver.find_element(By.CSS_SELECTOR, "#middle")
                driver.switch_to.frame(frame)
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#changeadminlnk")))
                driver.find_element(By.CSS_SELECTOR,"#changeadminlnk").click()
                time.sleep(2)
                main_table = pd.DataFrame()
                for i in range(10):
                    form_code = driver.find_element(By.CSS_SELECTOR,"#row"+str(i)+"jqxgridAdmin > div:nth-child(1) > div > a")
                    start_date = driver.find_element(By.CSS_SELECTOR,"#row"+str(i)+"jqxgridAdmin > div:nth-child(2) > div")
                    end_date = driver.find_element(By.CSS_SELECTOR,"#row"+str(i)+"jqxgridAdmin > div:nth-child(3) > div")
                    start_date = datetime.strptime(start_date.text, "%m/%d/%Y")
                    end_date = datetime.strptime(end_date.text, "%m/%d/%Y")
                    
                    if test_type in form_code.text and start_date <= test_date <= end_date:
                        form_code.click()
                        time.sleep(5)
                        if "test_4" in test_type:
                            driver.find_element(By.CSS_SELECTOR,"#atab9").click()
                            time.sleep(5)
                        html=driver.page_source
                        soup=BeautifulSoup(html,'html.parser')
                        div=soup.select_one("div#DataTables_Table_0_wrapper")
                        table=pd.read_html(str(div))[0]
                        table.columns = table.columns.droplevel()
                        main_table = pd.concat([main_table,table])
                        driver.find_element(By.CSS_SELECTOR,"#changeadminlnk").click()
                        time.sleep(2)
                return main_table

            def main(country):
                self.irr_label_signal.emit('İşlem başlatılıyor')
                if country == "TR":
                    yss_user = "XXX"
                    test_4_user = 'XXX'
                elif country == "NL":
                    yss_user = "XXX"
                    test_4_user = 'XXX'
                date_now = datetime.now().strftime('%#m_%#d_%Y')
                month = datetime.now().strftime('%m')
                test_dict = {4:'Test Type 4 Test',5:'Test Type 3 Test',8:'Test Type 1 Test',
                            9:'Test Type 2 Test',20:'Test Type 5 Test',21:'Test Type 6 Test'}

                file = os.path.expanduser('~')+'/Downloads/IncidentReport_'+date_now+'.xlsx'
                if os.path.exists(file):
                    os.remove(file)
                for i in range(10):
                    tmp = os.path.expanduser('~')+'/Downloads/IncidentReport_'+date_now+' ('+str(i)+').xlsx'
                    if os.path.exists(tmp):
                        os.remove(tmp)
                        
                break_num_1 = get_irr_report(yss_user,'8','17')
                break_num_2 = get_irr_report(test_4_user,'9','16')
                
                if break_num_1 == False or break_num_2 == False:
                    if break_num_1 == False and break_num_2 == False:
                        yss_file = os.path.expanduser('~')+'/Downloads/IncidentReport_'+date_now+'.xlsx'
                        if os.path.exists(yss_file):
                            df1 = pd.read_excel(yss_file)
                        test_4_file = os.path.expanduser('~')+'/Downloads/IncidentReport_'+date_now+' (1).xlsx'
                        if os.path.exists(test_4_file):
                            df2 = pd.read_excel(test_4_file)
                        df = pd.concat([df1,df2]).reset_index(drop=True)
                        self.irr_label_signal.emit('YSS ve test_4 Irregularity Report indirildi.')
                    elif break_num_1 == False and break_num_2 != False:
                        yss_file = os.path.expanduser('~')+'/Downloads/IncidentReport_'+date_now+'.xlsx'
                        if os.path.exists(yss_file):
                            df = pd.read_excel(yss_file)
                        self.irr_label_signal.emit('YSS Irregularity Report indirildi. test_4 yok.')
                    elif break_num_1 != False and break_num_2 == False:
                        test_4_file = os.path.expanduser('~')+'/Downloads/IncidentReport_'+date_now+' (1).xlsx'
                        if os.path.exists(test_4_file):
                            df = pd.read_excel(test_4_file)
                        self.irr_label_signal.emit('test_4 Irregularity Report indirildi. YSS yok.')

                    df = df[df['Incident Date'].dt.strftime('%m') == month]
                    df['NS'] = ''
                    df = df[['Institution','Institution ID','Program','Incident ID','Result ID','Candidate ID',
                            'Incident Date','Type Code','First Name','Last Name','Incident Details','Test Name','NS']]
                    for key,val in test_dict.items():
                        df['Test Name'] = df['Test Name'].apply(lambda x:val if x==key else x)
                    df['FullName'] = df['First Name']+" "+df['Last Name']
                    for index,row in df.iterrows():
                        self.irr_label_signal.emit(row['FullName']+' NS kontrolü yapılıyor...')
                        if row['Test Name'] != "Test Type 5 Test" or row['Test Name'] != "Test Type 6 Test":
                            if row['Test Name'] == "Test Type 3 Test":
                                test_type = "test_3"
                                control_df = check_ns(yss_user,'6',test_type,row['Incident Date'])
                                control_df['FullName'] = control_df['Given Name']+" "+control_df['Family Name']
                                new_df = control_df[control_df['FullName'] == row['FullName']]
                                check_df = new_df[new_df['Total Score'] == 'NS']
                            elif row['Test Name'] == "Test Type 1 Test" or row['Test Name'] == "Test Type 2 Test":
                                test_type = "Step"
                                control_df = check_ns(yss_user,'6',test_type,row['Incident Date'])
                                control_df['FullName'] = control_df['Given Name']+" "+control_df['Family Name']
                                new_df = control_df[control_df['FullName'] == row['FullName']].reset_index(drop=True)
                                cols=pd.Series(new_df.columns)
                                for dup in cols[cols.duplicated()].unique(): 
                                    cols[cols[cols == dup].index.values.tolist()] = [dup + '.' + str(i) if i != 0 else dup for i in range(sum(cols == dup))]
                                new_df.columns=cols
                                if not new_df.empty:
                                    check_df = new_df[(new_df['Score'].astype(str) == 'NS') | (new_df['Score.1'].astype(str) == 'NS')]
                                else:
                                    check_df = pd.DataFrame()
                            elif row['Test Name'] == "Test Type 4 Test":
                                test_type = "test_4"
                                control_df = check_ns(test_4_user,'7',test_type,row['Incident Date'])
                                control_df['FullName'] = control_df['Given Name']+" "+control_df['Family Name']
                                new_df = control_df[control_df['FullName'] == row['FullName']]
                                check_df = new_df[new_df['Total Score'] == 'NS']
                            if not check_df.empty:
                                df.loc[df['FullName'] == row['FullName'],'NS'] = "NS"
                    df = df.drop('FullName', axis=1)
                    df['NS'] = df['NS'].fillna("-")
                    df.to_excel('{}/Irregularity_Report_{}_{}.xlsx'.format(self.save_directory,i_date,country),index=False)
                    self.irr_label_signal.emit('İşlem tamamlandı.')
                else:
                    self.irr_label_signal.emit('Irregularity Report Yok')

            main(self.country)
        except:
            self.irr_label_signal.emit('Bilinmeyen Hata!')

    def stop(self):
        self.is_running = False
        self.terminate()
        
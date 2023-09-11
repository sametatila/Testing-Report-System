from main_funcs.mixed.all_imports import *
from main_funcs.mixed.make_plan_dialog import PandasModelPlan

class MainUi(QMainWindow):
    _gripSize = 8
    def __init__(self):
        
        super(MainUi, self).__init__()
        uic.loadUi('./data/gui_data/GUI_BASE.ui', self)
        
        
        #Create All DB Tables
        import main_funcs.mixed.create_all_tables
        #Create new title bar and click funcs
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.pressing = False
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_max.clicked.connect(self.btn_max_clicked)
        self.btn_maxr.clicked.connect(self.btn_maxr_clicked)
        self.btn_maxr.hide()
        self.size_down.clicked.connect(self.all_size_down)
        self.size_up.clicked.connect(self.all_size_up)
        self.size_normal.clicked.connect(self.all_size_normal)
        self.refresh.clicked.connect(self.refresh_gui)
        self.start = QPoint(0, 0)
        self.pressing = False
        self.sideGrips = [
            SideGrip(self, Qt.LeftEdge), 
            SideGrip(self, Qt.TopEdge), 
            SideGrip(self, Qt.RightEdge), 
            SideGrip(self, Qt.BottomEdge), 
        ]
        self.cornerGrips = [QSizeGrip(self) for i in range(4)]
        
        #Create bottom-right resizable window icon
        self.sizegrip = QSizeGrip(self.frame_size_grip)
        self.showMaximized()
        #Set openning page
        self.current_date_time = QDateTime.currentDateTime()
        self.stackedWidget.setCurrentWidget(self.page_home)
        self.btn_main_table_export.setEnabled(False)
        self.get_year_data.clicked.connect(self.get_date_ranged_historical)
        self.historical_start_date.setDateTime(self.current_date_time)
        self.historical_end_date.setDateTime(self.current_date_time)
        self.home_higher_institution_comboBox.currentTextChanged.connect(self.higher_institution_changed)
        self.home_city_comboBox.currentTextChanged.connect(self.city_changed)
        self.home_higher_institution_comboBox.addItems(["Kurum Seç"]+sd.higher_inst_list)
        self.home_higher_institution_comboBox.setCurrentText("Kurum Seç")
        self.home_city_comboBox.addItems(["Şehir Seç"]+sorted(ghd.city_list()))
        self.home_city_comboBox.setCurrentText("Şehir Seç")
        self.home_institution_comboBox.addItems(["Okul Seç"]+sorted(ghd.institution_list()))
        self.home_institution_comboBox.setCurrentText("Okul Seç")
        self.btn_main_table_export.clicked.connect(self.export_selected_historical)
        last_version = str(vi.last_version_info())
        pc_version = str(vi.get_version_info())
        self.label_version.setText("Son sürüm: "+last_version+" | Sürüm: "+pc_version)
        self.btn_update_version.setVisible(False)
        if pc_version != last_version:
            self.btn_update_version.setVisible(True)
        
        
        #Set left menu object funcs
        self.btn_home.clicked.connect(self.open_page_home)
        self.btn_plan.clicked.connect(self.open_page_plan)
        self.btn_result.clicked.connect(self.open_page_result)
        self.btn_student.clicked.connect(self.open_page_student)
        self.btn_edit_info.clicked.connect(self.open_page_edit_info)
        self.btn_tools.clicked.connect(self.open_page_tools)
        self.btn_docs.clicked.connect(self.open_page_docs)
        
        self.tabWidget_5.currentChanged.connect(self.plan_tab_changed)
        self.tabWidget.currentChanged.connect(self.result_tab_changed)
        self.tabWidget_3.currentChanged.connect(self.student_tab_changed)
        self.tabWidget_2.currentChanged.connect(self.edit_info_tab_changed)
        
        #Setting of planning part
        self.u_plan_comboBox = ExtendedComboBox()
        self.gridLayout.addWidget(self.dateEdit_upload_plan,0,0)
        self.gridLayout.addWidget(self.u_plan_comboBox,0,1)
        self.btn_browse_upload_plan.clicked.connect(self.open_plan_file)
        self.btn_upload_plan.clicked.connect(self.upload_plan_file)
        self.dateEdit_upload_plan.dateChanged.connect(self.hide_u_plan_info_label)
        self.dateEdit_create_plan.dateChanged.connect(self.get_school_date_changed)
        self.btn_create_plan.clicked.connect(self.get_form_code)
        self.btn_pri_optic.clicked.connect(self.create_test_1optic)
        self.btn_jun_optic.clicked.connect(self.create_test_3_optic)
        self.btn_test_4_optic.clicked.connect(self.create_test_4_optic)
        self.btn_attendance_id.clicked.connect(self.create_attendance_sheet_with_id)
        self.btn_attendance_no_id.clicked.connect(self.create_attendance_sheet_without_id)
        self.btn_booklet.clicked.connect(self.create_booklet)
        self.btn_del_plan.clicked.connect(self.delete_plan)
        self.btn_ps1_dn.clicked.connect(self.create_ps1_dn)
        self.btn_ps2_dn.clicked.connect(self.create_ps2_dn)
        self.btn_js_dn.clicked.connect(self.create_js_dn)
        self.btn_test_4_dn.clicked.connect(self.create_test_4_dn)
        self.attendance_check_checkBox.stateChanged.connect(self.attendance_check_checked)
        self.btn_upload_attendance_text.clicked.connect(self.upload_attendance_text)
        self.btn_scanner_text.clicked.connect(self.plan_to_scanner_text)

        self.convert_plan_comboBox = ExtendedComboBox()
        self.gridLayout_54.addWidget(self.convert_plan_comboBox,0,1)
        self.logic_plan_comboBox.currentTextChanged.connect(self.plan_logic_changed)
        self.btn_browse_upload_draft.clicked.connect(self.open_plan_dialog)
        self.btn_convert_plan.clicked.connect(self.run_plan_dialog)

        self.convert_plan_2_comboBox = ExtendedComboBox()
        self.gridLayout_56.addWidget(self.whole_plan_checkBox,0,0)
        self.gridLayout_56.addWidget(self.logic_plan_comboBox_2,0,1)
        self.gridLayout_56.addWidget(self.convert_plan_2_comboBox,0,2)
        self.gridLayout_56.addWidget(self.total_class_spinBox_2,0,3)
        self.gridLayout_56.addWidget(self.btn_browse_upload_draft_2,0,4)
        self.gridLayout_56.addWidget(self.btn_convert_plan_2,0,5)
        self.logic_plan_comboBox_2.currentTextChanged.connect(self.plan_logic_changed_2)
        self.whole_plan_checkBox.stateChanged.connect(self.divide_plan_checked)
        self.btn_browse_upload_draft_2.clicked.connect(self.open_plan_control)
        self.btn_convert_plan_2.clicked.connect(self.get_plan_control)

        
        #Setting of result part tab "IOPS"
        self.u_iops_comboBox = ExtendedComboBox()
        self.gridLayout_13.addWidget(self.dateEdit_upload_iops,0,0)
        self.gridLayout_13.addWidget(self.u_iops_comboBox,0,1)
        self.iops_upload_result_comboBox = ExtendedComboBox()   
        self.gridLayout_13.addWidget(self.iops_upload_result_comboBox,0,2)
        self.gridLayout_13.addWidget(self.iops_upload_date_comboBox,0,3)
        self.gridLayout_13.addWidget(self.edit_iops_form,0,4)
        self.gridLayout_13.addWidget(self.btn_browse_upload_iops,0,5)
        self.gridLayout_13.addWidget(self.btn_upload_iops,0,6)
        self.radioButton_iops_ps1.toggled.connect(self.iops_test_type_selected)
        self.radioButton_iops_ps2.toggled.connect(self.iops_test_type_selected)
        self.radioButton_iops_js.toggled.connect(self.iops_test_type_selected)
        self.radioButton_iops_test_4.toggled.connect(self.iops_test_type_selected)
        self.btn_browse_upload_iops.clicked.connect(self.open_iops_file)
        self.btn_upload_iops.clicked.connect(self.upload_iops_file)
        self.btn_upload_iops_test_4_no_class.clicked.connect(self.upload_iops_test_4_file)
        self.btn_iops_opt_student.clicked.connect(self.open_page_student_add_plan)
        self.dateEdit_upload_iops.dateChanged.connect(self.hide_iops_info_label)

        self.iops_upload_result_comboBox.currentTextChanged.connect(self.iops_upload_school_changed)
        self.checkBox_iops_make_up.stateChanged.connect(self.iops_upload_make_up_check_state)
        #Setting of result part tab "ProgramWorkshop"
        self.u_roster_comboBox = ExtendedComboBox()
        self.gridLayout_23.addWidget(self.dateEdit_upload_roster,0,0)
        self.gridLayout_23.addWidget(self.u_roster_comboBox,0,1)
        self.radioButton_roster_ps1.toggled.connect(self.roster_test_type_selected)
        self.radioButton_roster_ps2.toggled.connect(self.roster_test_type_selected)
        self.radioButton_roster_js.toggled.connect(self.roster_test_type_selected)
        self.radioButton_roster_test_4.toggled.connect(self.roster_test_type_selected)
        self.radioButton_roster_pspk.toggled.connect(self.roster_test_type_selected)
        self.radioButton_roster_jspk.toggled.connect(self.roster_test_type_selected)
        self.btn_browse_upload_roster.clicked.connect(self.open_roster_file)
        self.btn_upload_roster.clicked.connect(self.upload_roster_file)
        self.btn_upload_roster_test_4_no_class.clicked.connect(self.upload_roster_test_4_file)
        self.btn_roster_opt_student.clicked.connect(self.open_page_student_add_plan)
        self.dateEdit_upload_roster.dateChanged.connect(self.hide_roster_info_label)

        #Setting of result part tab "Sonuç Getir/Rapor Al"
        self.get_result_comboBox = ExtendedComboBox()        
        self.gridLayout_31.addWidget(self.get_result_comboBox,0,1)
        self.get_result_test_type_comboBox.currentTextChanged.connect(self.get_school_date_changed_result)
        self.get_result_comboBox.currentTextChanged.connect(self.get_school_date_changed_result)
        self.btn_get_result.clicked.connect(self.get_school_result)
        self.btn_turkish_report.clicked.connect(self.create_turkish_report)
        self.btn_institutional_report.clicked.connect(self.create_institutional_report)
        self.btn_class_table.clicked.connect(self.create_class_table)
        self.btn_export_excel.clicked.connect(self.export_score_excel)
        self.btn_result_letter.clicked.connect(self.create_result_letter)
        self.btn_aio_digital.clicked.connect(self.create_aio_digital_report)
        self.checkBox_iops_split.stateChanged.connect(self.iops_split_check_checked)
        self.btn_browse_upload_sr.clicked.connect(self.iops_split_sr_browse)
        self.btn_browse_upload_c.clicked.connect(self.iops_split_c_browse)

        ######################################################################################################################################################
        #Setting of result part tab "Sonuç Sil"
        self.delete_result_comboBox = ExtendedComboBox()
        self.gridLayout_27.addWidget(self.delete_result_comboBox,0,0)
        self.radioButton_delete_ps1.toggled.connect(self.get_school_date_changed_delete_result)
        self.radioButton_delete_ps2.toggled.connect(self.get_school_date_changed_delete_result)
        self.radioButton_delete_js.toggled.connect(self.get_school_date_changed_delete_result)
        self.radioButton_delete_test_4.toggled.connect(self.get_school_date_changed_delete_result)
        self.radioButton_delete_pspk.toggled.connect(self.get_school_date_changed_delete_result)
        self.radioButton_delete_jspk.toggled.connect(self.get_school_date_changed_delete_result)
        self.delete_result_comboBox.currentTextChanged.connect(self.get_school_date_changed_delete_result)
        self.btn_get_result_delete.clicked.connect(self.get_school_result_for_delete)
        self.btn_del_result.clicked.connect(self.delete_result)
        self.btn_del_result_selected.clicked.connect(self.delete_selected_result)
        
        #Setting of student part
        self.btn_search_student.clicked.connect(self.get_student_info)
        self.btn_update_student.clicked.connect(self.edit_student_info)
        self.btn_create_student.clicked.connect(self.create_student_info)
        #Setting of editable system info part
        self.sch_comboBox_3 = ExtendedComboBox()
        self.gridLayout_57.addWidget(self.sch_comboBox_3,0,1)
        self.btn_sch_get_3.clicked.connect(self.get_school_info)
        self.btn_sch_run.clicked.connect(self.save_school_info)
        self.btn_sch_run_3.clicked.connect(self.edit_school_info)
        self.btn_export_schools.clicked.connect(self.export_schools_info)
        self.add_school_logo_comboBox.currentTextChanged.connect(self.select_logo_change)
        self.update_school_logo_comboBox.currentTextChanged.connect(self.select_logo_change_edit)
        self.btn_browse_logo.clicked.connect(self.open_logo_file)
        self.btn_upload_logo.clicked.connect(self.upload_logo_file)
        self.checkBox_new_school_name.stateChanged.connect(self.change_school_name)
        self.btn_delete_logo.clicked.connect(self.delete_logo_file)
        #Setting of editable form_code part
        self.btn_save_form_code.clicked.connect(self.save_form_code_info)
        self.btn_get_form_code.clicked.connect(self.get_form_code_info)
        self.btn_update_form_code.clicked.connect(self.edit_form_code_info)
        self.btn_delete_form_code.clicked.connect(self.delete_form_code_info)
        
        #Setting of tools part
        self.btn_irr_dir.clicked.connect(self.open_irr_save_dir)
        self.btn_create_irr.clicked.connect(self.get_irregularity_report)
        self.btn_create_sales_card.clicked.connect(self.create_sales_card)
        self.radioButton_iops_ps1_2.toggled.connect(self.get_school_date_changed_iops_separation)
        self.radioButton_iops_ps2_2.toggled.connect(self.get_school_date_changed_iops_separation)
        self.radioButton_iops_js_2.toggled.connect(self.get_school_date_changed_iops_separation)
        self.radioButton_iops_test_4_2.toggled.connect(self.get_school_date_changed_iops_separation)
        self.dateEdit_upload_iops_2.dateChanged.connect(self.get_school_date_changed_iops_separation)
        self.btn_browse_upload_iops_2.clicked.connect(self.open_iops_pdf_file)
        self.btn_upload_iops_2.clicked.connect(self.create_iops_pdf_files)
        self.btn_browse_pdf.clicked.connect(self.open_password_pdfs)
        self.btn_remove_pass.clicked.connect(self.pdf_remove_password)
        self.main_formcode_comboBox = ExtendedComboBox()
        self.gridLayout_60.addWidget(self.main_formcode_comboBox,0,0)
        self.main_formcode_comboBox.currentTextChanged.connect(self.copy_form_code_change)
        self.btn_select_main_form_code_folder.clicked.connect(self.select_main_form_code_folder)
        self.btn_start_copy_all.clicked.connect(self.copy_all_files_to_drive)
        self.gridLayout_73.addWidget(self.main_formcode_comboBox,0,0)
        self.btn_select_main_form_code_folder_t1.clicked.connect(self.select_main_form_code_folder_t1)
        self.btn_select_main_output_folder_t1.clicked.connect(self.copy_all_files_to_drive_t1)

        #Shortcuts
        self.btn_institutional_report.setShortcut(QKeySequence("Ctrl+Shift+K"))
        self.btn_turkish_report.setShortcut(QKeySequence("Ctrl+Shift+T"))
        self.btn_class_table.setShortcut(QKeySequence("Ctrl+Shift+S"))
        self.shortcut_ps = QShortcut(QKeySequence("Ctrl+Shift+1"), self)
        self.shortcut_ps.activated.connect(self.test_1plan_shortcombo)
        self.shortcut_js = QShortcut(QKeySequence("Ctrl+Shift+2"), self)
        self.shortcut_js.activated.connect(self.test_3_plan_shortcombo)
        self.shortcut_test_4 = QShortcut(QKeySequence("Ctrl+Shift+3"), self)
        self.shortcut_test_4.activated.connect(self.test_4_plan_shortcombo)
        shortcuts = """Ctrl+Shift+K - Kurumsal Rapor
        \nCtrl+Shift+T - Türkçe Karne
        \nCtrl+Shift+S - Sınıf Listesi
        \nCtrl+Shift+1 - Toplu test_1 Plan Belgeleri
        \nCtrl+Shift+2 - Toplu test_3 Plan Belgeleri
        \nCtrl+Shift+3 - Toplu test_4 Plan Belgeleri
        """
        self.shortcut_info_label.setToolTip(shortcuts)
        
        #Setting of docs part
        self.btn_attendance_form.clicked.connect(partial(self.doc_btn, 'b1'))
        self.btn_proctor_form.clicked.connect(partial(self.doc_btn, 'b2'))
        self.btn_admission_form.clicked.connect(partial(self.doc_btn, 'b3'))
        self.btn_consent_form.clicked.connect(partial(self.doc_btn, 'b4'))
        self.btn_delivery_note.clicked.connect(partial(self.doc_btn, 'b5'))
        self.btn_delivery_control.clicked.connect(partial(self.doc_btn, 'b6'))
        self.btn_tca_id_card.clicked.connect(partial(self.doc_btn, 'b7'))
        self.btn_team_leader_id_card.clicked.connect(partial(self.doc_btn, 'b8'))
        self.btn_proctor_id_card.clicked.connect(partial(self.doc_btn, 'b9'))
        self.btn_proctor_instructions.clicked.connect(partial(self.doc_btn, 'b10'))
        self.btn_turkish_report_bg.clicked.connect(self.create_turkish_report_bg)

        


        #App Setting part
        self.btn_update_version.clicked.connect(self.update_version)
        if os.path.exists(os.path.expanduser("~/Documents/GTO_Docs")) == False:os.makedirs(os.path.expanduser("~/Documents/GTO_Docs"))
    

    def test_1plan_shortcombo(self):
        self.create_test_1optic()
        self.create_ps1_dn()
        self.create_ps2_dn()
        self.create_attendance_sheet_with_id()
        self.create_attendance_sheet_without_id()
        self.create_booklet()

    def test_3_plan_shortcombo(self):
        self.create_test_3_optic()
        self.create_js_dn()
        self.create_attendance_sheet_with_id()
        self.create_attendance_sheet_without_id()
        self.create_booklet()

    def test_4_plan_shortcombo(self):
        self.create_test_4_optic()
        self.create_test_4_dn()
        self.create_attendance_sheet_with_id()
        self.create_attendance_sheet_without_id()
        self.create_booklet()
    
    def update_version(self):
        os.startfile("updater.exe")
        self.close()
        
    def refresh_gui(self):
        os.execl(sys.executable, sys.executable, *sys.argv)     
    #################################################################################
    #Home Part START
    def calculate(self, value):
        ps1 = value[0]
        ps2 = value[1]
        pspk = value[2]
        js = value[3]
        jspk = value[4]
        test_4 = value[5]
        main_list = [["Sinif", "test_1 Step 1", "test_1 Step 2", "test_1 Speaking", "test_3 Standard", "test_3 Speaking", "test_4", "TOPLAM"], 
                     ["1.Sinif", "", "", "", "", "", "", ""], 
                     ["2.Sinif", "", "", "", "", "", "", ""], 
                     ["3.Sinif", "", "", "", "", "", "", ""], 
                     ["4.Sinif", "", "", "", "", "", "", ""], 
                     ["5.Sinif", "", "", "", "", "", "", ""], 
                     ["6.Sinif", "", "", "", "", "", "", ""], 
                     ["7.Sinif", "", "", "", "", "", "", ""], 
                     ["8.Sinif", "", "", "", "", "", "", ""], 
                     ["Haz.Sinif", "", "", "", "", "", "", ""], 
                     ["9.Sinif", "", "", "", "", "", "", ""], 
                     ["10.Sinif", "", "", "", "", "", "", ""], 
                     ["11.Sinif", "", "", "", "", "", "", ""], 
                     ["12.Sinif", "", "", "", "", "", "", ""], 
                     ["TOPLAM", sum(ps1.values()), sum(ps2.values()), sum(pspk.values()), sum(js.values()), sum(jspk.values()), sum(test_4.values()), ""]]
        test_type = ["ps1", "ps2", "pspk", "js", "jspk", "test_4"]
        count_number = 0
        for i in test_type:
            count_number += 1
            if eval(i) != {}:
                for key, val in eval(i).items():
                    for item in main_list:
                        if item[0] == key:
                            item[count_number] = val
        for item in main_list[1:]:
            item[7] = sum(filter(lambda i: isinstance(i, int), item))
        self.main_table.setRowCount(0)
        for row_number, row_data in enumerate(main_list):
            self.main_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.main_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                
    def export_selected_historical(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            df = pd.DataFrame()
            for row in range(self.main_table.rowCount()):
                for col in range(self.main_table.columnCount()):
                    df.at[row, col] = self.main_table.item(row, col).text()
            df.to_csv(upload_file+'/Toplam Sınav Sayıları.csv', index = False)
            os.startfile(upload_file+'/Toplam Sınav Sayıları.csv')
        
    def get_date_ranged_historical(self):
        self.thread = GetHistoricalDataClass(parent = None, index = 0)
        self.thread.start_date = self.historical_start_date.date()
        self.thread.end_date = self.historical_end_date.date()
        self.thread.higher_institution = self.home_higher_institution_comboBox.currentText()
        self.thread.city = self.home_city_comboBox.currentText()
        self.thread.institution = self.home_institution_comboBox.currentText()
        self.thread.start()
        self.thread.count_main_signal.connect(self.calculate)
        self.btn_main_table_export.setEnabled(True)
    
    def higher_institution_changed(self, value):
        if value != "Kurum Seç":
            self.home_city_comboBox.clear()
            self.home_city_comboBox.addItems(["Şehir Seç"]+sorted(ghd.higher_institution_change_city(value)))
            self.home_city_comboBox.setCurrentText("Şehir Seç")
            self.home_institution_comboBox.clear()
            self.home_institution_comboBox.addItems(["Okul Seç"]+sorted(ghd.higher_institution_change_school(value)))
            self.home_institution_comboBox.setCurrentText("Okul Seç")
        else:
            self.home_institution_comboBox.clear()
            self.home_institution_comboBox.addItems(["Okul Seç"]+sorted(ghd.institution_list()))
            self.home_institution_comboBox.setCurrentText("Okul Seç")
            self.home_city_comboBox.clear()
            self.home_city_comboBox.addItems(["Şehir Seç"]+sorted(ghd.city_list()))
            self.home_city_comboBox.setCurrentText("Şehir Seç")
            
    def city_changed(self, value):
        higher_institution = self.home_higher_institution_comboBox.currentText()
        if value != "Şehir Seç":
            if higher_institution == "Kurum Seç":
                self.home_institution_comboBox.clear()
                self.home_institution_comboBox.addItems(["Okul Seç"]+sorted(ghd.city_change(value)))
                self.home_institution_comboBox.setCurrentText("Okul Seç")
            else:
                self.home_institution_comboBox.clear()
                self.home_institution_comboBox.addItems(["Okul Seç"]+sorted(ghd.city_change_higher(higher_institution, value)))
                self.home_institution_comboBox.setCurrentText("Okul Seç")
        else:
            self.home_institution_comboBox.clear()
            self.home_institution_comboBox.addItems(["Okul Seç"]+sorted(ghd.institution_list()))
            self.home_institution_comboBox.setCurrentText("Okul Seç")
    #Home Part END
    #################################################################################
    
    #################################################################################
    #School Part START
    def open_logo_file(self):
        upload_file = QFileDialog.getOpenFileName(self, "Logo Seç", sfl.get(), "Image File (*.jpg *png)")
        sfl.save(upload_file)
        if upload_file:
            self.logo_upload_label.setText(upload_file[0])
            if self.add_school_logo_comboBox.currentText() == "Logo seç":
                self.label_89.setVisible(False)
            if self.update_school_logo_comboBox.currentText() == "Logo seç":
                self.label_90.setVisible(False)

    def upload_logo_file(self):
        self.label_94.setText("Yükleniyor...")
        self.label_94.setVisible(True)
        self.thread = UploadLogoClass(parent = None, index = 0)
        self.thread.upload_file = self.logo_upload_label.text()
        self.thread.start()
        self.thread.label_94signal.connect(self.label_94.setText)
        self.add_school_logo_comboBox.clear()
        self.add_school_logo_comboBox.addItems(sorted(sm.get_school_logo_list()))
        self.add_school_logo_comboBox.setCurrentText('Logo seç')
        self.update_school_logo_comboBox.clear()
        self.update_school_logo_comboBox.addItems(sorted(sm.get_school_logo_list()))
        self.update_school_logo_comboBox.setCurrentText('Logo seç')
        self.delete_logo_comboBox.clear()
        self.delete_logo_comboBox.addItems(sorted(sm.get_school_logo_list()))
        self.delete_logo_comboBox.setCurrentText('Logo seç')
        self.label_89.setVisible(False)
        self.label_90.setVisible(False)
        self.label_94.setVisible(True)
        if self.add_school_logo_comboBox.currentText() == "Logo seç":
            self.label_89.setVisible(False)
        if self.update_school_logo_comboBox.currentText() == "Logo seç":
            self.label_90.setVisible(False)
        
    def delete_logo_file(self):
        self.label_96.setText("Yükleniyor...")
        self.label_96.setVisible(True)
        self.thread = DeleteLogoClass(parent = None, index = 0)
        self.thread.filename = self.delete_logo_comboBox.currentText()
        self.thread.start()
        self.thread.label_96signal.connect(self.label_96.setText)
        self.add_school_logo_comboBox.clear()
        self.add_school_logo_comboBox.addItems(sorted(sm.get_school_logo_list()))
        self.add_school_logo_comboBox.setCurrentText('Logo seç')
        self.update_school_logo_comboBox.clear()
        self.update_school_logo_comboBox.addItems(sorted(sm.get_school_logo_list()))
        self.update_school_logo_comboBox.setCurrentText('Logo seç')
        self.delete_logo_comboBox.clear()
        self.delete_logo_comboBox.addItems(sorted(sm.get_school_logo_list()))
        self.delete_logo_comboBox.setCurrentText('Logo seç')
        self.label_96.setVisible(True)
        if self.add_school_logo_comboBox.currentText() == "Logo seç":
            self.label_89.setVisible(False)
        if self.update_school_logo_comboBox.currentText() == "Logo seç":
            self.label_90.setVisible(False)

    def select_logo_change(self,value):
        self.label_89.setVisible(True)
        if value != "Logo seç" and value != '':
            self.pixmap_1 = QPixmap('./data/tmp/'+sm.download_school_logo(value))
            self.label_89.setPixmap(self.pixmap_1)
            self.label_89.setScaledContents(True)
            
    def select_logo_change_edit(self,value):
        self.label_90.setVisible(True)
        if value != "Logo seç" and value != '':
            self.pixmap_2 = QPixmap('./data/tmp/'+sm.download_school_logo(value))
            self.label_90.setPixmap(self.pixmap_2)
            self.label_90.setScaledContents(True)
            
    def save_school_info(self):
        self.thread = SaveSchoolClass(parent = None, index = 0)
        self.label_19.setText("Kaydediliyor...")
        self.label_19.setVisible(True)
        self.thread.school_name = self.sch_name.text()
        self.thread.school_country = self.sch_country.currentText()
        self.thread.school_city = self.sch_city.currentText()
        self.thread.school_address = self.sch_address.text()
        self.thread.school_teacher = self.sch_teacher.text()
        self.thread.school_teacher_tel = self.sch_teacher_tel.text()
        self.thread.school_teacher_mail = self.sch_teacher_mail.text()
        self.thread.logo = self.add_school_logo_comboBox.currentText()
        self.thread.start()
        self.thread.label_19signal.connect(self.label_19.setText)
        self.sch_comboBox_3.clear()
        self.thread.sch_comboBox_3signal.connect(self.sch_comboBox_3.addItems)
        self.u_plan_comboBox.clear()
        self.thread.sch_comboBox_3signal.connect(self.u_plan_comboBox.addItems)
        self.sch_name.clear()
        self.sch_address.clear()
        self.sch_teacher.clear()
        self.sch_teacher_tel.clear()
        self.sch_teacher_mail.clear()
        
    def get_school_info(self):
        self.label_38.setText("Yükleniyor...")
        self.label_38.setVisible(True)
        if self.add_school_logo_comboBox.currentText() == "Logo seç":
            self.label_89.setVisible(False)
        if self.update_school_logo_comboBox.currentText() == "Logo seç":
            self.label_90.setVisible(False)
        self.thread = GetSchoolInfoClass(parent = None, index = 0)
        self.thread.school_name = self.sch_comboBox_3.currentText()
        self.thread.start()
        self.thread.label_38signal.connect(self.label_38.setText)
        self.thread.sch_country_3signal.connect(self.sch_country_3.setCurrentText)
        self.thread.sch_city_3signal.connect(self.sch_city_3.setCurrentText)
        self.thread.sch_address_3signal.connect(self.sch_address_3.setText)
        self.thread.sch_teacher_3signal.connect(self.sch_teacher_3.setText)
        self.thread.sch_teacher_tel_3signal.connect(self.sch_teacher_tel_3.setText)
        self.thread.sch_teacher_mail_3signal.connect(self.sch_teacher_mail_3.setText)
        self.thread.logo_signal.connect(self.update_school_logo_comboBox.setCurrentText)
        self.checkBox_new_school_name.setChecked(False)
        self.label_38.setVisible(True)
            
    def edit_school_info(self):
        self.label_38.setText("Yükleniyor...")
        self.label_38.setVisible(True)
        if self.add_school_logo_comboBox.currentText() == "Logo seç":
            self.label_89.setVisible(False)
        if self.update_school_logo_comboBox.currentText() == "Logo seç":
            self.label_90.setVisible(False)
        self.thread = EditSchoolClass(parent = None, index = 0)
        self.thread.selected_type = self.checkBox_new_school_name.isChecked()
        self.thread.school_name = self.sch_comboBox_3.currentText()
        self.thread.new_school_name = self.sch_new_school_name.text()
        self.thread.school_country = self.sch_country_3.currentText()
        self.thread.school_city = self.sch_city_3.currentText()
        self.thread.school_address = self.sch_address_3.text()
        self.thread.school_teacher = self.sch_teacher_3.text()
        self.thread.school_teacher_tel = self.sch_teacher_tel_3.text()
        self.thread.school_teacher_mail = self.sch_teacher_mail_3.text()
        self.thread.logo = self.update_school_logo_comboBox.currentText()
        self.thread.start()
        self.thread.label_38signal.connect(self.label_38.setText)
        self.checkBox_new_school_name.setChecked(False)
        self.label_38.setVisible(True)
        self.label_71.setVisible(False)
        
    def change_school_name(self):
        self.label_38.setVisible(False)
        if self.checkBox_new_school_name.isChecked():
            dialog = ChangeSchoolNameConfirmationDialogUi()
            dialog_value = dialog.exec_()
            if dialog_value == 1:
                self.checkBox_new_school_name.setChecked(True)
            else:
                self.checkBox_new_school_name.setChecked(False)
            self.sch_new_school_name.setVisible(True)
            self.label_71.setVisible(True)
        else:
            self.sch_new_school_name.setVisible(False)
            self.label_71.setVisible(False)

    def export_schools_info(self):
        self.thread = ExportSchoolsClass(parent = None, index = 0)
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.thread.save_directory = str(upload_file)
            self.thread.institution = self.search_schools.text()
            self.thread.start()
            self.thread.label_64signal.connect(self.label_64.setText)
            self.label_64.setVisible(True)
    #School Part END
    #################################################################################
    
    #################################################################################
    #Form Code Part START
    def save_form_code_info(self):
        self.label_48.setText("Yükleniyor...")
        self.label_48.setVisible(True)
        self.thread = SaveFormCodeClass(parent = None, index = 0)
        self.thread.form_code = self.add_form_code.text()
        self.thread.test_type = self.test_type_comboBox.currentText()
        self.thread.start()
        self.thread.label_48signal.connect(self.label_48.setText)
        self.edit_form_code_comboBox.clear()
        self.thread.edit_test_type_comboBoxsignal.connect(self.edit_form_code_comboBox.addItems)
        self.add_form_code.clear()
        self.test_type_comboBox.setCurrentText("Sınav Türü Seç")
        self.label_43.setVisible(False)
        self.label_49.setVisible(False)
        self.label_48.setVisible(True)
        
    def get_form_code_info(self):
        self.label_43.setText("Yükleniyor...")
        self.label_43.setVisible(True)
        self.thread = GetFormCodeInfoClass(parent = None, index = 0)
        self.thread.form_code = self.edit_form_code_comboBox.currentText()
        self.thread.start()
        self.thread.label_43signal.connect(self.label_43.setText)
        self.thread.edit_test_type_comboBoxsignal.connect(self.edit_test_type_comboBox.setCurrentText)
        self.label_48.setVisible(False)
        self.label_49.setVisible(False)
        self.label_43.setVisible(True)
        
    def edit_form_code_info(self):
        self.label_43.setText("Yükleniyor...")
        self.label_43.setVisible(True)
        self.thread = EditFormCodeClass(parent = None, index = 0)
        self.thread.form_code = self.edit_form_code_comboBox.currentText()
        self.thread.test_type = self.edit_test_type_comboBox.currentText()
        self.thread.start()
        self.thread.label_43signal.connect(self.label_43.setText)
        self.label_49.setVisible(True)
        self.label_43.setVisible(True)

    def delete_form_code_info(self):
        self.label_49.setText("Yükleniyor...")
        self.label_49.setVisible(True)
        self.thread = DeleteFormCodeClass(parent = None, index = 0)
        self.thread.form_code = self.edit_form_code_comboBox.currentText()
        self.thread.start()
        self.thread.label_49signal.connect(self.label_49.setText)
        self.edit_form_code_comboBox.clear()
        self.thread.edit_test_type_comboBoxsignal.connect(self.edit_form_code_comboBox.addItems)
        self.label_49.setVisible(True)
    #Form Code Part END
    #################################################################################

    #################################################################################
    #Upload Plan Part START
    def open_plan_file(self):
        if self.u_plan_comboBox.currentText() != "Okul Seç":
            upload_file = QFileDialog.getOpenFileName(self, "Plan Exceli Seç", sfl.get(), "Excel File (*.xls *.xlsx)")
            sfl.save(upload_file)
            if upload_file:
                self.label_upload_file_name.setText(upload_file[0])
                self.label_upload_file_name.setVisible(True)
                self.btn_upload_plan.setEnabled(True)
                self.label_22.setVisible(False)
                self.label_23.setVisible(False)
                self.u_plan_table.clear()
                plan_new_false_list = [('Tarih',"Okul",'Sınıf','Country Code','Language Code','Form Code',"Sınav Saati","Sınav Türü","Seans","Sayfa","Salon","Ad","Soyad","TC","Sınıf","Ay","Gün","Yıl","Cinsiyet")]
                self.u_plan_table.setRowCount(20)
                for row_number, row_data in enumerate(plan_new_false_list):
                    self.u_plan_table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.u_plan_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        else:
            self.label_21.setText("Önce okul seç")
            self.label_21.setVisible(True)

    def all_result_list_plan(self, upload_list):
        self.label_113.setText("Yükleniyor...")
        self.label_113.setVisible(True)
        upload_true_list = upload_list[0]
        upload_false_list = upload_list[1]
        duplicate_error = upload_list[2]
        true_list_dif = upload_list[3]
        if len(upload_false_list) > 0:
            plan_new_false_list = [('Tarih',"Okul",'Sınıf','Country Code','Language Code','Form Code',"Sınav Saati","Sınav Türü","Seans","Sayfa","Salon","Ad","Soyad","TC","Sınıf","Ay","Gün","Yıl","Cinsiyet")]
            plan_new_false_list.extend(upload_false_list)
            self.label_113.setText(str(true_list_dif[0])+" Öğrenci yüklenebilir. Yukarıdaki "+str(len(upload_false_list))+" öğrenci kayıtlı!")
            self.u_plan_table.setRowCount(0)
            for row_number, row_data in enumerate(plan_new_false_list):
                self.u_plan_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.u_plan_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        elif duplicate_error != []:
            self.label_113.setText(duplicate_error[0])
        else:
            plan_new_true_list = [('Tarih',"Okul",'Sınıf','Country Code','Language Code','Form Code',"Sınav Saati","Sınav Türü","Seans","Sayfa","Salon","Ad","Soyad","TC","Sınıf","Ay","Gün","Yıl","Cinsiyet")]
            plan_new_true_list.extend(upload_true_list)
            self.label_113.setText(str(len(upload_true_list))+" öğrenci sorunsuz aktarıldı!")
            self.u_plan_table.setRowCount(0)
            for row_number, row_data in enumerate(plan_new_true_list):
                self.u_plan_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.u_plan_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def upload_plan_file(self):
        self.label_21.setText("Yükleniyor...")
        self.label_21.setVisible(True)
        self.label_22.setVisible(False)
        self.label_23.setVisible(False)
        self.thread = UploadPlanClass(parent = None, index = 0)
        self.thread.upload_file = self.label_upload_file_name.text()
        self.thread.upload_date = self.dateEdit_upload_plan.date()
        self.thread.upload_school = self.u_plan_comboBox.currentText()
        self.thread.start()
        self.thread.label_21signal.connect(self.label_21.setText)
        self.thread.all_upload_list_signal.connect(self.all_result_list_plan)
        self.dateEdit_upload_plan.setDateTime(self.current_date_time)
        self.u_plan_comboBox.setCurrentText('Okul seç')
        self.label_upload_file_name.setText('Dosya')
        self.label_21.setVisible(True)

    def get_school_date_changed(self):
        selected_date = self.dateEdit_create_plan.date().toString('dd-MM-yyyy')
        self.g_plan_comboBox.clear()
        school_list_by_date = gslbd.get_school_list_by_date(selected_date)
        if len(school_list_by_date) == 0:
            self.g_plan_comboBox.addItems(['Sınav Bulunamadı!'])
        else:
            self.g_plan_comboBox.addItems(sorted(gslbd.get_school_list_by_date(selected_date)))
        self.label_22.setVisible(False)
        self.label_23.setVisible(False)
        self.label_21.setVisible(False)
        self.ps1_form.setVisible(False)
        self.ps2_form.setVisible(False)
        self.js_form.setVisible(False)
        self.test_4_form.setVisible(False)
        self.u_plan_table.clear()
        plan_new_false_list = [('Tarih',"Okul",'Sınıf','Country Code','Language Code','Form Code',"Sınav Saati","Sınav Türü","Seans","Sayfa","Salon","Ad","Soyad","TC","Sınıf","Ay","Gün","Yıl","Cinsiyet")]
        self.u_plan_table.setRowCount(20)
        for row_number, row_data in enumerate(plan_new_false_list):
            self.u_plan_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.u_plan_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    
    def hide_u_plan_info_label(self):
        self.label_21.setVisible(False)
    #Upload Plan Part END
    #################################################################################
    
    #################################################################################
    #Get, create, delete Plan Part START
    def get_form_code(self):
        if self.g_plan_comboBox.currentText() != "Okul Seç" and self.g_plan_comboBox.currentText() != "Sınav Bulunamadı!" and self.attendance_check_checkBox.isChecked() == False:
            self.label_22.setText("Yükleniyor...")
            self.label_22.setVisible(True)
            self.label_23.setVisible(False)
            self.btn_pri_optic.setEnabled(True)
            self.btn_jun_optic.setEnabled(True)
            self.btn_test_4_optic.setEnabled(True)
            self.btn_ps1_dn.setEnabled(True)
            self.btn_ps2_dn.setEnabled(True)
            self.btn_js_dn.setEnabled(True)
            self.btn_test_4_dn.setEnabled(True)
            self.btn_attendance_id.setEnabled(True)
            self.btn_attendance_no_id.setEnabled(True)
            self.btn_booklet.setEnabled(True)
            self.btn_scanner_text.setEnabled(True)
            self.btn_del_plan.setEnabled(True)
            self.thread = GetFormCodeClass(parent = None, index = 0)
            self.thread.plan_date = self.dateEdit_create_plan.date()
            self.thread.plan_school = self.g_plan_comboBox.currentText()
            self.thread.start()
            self.thread.ps1_formsignal.connect(self.ps1_form.setText)
            self.thread.ps2_formsignal.connect(self.ps2_form.setText)
            self.thread.js_formsignal.connect(self.js_form.setText)
            self.thread.test_4_formsignal.connect(self.test_4_form.setText)
            self.thread.ps1_formsignal.connect(self.edit_ps1_form.setCurrentText)
            self.thread.ps2_formsignal.connect(self.edit_ps2_form.setCurrentText)
            self.thread.js_formsignal.connect(self.edit_js_form.setCurrentText)
            self.thread.test_4_formsignal.connect(self.edit_test_4_form.setCurrentText)
            self.thread.label_22signal.connect(self.label_22.setText)
            self.ps1_form.setVisible(True)
            self.ps2_form.setVisible(True)
            self.js_form.setVisible(True)
            self.test_4_form.setVisible(True)
            self.label_22.setVisible(True)
        elif self.g_plan_comboBox.currentText() != "Okul Seç" and self.g_plan_comboBox.currentText() != "Sınav Bulunamadı!" and self.attendance_check_checkBox.isChecked():
            self.export_attendance()
        else:
            self.label_22.setText("Doğru veri seçin!")
            self.label_22.setVisible(True)
            self.label_23.setVisible(False)
        
    def update_same_form_codes(self, same_code):
        all_form_codes_for_plan = fcf.get_all_form_codes()
        ps1_form_codes = sorted(all_form_codes_for_plan[1])
        ps2_form_codes = sorted(all_form_codes_for_plan[2])
        js_form_codes = sorted(all_form_codes_for_plan[3])
        test_4_form_codes = sorted(all_form_codes_for_plan[4])
        new_ps1_form_codes = []
        for i in ps1_form_codes:
            if same_code != i[:-1]:
                new_ps1_form_codes.append(i)
        self.edit_ps1_form.clear()
        self.edit_ps1_form.addItems(sorted(new_ps1_form_codes))
        new_ps2_form_codes = []
        for i in ps2_form_codes:
            if same_code != i[:-1]:
                new_ps2_form_codes.append(i)
        self.edit_ps2_form.clear()
        self.edit_ps2_form.addItems(sorted(new_ps2_form_codes))
        new_js_form_codes = []
        for i in js_form_codes:
            if same_code != i[:-1]:
                new_js_form_codes.append(i)
        self.edit_js_form.clear()
        self.edit_js_form.addItems(sorted(new_js_form_codes))
        new_test_4_form_codes = []
        for i in test_4_form_codes:
            if same_code != i[:-1]:
                new_test_4_form_codes.append(i)
        self.edit_test_4_form.clear()
        self.edit_test_4_form.addItems(sorted(new_test_4_form_codes))
    
    def create_test_1optic(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_23.setText("Yükleniyor...")
            self.label_23.setVisible(True)
            self.thread = test_1OpticClass(parent = None, index = 0)
            self.thread.save_directory = str(upload_file)
            self.thread.plan_date = self.dateEdit_create_plan.date()
            self.thread.plan_school = self.g_plan_comboBox.currentText()
            self.thread.ps1_old_form = self.ps1_form.text()
            self.thread.ps2_old_form = self.ps2_form.text()
            self.thread.ps1_new_form = self.edit_ps1_form.currentText()
            self.thread.ps2_new_form = self.edit_ps2_form.currentText()
            self.thread.hp_printer = self.radioButton_hp.isChecked()
            self.thread.riso_printer = self.radioButton_riso.isChecked()
            self.thread.xerox_printer = self.radioButton_xerox.isChecked()
            self.thread.other_printer = self.radioButton_other.isChecked()
            self.thread.start()
            self.thread.same_form_short_ps1signal.connect(self.update_same_form_codes)
            self.thread.same_form_short_ps2signal.connect(self.update_same_form_codes)
            self.thread.label_23signal.connect(self.label_23.setText)
            self.label_23.setVisible(True)

    def create_test_3_optic(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_23.setText("Yükleniyor...")
            self.label_23.setVisible(True)
            self.thread = test_3OpticClass(parent = None, index = 0)
            self.thread.save_directory = str(upload_file)
            self.thread.plan_date = self.dateEdit_create_plan.date()
            self.thread.plan_school = self.g_plan_comboBox.currentText()
            self.thread.js_old_form = self.js_form.text()
            self.thread.js_new_form = self.edit_js_form.currentText()
            self.thread.hp_printer = self.radioButton_hp.isChecked()
            self.thread.riso_printer = self.radioButton_riso.isChecked()
            self.thread.xerox_printer = self.radioButton_xerox.isChecked()
            self.thread.other_printer = self.radioButton_other.isChecked()
            self.thread.start()
            self.thread.same_form_short_jssignal.connect(self.update_same_form_codes)
            self.thread.label_23signal.connect(self.label_23.setText)
            self.label_23.setVisible(True)
    
    def create_test_4_optic(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_23.setText("Yükleniyor...")
            self.label_23.setVisible(True)
            self.thread = test_4OpticClass(parent = None, index = 0)
            self.thread.save_directory = str(upload_file)
            self.thread.plan_date = self.dateEdit_create_plan.date()
            self.thread.plan_school = self.g_plan_comboBox.currentText()
            self.thread.test_4_old_form = self.test_4_form.text()
            self.thread.test_4_new_form = self.edit_test_4_form.currentText()
            self.thread.hp_printer = self.radioButton_hp.isChecked()
            self.thread.riso_printer = self.radioButton_riso.isChecked()
            self.thread.xerox_printer = self.radioButton_xerox.isChecked()
            self.thread.other_printer = self.radioButton_other.isChecked()
            self.thread.start()
            self.thread.label_23signal.connect(self.label_23.setText)
            self.thread.same_form_short_test_4signal.connect(self.update_same_form_codes)
            self.label_23.setVisible(True)

    def create_attendance_sheet_with_id(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_23.setText("Yükleniyor...")
            self.label_23.setVisible(True)
            self.thread = AttendanceSheetIDClass(parent = None, index = 0)
            self.thread.save_directory = str(upload_file)
            self.thread.plan_date = self.dateEdit_create_plan.date()
            self.thread.plan_school = self.g_plan_comboBox.currentText()
            self.thread.attendance_tr = self.radioButton_attendance_tr.isChecked()
            self.thread.attendance_eng = self.radioButton_attendance_eng.isChecked()
            self.thread.start()
            self.thread.label_23signal.connect(self.label_23.setText)
            self.label_23.setVisible(True)
        
    def create_attendance_sheet_without_id(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_23.setText("Yükleniyor...")
            self.label_23.setVisible(True)
            self.thread = AttendanceSheetNoIDClass(parent = None, index = 0)
            self.thread.save_directory = str(upload_file)
            self.thread.plan_date = self.dateEdit_create_plan.date()
            self.thread.plan_school = self.g_plan_comboBox.currentText()
            self.thread.attendance_tr = self.radioButton_attendance_tr.isChecked()
            self.thread.attendance_eng = self.radioButton_attendance_eng.isChecked()
            self.thread.start()
            self.thread.label_23signal.connect(self.label_23.setText)
            self.label_23.setVisible(True)
    
    def create_booklet(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_23.setText("Yükleniyor...")
            self.label_23.setVisible(True)
            self.thread = BookletClass(parent = None, index = 0)
            self.thread.save_directory = str(upload_file)
            self.thread.plan_date = self.dateEdit_create_plan.date()
            self.thread.plan_school = self.g_plan_comboBox.currentText()
            self.thread.start()
            self.thread.label_23signal.connect(self.label_23.setText)
            self.label_23.setVisible(True)

    def plan_to_scanner_text(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_23.setText("Yükleniyor...")
            self.label_23.setVisible(True)
            self.thread = PlantoTextClass(parent = None, index = 0)
            self.thread.save_directory = str(upload_file)
            self.thread.plan_date = self.dateEdit_create_plan.date()
            self.thread.plan_school = self.g_plan_comboBox.currentText()
            self.thread.start()
            self.thread.label_23signal.connect(self.label_23.setText)
            self.label_23.setVisible(True)

    def delete_plan(self):
        self.label_23.setText("Yükleniyor...")
        self.label_23.setVisible(True)
        dialog = PlanDeleteConfirmationDialogUi()
        dialog.date.setText(self.dateEdit_create_plan.date().toString('dd-MM-yyyy'))
        dialog.inst.setText(self.g_plan_comboBox.currentText())
        dialog.exec_()
        selected_date = self.dateEdit_create_plan.date().toString('dd-MM-yyyy')
        self.g_plan_comboBox.clear()
        school_list_by_date = gslbd.get_school_list_by_date(selected_date)
        if len(school_list_by_date) == 0:
            self.g_plan_comboBox.addItems(['Sınav Bulunamadı!'])
        else:
            self.g_plan_comboBox.addItems(sorted(gslbd.get_school_list_by_date(selected_date)))
        self.label_23.setText("Seçili Plan Silindi!")
        self.label_23.setVisible(True)
        
    def create_ps1_dn(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_23.setText("Yükleniyor...")
            self.label_23.setVisible(True)
            self.thread = PS1DeliveryNoteClass(parent = None, index = 0)
            self.thread.form_code = self.edit_ps1_form.currentText()
            self.thread.save_directory = str(upload_file)
            self.thread.plan_date = self.dateEdit_create_plan.date()
            self.thread.plan_school = self.g_plan_comboBox.currentText()
            self.thread.start()
            self.thread.label_23signal.connect(self.label_23.setText)
            self.label_23.setVisible(True)
    
    def create_ps2_dn(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_23.setText("Yükleniyor...")
            self.label_23.setVisible(True)
            self.thread = PS2DeliveryNoteClass(parent = None, index = 0)
            self.thread.form_code = self.edit_ps2_form.currentText()
            self.thread.save_directory = str(upload_file)
            self.thread.plan_date = self.dateEdit_create_plan.date()
            self.thread.plan_school = self.g_plan_comboBox.currentText()
            self.thread.start()
            self.thread.label_23signal.connect(self.label_23.setText)
            self.label_23.setVisible(True)
            
    def create_js_dn(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_23.setText("Yükleniyor...")
            self.label_23.setVisible(True)
            self.thread = JSDeliveryNoteClass(parent = None, index = 0)
            self.thread.form_code = self.edit_js_form.currentText()
            self.thread.save_directory = str(upload_file)
            self.thread.plan_date = self.dateEdit_create_plan.date()
            self.thread.plan_school = self.g_plan_comboBox.currentText()
            self.thread.start()
            self.thread.label_23signal.connect(self.label_23.setText)
            self.label_23.setVisible(True)
    
    def create_test_4_dn(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_23.setText("Yükleniyor...")
            self.label_23.setVisible(True)
            self.thread = test_4DeliveryNoteClass(parent = None, index = 0)
            self.thread.form_code = self.edit_test_4_form.currentText()
            self.thread.save_directory = str(upload_file)
            self.thread.plan_date = self.dateEdit_create_plan.date()
            self.thread.plan_school = self.g_plan_comboBox.currentText()
            self.thread.start()
            self.thread.label_23signal.connect(self.label_23.setText)
            self.label_23.setVisible(True)
    
    def attendance_check_checked(self):
        if self.attendance_check_checkBox.isChecked():
            self.g_plan_test_type_comboBox.setVisible(True)
            self.btn_upload_attendance_text.setVisible(True)
        else:
            self.g_plan_test_type_comboBox.setVisible(False)
            self.btn_upload_attendance_text.setVisible(False)

    def upload_attendance_text(self):
        upload_file = QFileDialog.getOpenFileName(self, "Metin Belgesi Seç", sfl.get(), "Txt File (*.txt)")
        sfl.save(upload_file)
        if upload_file:
            self.label_97.setText(upload_file[0])

    def export_attendance(self):
        save_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save(save_file)
        if save_file:
            self.label_23.setText("Yükleniyor...")
            self.label_23.setVisible(True)
            self.thread = ExportAttendanceClass(parent = None, index = 0)
            self.thread.file_directory = self.label_97.text()
            self.thread.institution = self.g_plan_comboBox.currentText()
            self.thread.test_date = self.dateEdit_create_plan.date()
            self.thread.test_type = self.g_plan_test_type_comboBox.currentText()
            self.thread.save_directory = save_file
            self.thread.start()
            self.thread.label_23signal.connect(self.label_23.setText)
            self.label_23.setVisible(True)
    #Get, create, delete Plan Part END
    #################################################################################


    def plan_logic_changed(self):
        if self.logic_plan_comboBox.currentText() == 'Tüm Öğrenciler A\'dan Z\'ye (PBT)':
            self.total_class_spinBox.setVisible(True)
        elif self.logic_plan_comboBox.currentText() == 'Aynı Sınıf A\'dan Z\'ye (CBT)':
            self.total_class_spinBox.setVisible(True)
        else:
            self.total_class_spinBox.setVisible(False)
    
    def converted_plan_df(self,values):
        dialog = MakePlan(values)
        dialog.exec_()
        
    def open_plan_dialog(self):
        upload_file = QFileDialog.getOpenFileName(self, "Veri Exceli Seç", sfl.get(), "Excel File (*.xls *.xlsx)")
        sfl.save(upload_file)
        if upload_file:
            self.plan_set_file_path.setText(upload_file[0])
        
    def run_plan_dialog(self):
        self.thread = ConvertPlanClass(parent = None, index = 0)
        self.thread.file = self.plan_set_file_path.text()
        self.thread.school = self.convert_plan_comboBox.currentText()
        self.thread.plan_logic = self.logic_plan_comboBox.currentText()
        self.thread.total_class = self.total_class_spinBox.value()
        self.thread.start()
        self.thread.df_signal.connect(self.converted_plan_df)

    def open_plan_control(self):
        upload_file = QFileDialog.getOpenFileName(self, "Veri Exceli Seç", sfl.get(), "Excel File (*.xls *.xlsx)")
        sfl.save(upload_file)
        if upload_file:
            self.plan_set_file_path_2.setText(upload_file[0])

    def get_plan_control(self):
        from main_funcs.mixed.make_plan import reshape_dataframe
        file = self.plan_set_file_path_2.text()
        df = reshape_dataframe(file)
        grade_list = df['class'].str[0].unique()
        grade_list = list(map(lambda x: x.replace('H', 'Haz'), grade_list))
        new_df = pd.DataFrame(grade_list,columns=['grade'])
        new_df['logic'] = 'Plan Mantığı Seç'
        new_df['school'] = 'Okul Seç'
        new_df['total class'] = ''
        choices = ['Plan Mantığı Seç','Aynı Sınıf A\'dan Z\'ye (PBT)','Aynı Sınıf A\'dan Z\'ye (CBT)','Tüm Öğrenciler A\'dan Z\'ye (PBT)','Sınıf Bölme (PBT)']
        all_school_list = sorted(sm.get_combobox_school())
        all_school_list.insert(0,'Okul Seç')
        self.model = PandasModelPlan(new_df)
        self.tableView_first.setModel(self.model)
        self.tableView_first.setItemDelegateForColumn(1, Delegate(self,choices))
        self.tableView_first.setItemDelegateForColumn(2, Delegate(self,all_school_list))
        self.tableView_first.setColumnWidth(1, 350)
        self.tableView_first.setColumnWidth(2, 350)
        for row in range(len(df)):
            self.tableView_first.openPersistentEditor(self.model.index(row, 1))
            self.tableView_first.openPersistentEditor(self.model.index(row, 2))
    
    def plan_logic_changed_2(self):
        if self.logic_plan_comboBox_2.currentText() == 'Tüm Öğrenciler A\'dan Z\'ye (PBT)':
            self.total_class_spinBox_2.setVisible(True)
        elif self.logic_plan_comboBox_2.currentText() == 'Aynı Sınıf A\'dan Z\'ye (CBT)':
            self.total_class_spinBox_2.setVisible(True)
        else:
            self.total_class_spinBox_2.setVisible(False)

    def divide_plan_checked(self):
        if self.whole_plan_checkBox.isChecked():
            self.tableView_first.setVisible(True)
            self.logic_plan_comboBox_2.setVisible(False)
            self.convert_plan_2_comboBox.setVisible(False)
            self.total_class_spinBox_2.setVisible(False)
        else:
            self.tableView_first.setVisible(False)
            self.logic_plan_comboBox_2.setVisible(True)
            self.convert_plan_2_comboBox.setVisible(True)
            if self.logic_plan_comboBox_2.currentText() == 'Tüm Öğrenciler A\'dan Z\'ye (PBT)':
                self.total_class_spinBox_2.setVisible(True)
            elif self.logic_plan_comboBox_2.currentText() == 'Aynı Sınıf A\'dan Z\'ye (CBT)':
                self.total_class_spinBox_2.setVisible(True)
            else:
                self.total_class_spinBox_2.setVisible(False)


    #################################################################################
    #Upload IOPS Result Part START
    def open_iops_file(self):
        radiobutton_control = [self.radioButton_iops_ps1.isChecked(),self.radioButton_iops_ps2.isChecked(),self.radioButton_iops_js.isChecked(),
                               self.radioButton_iops_test_4.isChecked()]
        if self.u_iops_comboBox.currentText() != "Okul Seç" and self.edit_iops_form.currentText() != "Form Code Seç" and any(radiobutton_control) == True:
            upload_file = QFileDialog.getOpenFileName(self, "IOPS Exceli Seç", sfl.get(), "Excel File (*.xls)")
            sfl.save(upload_file)
            if upload_file:
                self.label_upload_file_name_2.setText(upload_file[0])
                self.label_upload_file_name_2.setVisible(True)
                self.btn_upload_iops.setEnabled(True)
                self.btn_upload_iops_test_4_no_class.setEnabled(True)
        else:
            self.label_41.setText("Önce doğru verileri seçin")
            self.label_41.setVisible(True)
            
    def all_result_list_iops(self, iops_result_list):
        self.label_6.setText("Yükleniyor...")
        self.label_6.setVisible(True)
        iops_true_list = iops_result_list[0]
        iops_false_list = iops_result_list[1]
        if len(iops_false_list) > 0:
            iops_new_false_list = [('Ülke', 'Şehir', 'Okul', 'Form Code', 'Ana Sınav Tarihi', 'Sınav Tarihi', 'Soyad', 'Ad', 'TC No', 'Sınıf')]
            iops_new_false_list.extend(iops_false_list)
            self.label_6.setText("Yükleme başarısız. Yukarıdaki "+str(len(iops_false_list))+" öğrenci sistemde kayıtlı. Düzeltilmesi gerekiyor!")
            self.u_iops_table.setRowCount(0)
            for row_number, row_data in enumerate(iops_new_false_list):
                self.u_iops_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.u_iops_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        else:
            iops_new_true_list = [('Ülke', 'Şehir', 'Okul', 'Form Code', 'Ana Sınav Tarihi', 'Sınav Tarihi', 'Soyad', 'Ad', 'TC No', 'Sınıf')]
            iops_new_true_list.extend(iops_true_list)
            self.label_6.setText(str(len(iops_true_list))+" öğrenci sorunsuz aktarıldı!")
            self.u_iops_table.setRowCount(0)
            for row_number, row_data in enumerate(iops_new_true_list):
                self.u_iops_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.u_iops_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def upload_iops_file(self):
        radiobutton_control = [self.radioButton_iops_ps1.isChecked(),self.radioButton_iops_ps2.isChecked(),self.radioButton_iops_js.isChecked(),
                               self.radioButton_iops_test_4.isChecked()]
        if self.u_iops_comboBox.currentText() != "Okul Seç" and self.edit_iops_form.currentText() != "Form Code Seç" and any(radiobutton_control) == True:
            self.label_41.setText("Yükleniyor...")
            self.label_41.setVisible(True)
            self.thread = UploadIOPSClass(parent = None, index = 0)
            self.thread.test_type_ps1 = self.radioButton_iops_ps1.isChecked()
            self.thread.test_type_ps2 = self.radioButton_iops_ps2.isChecked()
            self.thread.test_type_js = self.radioButton_iops_js.isChecked()
            self.thread.test_type_test_4 = self.radioButton_iops_test_4.isChecked()
            self.thread.upload_file = self.label_upload_file_name_2.text()
            self.thread.upload_date = self.dateEdit_upload_iops.date()
            self.thread.upload_school = self.u_iops_comboBox.currentText()
            self.thread.upload_form_code = self.edit_iops_form.currentText()
            self.thread.start()
            self.thread.label_41signal.connect(self.label_41.setText)
            self.thread.all_result_list_signal.connect(self.all_result_list_iops)
            self.dateEdit_upload_iops.setDateTime(self.current_date_time)
            self.u_iops_comboBox.setCurrentText('Okul seç')
            self.label_upload_file_name_2.setText('Dosya')
            self.label_41.setVisible(True)
        else:
            self.label_41.setText("Önce doğru verileri seçin")
            self.label_41.setVisible(True)
    
    def upload_iops_test_4_file(self):
        radiobutton_control = [self.radioButton_iops_ps1.isChecked(),self.radioButton_iops_ps2.isChecked(),self.radioButton_iops_js.isChecked(),
                               self.radioButton_iops_test_4.isChecked()]
        if self.u_iops_comboBox.currentText() != "Okul Seç" and self.edit_iops_form.currentText() != "Form Code Seç" and any(radiobutton_control) == True:
            self.label_41.setText("Yükleniyor...")
            self.label_41.setVisible(True)
            self.thread = UploadIOPStest_4Class(parent = None, index = 0)
            self.thread.test_type_test_4 = self.radioButton_iops_test_4.isChecked()
            self.thread.upload_file = self.label_upload_file_name_2.text()
            self.thread.upload_date = self.dateEdit_upload_iops.date()
            self.thread.upload_school = self.u_iops_comboBox.currentText()
            self.thread.upload_form_code = self.edit_iops_form.currentText()
            self.thread.start()
            self.thread.label_41signal.connect(self.label_41.setText)
            self.thread.all_result_list_signal_1.connect(self.all_result_list_iops)
            self.dateEdit_upload_iops.setDateTime(self.current_date_time)
            self.u_iops_comboBox.setCurrentText('Okul seç')
            self.label_upload_file_name_2.setText('Dosya')
            self.label_41.setVisible(True)
        else:
            self.label_41.setText("Önce doğru verileri seçin")
            self.label_41.setVisible(True)

    def hide_iops_info_label(self):
        self.label_41.setVisible(False)
        self.btn_upload_iops_test_4_no_class.setVisible(False)
        self.btn_iops_opt_student.setVisible(False)
    
    def iops_test_type_selected(self):
        all_form_codes_for_result = fcf.get_all_form_codes()
        ps1_form_codes = sorted(all_form_codes_for_result[1])
        ps2_form_codes = sorted(all_form_codes_for_result[2])
        js_form_codes = sorted(all_form_codes_for_result[3])
        test_4_form_codes = sorted(all_form_codes_for_result[4])
        if self.radioButton_iops_ps1.isChecked():
            self.edit_iops_form.clear()
            self.edit_iops_form.addItems(sorted(ps1_form_codes))
            self.btn_upload_iops_test_4_no_class.setVisible(False)
            self.btn_iops_opt_student.setVisible(False)
            if self.checkBox_iops_make_up.isChecked():
                self.iops_upload_school_changed()
        if self.radioButton_iops_ps2.isChecked():
            self.edit_iops_form.clear()
            self.edit_iops_form.addItems(sorted(ps2_form_codes))
            self.btn_upload_iops_test_4_no_class.setVisible(False)
            self.btn_iops_opt_student.setVisible(False)
            if self.checkBox_iops_make_up.isChecked():
                self.iops_upload_school_changed()
        if self.radioButton_iops_js.isChecked():
            self.edit_iops_form.clear()
            self.edit_iops_form.addItems(sorted(js_form_codes))
            self.btn_upload_iops_test_4_no_class.setVisible(False)
            self.btn_iops_opt_student.setVisible(False)
            if self.checkBox_iops_make_up.isChecked():
                self.iops_upload_school_changed()
        if self.radioButton_iops_test_4.isChecked():
            self.edit_iops_form.clear()
            self.edit_iops_form.addItems(sorted(test_4_form_codes))
            self.btn_upload_iops_test_4_no_class.setVisible(True)
            self.btn_iops_opt_student.setVisible(True)
            if self.checkBox_iops_make_up.isChecked():
                self.iops_upload_school_changed()
        self.u_iops_table.clear()
        iops_new_false_list = [('Ülke', 'Şehir', 'Okul', 'Form Code', 'Ana Sınav Tarihi', 'Sınav Tarihi', 'Soyad', 'Ad', 'TC No', 'Sınıf')]
        self.u_iops_table.setRowCount(20)
        for row_number, row_data in enumerate(iops_new_false_list):
            self.u_iops_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.u_iops_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.label_41.setVisible(False)
        self.label_6.setVisible(False)
        self.label_upload_file_name_2.setVisible(False)
        self.u_iops_comboBox.setCurrentText("Okul Seç")
    
    def iops_upload_school_changed(self):
        if self.iops_upload_result_comboBox.currentText() == 'Okul Seç':
            self.iops_upload_date_comboBox.clear()
            self.iops_upload_date_comboBox.addItem('Tarih Seç')
            self.iops_upload_date_comboBox.setCurrentText('Tarih Seç')
        else:
            selected_school = self.iops_upload_result_comboBox.currentText()
            if selected_school in sm.get_combobox_school():
                self.iops_upload_date_comboBox.clear()
                school_list_by_date = gslbdr.get_date_list_by_school(selected_school)
                if self.radioButton_iops_ps1.isChecked():
                    if len(school_list_by_date[0]) == 0:
                        self.iops_upload_date_comboBox.addItems(['Sınav Bulunamadı!'])
                    else:
                        self.iops_upload_date_comboBox.addItems(self.date_list_sort_reversed(list(set(school_list_by_date[0]))))
                if self.radioButton_iops_ps2.isChecked():
                    if len(school_list_by_date[1]) == 0:
                        self.iops_upload_date_comboBox.addItems(['Sınav Bulunamadı!'])
                    else:
                        self.iops_upload_date_comboBox.addItems(self.date_list_sort_reversed(list(set(school_list_by_date[1]))))
                if self.radioButton_iops_js.isChecked():
                    if len(school_list_by_date[3]) == 0:
                        self.iops_upload_date_comboBox.addItems(['Sınav Bulunamadı!'])
                    else:
                        self.iops_upload_date_comboBox.addItems(self.date_list_sort_reversed(list(set(school_list_by_date[3]))))
                if self.radioButton_iops_test_4.isChecked():
                    if len(school_list_by_date[5]) == 0:
                        self.iops_upload_date_comboBox.addItems(['Sınav Bulunamadı!'])
                    else:
                        self.iops_upload_date_comboBox.addItems(self.date_list_sort_reversed(list(set(school_list_by_date[5]))))
                

                self.label_41.setVisible(False)
                self.label_6.setVisible(False)

    def iops_upload_make_up_check_state(self):
        if self.checkBox_iops_make_up.isChecked():
            self.iops_upload_result_comboBox.setVisible(True)
            self.iops_upload_date_comboBox.setVisible(True)
            self.u_iops_comboBox.setVisible(False)
            self.dateEdit_upload_iops.setVisible(False)
            self.iops_upload_result_comboBox.clear()
            self.iops_upload_result_comboBox.addItems(self.all_schools)
            self.iops_upload_result_comboBox.setCurrentText('Okul seç')
            self.iops_upload_date_comboBox.clear()
            self.iops_upload_date_comboBox.addItem('Tarih Seç')
            self.iops_upload_date_comboBox.setCurrentText('Tarih Seç')
        else:
            self.iops_upload_result_comboBox.setVisible(False)
            self.iops_upload_date_comboBox.setVisible(False)
            self.u_iops_comboBox.setVisible(True)
            self.dateEdit_upload_iops.setVisible(True)
    #Upload IOPS Result Part END
    #################################################################################

    #################################################################################
    #Upload Roster Result Part START
    def open_roster_file(self):
        radiobutton_control = [self.radioButton_roster_ps1.isChecked(),self.radioButton_roster_ps2.isChecked(),self.radioButton_roster_js.isChecked(),
                               self.radioButton_roster_test_4.isChecked(),self.radioButton_roster_pspk.isChecked(),self.radioButton_roster_jspk.isChecked()]
        if self.u_roster_comboBox.currentText() != "Okul Seç" and self.edit_roster_form.currentText() != "Form Code Seç" and any(radiobutton_control) == True:
            upload_file = QFileDialog.getOpenFileName(self, "Program Workshop Exceli Seç", sfl.get(), "Excel File (*.xlsx)")
            sfl.save(upload_file)
            if upload_file:
                self.label_upload_file_name_3.setText(upload_file[0])
                self.label_upload_file_name_3.setVisible(True)
                self.btn_upload_roster.setEnabled(True)
                self.btn_upload_roster_test_4_no_class.setEnabled(True)
        else:
            self.label_47.setText("Önce doğru verileri seçin")
            self.label_47.setVisible(True)
        
    def all_result_list_roster(self, roster_result_list):
        self.label.setText("Yükleniyor...")
        self.label.setVisible(True)
        roster_true_list = roster_result_list[0]
        roster_false_list = roster_result_list[1]
        if len(roster_false_list) > 0:
            roster_new_false_list = [('Ülke', 'Şehir', 'Okul', 'Form Code', 'Ana Sınav Tarihi', 'Sınav Tarihi', 'Soyad', 'Ad', 'TC No', 'Sınıf')]
            roster_new_false_list.extend(roster_false_list)
            self.label.setText("Yükleme başarısız. Yukarıdaki "+str(len(roster_false_list))+" öğrenci sistemde kayıtlı. Düzeltilmesi gerekiyor!")
            self.u_roster_table.setRowCount(0)
            for row_number, row_data in enumerate(roster_new_false_list):
                self.u_roster_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.u_roster_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        else:
            roster_new_true_list = [('Ülke', 'Şehir', 'Okul', 'Form Code', 'Ana Sınav Tarihi', 'Sınav Tarihi', 'Soyad', 'Ad', 'TC No', 'Sınıf')]
            roster_new_true_list.extend(roster_true_list)
            self.label.setText(str(len(roster_true_list))+" öğrenci sorunsuz aktarıldı!")
            self.u_roster_table.setRowCount(0)
            for row_number, row_data in enumerate(roster_new_true_list):
                self.u_roster_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.u_roster_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            
    def upload_roster_file(self):
        radiobutton_control = [self.radioButton_roster_ps1.isChecked(),self.radioButton_roster_ps2.isChecked(),self.radioButton_roster_js.isChecked(),
                               self.radioButton_roster_test_4.isChecked(),self.radioButton_roster_pspk.isChecked(),self.radioButton_roster_jspk.isChecked()]
        if self.u_roster_comboBox.currentText() != "Okul Seç" and self.edit_roster_form.currentText() != "Form Code Seç" and any(radiobutton_control) == True:
            self.label_47.setText("Yükleniyor...")
            self.label_47.setVisible(True)
            self.thread = UploadRosterClass(parent = None, index = 0)
            self.thread.test_type_ps1 = self.radioButton_roster_ps1.isChecked()
            self.thread.test_type_ps2 = self.radioButton_roster_ps2.isChecked()
            self.thread.test_type_js = self.radioButton_roster_js.isChecked()
            self.thread.test_type_test_4 = self.radioButton_roster_test_4.isChecked()
            self.thread.test_type_pspk = self.radioButton_roster_pspk.isChecked()
            self.thread.test_type_jspk = self.radioButton_roster_jspk.isChecked()
            self.thread.upload_file = self.label_upload_file_name_3.text()
            self.thread.upload_date = self.dateEdit_upload_roster.date()
            self.thread.upload_school = self.u_roster_comboBox.currentText()
            self.thread.upload_form_code = self.edit_roster_form.currentText()
            self.thread.start()
            self.thread.label_47signal.connect(self.label_47.setText)
            self.thread.all_result_list_signal2.connect(self.all_result_list_roster)
            self.dateEdit_upload_roster.setDateTime(self.current_date_time)
            self.u_roster_comboBox.setCurrentText('Okul seç')
            self.label_upload_file_name_3.setText('Dosya')
            self.label_47.setVisible(True)          
        else:
            self.label_47.setText("Önce doğru verileri seçin")
            self.label_47.setVisible(True)
    
    def upload_roster_test_4_file(self):
        radiobutton_control = [self.radioButton_roster_ps1.isChecked(),self.radioButton_roster_ps2.isChecked(),self.radioButton_roster_js.isChecked(),
                               self.radioButton_roster_test_4.isChecked(),self.radioButton_roster_pspk.isChecked(),self.radioButton_roster_jspk.isChecked()]
        if self.u_roster_comboBox.currentText() != "Okul Seç" and self.edit_roster_form.currentText() != "Form Code Seç" and any(radiobutton_control) == True:
            self.label_47.setText("Yükleniyor...")
            self.label_47.setVisible(True)
            self.thread = UploadRostertest_4Class(parent = None, index = 0)
            self.thread.test_type_test_4 = self.radioButton_roster_test_4.isChecked()
            self.thread.upload_file = self.label_upload_file_name_3.text()
            self.thread.upload_date = self.dateEdit_upload_roster.date()
            self.thread.upload_school = self.u_roster_comboBox.currentText()
            self.thread.upload_form_code = self.edit_roster_form.currentText()
            self.thread.start()
            self.thread.label_47signal.connect(self.label_47.setText)
            self.thread.all_result_list_signal_3.connect(self.all_result_list_roster)
            self.dateEdit_upload_roster.setDateTime(self.current_date_time)
            self.u_roster_comboBox.setCurrentText('Okul seç')
            self.label_upload_file_name_3.setText('Dosya')
            self.label_47.setVisible(True)        
        else:
            self.label_47.setText("Önce doğru verileri seçin")
            self.label_47.setVisible(True)

    def hide_roster_info_label(self):
        self.label_47.setVisible(False)
        self.label.setVisible(False)
    
    def roster_test_type_selected(self):
        all_form_codes_for_result = fcf.get_all_form_codes()
        ps1_form_codes = sorted(all_form_codes_for_result[1])
        ps2_form_codes = sorted(all_form_codes_for_result[2])
        js_form_codes = sorted(all_form_codes_for_result[3])
        test_4_form_codes = sorted(all_form_codes_for_result[4])
        pspk_form_codes = sorted(all_form_codes_for_result[5])
        jspk_form_codes = sorted(all_form_codes_for_result[6])
        if self.radioButton_roster_ps1.isChecked():
            self.edit_roster_form.clear()
            self.edit_roster_form.addItems(sorted(ps1_form_codes))
            self.btn_upload_roster_test_4_no_class.setVisible(False)
            self.btn_roster_opt_student.setVisible(False)
        if self.radioButton_roster_ps2.isChecked():
            self.edit_roster_form.clear()
            self.edit_roster_form.addItems(sorted(ps2_form_codes))
            self.btn_upload_roster_test_4_no_class.setVisible(False)
            self.btn_roster_opt_student.setVisible(False)
        if self.radioButton_roster_js.isChecked():
            self.edit_roster_form.clear()
            self.edit_roster_form.addItems(sorted(js_form_codes))
            self.btn_upload_roster_test_4_no_class.setVisible(False)
            self.btn_roster_opt_student.setVisible(False)
        if self.radioButton_roster_test_4.isChecked():
            self.edit_roster_form.clear()
            self.edit_roster_form.addItems(sorted(test_4_form_codes))
            self.btn_upload_roster_test_4_no_class.setVisible(True)
            self.btn_roster_opt_student.setVisible(True)
        if self.radioButton_roster_pspk.isChecked():
            self.edit_roster_form.clear()
            self.edit_roster_form.addItems(sorted(pspk_form_codes))
            self.btn_upload_roster_test_4_no_class.setVisible(False)
            self.btn_roster_opt_student.setVisible(False)
        if self.radioButton_roster_jspk.isChecked():
            self.edit_roster_form.clear()
            self.edit_roster_form.addItems(sorted(jspk_form_codes))
            self.btn_upload_roster_test_4_no_class.setVisible(False)
            self.btn_roster_opt_student.setVisible(False)
        self.u_roster_table.clear()
        roster_new_false_list = [('Ülke', 'Şehir', 'Okul', 'Form Code', 'Ana Sınav Tarihi', 'Sınav Tarihi', 'Soyad', 'Ad', 'TC No', 'Sınıf')]
        self.u_roster_table.setRowCount(20)
        for row_number, row_data in enumerate(roster_new_false_list):
            self.u_roster_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.u_roster_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.label_47.setVisible(False)
        self.label.setVisible(False)
        self.label_upload_file_name_3.setVisible(False)
        self.u_roster_comboBox.setCurrentText("Okul Seç")
    #Upload Roster Result Part END
    #################################################################################
    
    #################################################################################
    #Get Result Part START
    def date_list_sort_reversed(self,date_list):
        return [item.strftime('%d-%m-%Y') for item in sorted([datetime.strptime(item, '%d-%m-%Y') for item in date_list],reverse=True)]
    
    def get_school_date_changed_result(self):
        if self.get_result_comboBox.currentText() == 'Okul Seç':
            self.get_result_date_comboBox.clear()
            self.get_result_date_comboBox.addItem('Tarih Seç')
            self.get_result_date_comboBox.setCurrentText('Tarih Seç')
        else:
            if self.get_result_test_type_comboBox.currentText() == 'test_1 Step 1 & 2 & Speaking' or \
                self.get_result_test_type_comboBox.currentText() == 'test_3 Standard & Speaking':
                self.get_result_date_spk_comboBox.setVisible(True)
            else:
                self.get_result_date_spk_comboBox.setVisible(False)

            selected_school = self.get_result_comboBox.currentText()
            if selected_school in sm.get_combobox_school():
                self.get_result_date_comboBox.clear()
                self.get_result_date_spk_comboBox.clear()
                school_list_by_date = gslbdr.get_date_list_by_school(selected_school)
                
                test_type_list = [
                        'test_1 Step 1',
                        'test_1 Step 2',
                        'test_1 Speaking',
                        'test_3 Standard',
                        'test_3 Speaking',
                        'test_4'
                        ]
                
                for t_index ,test_type_rep in enumerate(test_type_list):
                    if self.get_result_test_type_comboBox.currentText() == test_type_rep:
                        if len(school_list_by_date[t_index]) == 0:
                            self.get_result_date_comboBox.addItems(['Sınav Bulunamadı!'])
                        else:
                            self.get_result_date_comboBox.addItems(self.date_list_sort_reversed(school_list_by_date[t_index]))
                            try:
                                self.get_result_date_comboBox.setCurrentText(get_result_selected_school)
                            except:
                                pass

                if self.get_result_test_type_comboBox.currentText() == 'test_1 Step 1 & 2':
                    if len(school_list_by_date[0])+len(school_list_by_date[1]) == 0:
                        self.get_result_date_comboBox.addItems(['Sınav Bulunamadı!'])
                    else:
                        self.get_result_date_comboBox.addItems(self.date_list_sort_reversed(list(set(school_list_by_date[0]+school_list_by_date[1]))))
                        try:
                            self.get_result_date_comboBox.setCurrentText(get_result_selected_school)
                        except:
                            pass

                if self.get_result_test_type_comboBox.currentText() == 'test_1 Step 1 & 2 & Speaking':
                    if len(school_list_by_date[0])+len(school_list_by_date[1]) == 0:
                        self.get_result_date_comboBox.addItems(['Sınav Bulunamadı!'])
                    else:
                        self.get_result_date_comboBox.addItems(self.date_list_sort_reversed(list(set(school_list_by_date[0]+school_list_by_date[1]))))
                        try:
                            self.get_result_date_comboBox.setCurrentText(get_result_selected_school)
                        except:
                            pass
                    if len(school_list_by_date[2]) == 0:
                        self.get_result_date_spk_comboBox.addItems(['Sınav Bulunamadı!'])
                    else:
                        self.get_result_date_spk_comboBox.addItems(self.date_list_sort_reversed(list(set(school_list_by_date[2]))))
                        try:
                            self.get_result_date_spk_comboBox.setCurrentText(get_result_selected_school)
                        except:
                            pass

                if self.get_result_test_type_comboBox.currentText() == 'test_3 Standard & Speaking':
                    if len(school_list_by_date[3]) == 0:
                        self.get_result_date_comboBox.addItems(['Sınav Bulunamadı!'])
                    else:
                        self.get_result_date_comboBox.addItems(self.date_list_sort_reversed(list(set(school_list_by_date[3]))))
                        try:
                            self.get_result_date_comboBox.setCurrentText(get_result_selected_school)
                        except:
                            pass
                    if len(school_list_by_date[4]) == 0:
                        self.get_result_date_spk_comboBox.addItems(['Sınav Bulunamadı!'])
                    else:
                        self.get_result_date_spk_comboBox.addItems(self.date_list_sort_reversed(list(set(school_list_by_date[4]))))
                        try:
                            self.get_result_date_spk_comboBox.setCurrentText(get_result_selected_school)
                        except:
                            pass
                    
                self.label_62.setVisible(False)
                self.label_15.setVisible(False)
    
    def all_result_list(self, result_list):
        self.label_62.setText("Yükleniyor...")
        self.label_62.setVisible(True)

        self.model = CheckablePandasModel(result_list)
        self.model.checkable_column = 0
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setFilterKeyColumn(-1)
        self.proxy_model.setSourceModel(self.model)
        self.proxy_model.setFilterCaseSensitivity(False)
        self.table_get_result.setModel(self.proxy_model)
        self.search_from_get_result.textChanged.connect(self.proxy_model.setFilterFixedString)
        self.table_get_result.horizontalHeader().resizeSection(0, 5)
        
        self.model.checklist_sig.connect(self.checked_row_list_result)
        
        self.label_62.setText(str(len(result_list))+" öğrenci listelendi!")
        self.label_62.setVisible(True)
        
    def checked_row_list_result(self,row_list):
        self.row_list_result = row_list
    
    def get_school_result(self):
        global get_result_selected_school
        if self.get_result_date_comboBox.currentText() != "Tarih Seç" and self.get_result_date_comboBox.currentText() != "Sınav Bulunamadı!" and self.get_result_comboBox.currentText() != "Okul Seç":
            get_result_selected_school = self.get_result_date_comboBox.currentText()
            self.thread = GetSchoolResultClass(parent = None, index = 0)
            self.thread.report_test_type = self.get_result_test_type_comboBox.currentText()
            self.thread.institution = self.get_result_comboBox.currentText()
            self.thread.main_date = self.get_result_date_comboBox.currentText()
            self.thread.speaking_main_date = self.get_result_date_spk_comboBox.currentText()
            self.thread.start()
            self.thread.label_15signal.connect(self.label_15.setText)
            self.thread.all_result_signal.connect(self.all_result_list)
            self.btn_turkish_report.setEnabled(True)
            self.btn_institutional_report.setEnabled(True)
            self.btn_class_table.setEnabled(True)
            self.btn_export_excel.setEnabled(True)
            self.btn_result_letter.setEnabled(True)
            self.btn_aio_digital.setEnabled(True)
            self.checkBox_iops_split.setEnabled(True)
        else:
            self.label_62.setText("Önce doğru verileri seçin")
            self.label_62.setVisible(True)
    
    def create_turkish_report(self):
        if self.get_result_date_comboBox.currentText() != "Tarih Seç" and self.get_result_date_comboBox.currentText() != "Sınav Bulunamadı!" and self.get_result_comboBox.currentText() != "Okul Seç":
            upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
            sfl.save_d(upload_file)
            if upload_file:
                self.proxy_model.setSortRole(Qt.InitialSortOrderRole)
                self.proxy_model.invalidate()
                self.search_from_get_result.clear()
                try:
                    self.row_list_result
                except:
                    self.row_list_result = []
                model = self.table_get_result.model()
                data = []
                for row in range(model.rowCount()):
                    data.append([])
                    for column in range(model.columnCount()):
                        if row in self.row_list_result:
                            index = model.index(row, column)
                            data[row].append(model.data(index))
                self.result_data = [tuple(item[1:]) for item in data if item != []]
                self.label_15.setText("Yükleniyor...")
                self.label_15.setVisible(True)
                self.label_65.setText(str(self.result_data))
                self.thread = CreateTurkishReportClass(parent = None, index = 0)
                self.thread.report_test_type = self.get_result_test_type_comboBox.currentText()
                self.thread.all = self.radioButton_all.isChecked()
                self.thread.selected = self.radioButton_selected.isChecked()
                self.thread.main_list = self.label_65.text()
                self.thread.printable = self.radioButton_printable.isChecked()
                self.thread.digital = self.radioButton_digital.isChecked()        
                self.thread.institution = self.get_result_comboBox.currentText()
                self.thread.main_date = self.get_result_date_comboBox.currentText()
                self.thread.save_directory = str(upload_file)
                self.thread.start()
                self.thread.label_15signal.connect(self.label_15.setText)
                self.label_15.setVisible(True)
        else:
            self.label_62.setText("Önce doğru verileri seçin")
            self.label_62.setVisible(True)
            
    def create_institutional_report(self):
        if self.get_result_date_comboBox.currentText() != "Tarih Seç" and self.get_result_date_comboBox.currentText() != "Sınav Bulunamadı!" and self.get_result_comboBox.currentText() != "Okul Seç":
            upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
            sfl.save_d(upload_file)
            if upload_file:
                self.label_15.setText("Yükleniyor...")
                self.label_15.setVisible(True)
                self.thread = CreateInstitutionalReportClass(parent = None, index = 0)
                self.thread.doc_type = 0
                self.thread.report_test_type = self.get_result_test_type_comboBox.currentText()
                self.thread.institution = self.get_result_comboBox.currentText()
                self.thread.main_date = self.get_result_date_comboBox.currentText()
                self.thread.save_directory = str(upload_file)
                self.thread.start()
                self.thread.label_15signal.connect(self.label_15.setText)
                self.label_15.setVisible(True)
        else:
            self.label_62.setText("Önce doğru verileri seçin")
            self.label_62.setVisible(True)
    
    def create_class_table(self):
        if self.get_result_date_comboBox.currentText() != "Tarih Seç" and self.get_result_date_comboBox.currentText() != "Sınav Bulunamadı!" and self.get_result_comboBox.currentText() != "Okul Seç":
            upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
            sfl.save_d(upload_file)
            if upload_file:
                self.proxy_model.setSortRole(Qt.InitialSortOrderRole)
                self.proxy_model.invalidate()
                self.search_from_get_result.clear()
                try:
                    self.row_list_result
                except:
                    self.row_list_result = []
                model = self.table_get_result.model()
                data = []
                for row in range(model.rowCount()):
                    data.append([])
                    for column in range(model.columnCount()):
                        if row in self.row_list_result:
                            index = model.index(row, column)
                            # We suppose data are strings
                            data[row].append(model.data(index))
                self.result_data = [tuple(item[1:]) for item in data if item != []]
                self.label_15.setText("Yükleniyor...")
                self.label_15.setVisible(True)
                self.label_65.setText(str(self.result_data))
                self.thread = CreateInstitutionalReportClass(parent = None, index = 0)
                self.thread.doc_type = 1
                self.thread.report_test_type = self.get_result_test_type_comboBox.currentText() 
                self.thread.all = self.radioButton_all.isChecked()
                self.thread.selected = self.radioButton_selected.isChecked()
                self.thread.main_list = self.label_65.text()   
                self.thread.institution = self.get_result_comboBox.currentText()
                self.thread.main_date = self.get_result_date_comboBox.currentText()
                self.thread.save_directory = str(upload_file)
                self.thread.logo_directory = ""
                self.thread.start() 
                self.thread.label_15signal.connect(self.label_15.setText)
                self.label_15.setVisible(True)
        else:
            self.label_62.setText("Önce doğru verileri seçin")
            self.label_62.setVisible(True)
            
    def export_score_excel(self):
        if self.get_result_date_comboBox.currentText() != "Tarih Seç" and self.get_result_date_comboBox.currentText() != "Sınav Bulunamadı!" and self.get_result_comboBox.currentText() != "Okul Seç":
            upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
            sfl.save_d(upload_file)
            if upload_file:
                self.label_15.setText("Yükleniyor...")
                self.label_15.setVisible(True)
                self.thread = ExportScoreExcelClass(parent = None, index = 0)
                self.thread.report_test_type = self.get_result_test_type_comboBox.currentText()   
                self.thread.institution = self.get_result_comboBox.currentText()
                self.thread.main_date = self.get_result_date_comboBox.currentText()
                self.thread.save_directory = str(upload_file)
                self.thread.start()
                self.thread.label_15signal.connect(self.label_15.setText)
                self.label_15.setVisible(True)
        else:
            self.label_62.setText("Önce doğru verileri seçin")
            self.label_62.setVisible(True)

    def create_result_letter(self):
        if self.get_result_date_comboBox.currentText() != "Tarih Seç" and self.get_result_date_comboBox.currentText() != "Sınav Bulunamadı!" and self.get_result_comboBox.currentText() != "Okul Seç":
            upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
            sfl.save_d(upload_file)
            if upload_file:
                self.label_15.setText("Yükleniyor...")
                self.label_15.setVisible(True)
                self.thread = CreateResultLetterClass(parent = None, index = 0)
                self.thread.institution = self.get_result_comboBox.currentText()
                self.thread.main_date = self.get_result_date_comboBox.currentText()
                self.thread.save_directory = str(upload_file)
                self.thread.person = self.person_name.text()
                self.thread.start()
                self.thread.label_15signal.connect(self.label_15.setText)
                self.label_15.setVisible(True)
        else:
            self.label_62.setText("Önce doğru verileri seçin")
            self.label_62.setVisible(True)
    
    def create_aio_digital_report(self):
        if self.get_result_date_comboBox.currentText() != "Tarih Seç" and self.get_result_date_comboBox.currentText() != "Sınav Bulunamadı!" and self.get_result_comboBox.currentText() != "Okul Seç":
            upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
            sfl.save_d(upload_file)
            if upload_file:
                self.proxy_model.setSortRole(Qt.InitialSortOrderRole)
                self.proxy_model.invalidate()
                self.search_from_get_result.clear()
                try:
                    self.row_list_result
                except:
                    self.row_list_result = []
                model = self.table_get_result.model()
                data = []
                for row in range(model.rowCount()):
                    data.append([])
                    for column in range(model.columnCount()):
                        if row in self.row_list_result:
                            index = model.index(row, column)
                            data[row].append(model.data(index))
                self.result_data = [tuple(item[1:]) for item in data if item != []]
                self.label_15.setText("Yükleniyor...")
                self.label_15.setVisible(True)
                self.label_65.setText(str(self.result_data))
                self.thread = CreateAIODigitalClass(parent = None, index = 0)
                self.thread.report_test_type = self.get_result_test_type_comboBox.currentText()
                self.thread.all = self.radioButton_all.isChecked()
                self.thread.selected = self.radioButton_selected.isChecked()
                self.thread.main_list = self.label_65.text()
                self.thread.digital = self.radioButton_digital.isChecked()        
                self.thread.institution = self.get_result_comboBox.currentText()
                self.thread.main_date = self.get_result_date_comboBox.currentText()
                self.thread.save_directory = str(upload_file)
                self.thread.logo_directory = ""
                if self.label_92.text() != "TextLabel":
                    self.thread.upload_file_sr = self.label_92.text()
                else:
                    self.thread.upload_file_sr = False
                if self.label_98.text() != "TextLabel":
                    self.thread.upload_file_c = self.label_98.text()
                else:
                    self.thread.upload_file_c = False
                self.thread.start()
                self.thread.label_15signal.connect(self.label_15.setText)
                self.label_15.setVisible(True)
                self.checkBox_iops_split.setChecked(False)
                self.checkBox_iops_split.setEnabled(False)
                self.label_92.setText("TextLabel")
                self.label_98.setText("TextLabel")
        else:
            self.label_62.setText("Önce doğru verileri seçin")
            self.label_62.setVisible(True)
    
    def iops_split_check_checked(self):
        self.label_92.setVisible(False)
        self.label_98.setVisible(False)
        self.label_99.setVisible(False)
        if self.checkBox_iops_split.isChecked():
            self.btn_browse_upload_sr.setVisible(True)
            self.btn_browse_upload_c.setVisible(True)
            self.btn_turkish_report.setEnabled(False)
            self.btn_institutional_report.setEnabled(False)
            self.btn_class_table.setEnabled(False)
            self.btn_export_excel.setEnabled(False)
            self.btn_result_letter.setEnabled(False)
        else:
            self.btn_browse_upload_sr.setVisible(False)
            self.btn_browse_upload_c.setVisible(False)
            self.btn_turkish_report.setEnabled(True)
            self.btn_institutional_report.setEnabled(True)
            self.btn_class_table.setEnabled(True)
            self.btn_export_excel.setEnabled(True)
            self.btn_result_letter.setEnabled(True)

    def iops_split_sr_browse(self):
        if self.get_result_test_type_comboBox.currentText() in ["test_1 Step 1", "test_1 Step 2", "test_3 Standard", "test_4"]:
            upload_file = QFileDialog.getOpenFileName(self, "IOPS PDF Seç", sfl.get(), "PDF File (*.pdf)")
            sfl.save(upload_file)
            if upload_file:
                self.label_92.setText(upload_file[0])
                self.label_92.setVisible(True)
        else:
            self.label_99.setText("SR için desteklenen sınav türleri test_1 Step 1, test_1 Step 2, test_3 Standard, test_4")
            self.label_99.setVisible(True)
    
    def iops_split_c_browse(self):
        if self.get_result_test_type_comboBox.currentText() in ["test_1 Step 1", "test_1 Step 2", "test_3 Standard", "test_4"]:
            upload_file = QFileDialog.getOpenFileName(self, "IOPS PDF Seç", sfl.get(), "PDF File (*.pdf)")
            sfl.save(upload_file)
            if upload_file:
                self.label_98.setText(upload_file[0])
                self.label_98.setVisible(True)
        else:
            self.label_99.setText("C için desteklenen sınav türleri test_1 Step 1, test_1 Step 2, test_3 Standard, test_4")
            self.label_99.setVisible(True)
      
    #Get Result Part END
    #################################################################################
    
    #################################################################################
    #Delete Result Part START
    def get_school_date_changed_delete_result(self):
        selected_school = self.delete_result_comboBox.currentText()
        if selected_school in sm.get_combobox_school():
            self.delete_result_date_comboBox.clear()
            school_list_by_date = gslbdr.get_date_list_by_school(selected_school)
            if self.radioButton_delete_ps1.isChecked():
                if len(school_list_by_date[0]) == 0:
                    self.delete_result_date_comboBox.addItems(['Sınav Bulunamadı!'])
                else:
                    self.delete_result_date_comboBox.addItems(self.date_list_sort_reversed(school_list_by_date[0]))
            if self.radioButton_delete_ps2.isChecked():
                if len(school_list_by_date[1]) == 0:
                    self.delete_result_date_comboBox.addItems(['Sınav Bulunamadı!'])
                else:
                    self.delete_result_date_comboBox.addItems(self.date_list_sort_reversed(school_list_by_date[1]))
            if self.radioButton_delete_pspk.isChecked():
                if len(school_list_by_date[2]) == 0:
                    self.delete_result_date_comboBox.addItems(['Sınav Bulunamadı!'])
                else:
                    self.delete_result_date_comboBox.addItems(self.date_list_sort_reversed(school_list_by_date[2]))
            if self.radioButton_delete_js.isChecked():
                if len(school_list_by_date[3]) == 0:
                    self.delete_result_date_comboBox.addItems(['Sınav Bulunamadı!'])
                else:
                    self.delete_result_date_comboBox.addItems(self.date_list_sort_reversed(school_list_by_date[3]))
            if self.radioButton_delete_jspk.isChecked():
                if len(school_list_by_date[4]) == 0:
                    self.delete_result_date_comboBox.addItems(['Sınav Bulunamadı!'])
                else:
                    self.delete_result_date_comboBox.addItems(self.date_list_sort_reversed(school_list_by_date[4]))
            if self.radioButton_delete_test_4.isChecked():
                if len(school_list_by_date[5]) == 0:
                    self.delete_result_date_comboBox.addItems(['Sınav Bulunamadı!'])
                else:
                    self.delete_result_date_comboBox.addItems(self.date_list_sort_reversed(school_list_by_date[5]))
            self.label_57.setVisible(False)
            self.label_52.setVisible(False)
    
    def all_result_list_delete(self, result_list):
        self.label_57.setText("Yükleniyor...")
        self.label_57.setVisible(True)
        
        self.model = CheckablePandasModel(result_list)
        self.model.checkable_column = 0
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setFilterKeyColumn(-1)
        self.proxy_model.setSourceModel(self.model)
        self.proxy_model.setFilterCaseSensitivity(False)
        self.table_delete_result.setModel(self.proxy_model)
        self.search_from_delete_result.textChanged.connect(self.proxy_model.setFilterFixedString)
        self.table_delete_result.horizontalHeader().resizeSection(0, 5)
    
        self.model.checklist_sig.connect(self.checked_row_list_delete_result)
        
        self.label_57.setText(str(len(result_list))+" öğrenci listelendi!")
        self.label_57.setVisible(True)
        
    def checked_row_list_delete_result(self,row_list):
        self.row_list_delete_result = row_list
    
    def get_school_result_for_delete(self):
        if self.delete_result_date_comboBox.currentText() != "Sınav Bulunamadı!" and self.delete_result_comboBox.currentText() != "Okul Seç":
            self.thread = GetDeleteSchoolResultClass(parent = None, index = 0)
            self.thread.test_type_ps1 = self.radioButton_delete_ps1.isChecked()
            self.thread.test_type_ps2 = self.radioButton_delete_ps2.isChecked()
            self.thread.test_type_js = self.radioButton_delete_js.isChecked()
            self.thread.test_type_test_4 = self.radioButton_delete_test_4.isChecked()
            self.thread.test_type_pspk = self.radioButton_delete_pspk.isChecked()
            self.thread.test_type_jspk = self.radioButton_delete_jspk.isChecked()
            self.thread.institution = self.delete_result_comboBox.currentText()
            self.thread.main_date = self.delete_result_date_comboBox.currentText()
            self.thread.start()
            self.thread.all_result_2_signal.connect(self.all_result_list_delete)
            self.btn_del_result.setEnabled(True)
            self.btn_del_result_selected.setEnabled(True)
        else:
            self.label_57.setText("Önce doğru verileri seçin")
            self.label_57.setVisible(True)
    
    def delete_result(self):
        selected_date = self.delete_result_date_comboBox.currentText()
        selected_school = self.delete_result_comboBox.currentText()
        if self.delete_result_date_comboBox.currentText() != "Sınav Bulunamadı!" and self.delete_result_comboBox.currentText() != "Okul Seç":
            self.label_52.setText("Yükleniyor...")
            self.label_52.setVisible(True)
            dialog = ResultDeleteConfirmationDialogUi()
            dialog.date.setText(selected_date)
            dialog.inst.setText(selected_school)
            if self.radioButton_delete_ps1.isChecked():
                dialog.test_type.setText("test_1step_1")
            if self.radioButton_delete_ps2.isChecked():
                dialog.test_type.setText("test_1step_2")
            if self.radioButton_delete_js.isChecked():
                dialog.test_type.setText("test_3_standard")
            if self.radioButton_delete_test_4.isChecked():
                dialog.test_type.setText("test_4")
            if self.radioButton_delete_pspk.isChecked():
                dialog.test_type.setText("test_1speaking")
            if self.radioButton_delete_jspk.isChecked():
                dialog.test_type.setText("test_3_speaking")
            dialog.exec_()
            self.delete_result_date_comboBox.clear()
            self.label_52.setText(selected_date+" tarihli "+selected_school+" okulunun sonucu silindi!")
            self.label_52.setVisible(True)
        else:
            self.label_52.setText("Önce doğru verileri seçin")
            self.label_52.setVisible(True)
            
    def delete_selected_result(self):
        self.proxy_model.setSortRole(Qt.InitialSortOrderRole)
        self.proxy_model.invalidate()
        self.search_from_delete_result.clear()
        try:
            self.row_list_delete_result
        except:
            self.row_list_delete_result = []
        model = self.table_delete_result.model()
        data = []
        for row in range(model.rowCount()):
            data.append([])
            for column in range(model.columnCount()):
                if row in self.row_list_delete_result:
                    index = model.index(row, column)
                    # We suppose data are strings
                    data[row].append(model.data(index))
        self.delete_result_data = [tuple(item[1:]) for item in data if item != []]
        selected_date = self.delete_result_date_comboBox.currentText()
        selected_school = self.delete_result_comboBox.currentText()
        if self.delete_result_date_comboBox.currentText() != "Sınav Bulunamadı!" and self.delete_result_comboBox.currentText() != "Okul Seç":
            self.label_52.setText("Yükleniyor...")
            self.label_52.setVisible(True)
            dialog = SelectedResultDeleteConfirmationDialogUi()
            dialog.date.setText(selected_date)
            dialog.inst.setText(selected_school)
            dialog.selected_list.setText(str(self.delete_result_data))
            if self.radioButton_delete_ps1.isChecked():
                dialog.test_type.setText("test_1step_1")
            if self.radioButton_delete_ps2.isChecked():
                dialog.test_type.setText("test_1step_2")
            if self.radioButton_delete_js.isChecked():
                dialog.test_type.setText("test_3_standard")
            if self.radioButton_delete_test_4.isChecked():
                dialog.test_type.setText("test_4")
            if self.radioButton_delete_pspk.isChecked():
                dialog.test_type.setText("test_1speaking")
            if self.radioButton_delete_jspk.isChecked():
                dialog.test_type.setText("test_3_speaking")
            dialog.exec_()
            self.table_delete_result.setModel(None)
            self.label_52.setText(selected_date+" tarihli "+selected_school+" okulunun sonucu silindi!")
            self.label_52.setVisible(True)
        else:
            self.label_52.setText("Önce doğru verileri seçin")
            self.label_52.setVisible(True)

    #Delete Result Part END
    #################################################################################
    
    #################################################################################
    #Student Edit Part START        
    def get_student_info(self):
        self.label_14.setText("Yükleniyor...")
        self.label_14.setVisible(True)
        self.thread = GetStudentInfoClass(parent = None, index = 0)
        self.thread.student_number = self.edit_search_student.text()
        self.thread.start()
        self.thread.label_14signal.connect(self.label_14.setText)
        self.thread.edit_student_idsignal.connect(self.edit_student_id.setText)
        self.thread.edit_student_namesignal.connect(self.edit_student_name.setText)
        self.thread.edit_student_lastnamesignal.connect(self.edit_student_lastname.setText)
        self.thread.edit_student_dobsignal.connect(self.edit_student_dob.setText)
        self.thread.edit_student_gendersignal.connect(self.edit_student_gender.setText)
        self.thread.edit_student_classsignal.connect(self.edit_student_class.setText)
        self.thread.edit_student_schoolsignal.connect(self.edit_student_school.setText)
        self.label_14.setVisible(True)
    
    def edit_student_info(self):
        self.label_39.setText("Yükleniyor...")
        self.label_39.setVisible(True)
        self.thread = EditStudentInfoClass(parent = None, index = 0)
        self.thread.first_student_id = self.edit_search_student.text()
        self.thread.student_id = self.edit_student_id.text()
        self.thread.student_name = self.edit_student_name.text()
        self.thread.student_lastname = self.edit_student_lastname.text()
        self.thread.student_dob = self.edit_student_dob.text()
        self.thread.student_gender = self.edit_student_gender.text()
        self.thread.student_class = self.edit_student_class.text()
        self.thread.student_school = self.edit_student_school.text()
        self.thread.start()
        self.thread.label_39signal.connect(self.label_39.setText)
        self.label_39.setVisible(True)
        
    def create_student_info(self):
        self.label_39.setText("Yükleniyor...")
        self.label_39.setVisible(True)
        self.thread = CreateStudentInfoClass(parent = None, index = 0)
        self.thread.student_id = self.edit_student_id.text()
        self.thread.student_name = self.edit_student_name.text()
        self.thread.student_lastname = self.edit_student_lastname.text()
        self.thread.student_dob = self.edit_student_dob.text()
        self.thread.student_gender = self.edit_student_gender.text()
        self.thread.student_class = self.edit_student_class.text()
        self.thread.student_school = self.edit_student_school.text()
        self.thread.start()
        self.thread.label_39signal.connect(self.label_39.setText)
        self.label_39.setVisible(True)
    #Student Edit Part END
    #################################################################################
    
    #################################################################################
    #Tools Part START        
    def create_sales_card(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_69.setText("Yükleniyor...")
            self.label_69.setVisible(True)
            self.thread = SalesCardClass(parent = None, index = 0)
            self.thread.save_directory = upload_file
            self.thread.institution = self.sales_inst_comboBox.currentText()
            self.thread.student_class = self.sales_class_comboBox.currentText()
            self.thread.period = self.sales_period_comboBox.currentText()
            self.thread.start_num = self.sales_start_num.text()
            self.thread.end_num = self.sales_end_num.text()
            self.thread.barcode = self.radioButton_barcode.isChecked()
            self.thread.no_barcode = self.radioButton_no_barcode.isChecked()
            self.thread.start()
            self.thread.label_69signal.connect(self.label_69.setText)
            self.label_69.setVisible(True)
    
    def get_school_date_changed_iops_separation(self):
        selected_date = self.dateEdit_upload_iops_2.date().toString('dd-MM-yyyy')
        self.u_iops_comboBox_2.clear()
        school_list_by_date = gslbdr.get_school_list_by_date(selected_date)
        if self.radioButton_iops_ps1_2.isChecked():
            if len(school_list_by_date[0]) == 0:
                self.u_iops_comboBox_2.addItems(['Sınav Bulunamadı!'])
            else:
                self.u_iops_comboBox_2.addItems(sorted(school_list_by_date[0]))
        if self.radioButton_iops_ps2_2.isChecked():
            if len(school_list_by_date[1]) == 0:
                self.u_iops_comboBox_2.addItems(['Sınav Bulunamadı!'])
            else:
                self.u_iops_comboBox_2.addItems(sorted(school_list_by_date[1]))
        if self.radioButton_iops_js_2.isChecked():
            if len(school_list_by_date[3]) == 0:
                self.u_iops_comboBox_2.addItems(['Sınav Bulunamadı!'])
            else:
                self.u_iops_comboBox_2.addItems(sorted(school_list_by_date[3]))
        if self.radioButton_iops_test_4_2.isChecked():
            if len(school_list_by_date[5]) == 0:
                self.u_iops_comboBox_2.addItems(['Sınav Bulunamadı!'])
            else:
                self.u_iops_comboBox_2.addItems(sorted(school_list_by_date[5]))
        
    def open_iops_pdf_file(self):
        if self.u_iops_comboBox_2.currentText() != "Okul Seç":
            upload_file = QFileDialog.getOpenFileName(self, "IOPS PDF Seç", sfl.get(), "PDF File (*.pdf)")
            sfl.save(upload_file)
            if upload_file:
                self.label_upload_file_name_4.setText(upload_file[0])
                self.label_upload_file_name_4.setVisible(True)
                self.btn_upload_iops_2.setEnabled(True)
        else:
            self.label_83.setText("Önce doğru verileri seçin")
            self.label_83.setVisible(True)

    def create_iops_pdf_files(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            if self.u_iops_comboBox_2.currentText() != "Okul Seç":
                self.label_83.setText("Yükleniyor...")
                self.label_83.setVisible(True)
                self.thread = UploadIOPSPdfClass(parent = None, index = 0)
                self.thread.test_type_ps1 = self.radioButton_iops_ps1_2.isChecked()
                self.thread.test_type_ps2 = self.radioButton_iops_ps2_2.isChecked()
                self.thread.test_type_js = self.radioButton_iops_js_2.isChecked()
                self.thread.test_type_test_4 = self.radioButton_iops_test_4_2.isChecked()
                self.thread.score_report = self.radioButton_iops_score_report.isChecked()
                self.thread.certificate = self.radioButton_iops_certificate.isChecked()
                self.thread.upload_file = self.label_upload_file_name_4.text()
                self.thread.upload_date = self.dateEdit_upload_iops_2.date()
                self.thread.upload_school = self.u_iops_comboBox_2.currentText()
                self.thread.save_directory = upload_file
                self.thread.start()
                self.thread.label_83signal.connect(self.label_83.setText)
                self.dateEdit_upload_iops_2.setDateTime(self.current_date_time)
                self.u_iops_comboBox_2.setCurrentText('Okul seç')
                self.label_upload_file_name_4.setText('Dosya')
                self.label_83.setVisible(True)
            else:
                self.label_83.setText("Önce doğru verileri seçin")
                self.label_83.setVisible(True)

    def hide_iops_pdf_info_label(self):
        self.label_83.setVisible(False)
    
    def open_password_pdfs(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_upload_file_name_5.setText(upload_file)
            self.label_upload_file_name_5.setVisible(True)
            self.btn_remove_pass.setEnabled(True)
    
    def pdf_remove_password(self):
        self.label_86.setText("Yükleniyor...")
        self.label_86.setVisible(True)
        self.thread = PDFRemovePasswordClass(parent = None, index = 0)
        self.thread.save_directory = self.label_upload_file_name_5.text()
        self.thread.start()
        self.thread.label_86signal.connect(self.label_86.setText)
        self.label_upload_file_name_5.setText("Klasör")
        self.label_86.setVisible(True)
    
    def open_irr_save_dir(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_upload_file_name_10.setText(upload_file)
            self.label_upload_file_name_10.setVisible(True)
            self.btn_create_irr.setEnabled(True)

    def get_irregularity_report(self):
        self.label_101.setText("Yükleniyor...")
        self.label_101.setVisible(True)
        self.thread = IrregularityReportClass(parent = None, index = 0)
        self.thread.save_directory = self.label_upload_file_name_10.text()
        self.thread.country = self.irr_country_comboBox.currentText()
        self.thread.i_date = self.dateEdit_irr.date()
        self.thread.start()
        self.thread.irr_label_signal.connect(self.label_101.setText)
        self.label_upload_file_name_10.setText("Klasör")
        self.label_101.setVisible(True)
    
    def copy_form_code_change(self):
        main_form_code = self.main_formcode_comboBox.currentText()
        for i in range(10):
            eval("self.formcode_comboBox_{}.setCurrentText('{}')".format(str(i+1),main_form_code))
            eval('self.confirm_copy_checkBox_'+str(i+1)+'.setChecked(True)')

    def select_main_form_code_folder(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_upload_file_name_11.setText(upload_file)
            all_drives = cfsd.get_sd_drives()
            for i in range(len(all_drives)):
                eval("self.sd_cart_name_{}.setText('{}')".format(str(i+1),all_drives[i][1]))
                eval("self.sd_cart_letter_{}.setText('{}')".format(str(i+1),all_drives[i][0][0]))
    
    def copy_act(self,val):
        if val:
            self.btn_start_copy_all.setEnabled(True)
        else:
            self.btn_start_copy_all.setEnabled(False)

    def copy_all_files_to_drive(self):
        all_info = []
        for i in range(10):
            info = [eval('self.confirm_copy_checkBox_'+str(i+1)+'.isChecked()'), 
                eval('self.sd_cart_name_'+str(i+1)+'.text()'), 
                eval('self.sd_cart_letter_'+str(i+1)+'.text()'), 
                eval('self.formcode_comboBox_'+str(i+1)+'.currentText()')]
            all_info.append(info)

        self.label_102.setText("Yükleniyor...")
        self.label_102.setVisible(True)
        self.thread = CopyFormCodeFilesClass(parent = None, index = 0)
        self.thread.form_code_directory = self.label_upload_file_name_11.text()
        self.thread.all_info = all_info
        self.thread.start()
        self.thread.label_102signal.connect(self.label_102.setText)
        self.thread.activate_signal.connect(self.copy_act)
        self.label_102.setVisible(True)

    def select_main_form_code_folder_t1(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_upload_file_name_15.setText(upload_file)

    def copy_all_files_to_drive_t1(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.label_117.setText("Yükleniyor...")
            self.label_117.setVisible(True)
            self.thread = CopyFormCodeFilesClassT1(parent = None, index = 0)
            self.thread.form_code_directory = self.label_upload_file_name_15.text()
            self.thread.form_code = self.main_formcode_comboBox.currentText()
            self.thread.save_directory = upload_file
            self.thread.total_num = int(self.form_code_spinBox.value())
            self.thread.start()
            self.thread.label_117signal.connect(self.label_117.setText)
            self.thread.activate_signal_t1.connect(self.copy_act)
            self.label_117.setVisible(True)

    #Tools Part END
    #################################################################################
    
    #################################################################################
    #Docs Part START 
    def doc_btn(self, value):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        doc_dict = {
            "b1":[".pdf"],
            "b2":[".pdf"],
            "b3":[".pdf"],
            "b4":[".pdf",".pdf"],
            "b5":[".pdf"],
            "b6":[".pdf"],
            "b7":[".pdf",".pdf"],
            "b8":[".pdf",".pdf"],
            "b9":[".pdf"],
            "b10":[".pdf",".pdf",".pdf"]
            }
        if upload_file:
            for key,val in doc_dict.items():
                for va in val:
                    if key == value:
                        copy2("./data/docs/"+va, upload_file)
                        os.startfile(upload_file+"/"+va)
    
    def create_turkish_report_bg(self):
        upload_file = QFileDialog.getExistingDirectory(self, "Klasör Seç", sfl.get())
        sfl.save_d(upload_file)
        if upload_file:
            self.thread = CreateTurkishReportBGClass(parent = None, index = 0)
            self.thread.save_directory = upload_file
            self.thread.pri_pbt = self.pri_pbt_radioButton.isChecked()
            self.thread.pri_cbt = self.pri_cbt_radioButton.isChecked()
            self.thread.jun_pbt = self.jun_pbt_radioButton.isChecked()
            self.thread.jun_cbt = self.jun_cbt_radioButton.isChecked()
            self.thread.start()
    #Docs Part END
    #################################################################################
    
    #################################################################################
    #Change tabs on pages START
    def plan_tab_changed(self):
        school_list = sorted(sm.get_combobox_school())
        all_form_codes_for_plan = fcf.get_all_form_codes()
        ps1_form_codes = sorted(all_form_codes_for_plan[1])
        ps2_form_codes = sorted(all_form_codes_for_plan[2])
        js_form_codes = sorted(all_form_codes_for_plan[3])
        test_4_form_codes = sorted(all_form_codes_for_plan[4])
        self.dateEdit_upload_plan.setDateTime(self.current_date_time)
        self.dateEdit_create_plan.setDateTime(self.current_date_time)
        self.u_plan_comboBox.clear()
        self.u_plan_comboBox.addItems(school_list)
        self.u_plan_comboBox.setCurrentText("Okul Seç")
        self.label_upload_file_name.setVisible(False)
        self.radioButton_attendance_tr.setChecked(True)
        self.radioButton_xerox.setChecked(True)
        self.label_21.setVisible(False)
        self.label_22.setVisible(False)
        self.label_23.setVisible(False)
        self.ps1_form.setVisible(False)
        self.ps2_form.setVisible(False)
        self.js_form.setVisible(False)
        self.test_4_form.setVisible(False)
        self.edit_ps1_form.clear()
        self.edit_ps2_form.clear()
        self.edit_js_form.clear()
        self.edit_test_4_form.clear()
        self.edit_ps1_form.addItems(sorted(list(set(ps1_form_codes))))
        self.edit_ps2_form.addItems(sorted(list(set(ps2_form_codes))))
        self.edit_js_form.addItems(sorted(list(set(js_form_codes))))
        self.edit_test_4_form.addItems(sorted(list(set(test_4_form_codes))))
        self.btn_upload_plan.setEnabled(False)
        self.btn_pri_optic.setEnabled(False)
        self.btn_jun_optic.setEnabled(False)
        self.btn_test_4_optic.setEnabled(False)
        self.btn_ps1_dn.setEnabled(False)
        self.btn_ps2_dn.setEnabled(False)
        self.btn_js_dn.setEnabled(False)
        self.btn_test_4_dn.setEnabled(False)
        self.btn_attendance_id.setEnabled(False)
        self.btn_attendance_no_id.setEnabled(False)
        self.btn_booklet.setEnabled(False)
        self.btn_scanner_text.setEnabled(False)
        self.btn_del_plan.setEnabled(False)
        self.label_113.setVisible(False)
        self.u_plan_table.clear()
        plan_new_false_list = [('Tarih',"Okul",'Sınıf','Country Code','Language Code','Form Code',"Sınav Saati","Sınav Türü","Seans","Sayfa","Salon","Ad","Soyad","TC","Sınıf","Ay","Gün","Yıl","Cinsiyet")]
        self.u_plan_table.setRowCount(20)
        for row_number, row_data in enumerate(plan_new_false_list):
            self.u_plan_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.u_plan_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.logic_plan_comboBox.clear()
        self.logic_plan_comboBox.addItems(['Aynı Sınıf A\'dan Z\'ye (PBT)','Aynı Sınıf A\'dan Z\'ye (CBT)','Tüm Öğrenciler A\'dan Z\'ye (PBT)','Sınıf Bölme (PBT)'])
        self.logic_plan_comboBox.setCurrentText('Plan Mantığı Seç')
        self.logic_plan_comboBox_2.clear()
        self.logic_plan_comboBox_2.addItems(['Aynı Sınıf A\'dan Z\'ye (PBT)','Aynı Sınıf A\'dan Z\'ye (CBT)','Tüm Öğrenciler A\'dan Z\'ye (PBT)','Sınıf Bölme (PBT)'])
        self.logic_plan_comboBox_2.setCurrentText('Plan Mantığı Seç')
        self.convert_plan_comboBox.clear()
        self.convert_plan_comboBox.addItems(school_list)
        self.convert_plan_comboBox.setCurrentText('Okul Seç')
        self.convert_plan_2_comboBox.clear()
        self.convert_plan_2_comboBox.addItems(school_list)
        self.convert_plan_2_comboBox.setCurrentText('Okul Seç')
        self.total_class_spinBox.setVisible(False)
        self.total_class_spinBox_2.setVisible(False)
        self.whole_plan_checkBox.setChecked(False)
        self.tableView_first.setVisible(False)
        self.attendance_check_checkBox.setChecked(False)
        self.label_97.setVisible(False)
        self.g_plan_test_type_comboBox.setVisible(False)
        self.btn_upload_attendance_text.setVisible(False)
    
    def result_tab_changed(self):
        radioButton_list = [self.radioButton_iops_ps1,self.radioButton_iops_ps2,self.radioButton_iops_js,self.radioButton_iops_test_4,
                            self.radioButton_roster_ps1,self.radioButton_roster_ps2,self.radioButton_roster_js,self.radioButton_roster_test_4,
                            self.radioButton_roster_pspk,self.radioButton_roster_jspk,
                            self.radioButton_delete_ps1,self.radioButton_delete_ps2,self.radioButton_delete_js,self.radioButton_delete_test_4,
                            self.radioButton_delete_pspk,self.radioButton_delete_jspk]
        for rbutton in radioButton_list:
            rbutton.setAutoExclusive(False)
            rbutton.setChecked(False)
            rbutton.setAutoExclusive(True)
        current_date = self.current_date_time
        #IOPS Part
        self.dateEdit_upload_iops.setDateTime(current_date)
        self.u_iops_comboBox.clear()
        self.u_iops_comboBox.addItems(self.all_schools)
        self.u_iops_comboBox.setCurrentText("Okul Seç")
        self.label_upload_file_name_2.setVisible(False)
        self.label_41.setVisible(False)
        self.label_6.setVisible(False)
        self.btn_upload_iops_test_4_no_class.setVisible(False)
        self.btn_iops_opt_student.setVisible(False)
        self.btn_upload_iops.setEnabled(False)
        self.btn_upload_iops_test_4_no_class.setEnabled(False)
        self.checkBox_iops_make_up.setChecked(False)
        self.iops_upload_result_comboBox.setVisible(False)
        self.iops_upload_date_comboBox.setVisible(False)
        #Roster Part
        self.dateEdit_upload_roster.setDateTime(current_date)
        self.u_roster_comboBox.clear()
        self.u_roster_comboBox.addItems(self.all_schools)
        self.u_roster_comboBox.setCurrentText("Okul Seç")
        self.label_upload_file_name_3.setVisible(False)
        self.label_47.setVisible(False)
        self.btn_upload_roster_test_4_no_class.setVisible(False)
        self.btn_roster_opt_student.setVisible(False)
        self.btn_upload_roster.setEnabled(False)
        self.btn_upload_roster_test_4_no_class.setEnabled(False)
        #Get Result Part
        self.label_62.setVisible(False)
        self.label_15.setVisible(False)
        self.get_result_comboBox.clear()
        self.get_result_comboBox.addItems(self.all_schools)
        self.get_result_comboBox.setCurrentText('Okul seç')
        self.get_result_date_comboBox.clear()
        self.get_result_date_comboBox.addItem('Tarih Seç')
        self.get_result_date_comboBox.setCurrentText("Tarih Seç")
        self.btn_score_report.setEnabled(False)
        self.btn_certificate.setEnabled(False)
        self.btn_turkish_report.setEnabled(False)
        self.btn_institutional_report.setEnabled(False)
        self.btn_class_table.setEnabled(False)
        self.btn_export_excel.setEnabled(False)
        self.btn_result_letter.setEnabled(False)
        self.btn_aio_digital.setEnabled(False)
        self.table_get_result.setModel(None)
        self.label_65.setVisible(False)
        self.get_result_date_spk_comboBox.setVisible(False)
        self.btn_browse_upload_sr.setVisible(False)
        self.btn_browse_upload_c.setVisible(False)
        self.label_92.setVisible(False)
        self.label_98.setVisible(False)
        self.label_99.setVisible(False)
        self.checkBox_iops_split.setEnabled(False)
        #Delete Result Part
        self.label_57.setVisible(False)
        self.label_52.setVisible(False)
        self.delete_result_comboBox.clear()
        self.delete_result_comboBox.addItems(self.all_schools)
        self.delete_result_comboBox.setCurrentText("Okul Seç")
        self.btn_del_result.setEnabled(False)
        self.btn_del_result_selected.setEnabled(False)
        self.table_delete_result.setModel(None)
        
    def student_tab_changed(self):
        self.label_14.setVisible(False)
        self.label_39.setVisible(False)
        self.label_72.setVisible(False)
        self.label_60.setVisible(False)
        
    def edit_info_tab_changed(self):
        self.label_19.setVisible(False)
        self.label_38.setVisible(False)
        self.label_48.setVisible(False)
        self.label_43.setVisible(False)
        self.label_49.setVisible(False)
        self.label_64.setVisible(False)
        self.search_schools.clear()
        all_form_codes = sorted(fcf.get_all_form_codes()[0])
        all_logo_list = sorted(sm.get_school_logo_list())
        country_list = sd.country_list
        city_list = sd.city_list
        test_type_list = ['Test Type 1', 'Test Type 2', 'Test Type 3', 'Test Type 4', 'Test Type 5', 'Test Type 6', 'Sonuç Bulunamadı!']
        self.sch_comboBox_3.clear()
        self.sch_comboBox_3.addItems(sorted(sm.get_combobox_school()))
        self.sch_comboBox_3.setCurrentText('Okul seç')
        self.sch_country.clear()
        self.sch_country.addItems(country_list)
        self.sch_country.setCurrentText('TURKEY')
        self.sch_city.clear()
        self.sch_city.addItems(city_list)
        self.sch_city.setCurrentText('ISTANBUL')
        self.sch_country_3.clear()
        self.sch_country_3.addItems(country_list)
        self.sch_country_3.setCurrentText('TURKEY')
        self.sch_city_3.clear()
        self.sch_city_3.addItems(city_list)
        self.sch_city_3.setCurrentText('ISTANBUL')
        self.test_type_comboBox.clear()
        self.test_type_comboBox.addItems(test_type_list)
        self.edit_form_code_comboBox.clear()
        self.edit_form_code_comboBox.addItems(sorted(all_form_codes))
        self.edit_test_type_comboBox.clear()
        self.edit_test_type_comboBox.addItems(test_type_list)
        self.add_school_logo_comboBox.clear()
        self.add_school_logo_comboBox.addItems(all_logo_list)
        self.add_school_logo_comboBox.setCurrentText('Logo seç')
        self.update_school_logo_comboBox.clear()
        self.update_school_logo_comboBox.addItems(all_logo_list)
        self.update_school_logo_comboBox.setCurrentText('Logo seç')
        self.label_89.setVisible(False)
        self.label_90.setVisible(False)
        self.label_94.setVisible(False)
        self.logo_upload_label.setVisible(False)
        self.sch_new_school_name.setVisible(False)
        self.label_71.setVisible(False)
        self.checkBox_new_school_name.setChecked(False)
    #Change tabs on pages END
    #################################################################################
    
    #################################################################################
    #Changing pages from left menu objects START
    def open_page_home(self):
        self.historical_start_date.setDateTime(self.current_date_time)
        self.historical_end_date.setDateTime(self.current_date_time)
        normal_school_list = ghd.institution_list()
        normal_city_list = ghd.city_list()
        self.home_higher_institution_comboBox.clear()
        self.home_higher_institution_comboBox.addItems(["Kurum Seç"]+sd.higher_inst_list)
        self.home_higher_institution_comboBox.setCurrentText("Kurum Seç")
        self.home_city_comboBox.clear()
        self.home_city_comboBox.addItems(["Şehir Seç"]+sorted(normal_city_list))
        self.home_city_comboBox.setCurrentText("Şehir Seç")
        self.home_institution_comboBox.clear()
        self.home_institution_comboBox.addItems(["Okul Seç"]+sorted(normal_school_list))
        self.home_institution_comboBox.setCurrentText("Okul Seç")
        self.btn_main_table_export.setEnabled(False)
        
        self.stackedWidget.setCurrentWidget(self.page_home)
        self.label_top_info_2.setText('| Anasayfa')
        
    def open_page_plan(self):
        school_list = sorted(sm.get_combobox_school())
        all_form_codes_for_plan = fcf.get_all_form_codes()
        ps1_form_codes = sorted(all_form_codes_for_plan[1])
        ps2_form_codes = sorted(all_form_codes_for_plan[2])
        js_form_codes = sorted(all_form_codes_for_plan[3])
        test_4_form_codes = sorted(all_form_codes_for_plan[4])
        self.dateEdit_upload_plan.setDateTime(self.current_date_time)
        self.dateEdit_create_plan.setDateTime(self.current_date_time)
        self.u_plan_comboBox.clear()
        self.u_plan_comboBox.addItems(school_list)
        self.u_plan_comboBox.setCurrentText("Okul Seç")
        self.label_upload_file_name.setVisible(False)
        self.radioButton_attendance_tr.setChecked(True)
        self.radioButton_xerox.setChecked(True)
        self.label_21.setVisible(False)
        self.label_22.setVisible(False)
        self.label_23.setVisible(False)
        self.ps1_form.setVisible(False)
        self.ps2_form.setVisible(False)
        self.js_form.setVisible(False)
        self.test_4_form.setVisible(False)
        self.edit_ps1_form.clear()
        self.edit_ps2_form.clear()
        self.edit_js_form.clear()
        self.edit_test_4_form.clear()
        self.edit_ps1_form.addItems(sorted(list(set(ps1_form_codes))))
        self.edit_ps2_form.addItems(sorted(list(set(ps2_form_codes))))
        self.edit_js_form.addItems(sorted(list(set(js_form_codes))))
        self.edit_test_4_form.addItems(sorted(list(set(test_4_form_codes))))
        self.btn_upload_plan.setEnabled(False)
        self.btn_pri_optic.setEnabled(False)
        self.btn_jun_optic.setEnabled(False)
        self.btn_test_4_optic.setEnabled(False)
        self.btn_ps1_dn.setEnabled(False)
        self.btn_ps2_dn.setEnabled(False)
        self.btn_js_dn.setEnabled(False)
        self.btn_test_4_dn.setEnabled(False)
        self.btn_attendance_id.setEnabled(False)
        self.btn_attendance_no_id.setEnabled(False)
        self.btn_booklet.setEnabled(False)
        self.btn_scanner_text.setEnabled(False)
        self.btn_del_plan.setEnabled(False)
        self.label_113.setVisible(False)
        self.u_plan_table.clear()
        plan_new_false_list = [('Tarih',"Okul",'Sınıf','Country Code','Language Code','Form Code',"Sınav Saati","Sınav Türü","Seans","Sayfa","Salon","Ad","Soyad","TC","Sınıf","Ay","Gün","Yıl","Cinsiyet")]
        self.u_plan_table.setRowCount(20)
        for row_number, row_data in enumerate(plan_new_false_list):
            self.u_plan_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.u_plan_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.logic_plan_comboBox.clear()
        self.logic_plan_comboBox.addItems(['Aynı Sınıf A\'dan Z\'ye (PBT)','Aynı Sınıf A\'dan Z\'ye (CBT)','Tüm Öğrenciler A\'dan Z\'ye (PBT)','Sınıf Bölme (PBT)'])
        self.logic_plan_comboBox.setCurrentText('Plan Mantığı Seç')
        self.logic_plan_comboBox_2.clear()
        self.logic_plan_comboBox_2.addItems(['Aynı Sınıf A\'dan Z\'ye (PBT)','Aynı Sınıf A\'dan Z\'ye (CBT)','Tüm Öğrenciler A\'dan Z\'ye (PBT)','Sınıf Bölme (PBT)'])
        self.logic_plan_comboBox_2.setCurrentText('Plan Mantığı Seç')
        self.convert_plan_comboBox.clear()
        self.convert_plan_comboBox.addItems(school_list)
        self.convert_plan_comboBox.setCurrentText('Okul Seç')
        self.convert_plan_2_comboBox.clear()
        self.convert_plan_2_comboBox.addItems(school_list)
        self.convert_plan_2_comboBox.setCurrentText('Okul Seç')
        self.total_class_spinBox.setVisible(False)
        self.total_class_spinBox_2.setVisible(False)
        self.whole_plan_checkBox.setChecked(False)
        self.tableView_first.setVisible(False)
        self.attendance_check_checkBox.setChecked(False)
        self.label_97.setVisible(False)
        self.g_plan_test_type_comboBox.setVisible(False)
        self.btn_upload_attendance_text.setVisible(False)
        
        
        self.stackedWidget.setCurrentWidget(self.page_plan)
        self.label_top_info_2.setText('| Planlama')
        
    def open_page_result(self):
        radioButton_list = [self.radioButton_iops_ps1,self.radioButton_iops_ps2,self.radioButton_iops_js,self.radioButton_iops_test_4,
                            self.radioButton_roster_ps1,self.radioButton_roster_ps2,self.radioButton_roster_js,self.radioButton_roster_test_4,
                            self.radioButton_roster_pspk,self.radioButton_roster_jspk,
                            self.radioButton_delete_ps1,self.radioButton_delete_ps2,self.radioButton_delete_js,self.radioButton_delete_test_4,
                            self.radioButton_delete_pspk,self.radioButton_delete_jspk]
        for rbutton in radioButton_list:
            rbutton.setAutoExclusive(False)
            rbutton.setChecked(False)
            rbutton.setAutoExclusive(True)
            
        self.all_schools = sorted(sm.get_combobox_school())
        
        #Get Result Part
        self.get_result_comboBox.clear()
        self.get_result_comboBox.addItems(self.all_schools)
        self.get_result_comboBox.setCurrentText('Okul seç')
        self.get_result_date_comboBox.clear()
        self.get_result_date_comboBox.addItem('Tarih Seç')
        self.get_result_date_comboBox.setCurrentText('Tarih Seç')
        self.label_62.setVisible(False)
        self.label_15.setVisible(False)
        self.btn_score_report.setEnabled(False)
        self.btn_certificate.setEnabled(False)
        self.btn_turkish_report.setEnabled(False)
        self.btn_institutional_report.setEnabled(False)
        self.btn_class_table.setEnabled(False)
        self.btn_export_excel.setEnabled(False)
        self.btn_result_letter.setEnabled(False)
        self.btn_aio_digital.setEnabled(False)
        self.table_get_result.setModel(None)
        self.label_65.setVisible(False)
        self.get_result_date_spk_comboBox.setVisible(False)
        self.btn_browse_upload_sr.setVisible(False)
        self.btn_browse_upload_c.setVisible(False)
        self.label_92.setVisible(False)
        self.label_98.setVisible(False)
        self.label_99.setVisible(False)
        self.checkBox_iops_split.setEnabled(False)
        self.checkBox_iops_make_up.setChecked(False)
        self.iops_upload_result_comboBox.setVisible(False)
        self.iops_upload_date_comboBox.setVisible(False)

        
        self.stackedWidget.setCurrentWidget(self.page_result)
        self.label_top_info_2.setText('| Sonuç')
        
    def open_page_student(self):
        self.label_14.setVisible(False)
        self.label_39.setVisible(False)
        self.label_72.setVisible(False)
        self.label_60.setVisible(False)
        
        self.stackedWidget.setCurrentWidget(self.page_student)
        self.label_top_info_2.setText('| Öğrenci')
        
    def open_page_student_add_plan(self):
        self.label_14.setVisible(False)
        self.label_39.setVisible(False)
        self.label_72.setVisible(False)
        self.label_60.setVisible(False)
        self.stackedWidget.setCurrentWidget(self.page_student)
        self.label_top_info_2.setText('| Öğrenci')
        self.tabWidget_3.setCurrentIndex(1)
        
    def open_page_edit_info(self):
        self.label_19.setVisible(False)
        self.label_38.setVisible(False)
        self.label_48.setVisible(False)
        self.label_43.setVisible(False)
        self.label_49.setVisible(False)
        self.label_64.setVisible(False)
        self.search_schools.clear()
        all_form_codes = sorted(fcf.get_all_form_codes()[0])
        all_logo_list = sorted(sm.get_school_logo_list())
        country_list = sd.country_list
        city_list = sd.city_list
        test_type_list = ['Test Type 1', 'Test Type 2', 'Test Type 3', 'Test Type 4', 'Test Type 5', 'Test Type 6', 'Sonuç Bulunamadı!']
        self.sch_comboBox_3.clear()
        self.sch_comboBox_3.addItems(sorted(sm.get_combobox_school()))
        self.sch_comboBox_3.setCurrentText('Okul seç')
        self.sch_country.clear()
        self.sch_country.addItems(country_list)
        self.sch_country.setCurrentText('TURKEY')
        self.sch_city.clear()
        self.sch_city.addItems(city_list)
        self.sch_city.setCurrentText('ISTANBUL')
        self.sch_country_3.clear()
        self.sch_country_3.addItems(country_list)
        self.sch_country_3.setCurrentText('TURKEY')
        self.sch_city_3.clear()
        self.sch_city_3.addItems(city_list)
        self.sch_city_3.setCurrentText('ISTANBUL')
        self.test_type_comboBox.clear()
        self.test_type_comboBox.addItems(test_type_list)
        self.edit_form_code_comboBox.clear()
        self.edit_form_code_comboBox.addItems(sorted(all_form_codes))
        self.edit_test_type_comboBox.clear()
        self.edit_test_type_comboBox.addItems(test_type_list)
        self.add_school_logo_comboBox.clear()
        self.add_school_logo_comboBox.addItems(all_logo_list)
        self.add_school_logo_comboBox.setCurrentText('Logo seç')
        self.update_school_logo_comboBox.clear()
        self.update_school_logo_comboBox.addItems(all_logo_list)
        self.update_school_logo_comboBox.setCurrentText('Logo seç')
        self.delete_logo_comboBox.clear()
        self.delete_logo_comboBox.addItems(all_logo_list)
        self.delete_logo_comboBox.setCurrentText('Logo seç')
        self.label_89.setVisible(False)
        self.label_90.setVisible(False)
        self.label_94.setVisible(False)
        self.logo_upload_label.setVisible(False)
        self.label_96.setVisible(False)
        self.logo_upload_label_2.setVisible(False)
        self.sch_new_school_name.setVisible(False)
        self.label_71.setVisible(False)
        self.checkBox_new_school_name.setChecked(False)
        
        self.stackedWidget.setCurrentWidget(self.page_edit_info)
        self.label_top_info_2.setText('| İşlemler')
    
    def open_page_tools(self):
        all_form_codes = sorted(fcf.get_all_form_codes()[0])
        self.label_69.setVisible(False)
        class_list = ["2. SINIF", "3. SINIF", "4. SINIF", "5. SINIF", "6. SINIF", "7. SINIF", "8. SINIF", "HAZIRLIK SINIFI", "9. SINIF", "10. SINIF", "11. SINIF", "12. SINIF",
                      "2. SINIF SPEAKING", "3. SINIF SPEAKING", "4. SINIF SPEAKING", "5. SINIF SPEAKING", "6. SINIF SPEAKING", "7. SINIF SPEAKING", "8. SINIF SPEAKING", "HAZIRLIK SINIFI SPEAKING", "9. SINIF SPEAKING", "10. SINIF SPEAKING", "11. SINIF SPEAKING", "12. SINIF SPEAKING",]
        period_list = ["2021 - 2022", "2022 - 2023", "2023 - 2024", "2024 - 2025", "2025 - 2026", "2026 - 2027", "2027 - 2028", "2028 - 2029", "2029 - 2030", "2030 - 2031"]
        school_list = ["BİLFEN KOLEJİ", "BAHÇEŞEHİR KOLEJİ", "TED KOLEJİ", "İSTEK KOLEJİ", "FMV IŞIK KOLEJİ", "MAYA KOLEJİ", "ENKA KOLEJİ", "TAN KOLEJİ"]
        self.label_upload_file_name_10.setVisible(False)
        self.label_101.setVisible(False)
        self.dateEdit_irr.setDateTime(self.current_date_time)
        self.irr_country_comboBox.clear()
        self.irr_country_comboBox.addItems(["TR","NL"])
        self.btn_create_irr.setEnabled(False)
        
        self.sales_inst_comboBox.clear()
        self.sales_class_comboBox.clear()
        self.sales_period_comboBox.clear()
        self.sales_inst_comboBox.addItems(sorted(school_list))
        self.sales_class_comboBox.addItems(class_list)
        self.sales_period_comboBox.addItems(period_list)
        
        self.btn_upload_iops_2.setEnabled(False)
        self.dateEdit_upload_iops_2.setDateTime(self.current_date_time)
        self.label_83.setVisible(False)
        
        self.btn_remove_pass.setEnabled(False)
        self.label_86.setVisible(False)

        
        self.label_102.setVisible(False)
        self.label_117.setVisible(False)
        self.main_formcode_comboBox.clear()
        self.main_formcode_comboBox.addItems(sorted(all_form_codes))

        
        self.stackedWidget.setCurrentWidget(self.page_tools)
        self.label_top_info_2.setText('| Araçlar')
    
    def open_page_docs(self):
        
        self.stackedWidget.setCurrentWidget(self.page_docs)
        self.label_top_info_2.setText('| Belgeler')
    #Changing pages from left menu objects END
    #################################################################################
    
    #################################################################################
    #Windows Settings START
    from main_funcs.mixed.gui_classes import all_size_down
    from main_funcs.mixed.gui_classes import all_size_up
    from main_funcs.mixed.gui_classes import all_size_normal
    from main_funcs.mixed.gui_classes import mousePressEvent
    from main_funcs.mixed.gui_classes import mouseMoveEvent
    from main_funcs.mixed.gui_classes import mouseReleaseEvent
    from main_funcs.mixed.gui_classes import btn_close_clicked
    from main_funcs.mixed.gui_classes import btn_max_clicked
    from main_funcs.mixed.gui_classes import btn_min_clicked
    from main_funcs.mixed.gui_classes import btn_maxr_clicked
    from main_funcs.mixed.gui_classes import windowStateChanged
    from main_funcs.mixed.gui_classes import changeEvent
    from main_funcs.mixed.gui_classes import gripSize
    from main_funcs.mixed.gui_classes import setGripSize
    from main_funcs.mixed.gui_classes import updateGrips
    from main_funcs.mixed.gui_classes import resizeEvent
    #Windows Settings END
    #################################################################################

if __name__ == '__main__':
    deviceuuid = WMI().Win32_ComputerSystemProduct()[0].UUID
    if deviceuuid != "XXX":
        logger()
    app = QApplication(sys.argv)
    window = MainUi()
    window.show()
    sys.exit(app.exec_())

   
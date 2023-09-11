from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


import os,csv,sys
import pandas as pd
from shutil import copy2
from datetime import datetime
from wmi import WMI
from functools import partial
import win32gui

from main_funcs.thread_class.school_class import *
from main_funcs.thread_class.upload_plan_class import *
from main_funcs.thread_class.upload_iops_class import *
from main_funcs.thread_class.form_code_class import *
from main_funcs.thread_class.get_historical_data_class import *
from main_funcs.thread_class.upload_roster_class import *
from main_funcs.thread_class.edit_student_class import *
from main_funcs.thread_class.export_schools_class import *
from main_funcs.thread_class.result_report_class import *
from main_funcs.thread_class.delivery_note_class import *
from main_funcs.thread_class.create_sales_card_class import *
from main_funcs.thread_class.iops_file_separation_class import *
from main_funcs.thread_class.remove_pdf_pass_class import *
from main_funcs.thread_class.irregulartity_report import *
from main_funcs.thread_class.copy_form_code_to_sd_class import *
from main_funcs.thread_class.create_t_r_bg import *


from main_funcs.mixed.gui_classes import *
from main_funcs.mixed.table_class import *

import data.gui_data.file_rc
import data.gui_data.some_data as sd
import main_funcs.mixed.get_historical_data as ghd
import main_funcs.planning.get_school_list_by_date as gslbd
import main_funcs.score_docs.get_school_list_by_date_result as gslbdr
import main_funcs.mixed.version_info as vi
from main_funcs.mixed.make_plan_dialog import MakePlan
import main_funcs.mixed.save_file_location as sfl
import main_funcs.tools.copy_form_code_to_sd_card as cfsd





##################################################################################################
#                                                                                                #
#   All imports are here and also this file is imported by GTO.py                                #         
#   All classes and functions separated and all of them have different file name                 #
#   but you can easily find all the functions. I worked hard for naming the variables.           #
#   Some files unfortunately don't have comments but you can check variable names all the time   #
#                                                                                                #
##################################################################################################
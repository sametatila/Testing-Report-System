import main_funcs.mixed.mysql_connection as mc
import pandas as pd



def ps1_df():
    db_pd = mc.engine.connect()
    ps1_df = pd.read_sql("SELECT * FROM test_1step_1", con=db_pd)
    db_pd.close()
    return ps1_df
def ps2_df():
    db_pd = mc.engine.connect()
    ps2_df = pd.read_sql("SELECT * FROM test_1step_2", con=db_pd)
    db_pd.close()
    return ps2_df
def pspk_df():
    db_pd = mc.engine.connect()
    pspk_df = pd.read_sql("SELECT * FROM test_1speaking", con=db_pd)
    db_pd.close()
    return pspk_df
def js_df():
    db_pd = mc.engine.connect()
    js_df = pd.read_sql("SELECT * FROM test_3_standard", con=db_pd)
    db_pd.close()
    return js_df
def jspk_df():
    db_pd = mc.engine.connect()
    jspk_df = pd.read_sql("SELECT * FROM test_3_speaking", con=db_pd)
    db_pd.close()
    return jspk_df




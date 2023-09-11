import os

def save(upload_file):
    last_file_loc = '/'.join(upload_file[0].split('/')[:-1])
    with open('./data/gui_data/tmp_loc','w', encoding='utf-8') as f:
        f.write(last_file_loc)

def get():
    if os.path.isfile('./data/gui_data/tmp_loc'):
        with open('./data/gui_data/tmp_loc','r', encoding='utf-8') as f:
            last_loc = f.read()
    if last_loc == "":
        last_loc = os.path.expanduser("~/Documents/GTO_Docs")
    return last_loc

def save_d(upload_file):
    with open('./data/gui_data/tmp_loc','w', encoding='utf-8') as f:
        f.write(upload_file)

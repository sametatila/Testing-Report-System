import os,ftplib,time
from zipfile import ZipFile
import main_funcs.mixed.mysql_connection as mc

print("İşlem başladı")
for i in ['./dist','./build']:
    for root, dirs, files in os.walk(i):
        for f in files:
            os.unlink(os.path.join(root, f))
print("Eski kalıntılar temizlendi")
os.system("""start /wait cmd  /c pyinstaller --onefile --icon="./data/gui_data/logos/gtfav.ico" -w GTO.py """)
print("GTO.exe oluşturuldu")
time.sleep(2)
os.replace("./dist/GTO.exe","GTO.exe")
print("GTO.exe ana klasöre taşındı")

db_pd = mc.engine.connect()
db_pd.execute("CREATE TABLE IF NOT EXISTS version_info(version_info FLOAT(10), test_1 KEY (version_info),version_detail VARCHAR(500))")
cursor = db_pd.execute("SELECT * FROM version_info")
version_info = cursor.fetchall()[-1][0]
new_version_info = round(version_info+0.001,3)
zip_file_name = str(new_version_info)+'.zip'
db_pd.execute("INSERT IGNORE INTO version_info(version_info) VALUES(%s)",(new_version_info))
db_pd.close()
with open('./main_funcs/mixed/version','w') as f:
    f.write(str(new_version_info))
print(f"Version Info güncellendi ({new_version_info})")

ftp = ftplib.FTP("XXX")
ftp.cwd('/GTO-Version')
print("Sunucuya bağlandı")

data_files = [os.path.join(path, name) for path, subdirs, files in os.walk('./data') for name in files if not name.endswith(".pyc") or name == 'tmp_loc']
main_funcs_files = [os.path.join(path, name) for path, subdirs, files in os.walk('./main_funcs') for name in files if not name.endswith(".pyc")]
root_files = ["./GTO.exe"]
all_files = data_files+main_funcs_files+root_files
print("Tüm dosyaları listeledi")
zf = ZipFile(zip_file_name, "w")
for file_path in all_files:
    dirname, filename = os.path.split(file_path)
    if dirname != "./":
        zf.write(dirname)
        zf.write(os.path.join(dirname, filename))
zf.close()
print(zip_file_name+" oluşturuldu")
try:
    ftp_files = ftp.nlst()
    for file in ftp_files:
        if '.zip' in file:
            c_version = file.split('.zip')[0]
            if float(c_version) < new_version_info-0.01:
                ftp.delete(f"{file}")
                print(file+" sunucudan silindi")
except:
    pass

print(zip_file_name+" sunucuya yükleniyor...")
with open(zip_file_name, "rb") as zip_file:
    ftp.storbinary(f"STOR {zip_file_name}", zip_file)
print(zip_file_name+" sunucuya yüklendi")
ftp.close()

try:
    os.remove(zip_file_name)
    os.remove("GTO.exe")
    os.remove("GTO.spec")
    os.remove("updater.spec")
except:
    pass

print(zip_file_name+" ana klasörden silindi")
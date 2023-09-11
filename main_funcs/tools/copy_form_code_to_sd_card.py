import win32api

def get_sd_drives():
    try:
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        drive_list = []
        for drive in drives:
            vol_name = win32api.GetVolumeInformation(drive)[0]
            if 'GT SD' in vol_name:
                drive_list.append([drive,vol_name])
    except Exception as e:
        print(e)
        pass
    return drive_list
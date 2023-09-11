def check_file_name(file_name):
    import os 
    filename, extension = os.path.splitext(file_name)
    i = 1
    while os.path.exists(file_name):
        file_name = '%s(%i)%s' % (filename, i, extension)
        i += 1
    return file_name
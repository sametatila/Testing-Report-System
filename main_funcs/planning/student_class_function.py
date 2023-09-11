classlist03 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
classlist03str = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Y', 'Z']

def student_class_val(student_class):
    for i in range(len(classlist03)):
        if len(str(student_class)) == 3:
            if str(student_class)[1:] == classlist03[i]:
                ps1class = str(student_class)[:1]+classlist03str[i]
        elif student_class >11200:
            if str(student_class)[3:] == classlist03[i]:
                ps1class = "12Fen"+classlist03str[i]
        elif student_class >11100:
            if str(student_class)[3:] == classlist03[i]:
                ps1class = "11Fen"+classlist03str[i]
        elif student_class >11000:
            if str(student_class)[3:] == classlist03[i]:
                ps1class = "10Fen"+classlist03str[i]
        elif student_class >1900:
            if str(student_class)[2:] == classlist03[i]:
                ps1class = "9Fen"+classlist03str[i]
        elif student_class >1800:
            if str(student_class)[2:] == classlist03[i]:
                ps1class = "Haz"+classlist03str[i]
        elif student_class >1000:
            if str(student_class)[2:] == classlist03[i]:
                ps1class = str(student_class)[:2]+classlist03str[i]
    return ps1class

def student_class_val_reverse(student_class):
    for i in range(len(classlist03)):
        if len(str(student_class)) == 2:
            if str(student_class)[1:] == classlist03str[i]:
                ps1class = str(student_class)[:1]+classlist03[i]
        elif len(str(student_class)) == 4:
            if str(student_class)[3:] == classlist03str[i]:
                ps1class = "18"+classlist03[i]
        elif len(str(student_class)) == 5:
            if str(student_class)[4:] == classlist03str[i]:
                if str(student_class)[:4] == '9Fen' or str(student_class)[:4] == '9FEN':
                    ps1class = "19"+classlist03[i]
        elif len(str(student_class)) > 5:
            if str(student_class)[5:] == classlist03str[i]:
                if str(student_class)[:5] == '10Fen' or str(student_class)[:5] == '10FEN':
                    ps1class = "110"+classlist03[i]
                elif str(student_class)[:5] == '11Fen' or str(student_class)[:5] == '11FEN':
                    ps1class = "111"+classlist03[i]
                elif str(student_class)[:5] == '12Fen' or str(student_class)[:5] == '12FEN':
                    ps1class = "112"+classlist03[i]
        elif len(str(student_class)) == 3:
            if str(student_class)[2:] == classlist03str[i]:
                ps1class = str(student_class)[:2]+classlist03[i]
    return ps1class

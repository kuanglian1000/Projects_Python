import os,shutil
os.chdir('C:\\kl\\LearnEnglish_ByCalendar_In365days')
for fileName in os.listdir():
    a = len(fileName.split('.')[0])
    fullName = os.getcwd()+'\\'+fileName
    if a == 3:
        # print(fullName)
        # print(os.getcwd()+'\\newName\\'+fileName[:2] + '0' + fileName[2:])
        shutil.copy(fullName,os.getcwd()+'\\newName\\'+fileName[:2] + '0' + fileName[2:])
        shutil.move(fullName,os.getcwd()+'\\badName\\'+fileName)
        print(fileName)
    else:
        if (fileName.startswith('10-') or fileName.startswith('11-') or fileName.startswith('12-')) and a == 4:
            print(fileName)
            shutil.copy(fullName,os.getcwd()+'\\newName\\'+fileName[:3] + '0' + fileName[3:])
            shutil.move(fullName,os.getcwd()+'\\badName\\'+fileName)
            # print(fileName)

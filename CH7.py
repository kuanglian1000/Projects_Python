import re
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Batwoman')
if mo1:
    print(mo1.group())
else:
    print('no match')
print('==============================')
bRegex = re.compile(r'(\d{2})+(Ha){2,5}')
mo1 = bRegex.search('12HaHaHaHaHa')
if mo1:
    print(mo1.group())
else:
    print('no match')
print('==============================')
cRegex = re.compile(r'\w{2,9}?') #{}加上?後,預設抓最短的,就是2碼
dRegex = re.compile(r'\w{2,9}') #{}後無?時,預設抓最長的,就是9碼
mo1 = cRegex.search('abcdefgef')
print(mo1.group()) #ab
mo1 = dRegex.search('abcdefgef')
print(mo1.group()) #abcdefgef

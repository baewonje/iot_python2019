import re

file_name_list = ["foo.bar","autoexec.bat","sendmail.ct"]

p = re.compile('.*[.][^b].*$')

for file_name in file_name_list:
    print(p.search(file_name))

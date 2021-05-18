import re
from past.builtins import raw_input


password = raw_input("Enter string to test: ")
regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*-+=|:.?~])[A-Za-z\d@$!#%*?&]{6,20}$"
# r'[A-Za-z0-9!@#$%^&*-+=|:.?~]{6,20}'
pattern = re.compile(regex)
total = re.search(pattern, password)

if total:
    print('Success')
else:
    print('Fail')

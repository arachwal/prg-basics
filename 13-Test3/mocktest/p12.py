import re

dates="2021-1-3,05/12/2024,1998-12-11,9 maj 2007,2001-12-07,15-09-2011"

pattern="\d\d\d\d-\d\d-\d\d"

found=re.findall(pattern,dates)

print(found)
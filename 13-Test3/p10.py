import re

pattern=r"\d\d/\d\d/\d\d\d\d"

dates='2021-1-3;05/12/2024:1998-12-11,9 maj 2007;;31/03/2021,,1/9/2011'

gud=re.findall(pattern,dates)
print(gud)

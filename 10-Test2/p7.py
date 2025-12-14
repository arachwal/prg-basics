import re

arr=["uek","water_7_x","anna.may","a_b_c_d_e_f"]

def f(arr):
    count=0
    pattern=r'^[a-z0-9_]{4,12}$'    
    for item in arr:
        if re.match(pattern, item):
            count+=1
    return count
print(f(arr))
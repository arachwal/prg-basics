subjects={
    "math":[5,5],
    "geo":[5,4,4,4],
    "comp":[5,4]
    }

def f(subjects):
    max_avg=0
    max_subject=''
    for subject,grade in subjects.items():
        average=round(sum(grade)/len(grade),2)
        if average>max_avg:
            max_avg=average
            max_subject=subject

    return max_subject
    
print(f(subjects))


    
    
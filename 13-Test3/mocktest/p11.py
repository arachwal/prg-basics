cars = [{"KR333":138},{"WL555":497},{"DB444":341},{"MC222":412}]
order=1

def f(cars, order):

    kms=[]
    plates=[]

    if order==2:
        for car in cars:
            for km in car.values():
                kms.append(km)  
        return sorted(kms, reverse=True)

    elif order==1:
        for car in cars:
            for plate in car.keys():
                plates.append(plate)
        return sorted(plates)
    
print(f(cars,order))


    
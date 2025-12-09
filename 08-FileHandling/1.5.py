with open('countries.txt', 'r') as file:
    counter=1
    for line in file:     
        print(f"{counter}. {line}", end="")
        counter+=1





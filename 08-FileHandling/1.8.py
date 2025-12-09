with open('pets.txt', 'r') as file:
    content=file.read()
    lines=content.splitlines() 
    for line in lines:
        lenght_of_sentence=(len(line.split(" ")))
        print(f'{line}; --- number of words {lenght_of_sentence}')
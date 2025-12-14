arr=[[-38, 19], [5,40],[-7,11],[29,16]]

najwieksza=arr[0][0]
najmniejsza=arr[0][0]

kolumna_max=wiersz_max=0
kolumna_min=wiersz_min=0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(j)
        if arr[i][j]>najwieksza:
            najwieksza=arr[i][j]
            wiersz_max=i
            kolumna_max=j

        elif arr[i][j]<najmniejsza:
            najmniejsza=arr[i][j]
            wiersz_min=i
            kolumna_min-j

print(f'najmniejsza: {najmniejsza} w kolumnie: {kolumna_min} i wierszu: {wiersz_min}')
print(f'najwieksza: {najwieksza} w kolumnie: {kolumna_max} i wierszu: {wiersz_max}')


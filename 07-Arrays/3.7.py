arr=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

najdluzsze=arr[0]

for name in arr:
    if len(name)>len(najdluzsze):
        najdluzsze=name
        
print(najdluzsze)
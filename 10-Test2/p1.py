
player1='AJ972'
player2='AQT72'

'''values = {
        'A': 10, 'K': 10, 'Q': 10, 'J': 10, 'T': 10,
        '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9
    }'''

def f(player1,player2):
    suma1=0
    suma2=0
    for i in player1:
        if i in 'AKQJT':
            suma1+=10
        else:
            suma2+=int(i)    
    for j in player2:
        if j in 'AKQJT':
            suma2+=10
        else:
            suma2+=int(j)

    if suma1>=suma2:
        return True
    return False

print(f(player1,player2))
 
card_number="5290312400019022"
def hide(card_numebr):
    first2=card_number[:2]
    last3=card_number[-4:]
    numbertomask=10
    mask="*"*numbertomask
    maskedcard=f'{first2}{mask}{last3}'
    return maskedcard
print(hide(card_number))
class TV:
    def __init__(self,number=1,):
        self.number=number
        self.is_on=False

    def turn_off(self):
        self.is_on=False

    def turn_on(self):
        self.is_on=True

    def channel_no(self,number):
            self.number=number

    def show_status(self):
        if self.is_on:
            print(f'tv is on, channel {self.number}')
        else:
            print('tv is off')
    
    def set_channel(self, new_channel_no):
         self.number=new_channel_no


'''telewizor=TV()
telewizor.show_status()
telewizor.turn_on()
telewizor.show_status()
telewizor.set_channel(5)
telewizor.show_status()
telewizor.turn_off()
telewizor.show_status()'''
    
        
        


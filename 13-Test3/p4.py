class C:
    def __init__(self,fname,age):
        self.fname=fname
        self.age=age
        
    def __str__(self):
        if self.age<18:
            return f"{self.fname[0].lower()}-{self.age}"
        elif self.age>=18:
            return f"{self.fname[0].upper()}-{self.age}"

    

    

        
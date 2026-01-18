class C:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def m1(self):
        if self.x>0 and self.y>0:
            self.quadrantXY=1
        elif self.x<0 and self.y>0:
            self.quadrantXY=2
        elif self.x<0 and self.y<0:
            self.quadrantXY=3
        elif self.x>0 and self.y<0:
            self.quadrantXY=4
        elif self.x==0 or self.y==0:
            self.quadrantXY=0
        return self.quadrantXY
    
    def m2(self,a,b):
        self.a=a
        self.b=b
        if self.a>0 and self.b>0:
            self.quadrantAB=1
        elif self.a<0 and self.b>0:
            self.quadrantAB=2
        elif self.a<0 and self.b<0:
            self.quadrantAB=3
        elif self.a>0 and self.b<0:
            self.quadrantAB=4
        elif self.a==0 or self.b==0:
            self.quadrantAB=0
        if self.quadrantXY==self.quadrantAB:
            return True
        return False

        
    
p=C(2,1)
print(p.m1())
print(p.m2(3,2))
p.m3(2,3)

        
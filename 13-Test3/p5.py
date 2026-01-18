class C:
    def __init__(self,sectors):
        self.sectors=sectors.copy()
    def m1(self,s,n):
        self.sectors[s]=n
    def m2(self,s):
        total=0
        count=0
        for sector in s:
            if sector in self.sectors:
                total+=self.sectors[sector]
                count+=1
            if count==0:
                return 0
            return total / count
        
stadion=C({"A":120,"D":150,"G":90,"K":110})
stadion.m1("G",130)
print(stadion.m2("GD"))
print(stadion.m2("KEJ"))

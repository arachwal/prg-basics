class C:
    def __init__(self,sectors):
        self.sectors=sectors.copy()
    
    def m1(self,n,s):
        self.sectors[s]=n

    def m2(self,s):
        total=0
        count=0
        for sector in s:
            if sector in self.sectors:
                total+=self.sectors[sector]:
                count+=1
            elif count == 0:
                return 0
            return total / count

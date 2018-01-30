class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        self.l=[]
        self.maximumDifference=0
        self.n=len(self.__elements)
        for i in range(0,self.n-1):
            for j in range(i+1,self.n):
                self.e=abs(a[i]-a[j])
                self.l.append(self.e)
        self.maximumDifference=max(self.l)
_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference

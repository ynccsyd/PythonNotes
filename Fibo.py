class Fibo:
    def __iter__(self):
        self.f1=0
        self.f2=1
        return self
    def __next__(self):
        self.f1, self.f2=self.f2, self.f1+self.f2
        return self.f2
fibos=Fibo()
x=iter(fibos)


""" """
x=[0,1]
y=[x.append(x[i-1]+x[i]) for i in  range(1,10)]
print(x)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
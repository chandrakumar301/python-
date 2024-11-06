import math
a,b,c=1,7,12
b1=-1*b
k1=pow(b,2)
k2=k1-(4*a*c)
k=math.sqrt(k2)
sum1=(b1+k)/(2*a)
sum2=(b1-k)/(2*a)
print("{:.2f}".format(sum1),"{:.2f}".format(sum2))
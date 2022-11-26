# 1.from functools import reduce
# l=[10,20,30,40,50]
# print(reduce(lambda x,y:x+y,l))
# 2.from functools import reduce
# l=[2,4,6,8,10]
# r=reduce(lambda x,y:x+y,l)
# print("Result: ",r)
# 3.from functools import reduce
# t=['Aditya'," Ranjan"," your are"," the best."]
# reduce_object=reduce(lambda x,y:x+y,t)
# print(reduce_object)
from functools import reduce
places=["Sitamarhi",",Seohar",",Samastipur"]
reduce_object=reduce(lambda x,y:x+y,places)
print(reduce_object)
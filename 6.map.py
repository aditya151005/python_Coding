# 1.
# fruits=["Apple","Banana","Mango"]
# map_object=map(lambda s:s[0]=="A",fruits)
# print(list(map_object))
# 2.
# names=["Aditya","Ranjan","Sonu","Arya"]
# map_object=map(lambda s:s[0]=="A",names)
# print(list(map_object))#[True,False,False,True]
# 3.
# places=["Sitamrhi","Patna","Seohar","Samastipur"]
# map_object=map(lambda p:p[0]=="S",places)
# print(list(map_object)) #[True,False,True,True]
# # 4.
# food=["Biryani","Litti-Chokha","Chicken-Curry"]
# map_object=map(lambda s:s[1]=='i',food)
# print(list(map_object))
# #[True,True,False]
# 5
designation=["Assistant","Associate","Manager","Team-Leader"]
r=map(lambda s:s[0]=="A",designation)
print(list(r))
# [True,True,False,,False]



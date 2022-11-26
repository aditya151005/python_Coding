# Not handling space and capital letters
# s1="cat"
# s2="tac"
# if sorted(s1)==sorted(s2):
#     print("An anagramm string")
# else:
#     print("Not an Anagram string")
def anagramm(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    if len(str1)==len(str2):
        for i in str1:
            if i in str2:
                pass
            else:
                return False
        else:
           return True 
    return False      
a="eleven1 plus two"
b="twelve0 plus one"
print(anagramm(a,b))
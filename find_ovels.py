ovw=['a','e','i','o','u']
word=input("entre some words:")
found=[]
for i in word:
    if i in ovw:
        if i not in found:
            found.append(i)
        print(found) 
print("the ovwels in word are ",word ,'is number ovwels are ',found) 

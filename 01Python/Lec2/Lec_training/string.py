myname="ibrahim"
myage=23
city="tanta"
#print 
print(f"name is {myname}  age is {myage} and cit is {city}")
print("name is {} , my age is {} and my city is {}".format(myname,myage,city))
print("name is %s , my age is %d and my city is %s"%(myname,myage,city))
#join list 
print("****************************************************************")
words=["ibrahim","reda","elmsery"]
word="".join(words)
print(word)
print("****************************************************************")
name:str ="ibrahim reda"
print(name.upper())
print(name.lower())
print(name.split(" "))
print(name.split(" ")[0])

print(type (name.split(" ")))
print(name.replace('i','d'))
print(name.strip())

text="ibraim reda ibrahim"
x="ibra" in text
print(x)
print("****************************************************************")

#example
mydecision=input("enter your decision :   ")
#enter space not recognized
if mydecision=="yes":
    print("decision yes")
elif mydecision=="no":
        print("decision no")
else :
    print("wrong choice")
#true way
if mydecision.strip().lower()=="yes":
    print("decision yes")
elif mydecision.strip().lower()=="no":
        print("decision no")
else:
    print("error")  
print("****************************************************************")
web=r"hello\nworld"
print(web)
#help
#help(str.join)
#help(dir) ctrl+p
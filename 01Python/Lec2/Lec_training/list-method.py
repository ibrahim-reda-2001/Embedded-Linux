ls=[1,2,3,4,5,6,7,8,"ibrahim","reda","elmsery"]
ls.append("elsayed")
ls2=ls
ls2.append(25)
print(ls)
print(ls2)
print("*********************************************************")
ls3=ls.copy()
ls3.append(25)
print(ls)
print(ls3)
print("*********************************************************")
ls.extend([55,75,88])
print(ls)
print("*********************************************************")
ls.insert(3,"ibrahimelmser1@gmail.com")
print(ls)
print("*********************************************************")
print(ls.count(25))
print("*********************************************************")
print(ls)
ls.pop()
ls.pop(0)
print(ls)
print("*********************************************************")
ls.reverse()
print(ls)
print("*********************************************************")
ls5=[1,2,45,8,7,9,71,56,48,125,500]
ls5.sort()
print(ls5)

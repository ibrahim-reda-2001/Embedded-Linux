x=555
def my_fun():
   # global x
    x=111
    print(id(x))
    print(x)

my_fun()
print(id(x))
print(x)
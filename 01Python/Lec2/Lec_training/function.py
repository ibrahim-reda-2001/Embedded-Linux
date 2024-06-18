print("*************************************************************")
def my_function(name):
    print(f"hello bro {name}")

my_function("ibra")

def sum(a,b):
    return a+b

print(sum(2,3))


def print_function(arg):
    for i in arg:
        print(i)
        
my_list=['ibrahim',"amr","samer"]
my_tuble=("ahmed","mohamed","elsayed")
print_function(my_list)
print_function(my_tuble)

print("*************************************************************")
def tuble_function(*arg):
    print(f"the youngest one is : {arg[2]}")
    print(type(arg))
my_tuble1=("amr","samer","ibrahim")
tuble_function(*my_tuble1)
print("*************************************************************")

def dec_function(**arg):
    print(arg["name"])
    print(arg["age"])
    print(arg["email"])
dec_function(name="ibrahim",age=23,email="ibrahimworkacount@gmail,com")
dec_test={"name":"ibra","age":"23","email":"ibrahimelmsery1@gmail.com"}
dec_function(**dec_test)
print("*************************************************************")
#Lambda
x=lambda a:a+10
print(x(5))
x=lambda a:a*10
print(x(5))
ls=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2==0,ls)))
print(list(map(lambda x:x*x,ls)))
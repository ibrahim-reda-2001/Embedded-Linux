def GPIO():
    register=0
    for i in range(8):
        x=input(f"Enter the Bit {i} mode(in/out) : ")
        if x=='in':
            register&=~(1<<i)
        elif x=='out':
            register|=(1<<i)
        else :
            print('wrong select:)')
            raise KeyError ("wrong choise")
        
    return register
    
GPIOA=GPIO()
print(f"GPIOA register value is : {GPIOA:08b}")
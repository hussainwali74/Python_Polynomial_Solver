print("Hello World!")
print("Please choose type of equation: \n" )
option = int(input(" 1) ax + b = 0 \n 2) ax - b = 0 \n 3) a + bx = 0 \n 4) a - bx = 0 \n "))
if option == 1:
    print("this is a simple equation solver of the form ax + b = 0")
    a = int(input('please enter first value: '))
    b = int(input('please enter second value: '))
    b = 0-b
    x = b/a
    print("the result is: " , x)
elif option == 2:
    print("this is a simple equation solver of the form ax - b = 0")
    a = int(input('please enter first value: '))
    b = int(input('please enter second value: '))
 
    x = b/a
    print("the result is: " , x)
elif option == 3:
    print("this is a simple equation solver of the form a + bx = 0")
    a = int(input('please enter first value: '))
    b = int(input('please enter second value: '))
    
    x = -a/b
    print("the result is: " , x)
elif option == 4:
    print("this is a simple equation solver of the form a - bx = 0")
    a = int(input('please enter first value: '))
    b = int(input('please enter second value: '))
 
    x = a/b
    print("the result is: " , x)






print("hello")
print("world")
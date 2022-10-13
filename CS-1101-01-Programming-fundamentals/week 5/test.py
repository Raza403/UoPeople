def my_sqrt(a): 

     x = 2 

     while True:

         y = (x + a/x )/2 

         if y==x:

             break 

         x = y

     return x 

     a = int(input('a positive numb:')) 

     x = my_sqrt(a) 

print(my_sqrt(4)) 

print('square root of 4 is 2') 

 #output 2

# Square root of 4 is 2 



def test_sqrt(): 

    a = 1 

    while a<26: 

        print('a =', a,'| my_sqrt(a) =',my_sqrt(a),'| math.sqrt(a) =', math.sqrt(a),'| diff =', abs(math.sqrt(a)-my_sqrt(a))) a = a + 1 )

    return 0
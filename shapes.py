# Mundhu pettina comment tisesa anthey
class shapes :
    def __init__(self) :
        self.n=10
    def equilateral_triangle():
       n=int(input("Enter the height of the triangle"))
       for i  in range(0,n) :
          print(" "*(n-i), end='')
          for j in range(0,i) :
            if i!=(n-1) :
             if i>=3 and j>0 and j<=i-2 :
                 print(" ", end=' ')
             else :
                print(chr(j+65), end=' ')
            else :
             print(chr(j+65), end=' ')
          print()# end of the equilateral triangle program
    def right_angle_triangle():
        n=int(input("Enter the hieght of the triangle : "))
        for i in range(1,n+1) :
           for j in range(1,i+1) :
              print(chr(j+65), end=" ")#basic programmer debba
           print( )#end of the right angle triangle program 
    def reverse_equi_traingle() :
        n=int(input(" Enter the height of the triangle : "))
        for i in  range(0,n) :
           print(" "*i, end='')
           for j in range((n-i),0,-1) :
              print(chr(j+65), end=' ')
           print()#end of reverse equilateral triangle program
    def rhombus() :
        n=int(input('Enter the height of the rhombus......:'))
        n1=n//2
        for i in range(1,n1+1) :
           print(' '*(n1-i), end=' ')
           for j in range(1,i) :
             if i>j and j!=1 and j!=i-1 and i<=n1 :
               print(" ", end=' ')
             else :
               print(chr(64+j), end=' ')
           print()
        for k in range(n1,0,-1) :
           print(' '*(n1-k), end='')
           for l in range(k,0,-1) :
             if l<k and l!=1 :
               print(" ", end=' ')
             else :
                print(chr(64+l), end=' ')
           print()#end of the alpha rhombus program..........................
    def square() :
        n=int(input("Enter the size if the square: "))
        for i in range(n+1) :
            for j in range(n+1) :
                print(chr(65+j),end=' ')
            print()
            

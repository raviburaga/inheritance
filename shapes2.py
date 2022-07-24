from shapes import*
sha=shapes
if __name__=='__main__' :
    print("\t\t_______THESE ARE THE SHAPES WE HAVE______")
    while 1==1 :
     choice=int(input("\t PRESS 1 for EQUILATERAL TRIANGLE\n \t 2 for RIGHT ANGLE TRIANGLE\n \t 3 for REVERSE EQUI TRIANGLE \n \t 4 for RHOMBUS \n \t 5 for SQUARE\n \t PRESS 6 for exit \n \t\t ENTER YOUR CHOICE :"))
     if choice == 1 :
        sha.equilateral_triangle()
     elif choice == 2 :
        sha.right_angle_triangle()
     elif choice == 3 :
        sha.reverse_equi_traingle()
     elif choice == 4 :
        sha.rhombus()
     elif choice ==5 :
        sha.square()
     else :
         exit(0)
   

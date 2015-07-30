#******************** Assignment-3 : Synthetic Division ******************
#Name : Naveen Sai Vupputuri
#Program Description :This program takes the coefficients of the equation
#        and two points as inputs and verifies whether the points are on 
#        the elliptical, curve if yes then finds out the point where the
#        line passing through the two points intersects the elliptical 
#        curve.
#*************************************************************************

import math
from fractions import Fraction

def syntheticDivision(c1,c2,c3,c4,c,x1,y1,x2,y2):
    #slope of the line passing through the two points
    m=(y2-y1)/(x2-x1)
    #constant in the line 'cl'
    cl=y1-(m*x1)

    #synthetic division:
    #after substituting the line y=mx+cl in cure equation
    # (c2)x^3 + (c3-(c1*m*m))x^2 + (c4-(2*c1*cL))x + (c-(cL*cL*c1))
    l1=c2
    l2=(c3-(c1*m*m))
    l3=(c4-(2*c1*cl*m))
    l4=(c-(cl*cl*c1))
    
    m1=l1
    m2=l2+(x1*m1)   
    m3=l3+(x1*m2)

    a=m1
    b=m2+(x2*a)
    xCord=-(b/a)
    yCord=(m*xCord) + cl
    return xCord , yCord 

print ("Enter the coefficients and constant of the elliptical equation ")
c1=int(input("coeff of y^2 :"))
c2=int(input("coeff of x^3 :"))
c3=int(input("coeff of x^2 :")) 
c4=int(input("coeff of x :"))
c=int(input("Constant :"))
print("Enter the coordinates of the two points x1, y1, x2, y2 :")
x1=int(input("First X-coordinate :"))
y1=int(input("First Y-coordinate :"))
x2=int(input("Second X-coordinate :"))
y2=int(input("Second Y-coordinate :"))

#Verifying whether the points lie on the curve
#For fist point
leftVer1=c1*y1*y1
rightVer1=(c2*x1*x1*x1)+(c3*x1*x1)+(c4*x1)+c
#For second point
leftVer2=c1*y2*y2
rightVer2=(c2*x2*x2*x2)+(c3*x2*x2)+(c4*x2)+c
if((leftVer1==rightVer1) and (leftVer2==rightVer2)):
    xcord,ycord=syntheticDivision(c1,c2,c3,c4,c,x1,y1,x2,y2)
    print("The intersecting coordinate is :")
    print(Fraction(xcord) , Fraction(ycord))
else:
    print("The points doesn't lie on the equation ")
    
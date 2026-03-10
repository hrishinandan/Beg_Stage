class complex:
     def __init__(self,real,img):
        self.real=real
        self.img=img
        
     def __add__(self,other):
        real_part=self.real+other.real
        img_part=self.img+other.img
        return complex(real_part,img_part)
        
real1 = float(input("Enter real part of first complex number: "))
imag1 = float(input("Enter imaginary part of first complex number: "))
real2 = float(input("Enter real part of second complex number: "))
imag2 = float(input("Enter imaginary part of second complex number: "))

complex1=complex(real1,imag1)
complex2=complex(real1,imag2)

result=complex1+complex2

print("sum of complex numbers:",result.real,"+",result.img,"i")

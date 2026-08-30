#1  


print("Hello sir may i know your name")
name =input()
print("Hello", name, " how's you day going")


#2 

r = int(input("Enter the radius of the circle : "  ))
area = (3.14*r*r)
print ("Area of the circle: ", area )


#3 araa of rectangle and area 
l= int(input("Enter the length of the rectangle : "  ))
w= int(input("Enter the width of the rectangle : "  ))
para = (2*(l+w))
area = (l*w)
print("parameter of the circle :",para )
print("area of the circle :",area )


#4sum, product, and average  ask for 3 int

n1= int(input("Enter the first number  : "  ))
n2= int(input("Enter the second number : "  ))
n3= int(input("Enter the third number : "  ))
sum = (n1+n2+n3) 
pro = (n1*n2*n3)
avg = float((n1+n2+n3)/3)
print("The sum of all three number:",sum )
print("The product of all three number:",pro )
print("The avereage of all three number:",avg )

#5 One talent is 20 pounds. One pound is 32 lots. One lot is 13,3 grams.

t = float(input("Enter talents: "))
p = float(input("Enter pounds: "))
l = float(input("Enter lots: "))

g = (t*20*32*13.3) + (p*32 *13.3) + (l*13.3)
kg = int(g/1000)
g = g%1000
print("weight in modern units:")
print(kg,"kilograms and", g,"grams.")







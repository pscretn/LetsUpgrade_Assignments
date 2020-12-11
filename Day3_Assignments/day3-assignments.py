# Question 1
# Use IF ELSE and ELIF to write a program in python for your Report Cards.

percent = 79

if percent <= 100 and percent >= 90 :
	print("Grade : A+")
elif percent < 90 and percent >= 80 :
	print("Grade : A")
elif percent < 80 and percent >= 70 :
	print("Grade : B+")
elif percent < 70 and percent >= 60 :
	print("Grade : B")
elif percent < 60 and percent >= 50 :
	print("Grade : C+")
elif percent < 50 and percent >= 45 :
	print("Grade : C")
else:
    print("Grade: Failed")

# Question 2
# Use For Loop to Print Prime Numbers in between 1 to 1000

print("\n")
print("Prime numbers from 1-1000 :") 
for num in range(1,1000 ,1): 
    
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  



# Question 3
# Write a program for printing the tables from 1,10 using Nested For Loop
 
print("\n")
for a in range (1,11,1):
    print("table of",a)
    for b in range(1,11,1):
        mul=a*b
        print(mul)


# Question 4
# Write a program to Print X Prime Numbers using While Loop starting from 0, and take the input of X from the user
print("\n")
print("Prime numbers from 0-x :") 
x=int(input("enter a number : "))
p=0
while p<= x:
    q=2
    while (q <= p):
        if (p == q):
            print(p)
        if (p % q == 0):
            break
        q+=1
    p+=1    



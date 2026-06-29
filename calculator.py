#python program for to create calculator
# Create function
def add(num1, num2):  #addition
    return num1+num2

def sub(num1, num2):  #Substraction
    return  num1 -num2

def mul(num1, num2):  #Multiply
    return num1 *num2

def div(num1, num2):  #division
    return num1/num2



# User input
print("Please select a operation:\n"
       "1.Addition\n", 
       "2.Substraction\n",
       "3. Multiplication\n",
       "4.Division\n",)
       

select = input ("select a operation from 1,2,3,4: ")
num1 = int(input("enter the number:"))
num2 = int(input("enter the number:"))

#Print the result
if select == 1:
    print(num1, "+", num2, "=", add(num1+num2))
elif select == 2:
        print(num1, "-", num2, "=", sub(num1-num2))
elif select == 3:
     print(num1, "*", num2, "=", mul(num1,num2) )
elif select == 4:
     print(num1, "/", num2, "=", div(num1,num2))

else:
     print("invalid operation !")
     





